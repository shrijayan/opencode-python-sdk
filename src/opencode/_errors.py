"""Errors the OpenCode server declares, keyed by the ``_tag`` of the error body.

Custom code (kept by Ferrule's regeneration): the generated client's ``_make_status_error`` asks
:func:`tagged_status_error` first, so a response whose body carries a known ``_tag`` raises its
own class, a subclass of the status class Ferrule's runtime would raise (``SessionNotFoundError``
is a ``NotFoundError``). ``error`` gives the body as an :class:`ErrorBody`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Optional, cast

import pydantic

from ._exceptions import (
    APIStatusError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
)
from ._models import BaseModel

if TYPE_CHECKING:
    import httpx

__all__ = [
    "TAGGED_ERRORS",
    "ContentTooLargeError",
    "ErrorBody",
    "NotImplementedServerError",
    "ServiceUnavailableError",
    "TaggedError",
    "AgentNotFoundError",
    "CommandExecutionError",
    "CommandNotFoundError",
    "RemoteFileNotFoundError",
    "ForbiddenError",
    "FormAlreadySettledError",
    "FormInvalidAnswerError",
    "FormNotFoundError",
    "InstructionEntryValueTooLargeError",
    "IntegrationAttemptNotFoundError",
    "IntegrationMethodNotFoundError",
    "IntegrationNotFoundError",
    "InvalidCursorError",
    "InvalidRequestError",
    "LocationNotFoundError",
    "McpServerNotFoundError",
    "MessageNotFoundError",
    "PermissionNotFoundError",
    "PermissionSavedNotFoundError",
    "ProjectNotFoundError",
    "ProviderNotFoundError",
    "PtyNotFoundError",
    "RpcError",
    "RpcInternalError",
    "SessionBusyError",
    "SessionNotFoundError",
    "ShellNotFoundError",
    "SkillNotFoundError",
    "UnauthorizedError",
    "UnknownError",
    "VcsInitNotSupportedError",
    "WorktreeError",
    "tagged_status_error",
]


class ErrorBody(BaseModel):
    """The JSON body of an OpenCode error. Fields other than ``_tag`` vary by error and stay as sent."""

    tag: Optional[str] = pydantic.Field(default=None, alias="_tag")

    message: Optional[str] = None


class ContentTooLargeError(APIStatusError):
    """The request body is too large (413)."""


class NotImplementedServerError(InternalServerError):
    """The server does not implement this (501)."""


class ServiceUnavailableError(InternalServerError):
    """The server is not ready or is overloaded (503)."""


class TaggedError(APIStatusError):
    """A server error with a ``_tag`` this client knows."""

    tag: ClassVar[str | None] = None
    """The server ``_tag`` this class represents."""

    @property
    def error_tag(self) -> str | None:
        """The ``_tag`` the server sent."""
        body = self.body
        value: object = cast("dict[str, Any]", body).get("_tag") if isinstance(body, dict) else None
        return value if isinstance(value, str) else None

    @property
    def error(self) -> ErrorBody:
        """The error body as a model; it is built as sent when it does not validate."""
        raw: object = self.body
        body: dict[str, Any] = cast("dict[str, Any]", raw) if isinstance(raw, dict) else {}
        try:
            return ErrorBody.model_validate(body)
        except pydantic.ValidationError:
            return ErrorBody.model_construct(**body)


class AgentNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``AgentNotFoundError``."""

    tag = "AgentNotFoundError"


class CommandExecutionError(TaggedError, InternalServerError):
    """The server answered 500 with ``_tag`` ``CommandExecutionError``."""

    tag = "CommandExecutionError"


class CommandNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``CommandNotFoundError``."""

    tag = "CommandNotFoundError"


class RemoteFileNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``FileNotFoundError``."""

    tag = "FileNotFoundError"


class ForbiddenError(TaggedError, PermissionDeniedError):
    """The server answered 403 with ``_tag`` ``ForbiddenError``."""

    tag = "ForbiddenError"


class FormAlreadySettledError(TaggedError, ConflictError):
    """The server answered 409 with ``_tag`` ``FormAlreadySettledError``."""

    tag = "FormAlreadySettledError"


class FormInvalidAnswerError(TaggedError, BadRequestError):
    """The server answered 400 with ``_tag`` ``FormInvalidAnswerError``."""

    tag = "FormInvalidAnswerError"


class FormNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``FormNotFoundError``."""

    tag = "FormNotFoundError"


class InstructionEntryValueTooLargeError(TaggedError, ContentTooLargeError):
    """The server answered 413 with ``_tag`` ``InstructionEntryValueTooLargeError``."""

    tag = "InstructionEntryValueTooLargeError"


class IntegrationAttemptNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``IntegrationAttemptNotFoundError``."""

    tag = "IntegrationAttemptNotFoundError"


class IntegrationMethodNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``IntegrationMethodNotFoundError``."""

    tag = "IntegrationMethodNotFoundError"


class IntegrationNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``IntegrationNotFoundError``."""

    tag = "IntegrationNotFoundError"


class InvalidCursorError(TaggedError, BadRequestError):
    """The server answered 400 with ``_tag`` ``InvalidCursorError``."""

    tag = "InvalidCursorError"


