# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

import typing as _t

from . import types
from ._types import NOT_GIVEN, Omit, NoneType, NotGiven, Transport, ProxiesTypes, omit, not_given
from ._utils import file_from_path
from ._client import (
    Client,
    Stream,
    Timeout,
    Opencode,
    Transport,
    AsyncClient,
    AsyncStream,
    AsyncOpencode,
    RequestOptions,
)
from ._models import BaseModel
from ._version import __title__, __version__
from ._response import APIResponse as APIResponse, AsyncAPIResponse as AsyncAPIResponse
from ._constants import DEFAULT_TIMEOUT, DEFAULT_MAX_RETRIES, DEFAULT_CONNECTION_LIMITS
from ._exceptions import (
    APIError,
    ConflictError,
    NotFoundError,
    OpencodeError,
    APIStatusError,
    RateLimitError,
    APITimeoutError,
    BadRequestError,
    APIConnectionError,
    AuthenticationError,
    InternalServerError,
    PermissionDeniedError,
    UnprocessableEntityError,
    APIResponseValidationError,
)
from ._base_client import DefaultHttpxClient, DefaultAioHttpClient, DefaultAsyncHttpxClient
from ._utils._logs import setup_logging as _setup_logging

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "NotGiven",
    "NOT_GIVEN",
    "not_given",
    "Omit",
    "omit",
    "OpencodeError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "Opencode",
    "AsyncOpencode",
    "file_from_path",
    "BaseModel",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_CONNECTION_LIMITS",
    "DefaultHttpxClient",
    "DefaultAsyncHttpxClient",
    "DefaultAioHttpClient",
]

if not _t.TYPE_CHECKING:
    from ._utils._resources_proxy import resources as resources

_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# opencode._exceptions.NotFoundError -> opencode.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            __locals[__name].__module__ = "opencode"
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass

# Custom code, kept by `ferrule regenerate`: the clients with this SDK's own features (lib/_client.py)
# and the public names of the hand-written modules.
from . import service  # noqa: E402
from ._pty import PtyConnection, AsyncPtyConnection, PtyConnectionError  # noqa: E402
from ._rpc import (  # noqa: E402
    RpcClient,
    RpcEvents,
    RpcMethod,
    RpcCallError,
    RpcDefinition,
    AsyncRpcClient,
    AsyncRpcEvents,
    RpcEventPayload,
    RpcEventDefinition,
    RpcCallInternalError,
    rpc_event,
    rpc_method,
)
from ._errors import *  # noqa: E402, F403
from ._errors import __all__ as _errors_all  # noqa: E402
from ._events import (  # noqa: E402
    SUBSCRIBER_CAPACITY,
    EventHub,
    Reconnect,
    Subscription,
    AsyncEventHub,
    AsyncSubscription,
    EventOverflowError,
    session_id_of,
)
from ._server import OpencodeServer, ServerStartError, AsyncOpencodeServer  # noqa: E402
from ._service import Endpoint, ServiceError  # noqa: E402
from .pagination import SyncCursorPage, AsyncCursorPage  # noqa: E402
from .lib._client import Opencode as Opencode, AsyncOpencode as AsyncOpencode  # noqa: E402
from ._base_client import AsyncPaginator  # noqa: E402

Client = Opencode
AsyncClient = AsyncOpencode

API_VERSION = "2.1.2"
"""The OpenCode server version this client was generated from."""

__all__ += [  # noqa: PLE0605
    *(_name for _name in _errors_all if _name != "TAGGED_ERRORS"),
    "API_VERSION",
    "AsyncCursorPage",
    "AsyncEventHub",
    "AsyncOpencodeServer",
    "AsyncPaginator",
    "AsyncPtyConnection",
    "AsyncRpcClient",
    "AsyncRpcEvents",
    "AsyncSubscription",
    "Endpoint",
    "EventHub",
    "EventOverflowError",
    "OpencodeServer",
    "PtyConnection",
    "PtyConnectionError",
    "Reconnect",
    "RpcCallError",
    "RpcCallInternalError",
    "RpcClient",
    "RpcDefinition",
    "RpcEventDefinition",
    "RpcEventPayload",
    "RpcEvents",
    "RpcMethod",
    "SUBSCRIBER_CAPACITY",
    "ServerStartError",
    "ServiceError",
    "Subscription",
    "SyncCursorPage",
    "rpc_event",
    "rpc_method",
    "service",
    "session_id_of",
]
