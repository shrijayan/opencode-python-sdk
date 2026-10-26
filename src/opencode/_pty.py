"""Interactive terminals: the PTY WebSocket endpoints.

The generator skips ``pty.connect`` and ``persistentPty.connect`` because they are WebSockets, so this module
implements them by hand and the generated ``client.pty`` and ``client.experimental.persistent_pty`` resources
mix the ``attach`` methods in. It needs the optional ``websockets`` dependency::

    pip install "opencode-python-sdk[pty]"

Protocol (OpenCode 2.1.2):

- Opening a socket takes a single-use ticket from ``POST .../connect-token`` (sent with
  ``x-opencode-ticket: 1``), passed as the ``ticket`` query parameter. Tickets expire after 60 seconds.
- ``GET /api/pty/:ptyID/connect`` takes ``location[directory]`` and an optional ``cursor`` (``-1`` skips the
  replay). The server replays buffered output, then sends one binary control frame, ``0x00`` followed by
  ``{"cursor": n}`` JSON, then live output. Output frames are UTF-8 text. Input frames are UTF-8 text or binary;
  invalid UTF-8 is dropped. Resizing goes through ``PUT /api/pty/:ptyID``.
- ``GET /api/experimental/persistent-pty/:ptyID/connect`` takes ``cursor`` (byte offset, default ``0``),
  ``role`` (``controller`` or ``observer``), ``attachment_id``, ``takeover`` and ``input_protocol``. Output frames
  are binary; text frames are JSON events: ``attached`` first, then ``replay_complete`` after the replay, and
  later ones such as ``resized``. With ``input_protocol=1`` every input frame is binary: one type byte (``0``
  control, ``1`` input), big-endian ``uint16`` columns and rows, then the input bytes. A control frame claims
  control at that size.
- Close code ``1000`` means the terminal ended; ``4404`` means it was not found, has exited or is unavailable.
"""

from __future__ import annotations

import json
import struct
import uuid
from typing import TYPE_CHECKING, Any, Literal, cast
from urllib.parse import urlencode

from typing_extensions import Self

from ._exceptions import OpencodeError
from ._resource import AsyncAPIResource, SyncAPIResource
from ._types import NOT_GIVEN, NotGiven
from .lib._support import encode_path_segment, encode_query

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping
    from types import TracebackType

    import httpx
    from websockets.asyncio.client import ClientConnection as AsyncWebSocket
    from websockets.sync.client import ClientConnection as SyncWebSocket

    from .types import Location, PtyID

__all__ = [
    "AsyncPersistentPtyAttachMixin",
    "AsyncPtyAttachMixin",
    "AsyncPtyConnection",
    "PersistentPtyAttachMixin",
    "PtyAttachMixin",
    "PtyConnection",
    "PtyConnectionError",
]

TICKET_HEADER = "x-opencode-ticket"
CLOSE_NORMAL = 1000
CLOSE_NOT_FOUND = 4404
_FRAME_CONTROL = 0
_FRAME_INPUT = 1


class PtyConnectionError(OpencodeError):
    """The terminal WebSocket could not be opened or closed abnormally.

    Attributes:
        status: HTTP status of a refused handshake (``403`` for a bad ticket, ``404`` for an unknown PTY).
        code: WebSocket close code (``4404`` when the terminal is not found, exited or unavailable).
        reason: WebSocket close reason.
    """

    def __init__(self, message: str, *, status: int | None = None, code: int | None = None, reason: str = "") -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.reason = reason


def _missing() -> PtyConnectionError:
    return PtyConnectionError(
        'Terminal support needs the websockets package. Install it with: pip install "opencode-python-sdk[pty]"'
    )


def _ws_url(base_url: httpx.URL, path: str, query: Mapping[str, object]) -> str:
    url = base_url.join(path.lstrip("/"))
    scheme = "wss" if url.scheme == "https" else "ws"
    return str(url.copy_with(scheme=scheme, query=urlencode(encode_query(query)).encode("ascii")))


def _headers(username: str, password: str | None, extra: Mapping[str, str] | None) -> dict[str, str]:
    import base64

    headers: dict[str, str] = {}
    if password is not None:
        headers["Authorization"] = "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode("ascii")
    headers.update(extra or {})
    return headers


