# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.agent_id import AgentID
from .shared_params.model_ref import ModelRef
from .shared_params.session_id import SessionID
from .shared_params.session_metadata import SessionMetadata
from .shared_params.permission_ruleset import PermissionRuleset
from .shared_params.location_public_ref import LocationPublicRef

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    id: Optional[SessionID]

    agent: Optional[AgentID]

    location: Optional[LocationPublicRef]

    metadata: Optional[SessionMetadata]

    model: Optional[ModelRef]

    parent_id: Annotated[Optional[SessionID], PropertyInfo(alias="parentID")]

    permissions: Optional[PermissionRuleset]

    title: Optional[str]
