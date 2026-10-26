# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

__all__ = ["ShellOutputParams", "Location"]


class ShellOutputParams(TypedDict, total=False):
    cursor: Optional[int]

    limit: Optional[int]

    location: Optional[Location]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
