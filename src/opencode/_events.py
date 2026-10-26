"""A shared, multiplexed event stream.

``GET /api/event`` delivers every event of the server to every connection. Opening one connection per consumer
wastes server work and sockets, so :class:`EventHub` and :class:`AsyncEventHub` share a single connection among all
of their subscribers, the way ``client.event`` does in the official TypeScript client:

- The connection opens with the first subscriber and closes when the last one leaves.
- Each subscriber has its own bounded queue (:data:`SUBSCRIBER_CAPACITY` events). A subscriber that falls that far
  behind fails with :class:`EventOverflowError`; the others keep receiving.
- The most recent ``server.connected`` event is replayed to subscribers that join after it arrived.

Beyond the TypeScript client, a hub can reconnect with backoff (:class:`Reconnect`), and subscriptions can be
narrowed with :meth:`Subscription.of_type`, :meth:`Subscription.for_session` and :meth:`Subscription.where`.

The event stream is volatile by contract: events published while no connection is open, including while a hub
waits to reconnect, are never delivered. Use it to react to changes, and read state through the API when exact
history matters.
"""

from __future__ import annotations

import random
import socket
import asyncio
import logging
import threading
import contextlib
import collections
from typing import TYPE_CHECKING, Any, Generic, TypeVar, cast
from dataclasses import dataclass
from typing_extensions import Self

import anyio

from ._exceptions import OpencodeError, APIStatusError, APIConnectionError

if TYPE_CHECKING:
    from types import TracebackType
    from collections.abc import Callable, Iterator, Awaitable, AsyncIterator

    from .types import Event, ServerConnectedEvent
    from ._streaming import Stream, AsyncStream
    from .lib._client import Opencode, AsyncOpencode

__all__ = [
    "SUBSCRIBER_CAPACITY",
    "AsyncEventHub",
    "AsyncSubscription",
    "EventHub",
    "EventOverflowError",
    "Reconnect",
    "Subscription",
]

log = logging.getLogger("opencode")

_E = TypeVar("_E")
_T = TypeVar("_T")

SUBSCRIBER_CAPACITY = 4096
"""Events a subscriber may have queued before it fails with :class:`EventOverflowError`. Matches the TS client."""


class EventOverflowError(OpencodeError):
    """A subscriber fell more than :data:`SUBSCRIBER_CAPACITY` events behind the shared stream.

    Only that subscriber fails. Its queued events are discarded, since they no longer form a gap-free sequence.
    """


@dataclass(frozen=True)
class Reconnect:
    """Opt-in reconnection policy for an event hub.

    After the connection ends or fails with a connection error, a 5xx or a 429, the hub waits and connects again.
    The delay starts at ``initial_delay`` seconds, doubles per failed attempt up to ``max_delay``, gets up to 25%
    jitter, and resets once a connection delivers an event. Other errors (authentication, malformed events) still
    end every subscription.

    Events published while disconnected are lost. The server sends ``server.connected`` again on every connection;
    subscribers see it only once, and late subscribers get the latest one.

    Args:
        initial_delay: Seconds before the first reconnection attempt.
        max_delay: Upper bound for the delay between attempts.
        max_attempts: Consecutive failed attempts before giving up, or ``None`` to retry forever.
    """

    initial_delay: float = 0.5
    max_delay: float = 30.0
    max_attempts: int | None = None

    def delay(self, attempt: int) -> float:
        """Seconds to wait before reconnection attempt ``attempt`` (counting from zero)."""
        delay = min(self.initial_delay * 2.0**attempt, self.max_delay)
        return delay * (1 - 0.25 * random.random())

    def allows(self, attempt: int) -> bool:
        """Whether reconnection attempt ``attempt`` (counting from zero) may run."""
        return self.max_attempts is None or attempt < self.max_attempts


def _policy(reconnect: bool | Reconnect) -> Reconnect | None:
    if isinstance(reconnect, Reconnect):
        return reconnect
    return Reconnect() if reconnect else None


