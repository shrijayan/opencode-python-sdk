# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.project_id import ProjectID
from .shared.absolute_path import AbsolutePath

__all__ = ["WorktreeRemoveParams"]


class WorktreeRemoveParams(TypedDict, total=False):
    directory: Required[AbsolutePath]

    force: Required[bool]

    project_id: Required[Annotated[ProjectID, PropertyInfo(alias="projectID")]]
