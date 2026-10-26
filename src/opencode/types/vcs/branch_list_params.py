# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

__all__ = ["BranchListParams", "Location"]


class BranchListParams(TypedDict, total=False):
    limit: Optional[int]

    location: Optional[Location]

    search: Optional[str]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