def _retryable(error: BaseException | None) -> bool:
    """Whether a connection that ended with ``error`` (``None`` for a clean end) may be reopened."""
    if error is None or isinstance(error, APIConnectionError):
        return True
    if isinstance(error, APIStatusError):
        return error.status_code >= 500 or error.status_code == 429
    return False


def session_id_of(event: object) -> str | None:
    """Returns the session an event belongs to, or ``None`` for events outside any session.

    Looks for ``data.session_id`` on typed events and ``data["sessionID"]`` on raw ones.
    """
    data: Any = getattr(event, "data", None)
    if isinstance(data, dict):
        value: object = cast("dict[str, Any]", data).get("sessionID")
    else:
        value = getattr(data, "session_id", None)
    return value if isinstance(value, str) else None


class _Filters(Generic[_E]):
    """Narrowing helpers shared by sync and async subscriptions."""

    _predicates: tuple[Callable[[Any], bool], ...]

    def _accepts(self, event: object) -> bool:
        return all(predicate(event) for predicate in self._predicates)


_End = anyio.EndOfStream


def _watch_activity(stream: Stream[Event], on_chunk: Callable[[], object]) -> None:
    """Calls ``on_chunk`` for every chunk the stream receives, keepalive comments included."""
    response = stream.response
    chunks = response.iter_bytes

    def iter_bytes(chunk_size: int | None = None) -> Iterator[bytes]:
        for chunk in chunks(chunk_size):
            on_chunk()
            yield chunk

    response.iter_bytes = iter_bytes  # type: ignore[method-assign]


def _async_watch_activity(stream: AsyncStream[Event], on_chunk: Callable[[], object]) -> None:
    """The async form of :func:`_watch_activity`."""
    response = stream.response
    chunks = response.aiter_bytes

    async def aiter_bytes(chunk_size: int | None = None) -> AsyncIterator[bytes]:
        async for chunk in chunks(chunk_size):
            on_chunk()
            yield chunk

    response.aiter_bytes = aiter_bytes  # type: ignore[method-assign]


def _interrupt(stream: Stream[Event]) -> None:
    """Unblocks a read in progress on another thread, which then ends with :class:`APIConnectionError`.

    ``close`` must run on the iterating thread. Call this from any other thread first to wake it.
    """
    network_stream: Any = stream.response.extensions.get("network_stream")
    sock: Any = network_stream.get_extra_info("socket") if network_stream is not None else None
    if isinstance(sock, socket.socket):
        with contextlib.suppress(OSError):
            sock.shutdown(socket.SHUT_RDWR)


"""Raised by :meth:`AsyncSubscription.get` once the stream is over."""

# Completion states of one subscriber.
_OPEN: object = object()
_DONE: object = object()


class _SyncSubscriber:
    def __init__(self, accepts: Callable[[object], bool], on_activity: Callable[[], object] | None) -> None:
        self.accepts = accepts
        self.on_activity = on_activity
        self.queue: collections.deque[object] = collections.deque()
        self.completion: object = _OPEN
        self.cond = threading.Condition()

    def push(self, event: object) -> bool:
        """Queues an event. Returns ``False`` when the subscriber overflowed and must be dropped."""
        if not self.accepts(event):
            return True
        with self.cond:
            if self.completion is not _OPEN:
                return True
            if len(self.queue) >= SUBSCRIBER_CAPACITY:
                self._finish(EventOverflowError(f"Event subscriber exceeded its {SUBSCRIBER_CAPACITY}-event capacity"))
                return False
            self.queue.append(event)
            self.cond.notify_all()
        return True

    def finish(self, completion: object, *, discard: bool) -> None:
        with self.cond:
            if self.completion is _OPEN:
                self._finish(completion, discard=discard)

    def _finish(self, completion: object, *, discard: bool = True) -> None:
        self.completion = completion
        if discard:
            self.queue.clear()
        self.cond.notify_all()


