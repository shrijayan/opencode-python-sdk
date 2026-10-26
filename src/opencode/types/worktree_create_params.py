# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.project_id import ProjectID
from .shared.absolute_path import AbsolutePath

__all__ = ["WorktreeCreateParams"]


class WorktreeCreateParams(TypedDict, total=False):
    project_id: Required[Annotated[ProjectID, PropertyInfo(alias="projectID")]]

    branch: str

    directory: AbsolutePath

    from_: Annotated[AbsolutePath, PropertyInfo(alias="from")]

    name: str
