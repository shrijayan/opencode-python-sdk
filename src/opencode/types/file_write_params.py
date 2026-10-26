# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["FileWriteParams", "Location"]


class FileWriteParams(TypedDict, total=False):
    path: Required[str]
    """An absolute path or a path relative to the requested location.

    Missing parent directories are created.
    """

    location: Optional[Location]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
