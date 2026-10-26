# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .mcp_protocol import McpProtocol
from .mcp_o_auth_config import McpOAuthConfig

__all__ = ["McpRemoteConfig", "Oauth", "Timeout"]

Oauth: TypeAlias = Union[Literal[False], McpOAuthConfig]


class Timeout(BaseModel):
    catalog: Optional[int] = None

    execution: Optional[int] = None

    startup: Optional[int] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class McpRemoteConfig(BaseModel):
    type: Literal["remote"]

    url: str

    codemode: Optional[bool] = None

    disabled: Optional[bool] = None

    headers: Optional[Dict[str, str]] = None

    oauth: Optional[Oauth] = None

    protocol: Optional[McpProtocol] = None
    """MCP protocol negotiation.

    "legacy" (default) opens with the initialize handshake and speaks protocol
    revisions up to 2025-11-25. "auto" probes for the 2026-07-28 revision and falls
    back to legacy when the server does not support it. "2026-07-28" requires that
    revision and fails otherwise.
    """

    timeout: Optional[Timeout] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
