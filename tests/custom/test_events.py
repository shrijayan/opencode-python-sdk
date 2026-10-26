"""The shared event hub: multiplexing, overflow, replay, reconnect, filters and cancellation."""

from __future__ import annotations

import json
import queue
import threading
import collections
from types import SimpleNamespace
from collections.abc import Iterator, AsyncIterator

import anyio
import httpx
import respx
import pytest

from opencode import (
    EventHub,
    Opencode,
    Reconnect,
    AsyncEventHub,
    AsyncOpencode,
    UnauthorizedError,
    EventOverflowError,
    session_id_of,
)
from opencode.types import Event, SessionIdleEvent, ServerConnectedEvent

from .conftest import BASE_URL, PASSWORD

SSE = {"content-type": "text/event-stream"}


def is_unknown(event: object) -> bool:
    """An event type this client has no class for still arrives, with its ``type``."""
    return getattr(event, "type", None) == "brand.new"


def frame(payload: dict[str, object]) -> bytes:
    return f"data: {json.dumps(payload)}\n\n".encode()


def connected(n: int = 1) -> bytes:
    return frame({"type": "server.connected", "id": f"evt_c{n}", "data": {}})


def idle(session_id: str, n: int = 1) -> bytes:
    return frame({"type": "session.idle", "id": f"evt_i{n}", "created": 1, "data": {"sessionID": session_id}})


def other(n: int = 1) -> bytes:
    return frame({"type": "brand.new", "id": f"evt_o{n}", "created": 1})


END = b""


class SyncFeed:
    """One fake SSE connection whose chunks the test pushes. ``END`` closes it."""

    def __init__(self) -> None:
        self.chunks: queue.Queue[bytes] = queue.Queue()
        self.closed = threading.Event()

    def push(self, *chunks: bytes) -> None:
        for chunk in chunks:
            self.chunks.put(chunk)

    def __iter__(self) -> Iterator[bytes]:
        try:
            while (chunk := self.chunks.get(timeout=5)) != END:
                yield chunk
        finally:
            self.closed.set()


class Server:
    """Hands out a new feed (or a prepared response) for each connection."""

    def __init__(self, mock_api: respx.MockRouter, *, sync: bool) -> None:
        self.sync = sync
        self.feeds: list[SyncFeed | AsyncFeed] = []
        self.prepared: list[httpx.Response] = []
        self.opened = threading.Semaphore(0)
        mock_api.get("/api/event").mock(side_effect=self._respond)

    def _respond(self, request: httpx.Request) -> httpx.Response:
        if self.prepared:
            response = self.prepared.pop(0)
        else:
            feed: SyncFeed | AsyncFeed = SyncFeed() if self.sync else AsyncFeed()
            self.feeds.append(feed)
            response = httpx.Response(200, headers=SSE, content=feed)
        self.opened.release()
        return response

    def wait_open(self, count: int) -> SyncFeed:
        while len(self.feeds) < count:
            assert self.opened.acquire(timeout=5)
        feed = self.feeds[count - 1]
        assert isinstance(feed, SyncFeed)
        return feed


class AsyncFeed:
    """The async counterpart of ``SyncFeed``. It polls, since ``anyio.sleep`` is patched in tests."""

    def __init__(self) -> None:
        self.chunks: collections.deque[bytes] = collections.deque()

    def push(self, *chunks: bytes) -> None:
        self.chunks.extend(chunks)

    async def __aiter__(self) -> AsyncIterator[bytes]:
        while True:
            while not self.chunks:
                await anyio.lowlevel.checkpoint()
            chunk = self.chunks.popleft()
            if chunk == END:
                return
            yield chunk


# ---------------------------------------------------------------- sync


def test_subscribers_share_one_connection(client: Opencode, mock_api: respx.MockRouter) -> None:
    server = Server(mock_api, sync=True)
    with client.events.subscribe() as first, client.events.subscribe() as second:
        feed_ready = threading.Thread(target=lambda: server.wait_open(1).push(connected()))
        feed_ready.start()
        assert isinstance(first.get(5), ServerConnectedEvent)
        assert isinstance(second.get(5), ServerConnectedEvent)
        feed_ready.join()
        server.feeds[0].push(idle("ses_1"))
        assert isinstance(first.get(5), SessionIdleEvent)
        assert isinstance(second.get(5), SessionIdleEvent)
    assert len(server.feeds) == 1
    server.feeds[0].push(END)


def test_late_subscriber_gets_server_connected_replayed(client: Opencode, mock_api: respx.MockRouter) -> None:
    server = Server(mock_api, sync=True)
    with client.events.subscribe() as first:
        threading.Thread(target=lambda: server.wait_open(1).push(connected(), other())).start()
        assert isinstance(first.get(5), ServerConnectedEvent)
        assert is_unknown(first.get(5))
        with client.events.subscribe() as late:
            assert isinstance(late.get(5), ServerConnectedEvent)
            server.wait_open(1).push(idle("ses_1"))
            assert isinstance(late.get(5), SessionIdleEvent)
        server.feeds[0].push(END)


