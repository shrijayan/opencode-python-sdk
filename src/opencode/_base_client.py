"""HTTP transport shared by the sync and async clients.

This module is the only place that talks to httpx. It builds requests, applies authentication, retries
transient failures, and turns responses into typed values or errors.
"""

from __future__ import annotations

import base64
import builtins
import email.utils
import functools
import json
import logging
import os
import platform
import random
import time
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

import anyio
import httpx
import pydantic
from typing_extensions import Self, override

from . import _constants as constants
from ._errors import TAGGED_ERRORS
from ._exceptions import (
    APIConnectionError,
    APIResponseValidationError,
    APIStatusError,
    APITimeoutError,
    OpencodeError,
    error_message,
    status_error_class,
    validation_summary,
)
from ._qs import encode_query, to_jsonable
from ._streaming import AsyncStream, Stream
from ._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout
from ._version import __version__

if TYPE_CHECKING:
    from collections.abc import Mapping
    from types import TracebackType

    from ._pagination import AsyncPaginator, SyncCursorPage

__all__ = ["AsyncAPIClient", "SyncAPIClient"]

log = logging.getLogger("opencode")

_T = TypeVar("_T")

ResponseKind = Literal["json", "void", "binary"]


@functools.cache
def _cached_adapter(tp: Any) -> pydantic.TypeAdapter[Any]:
    return pydantic.TypeAdapter(tp)


@functools.cache
def _resolve_type(expr: str) -> Any:
    # Generated resources name their response types as strings, so `import opencode` does not build every model.
    from . import types

    return eval(expr, {**vars(types), "builtins": builtins})  # expressions come from the generator


def type_adapter(tp: Any) -> pydantic.TypeAdapter[Any]:
    """Returns a cached ``TypeAdapter`` for a response type, or for a type expression over ``opencode.types``."""
    if isinstance(tp, str):
        tp = _resolve_type(tp)
    try:
        return _cached_adapter(tp)
    except TypeError:  # unhashable type expression
        return pydantic.TypeAdapter(tp)


@dataclass
class RequestOptions:
    """Everything needed to send one request. Generated methods build these."""

    method: str
    path: str
    query: Mapping[str, object] = field(default_factory=dict[str, object])
    headers: Mapping[str, object] = field(default_factory=dict[str, object])
    body: object | NotGiven = NOT_GIVEN
    content: bytes | None = None
    extra_headers: Headers | None = None
    extra_query: Query | None = None
    extra_body: Body | None = None
    timeout: Timeout | NotGiven = NOT_GIVEN
    stream: bool = False

    @property
    def idempotent(self) -> bool:
        return self.method.upper() in constants.IDEMPOTENT_METHODS


def _platform_headers() -> dict[str, str]:
    return {
        "User-Agent": f"opencode-python/{__version__} python/{platform.python_version()} httpx/{httpx.__version__}",
    }


def _resolve_password(password: str | None) -> str | None:
    if password is not None:
        return password or None
    for name in constants.PASSWORD_ENVS:
        value = os.environ.get(name)
        if value:
            return value
    return None


def _resolve_base_url(base_url: str | httpx.URL | None) -> httpx.URL:
    if base_url is None:
        base_url = os.environ.get(constants.BASE_URL_ENV)
    if not base_url:
        raise OpencodeError(
            "No OpenCode server URL. Pass base_url=..., set the OPENCODE_BASE_URL environment variable, "
            "or start a server with opencode.OpencodeServer()."
        )
    url = httpx.URL(str(base_url))
    if url.scheme not in ("http", "https"):
        raise OpencodeError(f"OpenCode base_url must be an http(s) URL, got {str(base_url)!r}")
    # A path prefix on the base URL is kept: requests are joined relative to it.
    return url if url.raw_path.endswith(b"/") else url.copy_with(raw_path=url.raw_path + b"/")


