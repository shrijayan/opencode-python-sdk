"""Typed Python client for the OpenCode 2.x server API.

Quick start::

    from opencode import Opencode, OpencodeServer

    with OpencodeServer() as server, Opencode(server.url, password=server.password) as client:
        session = client.session.create(agent="build")
        client.session.prompt(session.id, text="Summarize this repository")
        client.session.wait(session.id)
        for message in client.message.list(session.id):
            print(message.type)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from . import service
from ._client import AsyncOpencode, Opencode

# <generated:error-imports>
from ._errors import (
    AgentNotFoundError,
    CommandExecutionError,
    CommandNotFoundError,
    ForbiddenError,
    FormAlreadySettledError,
    FormInvalidAnswerError,
    FormNotFoundError,
    InstructionEntryValueTooLargeError,
    IntegrationAttemptNotFoundError,
    IntegrationMethodNotFoundError,
    IntegrationNotFoundError,
    InvalidCursorError,
    InvalidRequestError,
    LocationNotFoundError,
    McpServerNotFoundError,
    MessageNotFoundError,
    PermissionNotFoundError,
    PermissionSavedNotFoundError,
    ProjectNotFoundError,
    ProviderNotFoundError,
    PtyNotFoundError,
    RemoteFileNotFoundError,
    RpcError,
    RpcInternalError,
    SessionBusyError,
    SessionNotFoundError,
    ShellNotFoundError,
    SkillNotFoundError,
    UnauthorizedError,
    UnknownError,
    VcsInitNotSupportedError,
    WorktreeError,
)

# </generated:error-imports>
from ._exceptions import (
    APIConnectionError,
    APIError,
    APIResponseValidationError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    ContentTooLargeError,
    InternalServerError,
    NotFoundError,
    NotImplementedServerError,
    OpencodeError,
    PermissionDeniedError,
    RateLimitError,
    ServiceUnavailableError,
    UnprocessableEntityError,
)
from ._models import BaseModel
from ._pagination import AsyncCursorPage, AsyncPaginator, SyncCursorPage
from ._pty import AsyncPtyConnection, PtyConnection, PtyConnectionError
from ._server import AsyncOpencodeServer, OpencodeServer, ServerStartError
from ._service import Endpoint, ServiceError
from ._streaming import AsyncStream, Stream
from ._types import NOT_GIVEN, NotGiven
from ._version import __version__

# isort: split
# Hand-written helpers, kept apart from the generated error-import block above.
from ._events import (
    SUBSCRIBER_CAPACITY,
    AsyncEventHub,
    AsyncSubscription,
    EventHub,
    EventOverflowError,
    Reconnect,
    Subscription,
    session_id_of,
)
from ._rpc import (
    AsyncRpcClient,
    AsyncRpcEvents,
    RpcCallError,
    RpcCallInternalError,
    RpcClient,
    RpcDefinition,
    RpcEventDefinition,
    RpcEventPayload,
    RpcEvents,
    RpcMethod,
    rpc_event,
    rpc_method,
)

if TYPE_CHECKING:
    from . import types

# <generated:api-version>
API_VERSION = "2.1.2"
"""The OpenCode server version this client was generated from."""
# </generated:api-version>

__all__ = [
    "API_VERSION",
    "NOT_GIVEN",
    "APIConnectionError",
    "APIError",
    "APIResponseValidationError",
    "APIStatusError",
    "APITimeoutError",
    "AsyncCursorPage",
    "AsyncOpencode",
    "AsyncOpencodeServer",
    "AsyncPaginator",
    "AsyncPtyConnection",
    "AsyncStream",
    "AuthenticationError",
    "BadRequestError",
    "BaseModel",
    "ConflictError",
    "ContentTooLargeError",
    "Endpoint",
    "InternalServerError",
    "NotFoundError",
    "NotGiven",
    "NotImplementedServerError",
    "Opencode",
    "OpencodeError",
    "OpencodeServer",
    "PermissionDeniedError",
    "PtyConnection",
    "PtyConnectionError",
    "RateLimitError",
    "ServerStartError",
    "ServiceError",
    "ServiceUnavailableError",
    "Stream",
    "SyncCursorPage",
    "UnprocessableEntityError",
    "__version__",
    "service",
    "types",
    # Shared event stream and typed plugin RPC
    "SUBSCRIBER_CAPACITY",
    "AsyncEventHub",
    "AsyncRpcClient",
    "AsyncRpcEvents",
    "AsyncSubscription",
    "EventHub",
    "EventOverflowError",
    "Reconnect",
    "RpcCallError",
    "RpcCallInternalError",
    "RpcClient",
    "RpcDefinition",
    "RpcEventDefinition",
    "RpcEventPayload",
    "RpcEvents",
    "RpcMethod",
    "Subscription",
    "rpc_event",
    "rpc_method",
    "session_id_of",
    # <generated:error-exports>
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
    # </generated:error-exports>
]


def __getattr__(name: str) -> Any:
    # `opencode.types` builds several hundred models, so it is imported on first use rather than with the package.
    if name == "types":
        import importlib

        return importlib.import_module(".types", __name__)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