def _handshake_error(exc: Exception) -> PtyConnectionError:
    response = getattr(exc, "response", None)
    status = cast("int | None", getattr(response, "status_code", None))
    return PtyConnectionError(f"Could not open the terminal WebSocket: {exc}", status=status)


class _Protocol:
    """Frame handling shared by the sync and async connections."""

    def __init__(self, *, persistent: bool, cols: int, rows: int) -> None:
        self.persistent = persistent
        self.cols = cols
        self.rows = rows
        self.cursor: int | None = None
        self.attached: dict[str, Any] | None = None

    def encode_input(self, data: bytes | str) -> bytes | str:
        if not self.persistent:
            return data
        payload = data.encode() if isinstance(data, str) else data
        return struct.pack(">BHH", _FRAME_INPUT, self.cols, self.rows) + payload

    def encode_control(self, cols: int, rows: int) -> bytes:
        return struct.pack(">BHH", _FRAME_CONTROL, cols, rows)

    def decode(self, frame: bytes | str) -> tuple[bytes | None, dict[str, Any] | None]:
        """Returns ``(output, event)``; control frames update the connection state and return no output."""
        if self.persistent:
            if isinstance(frame, bytes):
                # Output frames are the daemon's byte range, so the resume offset advances by their length.
                if self.cursor is not None:
                    self.cursor += len(frame)
                return frame, None
            event = cast("dict[str, Any]", json.loads(frame))
            self._apply(event)
            return None, event
        if isinstance(frame, str):
            return frame.encode(), None
        if frame[:1] == b"\x00":
            meta = cast("dict[str, Any]", json.loads(frame[1:]))
            self.cursor = int(meta["cursor"])
            return None, meta
        return frame, None

    def _apply(self, event: dict[str, Any]) -> None:
        kind = event.get("type")
        if kind == "attached":
            self.attached = event
            size = cast("dict[str, int]", event.get("info", {}).get("size") or {})
            self.cols = size.get("cols", self.cols)
            self.rows = size.get("rows", self.rows)
            self.cursor = cast("int | None", event.get("replay", {}).get("endOffset", self.cursor))
        elif kind == "replay_complete":
            self.cursor = int(event["endOffset"])
        elif kind == "resized":
            self.cols = int(event.get("cols", self.cols))
            self.rows = int(event.get("rows", self.rows))


def _closed(code: int | None, reason: str) -> PtyConnectionError | None:
    if code in (CLOSE_NORMAL, None):
        return None
    return PtyConnectionError(
        f"Terminal connection closed with code {code}: {reason or 'no reason'}", code=code, reason=reason
    )


