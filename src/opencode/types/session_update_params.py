# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.session_metadata import SessionMetadata
from .shared_params.permission_ruleset import PermissionRuleset

__all__ = ["SessionUpdateParams"]


class SessionUpdateParams(TypedDict, total=False):
    archived: Optional[bool]
    """Archive the session with true or restore it with false.

    Repeating the current state is a no-op.
    """

    metadata: Optional[SessionMetadata]

    permissions: Optional[PermissionRuleset]

    title: Optional[str]
