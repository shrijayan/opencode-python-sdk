# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .shared.agent_id import AgentID
from .shared.permission_id import PermissionID
from .shared.permission_source import PermissionSource

__all__ = ["PermissionCreateParams"]


class PermissionCreateParams(TypedDict, total=False):
    action: Required[str]

    resources: Required[SequenceNotStr[str]]

    id: Optional[PermissionID]

    agent: Optional[AgentID]

    metadata: Dict[str, object]

    save: SequenceNotStr[str]

    source: PermissionSource