class PtyConnection:
    """A synchronous connection to a remote terminal.

    Iterate over it, or call :meth:`recv`, for output bytes; it stops when the terminal ends. Control frames
    are handled internally: :attr:`cursor` holds the latest output position the server reported, and
    ``on_event`` (persistent terminals) receives every JSON event.

    Example::

        with client.pty.attach(pty.id) as term:
            term.send("echo hi\\n")
            for chunk in term:
                print(chunk.decode(errors="replace"), end="")
    """

    def __init__(
        self,
        ws: SyncWebSocket,
        protocol: _Protocol,
        resize: Callable[[int, int], object],
        on_event: Callable[[dict[str, Any]], object] | None = None,
    ) -> None:
        self._ws = ws
        self._protocol = protocol
        self._resize = resize
        self._on_event = on_event

    @property
    def cursor(self) -> int | None:
        """Output position to pass as ``cursor`` when reattaching, once the server has reported one."""
        return self._protocol.cursor

    @property
    def attached(self) -> dict[str, Any] | None:
        """The ``attached`` event of a persistent terminal (attachment id, role, info, replay offsets)."""
        return self._protocol.attached

    @property
    def close_code(self) -> int | None:
        """The WebSocket close code once the connection has closed."""
        return self._ws.protocol.close_code

    def send(self, data: bytes | str) -> None:
        """Writes input to the terminal. ``str`` is sent as UTF-8."""
        self._ws.send(self._protocol.encode_input(data))

    def resize(self, cols: int, rows: int) -> None:
        """Resizes the terminal."""
        if self._protocol.persistent:
            self._protocol.cols, self._protocol.rows = cols, rows
            self._ws.send(self._protocol.encode_control(cols, rows))
        else:
            self._resize(cols, rows)

    def recv(self, timeout: float | None = None) -> bytes | None:
        """Returns the next output chunk, or ``None`` once the terminal has ended.

        Raises:
            TimeoutError: No output within ``timeout`` seconds.
            PtyConnectionError: The server closed the connection abnormally (``4404``: terminal unavailable).
        """
        while (output := self._next(timeout)) == b"":
            pass
        return output

    def _next(self, timeout: float | None) -> bytes | None:
        """Reads one frame: output bytes, ``b""`` for a control frame, ``None`` after a normal close."""
        from websockets.exceptions import ConnectionClosed

        try:
            frame = self._ws.recv(timeout)
        except ConnectionClosed as exc:
            error = _closed(exc.rcvd.code if exc.rcvd else None, exc.rcvd.reason if exc.rcvd else "")
            if error is not None:
                raise error from None
            return None
        output, event = self._protocol.decode(frame)
        if event is not None and self._on_event is not None and self._protocol.persistent:
            self._on_event(event)
        return output or b""

    def wait_attached(self, timeout: float | None) -> None:
        """Reads frames until the ``attached`` event of a persistent terminal; ``attach`` already does this."""
        while self._protocol.attached is None:
            if self._next(timeout) is None:
                raise PtyConnectionError("Terminal connection closed before it was attached", code=self.close_code)

    def __iter__(self) -> Iterator[bytes]:
        while (chunk := self.recv()) is not None:
            yield chunk

    def close(self) -> None:
        """Closes the connection. The terminal keeps running on the server."""
        self._ws.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        self.close()


class AsyncPtyConnection:
    """An asyncio connection to a remote terminal. Same interface as :class:`PtyConnection`, with awaitables.

    Example::

        async with await client.pty.attach(pty.id) as term:
            await term.send("echo hi\\n")
            async for chunk in term:
                print(chunk.decode(errors="replace"), end="")
    """

    def __init__(
        self,
        ws: AsyncWebSocket,
        protocol: _Protocol,
        resize: Callable[[int, int], Awaitable[object]],
        on_event: Callable[[dict[str, Any]], object] | None = None,
    ) -> None:
        self._ws = ws
        self._protocol = protocol
        self._resize = resize
        self._on_event = on_event

    @property
    def cursor(self) -> int | None:
        """Output position to pass as ``cursor`` when reattaching, once the server has reported one."""
        return self._protocol.cursor

    @property
    def attached(self) -> dict[str, Any] | None:
        """The ``attached`` event of a persistent terminal (attachment id, role, info, replay offsets)."""
        return self._protocol.attached

    @property
    def close_code(self) -> int | None:
        """The WebSocket close code once the connection has closed."""
        return self._ws.protocol.close_code

    async def send(self, data: bytes | str) -> None:
        """Writes input to the terminal. ``str`` is sent as UTF-8."""
        await self._ws.send(self._protocol.encode_input(data))

    async def resize(self, cols: int, rows: int) -> None:
        """Resizes the terminal."""
        if self._protocol.persistent:
            self._protocol.cols, self._protocol.rows = cols, rows
            await self._ws.send(self._protocol.encode_control(cols, rows))
        else:
            await self._resize(cols, rows)

    async def recv(self) -> bytes | None:
        """Returns the next output chunk, or ``None`` once the terminal has ended.

        Raises:
            PtyConnectionError: The server closed the connection abnormally (``4404``: terminal unavailable).
        """
        while (output := await self._next()) == b"":
            pass
        return output

    async def _next(self) -> bytes | None:
        """Reads one frame: output bytes, ``b""`` for a control frame, ``None`` after a normal close."""
        from websockets.exceptions import ConnectionClosed

        try:
            frame = await self._ws.recv()
        except ConnectionClosed as exc:
            error = _closed(exc.rcvd.code if exc.rcvd else None, exc.rcvd.reason if exc.rcvd else "")
            if error is not None:
                raise error from None
            return None
        output, event = self._protocol.decode(frame)
        if event is not None and self._on_event is not None and self._protocol.persistent:
            self._on_event(event)
        return output or b""

    async def wait_attached(self) -> None:
        """Reads frames until the ``attached`` event of a persistent terminal; ``attach`` already does this."""
        while self._protocol.attached is None:
            if await self._next() is None:
                raise PtyConnectionError("Terminal connection closed before it was attached", code=self.close_code)

    async def __aiter__(self) -> AsyncIterator[bytes]:
        while (chunk := await self.recv()) is not None:
            yield chunk

    async def close(self) -> None:
        """Closes the connection. The terminal keeps running on the server."""
        await self._ws.close()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self.close()


