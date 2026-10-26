# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.project_id import ProjectID

__all__ = ["WorktreeListParams"]


class WorktreeListParams(TypedDict, total=False):
    project_id: Required[Annotated[ProjectID, PropertyInfo(alias="projectID")]]
