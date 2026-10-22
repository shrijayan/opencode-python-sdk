"""Server-sent event streams."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Generic, TypeVar

import httpx
import pydantic
from typing_extensions import Self

from ._exceptions import APIConnectionError, APIResponseValidationError, validation_summary

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator, AsyncIterator, Generator, Iterator
    from types import TracebackType

__all__ = ["AsyncStream", "ServerSentEvent", "Stream"]

_T = TypeVar("_T")

MAX_EVENT_BYTES = 16 * 1024 * 1024
"""Upper bound for one buffered event, matching the official TypeScript client."""


@dataclass(frozen=True)
class ServerSentEvent:
    """One decoded server-sent event."""

    data: str
    event: str | None = None
    id: str | None = None
    retry: int | None = None


@dataclass
class _Decoder:
    """Incremental SSE decoder following the WHATWG event-stream parsing rules."""

    _data: list[str] = field(default_factory=list[str])
    _event: str | None = None
    _id: str | None = None
    _retry: int | None = None
    _size: int = 0

    def feed_line(self, line: str) -> ServerSentEvent | None:
        if line == "":
            return self._dispatch()
        if line.startswith(":"):
            return None
        name, _, value = line.partition(":")
        value = value.removeprefix(" ")
        if name == "data":
            self._size += len(value)
            if self._size > MAX_EVENT_BYTES:
                raise ValueError(f"Server-sent event exceeds {MAX_EVENT_BYTES} bytes")
            self._data.append(value)
        elif name == "event":
            self._event = value
        elif name == "id":
            if "\0" not in value:
                self._id = value
        elif name == "retry" and value.isdigit():
            self._retry = int(value)
        return None

    def _dispatch(self) -> ServerSentEvent | None:
        if not self._data:
            self._event = None
            return None
        event = ServerSentEvent(data="\n".join(self._data), event=self._event, id=self._id, retry=self._retry)
        self._data = []
        self._event = None
        self._retry = None
        self._size = 0
        return event


_NEWLINE = re.compile(r"\r\n|\r|\n")


class _LineSplitter:
    """Splits decoded text into lines on CRLF, CR or LF, across chunk boundaries."""

    def __init__(self) -> None:
        self._buffer = ""

    def feed(self, chunk: str) -> list[str]:
        buffer = self._buffer + chunk
        lines: list[str] = []
        start = 0
        while (match := _NEWLINE.search(buffer, start)) is not None:
            if match.group() == "\r" and match.end() == len(buffer):
                break  # may be the first half of a CRLF split across chunks
            lines.append(buffer[start : match.start()])
            start = match.end()
        self._buffer = buffer[start:]
        if len(self._buffer) > MAX_EVENT_BYTES:
            raise ValueError(f"Server-sent event line exceeds {MAX_EVENT_BYTES} bytes")
        return lines

    def flush(self) -> list[str]:
        """Returns the final partial line, then an empty line so a pending event is dispatched."""
        rest, self._buffer = self._buffer.removesuffix("\r"), ""
        return [rest, ""] if rest else [""]


class _StreamBase(Generic[_T]):
    def __init__(self, response: httpx.Response, adapter: pydantic.TypeAdapter[_T]) -> None:
        self.response = response
        self._adapter = adapter

    def _decode(self, event: ServerSentEvent) -> _T:
        try:
            payload: Any = json.loads(event.data)
        except json.JSONDecodeError as exc:
            raise APIResponseValidationError(self.response, event.data, message="Malformed server-sent event") from exc
        try:
            return self._adapter.validate_python(payload)
        except pydantic.ValidationError as exc:
            raise APIResponseValidationError(self.response, payload, message=validation_summary(exc)) from exc


class Stream(_StreamBase[_T]):
    """A synchronous stream of decoded events.

    Iterate it to receive events. Close it, or use it as a context manager, to release the connection::

        with client.event.subscribe() as events:
            for event in events:
                ...
    """

    def __init__(self, response: httpx.Response, adapter: pydantic.TypeAdapter[_T]) -> None:
        super().__init__(response, adapter)
        self._iterator: Generator[_T, None, None] = self._events()

    def __iter__(self) -> Iterator[_T]:
        return self._iterator

    def __next__(self) -> _T:
        return next(self._iterator)

    def _events(self) -> Generator[_T, None, None]:
        decoder = _Decoder()
        try:
            splitter = _LineSplitter()
            for chunk in self.response.iter_text():
                for line in splitter.feed(chunk):
                    if (event := decoder.feed_line(line)) is not None:
                        yield self._decode(event)
            for line in splitter.flush():
                if (event := decoder.feed_line(line)) is not None:
                    yield self._decode(event)
        except (httpx.TransportError, ValueError) as exc:
            if isinstance(exc, ValueError):
                raise APIResponseValidationError(self.response, None, message=str(exc)) from exc
            raise APIConnectionError(request=self.response.request, message=f"Stream interrupted: {exc}") from exc
        finally:
            self.response.close()

    def close(self) -> None:
        """Closes the underlying connection."""
        self._iterator.close()
        self.response.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        self.close()


class AsyncStream(_StreamBase[_T]):
    """An asynchronous stream of decoded events.

    Iterate it with ``async for``. Close it, or use it as an async context manager, to release the connection::

        async with await client.event.subscribe() as events:
            async for event in events:
                ...
    """

    def __init__(self, response: httpx.Response, adapter: pydantic.TypeAdapter[_T]) -> None:
        super().__init__(response, adapter)
        self._iterator: AsyncGenerator[_T, None] = self._events()

    def __aiter__(self) -> AsyncIterator[_T]:
        return self._iterator

    async def __anext__(self) -> _T:
        return await self._iterator.__anext__()

    async def _events(self) -> AsyncGenerator[_T, None]:
        decoder = _Decoder()
        try:
            splitter = _LineSplitter()
            async for chunk in self.response.aiter_text():
                for line in splitter.feed(chunk):
                    if (event := decoder.feed_line(line)) is not None:
                        yield self._decode(event)
            for line in splitter.flush():
                if (event := decoder.feed_line(line)) is not None:
                    yield self._decode(event)
        except (httpx.TransportError, ValueError) as exc:
            if isinstance(exc, ValueError):
                raise APIResponseValidationError(self.response, None, message=str(exc)) from exc
            raise APIConnectionError(request=self.response.request, message=f"Stream interrupted: {exc}") from exc
        finally:
            await self.response.aclose()

    async def close(self) -> None:
        """Closes the underlying connection."""
        await self._iterator.aclose()
        await self.response.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self.close()