class _BaseClient:
    """Configuration and request building shared by both clients."""

    base_url: httpx.URL
    username: str
    password: str | None
    timeout: Timeout
    max_retries: int
    directory: str | None

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None,
        password: str | None,
        username: str,
        directory: str | os.PathLike[str] | None,
        timeout: Timeout,
        max_retries: int,
        default_headers: Mapping[str, str] | None,
        default_query: Mapping[str, object] | None,
    ) -> None:
        if max_retries < 0:
            raise ValueError("max_retries must be zero or more")
        self.base_url = _resolve_base_url(base_url)
        self.username = username
        self.password = _resolve_password(password)
        self._authorization = (
            None
            if self.password is None
            else "Basic " + base64.b64encode(f"{username}:{self.password}".encode()).decode("ascii")
        )
        self.directory = os.fspath(directory) if directory is not None else None
        self.timeout = timeout
        self.max_retries = max_retries
        self._default_headers = dict(default_headers or {})
        self._default_query = dict(default_query or {})

    @override
    def __repr__(self) -> str:
        # Never include the password.
        return f"{type(self).__name__}(base_url={str(self.base_url)!r})"

    def _build_request(self, options: RequestOptions) -> httpx.Request:
        url = self.base_url.join(options.path.lstrip("/"))
        query = {**self._default_query, **options.query, **(options.extra_query or {})}

        headers: dict[str, str] = {"Accept": "application/json", **_platform_headers(), **self._default_headers}
        for name, value in {**options.headers, **(options.extra_headers or {})}.items():
            if isinstance(value, NotGiven):
                headers.pop(name, None)
            elif value is not None:
                headers[name] = str(value)
        if options.stream:
            headers["Accept"] = "text/event-stream"
        if self._authorization is not None and "Authorization" not in headers:
            headers["Authorization"] = self._authorization

        content: bytes | None = options.content
        if content is not None:
            headers.setdefault("Content-Type", "application/octet-stream")
        elif not isinstance(options.body, NotGiven) or options.extra_body:
            body: Any = to_jsonable(options.body) if not isinstance(options.body, NotGiven) else {}
            if options.extra_body:
                if not isinstance(body, dict):
                    raise TypeError("extra_body can only be used with JSON object bodies")
                extra: dict[str, Any] = to_jsonable(options.extra_body)
                body = {**cast("dict[str, Any]", body), **extra}
            content = _json_bytes(body)
            headers["Content-Type"] = "application/json"

        timeout = self.timeout if isinstance(options.timeout, NotGiven) else options.timeout
        if options.stream and isinstance(options.timeout, NotGiven):
            # Event streams stay open between events, so only bound the connect phase by default.
            base = timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)
            timeout = httpx.Timeout(connect=base.connect, read=None, write=base.write, pool=base.pool)
        return httpx.Request(
            options.method,
            url,
            params=httpx.QueryParams(cast("list[tuple[str, str | int | float | bool | None]]", encode_query(query))),
            headers=headers,
            content=content,
            extensions={"timeout": _timeout_dict(timeout)},
        )

    def _status_error(self, response: httpx.Response, raw: object) -> APIStatusError:
        body: object = raw
        fields = cast("dict[str, Any]", raw) if isinstance(raw, dict) else {}
        tag: object = fields.get("_tag")
        cls = status_error_class(response.status_code, tag if isinstance(tag, str) else None, TAGGED_ERRORS)
        return cls(error_message(body, response.status_code), response=response, body=body)

    def _should_retry_status(self, options: RequestOptions, response: httpx.Response) -> bool:
        statuses = constants.RETRYABLE_STATUSES if options.idempotent else constants.RETRYABLE_STATUSES_UNSAFE
        return response.status_code in statuses

    @staticmethod
    def _should_retry_error(options: RequestOptions, error: httpx.TransportError) -> bool:
        # These fail before the request reaches the server, so retrying never repeats work.
        if isinstance(error, (httpx.ConnectError, httpx.ConnectTimeout, httpx.PoolTimeout)):
            return True
        return options.idempotent

    @staticmethod
    def _retry_delay(attempt: int, response: httpx.Response | None) -> float:
        if response is not None:
            retry_after = _parse_retry_after(response.headers)
            if retry_after is not None and 0 <= retry_after <= constants.MAX_RETRY_AFTER:
                return retry_after
        delay: float = min(constants.INITIAL_RETRY_DELAY * 2.0**attempt, constants.MAX_RETRY_DELAY)
        return delay * (1 - 0.25 * random.random())

    @staticmethod
    def _decode_error_body(response: httpx.Response) -> object:
        if not response.content:
            return None
        try:
            return response.json()
        except ValueError:
            return response.text

    def _parse(self, response: httpx.Response, kind: ResponseKind, response_type: Any, unwrap: bool) -> Any:
        if kind == "void":
            return None
        if kind == "binary":
            return response.content
        try:
            payload: Any = response.json()
        except ValueError as exc:
            raise APIResponseValidationError(response, response.text, message="Response is not valid JSON") from exc
        if unwrap:
            if not isinstance(payload, dict) or "data" not in payload:
                raise APIResponseValidationError(
                    response, cast("object", payload), message="Response has no `data` field"
                )
            payload = cast("dict[str, Any]", payload)["data"]
        try:
            return type_adapter(response_type).validate_python(payload)
        except pydantic.ValidationError as exc:
            raise APIResponseValidationError(response, payload, message=validation_summary(exc)) from exc


