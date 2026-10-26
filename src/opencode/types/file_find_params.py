# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["FileFindParams", "Location"]


class FileFindParams(TypedDict, total=False):
    query: Required[str]

    limit: Optional[int]

    location: Optional[Location]

    type: Optional[Literal["file", "directory"]]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
