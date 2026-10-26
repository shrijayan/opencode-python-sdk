# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["PtyUpdateParams", "Location", "Size"]


class PtyUpdateParams(TypedDict, total=False):
    location: Optional[Location]

    size: Size

    title: str


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]


class SizeTyped(TypedDict, total=False):
    cols: Required[int]

    rows: Required[int]


Size: TypeAlias = Union[SizeTyped, Dict[str, object]]