def test_slow_subscriber_overflows_alone(
    client: Opencode, mock_api: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("opencode._events.SUBSCRIBER_CAPACITY", 3)
    server = Server(mock_api, sync=True)
    with client.events.subscribe() as slow, client.events.subscribe() as fast:
        # Both join on first use; the slow one never reads after that.
        threading.Thread(target=lambda: server.wait_open(1).push(connected())).start()
        assert isinstance(slow.get(5), ServerConnectedEvent)
        assert isinstance(fast.get(5), ServerConnectedEvent)
        feed = server.wait_open(1)
        for n in range(5):
            feed.push(idle("ses_1", n))
            assert isinstance(fast.get(5), SessionIdleEvent)
        with pytest.raises(EventOverflowError, match="3-event capacity"):
            slow.get(5)
        feed.push(other())
        assert is_unknown(fast.get(5))
        feed.push(END)


def test_last_subscriber_leaving_closes_the_connection(client: Opencode, mock_api: respx.MockRouter) -> None:
    server = Server(mock_api, sync=True)
    subscription = client.events.subscribe()
    threading.Thread(target=lambda: server.wait_open(1).push(connected())).start()
    assert isinstance(subscription.get(5), ServerConnectedEvent)
    subscription.close()
    with pytest.raises(StopIteration):
        subscription.get(1)
    feed = server.wait_open(1)
    feed.push(other())  # wakes the reader, which sees the hub stopped
    assert feed.closed.wait(5)
    assert client.events._current is None


def test_close_from_another_thread_unblocks_iteration(client: Opencode, mock_api: respx.MockRouter) -> None:
    server = Server(mock_api, sync=True)
    subscription = client.events.subscribe()
    received: list[Event] = []

    def consume() -> None:
        received.extend(subscription)

    worker = threading.Thread(target=consume)
    worker.start()
    server.wait_open(1).push(connected())
    while not received:
        threading.Event().wait(0.01)
    subscription.close()
    worker.join(5)
    assert not worker.is_alive()
    server.feeds[0].push(END)


def test_stream_end_finishes_after_queued_events(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").respond(headers=SSE, content=connected() + idle("ses_1"))
    events = list(client.events)
    assert [event.type for event in events] == ["server.connected", "session.idle"]


def test_filters_narrow_by_type_and_session(client: Opencode, mock_api: respx.MockRouter) -> None:
    body = connected() + idle("ses_1", 1) + other() + idle("ses_2", 2) + idle("ses_1", 3)
    mock_api.get("/api/event").respond(headers=SSE, content=body)
    with client.events.of_type(SessionIdleEvent).for_session("ses_1") as events:
        ids = [event.id for event in events]
    assert ids == ["evt_i1", "evt_i3"]
    with client.events.for_session("ses_2") as events:
        assert [event.id for event in events] == ["evt_i2"]
    with client.events.subscribe().where(lambda event: event.type == "brand.new") as events:
        assert [event.id for event in events] == ["evt_o1"]


def test_filters_cannot_be_added_after_iteration_starts(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").respond(headers=SSE, content=connected())
    with client.events.subscribe() as events:
        next(events)
        with pytest.raises(RuntimeError, match="before"):
            events.of_type(SessionIdleEvent)
    with pytest.raises(TypeError):
        client.events.of_type()


def test_on_activity_fires_on_keepalive_comments(client: Opencode, mock_api: respx.MockRouter) -> None:
    server = Server(mock_api, sync=True)
    beats = threading.Semaphore(0)
    with client.events.subscribe(on_activity=beats.release) as events:
        threading.Thread(target=lambda: server.wait_open(1).push(b": keepalive\n\n")).start()
        with pytest.raises(TimeoutError):
            events.get(0.2)
        assert beats.acquire(timeout=5)
        server.feeds[0].push(END)


def test_reconnect_dedupes_server_connected(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").mock(
        side_effect=[
            httpx.Response(200, headers=SSE, content=connected(1) + idle("ses_1", 1)),
            httpx.ConnectError("refused"),
            httpx.Response(503),
            httpx.Response(200, headers=SSE, content=connected(2) + idle("ses_1", 2)),
            httpx.Response(401, json={"_tag": "UnauthorizedError", "message": "no"}),
        ]
    )
    hub = EventHub(client.with_options(max_retries=0), reconnect=Reconnect(initial_delay=0, max_delay=0))
    received: list[Event] = []
    with pytest.raises(UnauthorizedError), hub.subscribe() as events:
        received.extend(events)
    assert [event.id for event in received] == ["evt_c1", "evt_i1", "evt_i2"]
    with hub.subscribe() as late:  # the hub keeps working after a failure
        assert late._hub is hub


def test_reconnect_gives_up_after_max_attempts(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/event").mock(side_effect=httpx.ConnectError("refused"))
    hub = EventHub(client.with_options(max_retries=0), reconnect=Reconnect(initial_delay=0, max_attempts=2))
    with pytest.raises(Exception, match="Connection error"), hub.subscribe() as events:
        next(events)
    assert route.call_count == 3


def test_without_reconnect_errors_end_every_subscription(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").mock(side_effect=httpx.ConnectError("refused"))
    with (
        pytest.raises(Exception, match="Connection error"),
        client.with_options(max_retries=0).events.subscribe() as events,
    ):
        next(events)


def test_session_id_of() -> None:
    assert session_id_of(ServerConnectedEvent.construct(id="e", type="server.connected", data={})) is None
    # An event type this client has no class for: its data stays as sent.
    assert session_id_of(SimpleNamespace(type="x", data={"sessionID": "ses_9"})) == "ses_9"


def test_generated_subscribe_still_works(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").respond(headers=SSE, content=connected())
    with client.event.subscribe() as stream:
        assert [event.type for event in stream] == ["server.connected"]


# ---------------------------------------------------------------- async


@pytest.fixture(params=["asyncio", "trio"])
def anyio_backend(request: pytest.FixtureRequest) -> str:
    return str(request.param)


async def _wait_feed(server: Server, count: int) -> AsyncFeed:
    with anyio.fail_after(5):
        while len(server.feeds) < count:
            await anyio.lowlevel.checkpoint()  # anyio.sleep is patched to return at once
    feed = server.feeds[count - 1]
    assert isinstance(feed, AsyncFeed)
    return feed


@pytest.fixture
async def aclient(mock_api: respx.MockRouter) -> AsyncIterator[AsyncOpencode]:
    async with AsyncOpencode(base_url=BASE_URL, password=PASSWORD, max_retries=0) as instance:
        yield instance


@pytest.mark.anyio
async def test_async_multiplexing_and_replay(aclient: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    server = Server(mock_api, sync=False)
    async with aclient.events.subscribe() as first, aclient.events.subscribe() as second:
        with anyio.fail_after(5):
            feed = await _wait_feed(server, 1)
            feed.push(connected())
            assert isinstance(await first.get(), ServerConnectedEvent)
            assert isinstance(await second.get(), ServerConnectedEvent)
            feed.push(idle("ses_1"))
            assert isinstance(await first.get(), SessionIdleEvent)
            assert isinstance(await second.get(), SessionIdleEvent)
            async with aclient.events.subscribe() as late:
                assert isinstance(await late.get(), ServerConnectedEvent)
    assert len(server.feeds) == 1
    assert aclient.events._current is None


@pytest.mark.anyio
async def test_async_cancellation_keeps_subscription_usable(aclient: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    server = Server(mock_api, sync=False)
    async with aclient.events.of_type(SessionIdleEvent) as idle_events:
        with anyio.move_on_after(0.05) as scope:
            await idle_events.get()
        assert scope.cancelled_caught
        feed = await _wait_feed(server, 1)
        feed.push(connected(), idle("ses_1"))
        with anyio.fail_after(5):
            assert (await idle_events.get()).data.session_id == "ses_1"
    assert aclient.events._current is None


@pytest.mark.anyio
async def test_async_overflow_and_end(
    aclient: AsyncOpencode, mock_api: respx.MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("opencode._events.SUBSCRIBER_CAPACITY", 2)
    server = Server(mock_api, sync=False)
    async with aclient.events.subscribe() as slow, aclient.events.for_session("ses_1") as fast:
        feed = await _wait_feed(server, 1)
        feed.push(connected())
        with anyio.fail_after(5):
            for n in (1, 2, 3):
                feed.push(idle("ses_1", n))
                assert (await fast.get()).id == f"evt_i{n}"
            feed.push(END)
            assert [event async for event in fast] == []
        with pytest.raises(EventOverflowError):
            await slow.get()


@pytest.mark.anyio
async def test_async_reconnect_and_activity(aclient: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").mock(
        side_effect=[
            httpx.Response(200, headers=SSE, content=b": hi\n\n" + connected(1)),
            httpx.Response(502),
            httpx.Response(200, headers=SSE, content=connected(2) + other(1)),
            httpx.Response(401, json={"_tag": "UnauthorizedError", "message": "no"}),
        ]
    )
    beats: list[None] = []
    hub = AsyncEventHub(aclient, reconnect=Reconnect(initial_delay=0))
    received: list[Event] = []
    async with hub.subscribe(on_activity=lambda: beats.append(None)) as events:
        with anyio.fail_after(5):
            received.extend([await events.get(), await events.get()])
            with pytest.raises(UnauthorizedError):
                await events.get()
    assert [event.id for event in received] == ["evt_c1", "evt_o1"]
    assert len(beats) >= 2


@pytest.mark.anyio
async def test_async_request_cancellation_leaves_client_usable(
    aclient: AsyncOpencode, mock_api: respx.MockRouter
) -> None:
    async def slow(request: httpx.Request) -> httpx.Response:
        await anyio.Event().wait()
        raise AssertionError("unreachable")

    mock_api.get("/api/agent").mock(side_effect=slow)
    with anyio.move_on_after(0.05) as scope:
        await aclient.agent.list()
    assert scope.cancelled_caught
    mock_api.get("/api/event").respond(headers=SSE, content=connected())
    with anyio.fail_after(5):
        assert [event.type async for event in aclient.events] == ["server.connected"]
