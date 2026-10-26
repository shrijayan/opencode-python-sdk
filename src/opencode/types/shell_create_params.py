# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["ShellCreateParams", "Location"]


class ShellCreateParams(TypedDict, total=False):
    command: Required[str]

    cwd: str

    location: Optional[Location]

    metadata: Dict[str, object]

    api_timeout: Annotated[int, PropertyInfo(alias="timeout")]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
