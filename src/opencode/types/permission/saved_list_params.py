# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.project_id import ProjectID

__all__ = ["SavedListParams"]


class SavedListParams(TypedDict, total=False):
    project_id: Annotated[Optional[ProjectID], PropertyInfo(alias="projectID")]