class _SyncConnection:
    def __init__(self) -> None:
        self.subscribers: set[_SyncSubscriber] = set()
        self.connected: ServerConnectedEvent | None = None
        self.stopped = threading.Event()
        self.stream: Stream[Event] | None = None
        self.delivered = False

    def activity(self) -> None:
        for subscriber in list(self.subscribers):
            if subscriber.on_activity is not None:
                subscriber.on_activity()


class EventHub:
    """One shared event connection for any number of synchronous subscribers.

    ``client.events`` is the hub of a client. Create another hub with different options, such as reconnection, with
    ``EventHub(client, reconnect=True)``. A background thread reads the connection while it is open.

    Example::

        with client.events.of_type(SessionIdleEvent).for_session(session.id) as idle:
            client.session.prompt(session.id, text="Hello")
            next(idle)

    Args:
        client: The client that opens the connection.
        reconnect: ``True`` or a :class:`Reconnect` policy to reopen the connection after it drops. Off by default.
    """

    def __init__(self, client: Opencode, *, reconnect: bool | Reconnect = False) -> None:
        self._client = client
        self._reconnect = _policy(reconnect)
        self._lock = threading.Lock()
        self._current: _SyncConnection | None = None

    def subscribe(self, *, on_activity: Callable[[], object] | None = None) -> Subscription[Event]:
        """Returns a subscription to every event. It joins the shared connection when first iterated.

        Args:
            on_activity: Called on the reader thread for every chunk received, including keepalive comments.
                Use it as a liveness signal; keep it fast.
        """
        return Subscription(self, (), on_activity)

    def of_type(self, *types: type[_T]) -> Subscription[_T]:
        """Shortcut for ``subscribe().of_type(*types)``."""
        return self.subscribe().of_type(*types)

    def for_session(self, session_id: str) -> Subscription[Event]:
        """Shortcut for ``subscribe().for_session(session_id)``."""
        return self.subscribe().for_session(session_id)

    def __iter__(self) -> Iterator[Event]:
        """Iterates a new subscription. Prefer ``with hub.subscribe() as events`` to release it deterministically."""
        return iter(self.subscribe())

    def _join(self, subscriber: _SyncSubscriber) -> _SyncConnection:
        with self._lock:
            connection = self._current
            fresh = connection is None
            if connection is None:
                connection = self._current = _SyncConnection()
            connection.subscribers.add(subscriber)
            if connection.connected is not None:
                subscriber.push(connection.connected)
        if fresh:
            threading.Thread(target=self._run, args=(connection,), name="opencode-events", daemon=True).start()
        return connection

    def _leave(self, connection: _SyncConnection, subscriber: _SyncSubscriber) -> None:
        with self._lock:
            connection.subscribers.discard(subscriber)
            if not connection.subscribers:
                self._stop(connection)

    def _stop(self, connection: _SyncConnection) -> None:
        # Called with the lock held.
        connection.stopped.set()
        if self._current is connection:
            self._current = None
        if connection.stream is not None:
            _interrupt(connection.stream)

    def _publish(self, connection: _SyncConnection, event: Event) -> None:
        for subscriber in list(connection.subscribers):
            if not subscriber.push(event):
                self._leave(connection, subscriber)

    def _run(self, connection: _SyncConnection) -> None:
        error: BaseException | None = None
        attempt = 0
        try:
            while not connection.stopped.is_set():
                error = None
                connection.delivered = False
                try:
                    self._read(connection)
                except Exception as exc:
                    error = exc
                if connection.stopped.is_set():
                    error = None
                    break
                if connection.delivered:
                    attempt = 0
                if self._reconnect is None or not _retryable(error) or not self._reconnect.allows(attempt):
                    break
                delay = self._reconnect.delay(attempt)
                log.info("Event stream ended (%r); reconnecting in %.2fs", error, delay)
                attempt += 1
                if connection.stopped.wait(delay):
                    error = None
                    break
        finally:
            with self._lock:
                self._stop(connection)
                subscribers = list(connection.subscribers)
            completion = _DONE if error is None else error
            for subscriber in subscribers:
                subscriber.finish(completion, discard=False)

    def _read(self, connection: _SyncConnection) -> None:
        """Reads one connection until it ends, setting ``connection.delivered`` once an event arrives."""
        from .types import ServerConnectedEvent

        stream = self._client.event.subscribe()
        with self._lock:
            connection.stream = stream
            stopped = connection.stopped.is_set()
        try:
            if stopped:
                return
            _watch_activity(stream, connection.activity)
            # A fresh connection replays nothing yet; reconnects must not repeat server.connected.
            seen_connected = connection.connected is not None
            for event in stream:
                if connection.stopped.is_set():
                    return
                connection.delivered = True
                if isinstance(event, ServerConnectedEvent):
                    connection.connected = event
                    if seen_connected:
                        continue
                    seen_connected = True
                self._publish(connection, event)
        finally:
            connection.stream = None
            # End the iteration first, so the response's byte stream is closed with it.
            stream._iterator.close()  # pyright: ignore[reportPrivateUsage, reportAttributeAccessIssue]
            stream.close()


