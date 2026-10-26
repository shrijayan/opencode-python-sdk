# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared.vcs_mode import VcsMode

__all__ = ["VcDiffParams", "Location"]


class VcDiffParams(TypedDict, total=False):
    mode: Required[VcsMode]

    base: Optional[str]

    context: Optional[int]

    location: Optional[Location]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
