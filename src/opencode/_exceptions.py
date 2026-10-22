"""Exception hierarchy.

Every error raised by the client derives from :class:`OpencodeError`::

    OpencodeError
    └── APIError
        ├── APIConnectionError
        │   └── APITimeoutError
        ├── APIResponseValidationError
        └── APIStatusError
            ├── BadRequestError            400
            ├── AuthenticationError        401
            ├── PermissionDeniedError      403
            ├── NotFoundError              404
            ├── ConflictError              409
            ├── ContentTooLargeError       413
            ├── UnprocessableEntityError   422
            ├── RateLimitError             429
            └── InternalServerError        5xx
                ├── NotImplementedServerError  501
                └── ServiceUnavailableError    503

The server tags each declared error with a ``_tag`` such as ``"SessionNotFoundError"``. Tagged errors are raised
as the matching subclass from :mod:`opencode._errors` (for example ``SessionNotFoundError(NotFoundError)``), so
callers can catch a precise error or any error of that status.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, TypeVar

import pydantic
from typing_extensions import override

if TYPE_CHECKING:
    import httpx

_M = TypeVar("_M", bound=pydantic.BaseModel)

__all__ = [
    "APIConnectionError",
    "APIError",
    "APIResponseValidationError",
    "APIStatusError",
    "APITimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "ContentTooLargeError",
    "InternalServerError",
    "NotFoundError",
    "NotImplementedServerError",
    "OpencodeError",
    "PermissionDeniedError",
    "RateLimitError",
    "ServiceUnavailableError",
    "UnprocessableEntityError",
]


class OpencodeError(Exception):
    """Base class for every error raised by this package."""


class APIError(OpencodeError):
    """An error that happened while talking to the OpenCode server."""

    message: str
    request: httpx.Request
    body: object | None
    """The decoded JSON error body, the raw text when it is not JSON, or ``None``."""

    def __init__(self, message: str, request: httpx.Request, *, body: object | None) -> None:
        super().__init__(message)
        self.message = message
        self.request = request
        self.body = body


class APIConnectionError(APIError):
    """The request could not reach the server, or the connection broke before a response arrived."""

    def __init__(self, *, request: httpx.Request, message: str = "Connection error.") -> None:
        super().__init__(message, request, body=None)


class APITimeoutError(APIConnectionError):
    """The request timed out."""

    def __init__(self, request: httpx.Request) -> None:
        super().__init__(request=request, message="Request timed out.")


class APIResponseValidationError(APIError):
    """The server answered, but the response does not match the expected shape."""

    response: httpx.Response
    status_code: int

    def __init__(self, response: httpx.Response, body: object | None, *, message: str | None = None) -> None:
        super().__init__(
            message or "The server response did not match the expected schema.", response.request, body=body
        )
        self.response = response
        self.status_code = response.status_code


class APIStatusError(APIError):
    """The server returned a non-success HTTP status."""

    status: ClassVar[int | None] = None
    """The HTTP status this class represents, or ``None`` for the generic base."""

    tag: ClassVar[str | None] = None
    """The server ``_tag`` this class represents, or ``None`` for status-only classes."""

    response: httpx.Response
    status_code: int
    error_tag: str | None
    """The ``_tag`` the server sent, which can be a tag this client version does not know yet."""

    def __init__(self, message: str, *, response: httpx.Response, body: object | None) -> None:
        super().__init__(message, response.request, body=body)
        self.response = response
        self.status_code = response.status_code
        self.error_tag = _string_field(body, "_tag")

    def _typed_body(self, model: type[_M]) -> _M:
        body = self.body if isinstance(self.body, dict) else {}
        try:
            return model.model_validate(body)
        except pydantic.ValidationError:
            # Keep the error usable even when the body does not match this client's schema.
            return model.model_construct(**body)  # pyright: ignore[reportUnknownArgumentType]

    @property
    def request_id(self) -> str | None:
        """The server's request identifier, when it sends one."""
        return self.response.headers.get("x-request-id")

    @override
    def __str__(self) -> str:
        detail = f"{self.status_code} {self.error_tag}" if self.error_tag else str(self.status_code)
        return f"{self.message} ({detail})"


class BadRequestError(APIStatusError):
    status = 400


class AuthenticationError(APIStatusError):
    status = 401


class PermissionDeniedError(APIStatusError):
    status = 403


class NotFoundError(APIStatusError):
    status = 404


class ConflictError(APIStatusError):
    status = 409
    tag = "ConflictError"


class ContentTooLargeError(APIStatusError):
    status = 413


class UnprocessableEntityError(APIStatusError):
    status = 422


class RateLimitError(APIStatusError):
    status = 429


class InternalServerError(APIStatusError):
    status = 500


class NotImplementedServerError(InternalServerError):
    status = 501


class ServiceUnavailableError(InternalServerError):
    status = 503
    tag = "ServiceUnavailableError"


_STATUS_ERRORS: dict[int, type[APIStatusError]] = {
    cls.status: cls
    for cls in (
        BadRequestError,
        AuthenticationError,
        PermissionDeniedError,
        NotFoundError,
        ConflictError,
        ContentTooLargeError,
        UnprocessableEntityError,
        RateLimitError,
        InternalServerError,
        NotImplementedServerError,
        ServiceUnavailableError,
    )
    if cls.status is not None
}


def status_error_class(
    status_code: int, tag: str | None, tagged: dict[str, type[APIStatusError]]
) -> type[APIStatusError]:
    """Picks the most specific error class for a status code and server tag."""
    # The tag is the server's own classification, so it wins over the status code.
    if tag is not None and tag in tagged:
        return tagged[tag]
    if status_code in _STATUS_ERRORS:
        return _STATUS_ERRORS[status_code]
    if status_code >= 500:
        return InternalServerError
    return APIStatusError


def error_message(body: object | None, status_code: int) -> str:
    """Extracts a human-readable message from an error body."""
    message = _string_field(body, "message")
    if message is None and isinstance(body, dict):
        message = _string_field(body.get("data"), "message")  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType]
    if message:
        return message
    if isinstance(body, str) and body.strip():
        return body.strip()[:500]
    return f"Request failed with status {status_code}"


def _string_field(body: object | None, key: str) -> str | None:
    if isinstance(body, dict):
        value: Any = body.get(key)  # pyright: ignore[reportUnknownMemberType]
        if isinstance(value, str):
            return value
    return None
