# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConnectTokenParams", "Location"]


class ConnectTokenParams(TypedDict, total=False):
    location: Optional[Location]

    x_opencode_ticket: Annotated[Optional[str], PropertyInfo(alias="x-opencode-ticket")]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