class InvalidRequestError(TaggedError, BadRequestError):
    """The server answered 400 with ``_tag`` ``InvalidRequestError``."""

    tag = "InvalidRequestError"


class LocationNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``LocationNotFoundError``."""

    tag = "LocationNotFoundError"


class McpServerNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``McpServerNotFoundError``."""

    tag = "McpServerNotFoundError"


class MessageNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``MessageNotFoundError``."""

    tag = "MessageNotFoundError"


class PermissionNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``PermissionNotFoundError``."""

    tag = "PermissionNotFoundError"


class PermissionSavedNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``PermissionSavedNotFoundError``."""

    tag = "PermissionSavedNotFoundError"


class ProjectNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``ProjectNotFoundError``."""

    tag = "ProjectNotFoundError"


class ProviderNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``ProviderNotFoundError``."""

    tag = "ProviderNotFoundError"


class PtyNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``PtyNotFoundError``."""

    tag = "PtyNotFoundError"


class RpcError(TaggedError, BadRequestError):
    """The server answered 400 with ``_tag`` ``RpcError``."""

    tag = "RpcError"


class RpcInternalError(TaggedError, InternalServerError):
    """The server answered 500 with ``_tag`` ``RpcInternalError``."""

    tag = "RpcInternalError"


class SessionBusyError(TaggedError, ConflictError):
    """The server answered 409 with ``_tag`` ``SessionBusyError``."""

    tag = "SessionBusyError"


class SessionNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``SessionNotFoundError``."""

    tag = "SessionNotFoundError"


class ShellNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``ShellNotFoundError``."""

    tag = "ShellNotFoundError"


class SkillNotFoundError(TaggedError, NotFoundError):
    """The server answered 404 with ``_tag`` ``SkillNotFoundError``."""

    tag = "SkillNotFoundError"


class UnauthorizedError(TaggedError, AuthenticationError):
    """The server answered 401 with ``_tag`` ``UnauthorizedError``."""

    tag = "UnauthorizedError"


class UnknownError(TaggedError, InternalServerError):
    """The server answered 500 with ``_tag`` ``UnknownError``."""

    tag = "UnknownError"


class VcsInitNotSupportedError(TaggedError, NotImplementedServerError):
    """The server answered 501 with ``_tag`` ``VcsInitNotSupportedError``."""

    tag = "VcsInitNotSupportedError"


class WorktreeError(TaggedError, BadRequestError):
    """The server answered 400 with ``_tag`` ``WorktreeError``."""

    tag = "WorktreeError"


TAGGED_ERRORS: dict[str, type[APIStatusError]] = {
    "AgentNotFoundError": AgentNotFoundError,
    "CommandExecutionError": CommandExecutionError,
    "CommandNotFoundError": CommandNotFoundError,
    "ConflictError": ConflictError,
    "FileNotFoundError": RemoteFileNotFoundError,
    "ForbiddenError": ForbiddenError,
    "FormAlreadySettledError": FormAlreadySettledError,
    "FormInvalidAnswerError": FormInvalidAnswerError,
    "FormNotFoundError": FormNotFoundError,
    "InstructionEntryValueTooLargeError": InstructionEntryValueTooLargeError,
    "IntegrationAttemptNotFoundError": IntegrationAttemptNotFoundError,
    "IntegrationMethodNotFoundError": IntegrationMethodNotFoundError,
    "IntegrationNotFoundError": IntegrationNotFoundError,
    "InvalidCursorError": InvalidCursorError,
    "InvalidRequestError": InvalidRequestError,
    "LocationNotFoundError": LocationNotFoundError,
    "McpServerNotFoundError": McpServerNotFoundError,
    "MessageNotFoundError": MessageNotFoundError,
    "PermissionNotFoundError": PermissionNotFoundError,
    "PermissionSavedNotFoundError": PermissionSavedNotFoundError,
    "ProjectNotFoundError": ProjectNotFoundError,
    "ProviderNotFoundError": ProviderNotFoundError,
    "PtyNotFoundError": PtyNotFoundError,
    "RpcError": RpcError,
    "RpcInternalError": RpcInternalError,
    "ServiceUnavailableError": ServiceUnavailableError,
    "SessionBusyError": SessionBusyError,
    "SessionNotFoundError": SessionNotFoundError,
    "ShellNotFoundError": ShellNotFoundError,
    "SkillNotFoundError": SkillNotFoundError,
    "UnauthorizedError": UnauthorizedError,
    "UnknownError": UnknownError,
    "VcsInitNotSupportedError": VcsInitNotSupportedError,
    "WorktreeError": WorktreeError,
}

_BY_STATUS: dict[int, type[APIStatusError]] = {
    413: ContentTooLargeError,
    501: NotImplementedServerError,
    503: ServiceUnavailableError,
}


def tagged_status_error(err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError | None:
    """The error for a ``_tag`` this client knows, or for 413, 501 and 503; ``None`` otherwise."""
    tag: object = cast("dict[str, Any]", body).get("_tag") if isinstance(body, dict) else None
    cls = TAGGED_ERRORS.get(tag) if isinstance(tag, str) else None
    cls = cls or _BY_STATUS.get(response.status_code)
    return None if cls is None else cls(err_msg, response=response, body=body)
