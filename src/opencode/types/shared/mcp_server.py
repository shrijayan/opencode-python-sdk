# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .integration_id import IntegrationID
from .mcp_status_failed import McpStatusFailed
from .mcp_status_pending import McpStatusPending
from .mcp_status_disabled import McpStatusDisabled
from .mcp_status_connected import McpStatusConnected
from .mcp_status_needs_auth import McpStatusNeedsAuth

__all__ = ["McpServer", "Status"]

Status: TypeAlias = Union[McpStatusConnected, McpStatusPending, McpStatusDisabled, McpStatusFailed, McpStatusNeedsAuth]


class McpServer(BaseModel):
    name: str

    status: Status

    integration_id: Optional[IntegrationID] = FieldInfo(alias="integrationID", default=None)

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
