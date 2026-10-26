# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .agent_id import AgentID
from ..._models import BaseModel
from .model_ref import ModelRef
from .agent_color import AgentColor
from .provider_request import ProviderRequest
from .permission_ruleset import PermissionRuleset

__all__ = ["AgentInfo"]


class AgentInfo(BaseModel):
    id: AgentID

    hidden: bool

    mode: Literal["subagent", "primary", "all"]

    name: str

    permissions: PermissionRuleset

    request: ProviderRequest

    color: Optional[AgentColor] = None

    description: Optional[str] = None

    model: Optional[ModelRef] = None

    steps: Optional[int] = None

    system: Optional[str] = None

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
