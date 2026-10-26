# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.project_id import ProjectID
from .shared_params.session_id import SessionID
from .shared_params.absolute_path import AbsolutePath
from .shared_params.relative_path import RelativePath
from .shared_params.sessions_cursor import SessionsCursor

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    archived: Optional[bool]

    cursor: Optional[SessionsCursor]

    directory: Optional[AbsolutePath]

    limit: Optional[int]
    """Maximum number of sessions to return. Defaults to the newest 50 sessions."""

    order: Optional[Literal["asc", "desc"]]
    """Session order for the first page.

    Use desc for newest first or asc for oldest first.
    """

    parent_id: Annotated[Optional[SessionID], PropertyInfo(alias="parentID")]

    project: Optional[ProjectID]

    search: Optional[str]

    subpath: Optional[RelativePath]
