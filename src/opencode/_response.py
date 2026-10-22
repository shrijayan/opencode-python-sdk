"""Raw HTTP response access for generated methods.

``client.session.with_raw_response.get(...)`` calls the same method, but returns an :class:`APIResponse` with the
status, headers and request instead of the parsed value; :meth:`APIResponse.parse` gives the value the plain call
would have returned. ``with_streaming_response`` does the same without reading the body, inside a context manager::

    with client.file.with_streaming_response.content(...) as response:
        for chunk in response.iter_bytes():
            ...

The generated methods are unchanged: a context variable tells the transport to hand back the response instead of
parsing it.
"""

from __future__ import annotations

import contextvars
import functools
import json
from typing import TYPE_CHECKING, Any, Generic, Literal, TypeVar, cast, overload

from typing_extensions import ParamSpec, override

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Awaitable, Callable, Iterator
    from types import TracebackType

    import httpx

    from ._pagination import AsyncCursorPage, AsyncPaginator

__all__ = [
    "APIResponse",
    "AsyncAPIResponse",
    "AsyncResponseContextManager",
    "ResponseContextManager",
]

_P = ParamSpec("_P")
_R = TypeVar("_R")
_T = TypeVar("_T")

RawMode = Literal["raw", "stream"]

_raw_mode: contextvars.ContextVar[RawMode | None] = contextvars.ContextVar("opencode_raw_mode", default=None)


def raw_mode() -> RawMode | None:
    """The raw-response mode of the current call, or ``None`` for a normal call."""
    return _raw_mode.get()


class _BaseAPIResponse(Generic[_R]):
    http_response: httpx.Response
    """The underlying ``httpx.Response``."""

    def __init__(
        self, response: httpx.Response, parser: Callable[[httpx.Response], Any], *, event_stream: bool
    ) -> None:
        self.http_response = response
        self._parser = parser
        self._event_stream = event_stream
        self._parsed: Any = _UNSET

    @property
    def headers(self) -> httpx.Headers:
        """Response headers."""
        return self.http_response.headers

    @property
    def status_code(self) -> int:
        """HTTP status code."""
        return self.http_response.status_code

    @property
    def request(self) -> httpx.Request:
        """The request that was sent (the last attempt, when it was retried)."""
        return self.http_response.request

    @property
    def url(self) -> httpx.URL:
        """The request URL."""
        return self.http_response.url

    @property
    def method(self) -> str:
        """The request method."""
        return self.http_response.request.method

    @property
    def elapsed(self) -> Any:
        """Time from sending the request to receiving the response headers."""
        return self.http_response.elapsed

    @property
    def is_closed(self) -> bool:
        """Whether the connection has been released."""
        return self.http_response.is_closed

    @override
    def __repr__(self) -> str:
        return f"<{type(self).__name__} [{self.status_code} {self.http_response.reason_phrase}]>"


class _Unset:
    pass


_UNSET = _Unset()


class APIResponse(_BaseAPIResponse[_R]):
    """An HTTP response from a sync ``with_raw_response`` / ``with_streaming_response`` call."""

    def parse(self) -> _R:
        """Returns the value the plain method call would have returned, reading the body first if needed.

        For event-stream endpoints this is the :class:`~opencode.Stream`, which consumes the body as you iterate.
        """
        if isinstance(self._parsed, _Unset):
            if not self._event_stream:
                self.read()
            self._parsed = self._parser(self.http_response)
        return cast("_R", self._parsed)

    def read(self) -> bytes:
        """Reads and returns the whole body."""
        return self.http_response.read()

    @property
    def content(self) -> bytes:
        """The whole body, read on first access."""
        return self.read()

    @property
    def text(self) -> str:
        """The body decoded as text."""
        self.read()
        return self.http_response.text

    def json(self) -> Any:
        """The body decoded as JSON."""
        return json.loads(self.read())

    def iter_bytes(self, chunk_size: int | None = None) -> Iterator[bytes]:
        """Iterates over the body in byte chunks, decoding any content encoding."""
        yield from self.http_response.iter_bytes(chunk_size)

    def iter_text(self, chunk_size: int | None = None) -> Iterator[str]:
        """Iterates over the body as decoded text chunks."""
        yield from self.http_response.iter_text(chunk_size)

    def iter_lines(self) -> Iterator[str]:
        """Iterates over the body line by line."""
        yield from self.http_response.iter_lines()

    def close(self) -> None:
        """Releases the connection without reading the rest of the body."""
        self.http_response.close()


