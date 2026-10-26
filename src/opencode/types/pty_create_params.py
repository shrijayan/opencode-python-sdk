# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = ["PtyCreateParams", "Location"]


class PtyCreateParams(TypedDict, total=False):
    args: SequenceNotStr[str]

    command: str

    cwd: str

    env: Dict[str, str]

    location: Optional[Location]

    title: str


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