def _open_sync(url: str, headers: dict[str, str], open_timeout: float | None) -> SyncWebSocket:
    try:
        from websockets.exceptions import InvalidHandshake
        from websockets.sync.client import connect
    except ImportError:
        raise _missing() from None
    try:
        return connect(url, additional_headers=headers, max_size=None, open_timeout=open_timeout)
    except InvalidHandshake as exc:
        raise _handshake_error(exc) from exc


async def _open_async(url: str, headers: dict[str, str], open_timeout: float | None) -> AsyncWebSocket:
    try:
        from websockets.asyncio.client import connect
        from websockets.exceptions import InvalidHandshake
    except ImportError:
        raise _missing() from None
    try:
        return await connect(url, additional_headers=headers, max_size=None, open_timeout=open_timeout)
    except InvalidHandshake as exc:
        raise _handshake_error(exc) from exc


def _require_websockets() -> None:
    try:
        import websockets  # noqa: F401  # pyright: ignore[reportUnusedImport]
    except ImportError:
        raise _missing() from None


def _pty_query(location: object, cursor: int | None, ticket: str) -> dict[str, object]:
    return {"location": location, "cursor": NOT_GIVEN if cursor is None else cursor, "ticket": ticket}


def _persistent_query(
    cursor: int, role: Literal["controller", "observer"], attachment_id: str, takeover: bool, ticket: str
) -> dict[str, object]:
    return {
        "ticket": ticket,
        "cursor": cursor,
        "role": role,
        "attachment_id": attachment_id,
        "takeover": takeover,
        "input_protocol": 1,
    }


