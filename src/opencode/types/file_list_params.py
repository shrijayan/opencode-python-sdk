# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

__all__ = ["FileListParams", "Location"]


class FileListParams(TypedDict, total=False):
    location: Optional[Location]

    path: Optional[str]
    """An absolute path or a path relative to the requested location.

    Defaults to the location directory.
    """


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
