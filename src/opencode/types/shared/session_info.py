# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .agent_id import AgentID
from ..._models import BaseModel
from .model_ref import ModelRef
from .money_usd import MoneyUSD
from .project_id import ProjectID
from .session_id import SessionID
from .relative_path import RelativePath
from .session_revert import SessionRevert
from .session_metadata import SessionMetadata
from .token_usage_info import TokenUsageInfo
from .permission_ruleset import PermissionRuleset
from .location_public_ref import LocationPublicRef
from .session_fork_boundary import SessionForkBoundary

__all__ = ["SessionInfo", "Time", "Fork"]


class Time(BaseModel):
    created: float

    updated: float

    archived: Optional[float] = None

    idle: Optional[float] = None

    viewed: Optional[float] = None

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


class Fork(BaseModel):
    boundary: SessionForkBoundary

    session_id: SessionID = FieldInfo(alias="sessionID")

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


class SessionInfo(BaseModel):
    id: SessionID

    cost: MoneyUSD

    location: LocationPublicRef

    project_id: ProjectID = FieldInfo(alias="projectID")

    time: Time

    tokens: TokenUsageInfo

    agent: Optional[AgentID] = None

    fork: Optional[Fork] = None

    metadata: Optional[SessionMetadata] = None

    model: Optional[ModelRef] = None

    outcome: Optional[Literal["succeeded", "failed", "interrupted"]] = None

    parent_id: Optional[SessionID] = FieldInfo(alias="parentID", default=None)

    permissions: Optional[PermissionRuleset] = None

    revert: Optional[SessionRevert] = None

    subpath: Optional[RelativePath] = None

    title: Optional[str] = None

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
