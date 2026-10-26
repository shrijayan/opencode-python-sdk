# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.project_id import ProjectID

__all__ = ["SessionStatsParams"]


class SessionStatsParams(TypedDict, total=False):
    from_: Annotated[Union[Literal["Infinity", "-Infinity", "NaN"], float, None], PropertyInfo(alias="from")]

    project: Optional[ProjectID]

    timezone: Optional[str]

    to: Union[Literal["Infinity", "-Infinity", "NaN"], float, None]

    tools: Optional[Literal["none", "summary", "detail"]]
