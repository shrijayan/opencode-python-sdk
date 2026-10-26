"""Tests for the hand-written helpers (``session.run``, ``wait_until_ready``) and the fake server."""

from __future__ import annotations

import anyio
import httpx
import pytest
from typing_extensions import override

from opencode import (
    AsyncOpencode,
    InvalidRequestError,
    NotFoundError,
    Opencode,
    ServiceUnavailableError,
    SessionNotFoundError,
)
from opencode.lib import RunResult
from opencode.testing import FakeServer
from opencode.types import ModelRef, ServerConnectedEvent, SessionCreatedEvent, SessionIdleEvent


@pytest.fixture(autouse=True)
def _fast_polls(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("opencode.lib._ready.POLL_INTERVAL", 0.0)


def _paths(fake: FakeServer) -> list[str]:
    return [f"{request.method} {request.url.path}" for request in fake.requests]


# -- session.run ----------------------------------------------------------------------------------------------


def test_run_creates_session_and_returns_result() -> None:
    fake = FakeServer(reply=lambda text: f"echo: {text}", cost=0.5, tokens=(100, 20))
    client = Opencode.fake(fake)
    model = ModelRef(id="claude", provider_id="anthropic")

    result = client.session.run("hello", agent="build", model=model)

    assert isinstance(result, RunResult)
    assert result.text == "echo: hello"
    assert result.outcome == "succeeded"
    assert [message.type for message in result.messages] == ["user", "assistant", "idle"]
    assert result.cost == 0.5
    assert (result.tokens.input, result.tokens.output) == (100, 20)
    assert result.session.agent == "build"
    assert result.session.model == model
    assert result.session.cost == 0.5
    assert fake.prompts == ["hello"]


def test_run_reuses_session_and_only_returns_new_messages() -> None:
    fake = FakeServer(reply="ok")
    client = Opencode.fake(fake)
    first = client.session.run("one")

    second = client.session.run("two", session_id=first.session.id, agent="plan")

    assert [message.type for message in second.messages] == ["user", "assistant", "idle"]
    assert second.messages[0].text == "two"  # type: ignore[union-attr]
    assert second.cost == pytest.approx(fake.cost)
    assert second.session.cost == pytest.approx(2 * fake.cost)
    assert second.session.agent == "plan"
    assert len(fake.sessions) == 1


def test_run_follows_message_pages() -> None:
    fake = FakeServer()
    client = Opencode.fake(fake)
    session = client.session.run("first").session
    for index in range(30):
        client.session.prompt(session.id, text=f"filler {index}")

    result = client.session.run("last", session_id=session.id)

    assert result.messages[0].text == "last"  # type: ignore[union-attr]
    assert len(result.messages) == 3


def test_run_without_assistant_text() -> None:
    client = Opencode.fake(FakeServer(reply=""))
    assert client.session.run("quiet").text == ""


def test_run_interrupts_when_wait_fails() -> None:
    fake = FakeServer()
    fake.fail("POST", r"/api/experimental/session/.+/wait", status=503, times=None)
    client = Opencode.fake(fake, max_retries=0)

    with pytest.raises(ServiceUnavailableError):
        client.session.run("long task")

    assert _paths(fake)[-1].endswith("/interrupt")


def test_run_interrupts_on_keyboard_interrupt() -> None:
    fake = FakeServer()
    fake.fail("POST", r"/api/experimental/session/.+/wait", exception=KeyboardInterrupt())
    client = Opencode.fake(fake)

    with pytest.raises(KeyboardInterrupt):
        client.session.run("long task")

    assert _paths(fake)[-1].endswith("/interrupt")


def test_run_unknown_session() -> None:
    client = Opencode.fake()
    with pytest.raises(SessionNotFoundError) as caught:
        client.session.run("hi", session_id="ses_missing")
    assert caught.value.error.session_id == "ses_missing"


@pytest.mark.anyio
async def test_async_run() -> None:
    fake = FakeServer(reply="async ok")
    async with AsyncOpencode.fake(fake) as client:
        result = await client.session.run("hello", agent="build")
        again = await client.session.run("more", session_id=result.session.id)
    assert result.text == "async ok"
    assert [message.type for message in again.messages] == ["user", "assistant", "idle"]


@pytest.mark.anyio
async def test_async_run_interrupts_on_cancel() -> None:
    fake = FakeServer()
    entered = anyio.Event()

    class Blocking(FakeServer):
        @override
        async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
            if request.url.path.endswith("/wait"):
                fake.requests.append(request)
                entered.set()
                await anyio.sleep_forever()
            return await fake.handle_async_request(request)

    client = AsyncOpencode(transport=Blocking(), base_url="http://opencode.fake")
    async with anyio.create_task_group() as group:
        group.start_soon(client.session.run, "long task")
        await entered.wait()
        group.cancel_scope.cancel()

    assert _paths(fake)[-1].endswith("/interrupt")


# -- wait_until_ready -----------------------------------------------------------------------------------------


def test_wait_until_ready_polls_until_agents_and_mcp_appear() -> None:
    fake = FakeServer(agents=["build"])
    fake.add_agent("reviewer", after_polls=3)
    fake.set_mcp_status("github", "connected", after_polls=2)
    client = Opencode.fake(fake)

    client.wait_until_ready(agents=["build", "reviewer"], mcp_servers=["github"], timeout=5)

    assert _paths(fake).count("GET /api/agent") == 4


def test_wait_until_ready_times_out_naming_what_is_missing() -> None:
    fake = FakeServer()
    fake.set_mcp_status("broken", "failed")
    client = Opencode.fake(fake)

    with pytest.raises(TimeoutError, match=r"agent 'ghost'.*MCP server 'broken'"):
        client.wait_until_ready(agents=["ghost"], mcp_servers=["broken"], timeout=0.05)


def test_wait_until_ready_retries_while_server_boots() -> None:
    fake = FakeServer()
    fake.fail("GET", "/api/info", exception=httpx.ConnectError("refused"), times=2)
    client = Opencode.fake(fake, max_retries=0)

    client.wait_until_ready(timeout=5)

    assert _paths(fake).count("GET /api/info") == 3


@pytest.mark.anyio
async def test_async_wait_until_ready() -> None:
    fake = FakeServer(agents=[])
    fake.add_agent("build", after_polls=1)
    async with AsyncOpencode.fake(fake) as client:
        await client.wait_until_ready(agents=["build"], timeout=5)
        with pytest.raises(TimeoutError):
            await client.wait_until_ready(mcp_servers=["nope"], timeout=0.01)


# -- FakeServer -----------------------------------------------------------------------------------------------


def test_fake_session_crud_and_listing() -> None:
    fake = FakeServer()
    client = Opencode.fake(fake)
    created = [client.session.create(title=f"s{index}") for index in range(3)]

    assert client.session.get(created[0].id).title == "s0"
    assert [session.title for session in client.session.list(limit=2)] == ["s2", "s1", "s0"]
    client.session.remove(created[0].id)
    with pytest.raises(SessionNotFoundError):
        client.session.get(created[0].id)


def test_fake_queued_prompt_does_not_run() -> None:
    fake = FakeServer()
    client = Opencode.fake(fake)
    session = client.session.create()

    queued = client.session.prompt(session.id, text="later", resume=False)

    assert queued.type == "user"
    assert queued.payload.text == "later"
    assert list(client.message.list(session.id)) == []
    assert len(fake.inbox[session.id]) == 1


def test_fake_message_filter_and_order() -> None:
    client = Opencode.fake()
    session = client.session.run("hi").session

    assert [message.type for message in client.message.list(session.id, type="assistant")] == ["assistant"]
    assert [message.type for message in client.message.list(session.id, order="desc")] == ["idle", "assistant", "user"]


def test_fake_event_stream() -> None:
    client = Opencode.fake()
    client.session.run("hi")
    with client.event.subscribe() as events:
        received = list(events)
    assert isinstance(received[0], ServerConnectedEvent)
    assert isinstance(received[1], SessionCreatedEvent)
    assert isinstance(received[2], SessionIdleEvent)


def test_fake_errors() -> None:
    fake = FakeServer()
    client = Opencode.fake(fake, max_retries=0)
    session = client.session.create()

    with pytest.raises(InvalidRequestError) as invalid:
        client.session.prompt(session.id, text="x", extra_body={"text": 1})
    assert invalid.value.status_code == 400
    with pytest.raises(NotFoundError, match="does not implement"):
        client.config.get()


def test_fake_and_http_client_are_exclusive() -> None:
    with pytest.raises(ValueError, match="either"):
        Opencode("http://x", transport=FakeServer(), http_client=httpx.Client())