class Subscription(_Filters[_E]):
    """One consumer of a shared event stream. Iterate it with ``for``; close it, or use ``with``, to leave.

    The subscription joins the shared connection when entered as a context manager or first iterated, so filters
    can be chained before that::

        for event in client.events.for_session(session_id).of_type(SessionIdleEvent):
            ...

    Iteration ends when the connection ends, and raises the connection's error if it failed, after delivering the
    events already queued. ``close()`` may be called from any thread to stop a blocked iteration.
    """

    def __init__(
        self,
        hub: EventHub,
        predicates: tuple[Callable[[Any], bool], ...],
        on_activity: Callable[[], object] | None,
    ) -> None:
        self._hub = hub
        self._predicates = predicates
        self._on_activity = on_activity
        self._subscriber: _SyncSubscriber | None = None
        self._connection: _SyncConnection | None = None
        self._closed = False

    def _narrowed(self, predicate: Callable[[Any], bool]) -> Any:
        if self._subscriber is not None:
            raise RuntimeError("Filters must be added before the subscription is iterated")
        return Subscription[Any](self._hub, (*self._predicates, predicate), self._on_activity)

    def of_type(self, *types: type[_T]) -> Subscription[_T]:
        """Returns a subscription that only yields events that are instances of ``types``.

        Type checkers narrow the yielded type, so ``of_type(SessionIdleEvent)`` yields ``SessionIdleEvent``.
        """
        if not types:
            raise TypeError("of_type() needs at least one event type")
        return cast("Subscription[_T]", self._narrowed(lambda event: isinstance(event, types)))

    def for_session(self, session_id: str) -> Subscription[_E]:
        """Returns a subscription that only yields events of one session (see :func:`session_id_of`)."""
        return cast("Subscription[_E]", self._narrowed(lambda event: session_id_of(event) == session_id))

    def where(self, predicate: Callable[[_E], bool]) -> Subscription[_E]:
        """Returns a subscription that only yields events for which ``predicate`` returns true.

        The predicate runs on the reader thread, after the other filters of this subscription.
        """
        return cast("Subscription[_E]", self._narrowed(predicate))

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> _E:
        return self.get()

    def get(self, timeout: float | None = None) -> _E:
        """Returns the next event, waiting up to ``timeout`` seconds (forever when ``None``).

        Raises:
            StopIteration: The connection ended or the subscription was closed.
            TimeoutError: No event arrived in time. The subscription stays usable.
            EventOverflowError: This subscriber fell too far behind.
        """
        subscriber = self._start()
        if subscriber is None:
            raise StopIteration
        with subscriber.cond:
            if not subscriber.cond.wait_for(lambda: subscriber.queue or subscriber.completion is not _OPEN, timeout):
                raise TimeoutError("No event arrived in time")
            if subscriber.queue:
                return cast("_E", subscriber.queue.popleft())
            completion = subscriber.completion
        if isinstance(completion, BaseException):
            raise completion
        raise StopIteration

    def _start(self) -> _SyncSubscriber | None:
        if self._subscriber is None and not self._closed:
            self._subscriber = _SyncSubscriber(self._accepts, self._on_activity)
            self._connection = self._hub._join(self._subscriber)  # pyright: ignore[reportPrivateUsage]
        return self._subscriber

    def close(self) -> None:
        """Leaves the shared stream. Pending and future iterations end. Safe to call more than once."""
        self._closed = True
        subscriber, connection = self._subscriber, self._connection
        if subscriber is not None and connection is not None:
            subscriber.finish(_DONE, discard=True)
            self._hub._leave(connection, subscriber)  # pyright: ignore[reportPrivateUsage]

    def __enter__(self) -> Self:
        """Joins the shared stream now, so every event published after this point is delivered."""
        self._start()
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        self.close()