class PtyAttachMixin(SyncAPIResource):
    """Adds :meth:`attach` to ``client.pty``."""

    def attach(
        self,
        pty_id: PtyID,
        *,
        location: Location | NotGiven | None = NOT_GIVEN,
        cursor: int | None = None,
        open_timeout: float | None = 10,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PtyConnection:
        """Opens an interactive connection to a PTY created with :meth:`create`.

        Args:
            pty_id: The PTY to attach to.
            location: Project location; defaults to the client's ``directory``.
            cursor: Output position to resume from (:attr:`PtyConnection.cursor` of an earlier connection).
                ``None`` replays the whole buffer, ``-1`` skips the replay.
            open_timeout: Seconds to wait for the WebSocket handshake.
            extra_headers: Additional handshake headers.

        Raises:
            PtyConnectionError: ``websockets`` is not installed, or the server refused the connection.

        ``GET /api/pty/:ptyID/connect`` (WebSocket)
        """
        _require_websockets()
        client = self._client
        token = client.pty.connect.token(pty_id, location=location, x_opencode_ticket="1")
        url = _ws_url(
            client.base_url,
            f"/api/pty/{encode_path_segment(pty_id)}/connect",
            _pty_query(self._location(location), cursor, token.data.ticket),
        )
        ws = _open_sync(url, _headers(client.username, client.password, extra_headers), open_timeout)

        def resize(cols: int, rows: int) -> object:
            from .types import PtyUpdateSize

            return client.pty.update(pty_id, location=location, size=PtyUpdateSize(cols=cols, rows=rows))

        return PtyConnection(ws, _Protocol(persistent=False, cols=0, rows=0), resize)


class AsyncPtyAttachMixin(AsyncAPIResource):
    """Adds :meth:`attach` to ``client.pty``."""

    async def attach(
        self,
        pty_id: PtyID,
        *,
        location: Location | NotGiven | None = NOT_GIVEN,
        cursor: int | None = None,
        open_timeout: float | None = 10,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncPtyConnection:
        """Opens an interactive connection to a PTY. See :meth:`PtyAttachMixin.attach`. Needs asyncio.

        ``GET /api/pty/:ptyID/connect`` (WebSocket)
        """
        _require_websockets()
        client = self._client
        token = await client.pty.connect.token(pty_id, location=location, x_opencode_ticket="1")
        url = _ws_url(
            client.base_url,
            f"/api/pty/{encode_path_segment(pty_id)}/connect",
            _pty_query(self._location(location), cursor, token.data.ticket),
        )
        ws = await _open_async(url, _headers(client.username, client.password, extra_headers), open_timeout)

        async def resize(cols: int, rows: int) -> object:
            from .types import PtyUpdateSize

            return await client.pty.update(pty_id, location=location, size=PtyUpdateSize(cols=cols, rows=rows))

        return AsyncPtyConnection(ws, _Protocol(persistent=False, cols=0, rows=0), resize)


class PersistentPtyAttachMixin(SyncAPIResource):
    """Adds :meth:`attach` to ``client.experimental.persistent_pty``."""

    def attach(
        self,
        pty_id: PtyID,
        *,
        cursor: int = 0,
        role: Literal["controller", "observer"] = "controller",
        attachment_id: str | None = None,
        takeover: bool = False,
        on_event: Callable[[dict[str, Any]], object] | None = None,
        open_timeout: float | None = 10,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PtyConnection:
        """Opens an interactive connection to a persistent terminal. *(experimental)*

        Args:
            pty_id: The terminal to attach to.
            cursor: Byte offset to replay from; ``0`` replays everything the server kept.
            role: ``controller`` sends input and sets the size; ``observer`` only watches.
            attachment_id: Identifies this client across reconnects; a random id by default.
            takeover: Take control from the current controller.
            on_event: Called with each JSON event (``attached``, ``replay_complete``, ``resized``, ...).
            open_timeout: Seconds to wait for the WebSocket handshake.
            extra_headers: Additional handshake headers.

        Raises:
            PtyConnectionError: ``websockets`` is not installed, or the server refused the connection.

        ``GET /api/experimental/persistent-pty/:ptyID/connect`` (WebSocket)
        """
        _require_websockets()
        client = self._client
        token = client.experimental.persistent_pty.connect_token(pty_id, x_opencode_ticket="1")
        url = _ws_url(
            client.base_url,
            f"/api/experimental/persistent-pty/{encode_path_segment(pty_id)}/connect",
            _persistent_query(cursor, role, attachment_id or str(uuid.uuid4()), takeover, token.ticket),
        )
        ws = _open_sync(url, _headers(client.username, client.password, extra_headers), open_timeout)
        protocol = _Protocol(persistent=True, cols=0, rows=0)
        connection = PtyConnection(ws, protocol, lambda cols, rows: None, on_event)
        connection.wait_attached(open_timeout)
        return connection


class AsyncPersistentPtyAttachMixin(AsyncAPIResource):
    """Adds :meth:`attach` to ``client.experimental.persistent_pty``."""

    async def attach(
        self,
        pty_id: PtyID,
        *,
        cursor: int = 0,
        role: Literal["controller", "observer"] = "controller",
        attachment_id: str | None = None,
        takeover: bool = False,
        on_event: Callable[[dict[str, Any]], object] | None = None,
        open_timeout: float | None = 10,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncPtyConnection:
        """Opens an interactive connection to a persistent terminal. See
        :meth:`PersistentPtyAttachMixin.attach`. Needs asyncio. *(experimental)*

        ``GET /api/experimental/persistent-pty/:ptyID/connect`` (WebSocket)
        """
        _require_websockets()
        client = self._client
        token = await client.experimental.persistent_pty.connect_token(pty_id, x_opencode_ticket="1")
        url = _ws_url(
            client.base_url,
            f"/api/experimental/persistent-pty/{encode_path_segment(pty_id)}/connect",
            _persistent_query(cursor, role, attachment_id or str(uuid.uuid4()), takeover, token.ticket),
        )
        ws = await _open_async(url, _headers(client.username, client.password, extra_headers), open_timeout)
        protocol = _Protocol(persistent=True, cols=0, rows=0)

        async def resize(cols: int, rows: int) -> None:
            return None

        connection = AsyncPtyConnection(ws, protocol, resize, on_event)
        await connection.wait_attached()
        return connection