def _json_bytes(body: object) -> bytes:
    return json.dumps(body, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def _timeout_dict(timeout: Timeout) -> dict[str, float | None]:
    resolved = timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)
    return resolved.as_dict()


def _parse_retry_after(headers: httpx.Headers) -> float | None:
    milliseconds = headers.get("retry-after-ms")
    if milliseconds is not None:
        try:
            return float(milliseconds) / 1000
        except ValueError:
            pass
    value = headers.get("retry-after")
    if value is None:
        return None
    try:
        return float(value)
    except ValueError:
        parsed = email.utils.parsedate_to_datetime(value) if value else None
        if parsed is None:
            return None
        return max(parsed.timestamp() - time.time(), 0.0)


class SyncAPIClient(_BaseClient):
    """Synchronous transport. Thread-safe: share one client across threads."""

    _http: httpx.Client

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None,
        password: str | None,
        username: str,
        directory: str | os.PathLike[str] | None,
        timeout: Timeout,
        max_retries: int,
        default_headers: Mapping[str, str] | None,
        default_query: Mapping[str, object] | None,
        http_client: httpx.Client | None,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        super().__init__(
            base_url=base_url,
            password=password,
            username=username,
            directory=directory,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
        )
        self._owns_http = http_client is None
        if http_client is not None and transport is not None:
            raise ValueError("Pass either http_client or transport, not both")
        self._http = http_client or httpx.Client(
            limits=constants.DEFAULT_CONNECTION_LIMITS, follow_redirects=True, transport=transport
        )

    def close(self) -> None:
        """Closes the connection pool, unless it was passed in by the caller."""
        if self._owns_http:
            self._http.close()

    @property
    def is_closed(self) -> bool:
        return self._http.is_closed

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        self.close()

    def _send(self, options: RequestOptions) -> httpx.Response:
        attempt = 0
        while True:
            request = self._build_request(options)
            log.debug("Request %s %s (attempt %d)", request.method, request.url, attempt + 1)
            try:
                response = self._http.send(request, stream=options.stream)
            except httpx.TransportError as exc:
                if attempt < self.max_retries and self._should_retry_error(options, exc):
                    delay = self._retry_delay(attempt, None)
                    log.info("Retrying %s %s in %.2fs after %s", request.method, request.url, delay, type(exc).__name__)
                    time.sleep(delay)
                    attempt += 1
                    continue
                if isinstance(exc, httpx.TimeoutException):
                    raise APITimeoutError(request) from exc
                raise APIConnectionError(request=request, message=f"Connection error: {exc}") from exc

            log.debug("Response %s %s -> %d", request.method, request.url, response.status_code)
            if response.is_success:
                return response
            if attempt < self.max_retries and self._should_retry_status(options, response):
                delay = self._retry_delay(attempt, response)
                response.close()
                log.info(
                    "Retrying %s %s in %.2fs after status %d", request.method, request.url, delay, response.status_code
                )
                time.sleep(delay)
                attempt += 1
                continue
            if options.stream:
                response.read()
            raise self._status_error(response, self._decode_error_body(response))

    def request(
        self,
        options: RequestOptions,
        *,
        kind: ResponseKind = "json",
        response_type: Any = object,
        unwrap: bool = False,
    ) -> Any:
        """Sends a request and returns the decoded response."""
        response = self._send(options)
        return self._parse(response, kind, response_type, unwrap)

    def stream(self, options: RequestOptions, *, item_type: type[_T] | Any) -> Stream[Any]:
        """Opens a server-sent event stream."""
        options.stream = True
        response = self._send(options)
        content_type = response.headers.get("content-type", "")
        if content_type.split(";", 1)[0].strip().lower() != "text/event-stream":
            response.read()
            response.close()
            raise APIResponseValidationError(
                response, response.text, message=f"Expected an event stream, got {content_type!r}"
            )
        return Stream(response, type_adapter(item_type))

    def page(self, options: RequestOptions, *, response_type: Any) -> SyncCursorPage[Any]:
        """Fetches the first page of a cursor-paginated list."""
        from ._pagination import SyncCursorPage

        return SyncCursorPage.fetch(self, options, response_type)


