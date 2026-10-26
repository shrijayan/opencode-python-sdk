# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .agent_id import AgentID
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


class Time(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    created: Required[float]

    updated: Required[float]

    archived: float

    idle: float

    viewed: float


class Fork(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    boundary: Required[SessionForkBoundary]

    session_id: Required[Annotated[SessionID, PropertyInfo(alias="sessionID")]]


class SessionInfo(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    id: Required[SessionID]

    cost: Required[MoneyUSD]

    location: Required[LocationPublicRef]

    project_id: Required[Annotated[ProjectID, PropertyInfo(alias="projectID")]]

    time: Required[Time]

    tokens: Required[TokenUsageInfo]

    agent: AgentID

    fork: Fork

    metadata: SessionMetadata

    model: ModelRef

    outcome: Literal["succeeded", "failed", "interrupted"]

    parent_id: Annotated[SessionID, PropertyInfo(alias="parentID")]

    permissions: PermissionRuleset

    revert: SessionRevert

    subpath: RelativePath

    title: str
