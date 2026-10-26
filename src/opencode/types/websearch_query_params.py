# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared.web_search_id import WebSearchID

__all__ = ["WebsearchQueryParams", "Location"]


class WebsearchQueryParams(TypedDict, total=False):
    query: Required[str]

    location: Optional[Location]

    provider_id: Annotated[WebSearchID, PropertyInfo(alias="providerID")]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