class AsyncAPIClient(_BaseClient):
    """Asynchronous transport. Works with asyncio and trio."""

    _http: httpx.AsyncClient

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None,
        password: str | None,
        username: str,
        directory: str | os.PathLike[str] | None,
        timeout: Timeout,
        max_retries: int,
        default_headers: Mapping[str, str] | None,
        default_query: Mapping[str, object] | None,
        http_client: httpx.AsyncClient | None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        super().__init__(
            base_url=base_url,
            password=password,
            username=username,
            directory=directory,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
        )
        self._owns_http = http_client is None
        if http_client is not None and transport is not None:
            raise ValueError("Pass either http_client or transport, not both")
        self._http = http_client or httpx.AsyncClient(
            limits=constants.DEFAULT_CONNECTION_LIMITS, follow_redirects=True, transport=transport
        )

    async def close(self) -> None:
        """Closes the connection pool, unless it was passed in by the caller."""
        if self._owns_http:
            await self._http.aclose()

    @property
    def is_closed(self) -> bool:
        return self._http.is_closed

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self.close()

    async def _send(self, options: RequestOptions) -> httpx.Response:
        attempt = 0
        while True:
            request = self._build_request(options)
            log.debug("Request %s %s (attempt %d)", request.method, request.url, attempt + 1)
            try:
                response = await self._http.send(request, stream=options.stream)
            except httpx.TransportError as exc:
                if attempt < self.max_retries and self._should_retry_error(options, exc):
                    delay = self._retry_delay(attempt, None)
                    log.info("Retrying %s %s in %.2fs after %s", request.method, request.url, delay, type(exc).__name__)
                    await anyio.sleep(delay)
                    attempt += 1
                    continue
                if isinstance(exc, httpx.TimeoutException):
                    raise APITimeoutError(request) from exc
                raise APIConnectionError(request=request, message=f"Connection error: {exc}") from exc

            log.debug("Response %s %s -> %d", request.method, request.url, response.status_code)
            if response.is_success:
                return response
            if attempt < self.max_retries and self._should_retry_status(options, response):
                delay = self._retry_delay(attempt, response)
                await response.aclose()
                log.info(
                    "Retrying %s %s in %.2fs after status %d", request.method, request.url, delay, response.status_code
                )
                await anyio.sleep(delay)
                attempt += 1
                continue
            if options.stream:
                await response.aread()
            raise self._status_error(response, self._decode_error_body(response))

    async def request(
        self,
        options: RequestOptions,
        *,
        kind: ResponseKind = "json",
        response_type: Any = object,
        unwrap: bool = False,
    ) -> Any:
        """Sends a request and returns the decoded response."""
        response = await self._send(options)
        return self._parse(response, kind, response_type, unwrap)

    async def stream(self, options: RequestOptions, *, item_type: type[_T] | Any) -> AsyncStream[Any]:
        """Opens a server-sent event stream."""
        options.stream = True
        response = await self._send(options)
        content_type = response.headers.get("content-type", "")
        if content_type.split(";", 1)[0].strip().lower() != "text/event-stream":
            await response.aread()
            await response.aclose()
            raise APIResponseValidationError(
                response, response.text, message=f"Expected an event stream, got {content_type!r}"
            )
        return AsyncStream(response, type_adapter(item_type))

    def page(self, options: RequestOptions, *, response_type: Any) -> AsyncPaginator[Any]:
        """Returns an awaitable, async-iterable paginator over a cursor-paginated list."""
        from ._pagination import AsyncPaginator

        return AsyncPaginator(self, options, response_type)