class _AsyncSubscriber:
    def __init__(self, accepts: Callable[[object], bool], on_activity: Callable[[], object] | None) -> None:
        self.accepts = accepts
        self.on_activity = on_activity
        self.queue: collections.deque[object] = collections.deque()
        self.completion: object = _OPEN
        self.wakeup: anyio.Event | None = None

    def _wake(self) -> None:
        if self.wakeup is not None:
            self.wakeup.set()
            self.wakeup = None

    def push(self, event: object) -> bool:
        if self.completion is not _OPEN or not self.accepts(event):
            return True
        if len(self.queue) >= SUBSCRIBER_CAPACITY:
            self.finish(EventOverflowError(f"Event subscriber exceeded its {SUBSCRIBER_CAPACITY}-event capacity"))
            return False
        self.queue.append(event)
        self._wake()
        return True

    def finish(self, completion: object, *, discard: bool = True) -> None:
        if self.completion is not _OPEN:
            return
        self.completion = completion
        if discard:
            self.queue.clear()
        self._wake()


class _AsyncConnection:
    def __init__(self) -> None:
        self.subscribers: set[_AsyncSubscriber] = set()
        self.connected: ServerConnectedEvent | None = None
        self.stopped = False
        self.scope: anyio.CancelScope | None = None
        self.delivered = False

    def is_stopped(self) -> bool:
        # A method, so type checkers do not narrow ``stopped`` across awaits that may change it.
        return self.stopped

    def activity(self) -> None:
        for subscriber in list(self.subscribers):
            if subscriber.on_activity is not None:
                subscriber.on_activity()


_background: set[object] = set()