class AsyncAPIResponse(_BaseAPIResponse[_R]):
    """An HTTP response from an async ``with_raw_response`` / ``with_streaming_response`` call."""

    async def parse(self) -> _R:
        """Returns the value the plain method call would have returned, reading the body first if needed.

        For event-stream endpoints this is the :class:`~opencode.AsyncStream`, which consumes the body as you
        iterate.
        """
        if isinstance(self._parsed, _Unset):
            if not self._event_stream:
                await self.read()
            self._parsed = self._parser(self.http_response)
        return cast("_R", self._parsed)

    async def read(self) -> bytes:
        """Reads and returns the whole body."""
        return await self.http_response.aread()

    async def text(self) -> str:
        """The body decoded as text."""
        await self.read()
        return self.http_response.text

    async def json(self) -> Any:
        """The body decoded as JSON."""
        return json.loads(await self.read())

    async def iter_bytes(self, chunk_size: int | None = None) -> AsyncIterator[bytes]:
        """Iterates over the body in byte chunks, decoding any content encoding."""
        async for chunk in self.http_response.aiter_bytes(chunk_size):
            yield chunk

    async def iter_text(self, chunk_size: int | None = None) -> AsyncIterator[str]:
        """Iterates over the body as decoded text chunks."""
        async for chunk in self.http_response.aiter_text(chunk_size):
            yield chunk

    async def iter_lines(self) -> AsyncIterator[str]:
        """Iterates over the body line by line."""
        async for line in self.http_response.aiter_lines():
            yield line

    async def close(self) -> None:
        """Releases the connection without reading the rest of the body."""
        await self.http_response.aclose()


class ResponseContextManager(Generic[_R]):
    """Sends the request on ``__enter__`` and closes the response on ``__exit__``."""

    def __init__(self, send: Callable[[], APIResponse[_R]]) -> None:
        self._send = send
        self._response: APIResponse[_R] | None = None

    def __enter__(self) -> APIResponse[_R]:
        self._response = self._send()
        return self._response

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        if self._response is not None:
            self._response.close()


class AsyncResponseContextManager(Generic[_R]):
    """Sends the request on ``__aenter__`` and closes the response on ``__aexit__``."""

    def __init__(self, send: Callable[[], Awaitable[AsyncAPIResponse[_R]]]) -> None:
        self._send = send
        self._response: AsyncAPIResponse[_R] | None = None

    async def __aenter__(self) -> AsyncAPIResponse[_R]:
        self._response = await self._send()
        return self._response

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        if self._response is not None:
            await self._response.close()


def _call_sync(mode: RawMode, func: Callable[..., Any], args: Any, kwargs: Any) -> Any:
    token = _raw_mode.set(mode)
    try:
        return func(*args, **kwargs)
    finally:
        _raw_mode.reset(token)


async def _call_async(mode: RawMode, func: Callable[..., Any], args: Any, kwargs: Any) -> Any:
    token = _raw_mode.set(mode)
    try:
        # Async list methods are plain functions; in raw mode they return a coroutine for the first page.
        return await func(*args, **kwargs)
    finally:
        _raw_mode.reset(token)


def to_raw_response_wrapper(func: Callable[_P, _R]) -> Callable[_P, APIResponse[_R]]:
    """Wraps a sync generated method so it returns an :class:`APIResponse`."""

    @functools.wraps(func)
    def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> APIResponse[_R]:
        return cast("APIResponse[_R]", _call_sync("raw", func, args, kwargs))

    return wrapped


def to_streamed_response_wrapper(func: Callable[_P, _R]) -> Callable[_P, ResponseContextManager[_R]]:
    """Wraps a sync generated method so it returns a context manager over an unread :class:`APIResponse`."""

    @functools.wraps(func)
    def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> ResponseContextManager[_R]:
        return ResponseContextManager(lambda: cast("APIResponse[_R]", _call_sync("stream", func, args, kwargs)))

    return wrapped


@overload
def async_to_raw_response_wrapper(
    func: Callable[_P, AsyncPaginator[_T]],
) -> Callable[_P, Awaitable[AsyncAPIResponse[AsyncCursorPage[_T]]]]: ...
@overload
def async_to_raw_response_wrapper(
    func: Callable[_P, Awaitable[_R]],
) -> Callable[_P, Awaitable[AsyncAPIResponse[_R]]]: ...
def async_to_raw_response_wrapper(func: Callable[_P, Any]) -> Callable[_P, Awaitable[AsyncAPIResponse[Any]]]:
    """Wraps an async generated method so it returns an :class:`AsyncAPIResponse`."""

    @functools.wraps(func)
    async def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> AsyncAPIResponse[Any]:
        return cast("AsyncAPIResponse[Any]", await _call_async("raw", func, args, kwargs))

    return wrapped


@overload
def async_to_streamed_response_wrapper(
    func: Callable[_P, AsyncPaginator[_T]],
) -> Callable[_P, AsyncResponseContextManager[AsyncCursorPage[_T]]]: ...
@overload
def async_to_streamed_response_wrapper(
    func: Callable[_P, Awaitable[_R]],
) -> Callable[_P, AsyncResponseContextManager[_R]]: ...
def async_to_streamed_response_wrapper(func: Callable[_P, Any]) -> Callable[_P, AsyncResponseContextManager[Any]]:
    """Wraps an async generated method so it returns an async context manager over an unread response."""

    @functools.wraps(func)
    def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> AsyncResponseContextManager[Any]:
        return AsyncResponseContextManager(lambda: _call_async("stream", func, args, kwargs))

    return wrapped