def _spawn(run: Callable[[], Awaitable[None]]) -> None:
    """Starts ``run`` as a detached task of the running event loop (asyncio or trio)."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        import trio  # only reachable under trio

        trio.lowlevel.spawn_system_task(run, name="opencode-events")
        return
    task = loop.create_task(cast("Any", run()), name="opencode-events")
    _background.add(task)
    task.add_done_callback(_background.discard)


class AsyncEventHub:
    """One shared event connection for any number of asynchronous subscribers. Works with asyncio and trio.

    ``client.events`` is the hub of a client. Create another hub with different options, such as reconnection, with
    ``AsyncEventHub(client, reconnect=True)``. The connection is read by a detached task of the running event loop,
    and a hub must only be used from one event loop.

    Example::

        async with client.events.of_type(SessionIdleEvent).for_session(session.id) as idle:
            await client.session.prompt(session.id, text="Hello")
            await idle.get()

    Args:
        client: The client that opens the connection.
        reconnect: ``True`` or a :class:`Reconnect` policy to reopen the connection after it drops. Off by default.
    """

    def __init__(self, client: AsyncOpencode, *, reconnect: bool | Reconnect = False) -> None:
        self._client = client
        self._reconnect = _policy(reconnect)
        self._current: _AsyncConnection | None = None

    def subscribe(self, *, on_activity: Callable[[], object] | None = None) -> AsyncSubscription[Event]:
        """Returns a subscription to every event. It joins the shared connection when first iterated.

        Args:
            on_activity: Called for every chunk received, including keepalive comments. Use it as a liveness
                signal; keep it fast and non-blocking.
        """
        return AsyncSubscription(self, (), on_activity)

    def of_type(self, *types: type[_T]) -> AsyncSubscription[_T]:
        """Shortcut for ``subscribe().of_type(*types)``."""
        return self.subscribe().of_type(*types)

    def for_session(self, session_id: str) -> AsyncSubscription[Event]:
        """Shortcut for ``subscribe().for_session(session_id)``."""
        return self.subscribe().for_session(session_id)

    def __aiter__(self) -> AsyncIterator[Event]:
        """Iterates a new subscription. Prefer ``async with hub.subscribe() as events`` to release it."""
        return self.subscribe()

    def _join(self, subscriber: _AsyncSubscriber) -> _AsyncConnection:
        connection = self._current
        if connection is None:
            connection = self._current = _AsyncConnection()
            connection.subscribers.add(subscriber)
            _spawn(lambda: self._run(connection))
        else:
            connection.subscribers.add(subscriber)
            if connection.connected is not None:
                subscriber.push(connection.connected)
        return connection

    def _leave(self, connection: _AsyncConnection, subscriber: _AsyncSubscriber) -> None:
        connection.subscribers.discard(subscriber)
        if not connection.subscribers:
            self._stop(connection)

    def _stop(self, connection: _AsyncConnection) -> None:
        connection.stopped = True
        if self._current is connection:
            self._current = None
        if connection.scope is not None:
            connection.scope.cancel()

    def _publish(self, connection: _AsyncConnection, event: Event) -> None:
        for subscriber in list(connection.subscribers):
            if not subscriber.push(event):
                self._leave(connection, subscriber)

    async def _run(self, connection: _AsyncConnection) -> None:
        error: BaseException | None = None
        attempt = 0
        try:
            with anyio.CancelScope() as scope:
                connection.scope = scope
                if connection.stopped:
                    scope.cancel()
                while not connection.stopped:
                    error = None
                    connection.delivered = False
                    try:
                        await self._read(connection)
                    except Exception as exc:
                        error = exc
                    if connection.is_stopped():
                        break
                    if connection.delivered:
                        attempt = 0
                    if self._reconnect is None or not _retryable(error) or not self._reconnect.allows(attempt):
                        break
                    delay = self._reconnect.delay(attempt)
                    log.info("Event stream ended (%r); reconnecting in %.2fs", error, delay)
                    attempt += 1
                    await anyio.sleep(delay)
        finally:
            if connection.stopped:
                error = None
            self._stop(connection)
            completion = _DONE if error is None else error
            for subscriber in list(connection.subscribers):
                subscriber.finish(completion, discard=False)

    async def _read(self, connection: _AsyncConnection) -> None:
        """Reads one connection until it ends, setting ``connection.delivered`` once an event arrives."""
        from .types import ServerConnectedEvent

        stream: AsyncStream[Event] = await self._client.event.subscribe()
        try:
            _async_watch_activity(stream, connection.activity)
            seen_connected = connection.connected is not None
            async for event in stream:
                connection.delivered = True
                if isinstance(event, ServerConnectedEvent):
                    connection.connected = event
                    if seen_connected:
                        continue
                    seen_connected = True
                self._publish(connection, event)
        finally:
            with anyio.CancelScope(shield=True):
                # End the iteration first, so the response's byte stream is closed with it.
                await stream._iterator.aclose()  # pyright: ignore[reportPrivateUsage, reportAttributeAccessIssue]
                await stream.close()


class AsyncSubscription(_Filters[_E]):
    """One consumer of a shared event stream. Iterate it with ``async for``; close it, or use ``async with``.

    The subscription joins the shared connection when entered as a context manager or first iterated, so filters
    can be chained before that::

        async for event in client.events.for_session(session_id).of_type(SessionIdleEvent):
            ...

    Iteration ends when the connection ends, and raises the connection's error if it failed, after delivering the
    events already queued. Cancelling a task that waits for an event (``anyio.fail_after``, ``asyncio.timeout``,
    trio cancel scopes) leaves the subscription usable; close it to leave the stream.
    """

    def __init__(
        self,
        hub: AsyncEventHub,
        predicates: tuple[Callable[[Any], bool], ...],
        on_activity: Callable[[], object] | None,
    ) -> None:
        self._hub = hub
        self._predicates = predicates
        self._on_activity = on_activity
        self._subscriber: _AsyncSubscriber | None = None
        self._connection: _AsyncConnection | None = None
        self._closed = False

    def _narrowed(self, predicate: Callable[[Any], bool]) -> Any:
        if self._subscriber is not None:
            raise RuntimeError("Filters must be added before the subscription is iterated")
        return AsyncSubscription[Any](self._hub, (*self._predicates, predicate), self._on_activity)

    def of_type(self, *types: type[_T]) -> AsyncSubscription[_T]:
        """Returns a subscription that only yields events that are instances of ``types``.

        Type checkers narrow the yielded type, so ``of_type(SessionIdleEvent)`` yields ``SessionIdleEvent``.
        """
        if not types:
            raise TypeError("of_type() needs at least one event type")
        return cast("AsyncSubscription[_T]", self._narrowed(lambda event: isinstance(event, types)))

    def for_session(self, session_id: str) -> AsyncSubscription[_E]:
        """Returns a subscription that only yields events of one session (see :func:`session_id_of`)."""
        return cast("AsyncSubscription[_E]", self._narrowed(lambda event: session_id_of(event) == session_id))

    def where(self, predicate: Callable[[_E], bool]) -> AsyncSubscription[_E]:
        """Returns a subscription that only yields events for which ``predicate`` returns true."""
        return cast("AsyncSubscription[_E]", self._narrowed(predicate))

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> _E:
        try:
            return await self.get()
        except _End:
            raise StopAsyncIteration from None

    async def get(self) -> _E:
        """Returns the next event. Bound the wait with ``anyio.fail_after`` or your event loop's timeout.

        Raises:
            EndOfStream: The connection ended or the subscription was closed.
            EventOverflowError: This subscriber fell too far behind.
        """
        subscriber = self._start()
        if subscriber is None:
            raise _End
        while not subscriber.queue and subscriber.completion is _OPEN:
            wakeup = subscriber.wakeup = subscriber.wakeup or anyio.Event()
            await wakeup.wait()
        if subscriber.queue:
            return cast("_E", subscriber.queue.popleft())
        if isinstance(subscriber.completion, BaseException):
            raise subscriber.completion
        raise _End

    def _start(self) -> _AsyncSubscriber | None:
        if self._subscriber is None and not self._closed:
            self._subscriber = _AsyncSubscriber(self._accepts, self._on_activity)
            self._connection = self._hub._join(self._subscriber)  # pyright: ignore[reportPrivateUsage]
        return self._subscriber

    async def close(self) -> None:
        """Leaves the shared stream. Pending and future iterations end. Safe to call more than once."""
        self.close_nowait()
        await anyio.lowlevel.checkpoint()

    def close_nowait(self) -> None:
        """Synchronous form of :meth:`close`, for callbacks and ``finally`` blocks that cannot await."""
        self._closed = True
        subscriber, connection = self._subscriber, self._connection
        if subscriber is not None and connection is not None:
            subscriber.finish(_DONE)
            self._hub._leave(connection, subscriber)  # pyright: ignore[reportPrivateUsage]

    async def __aenter__(self) -> Self:
        """Joins the shared stream now, so every event published after this point is delivered."""
        self._start()
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        self.close_nowait()
