# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.integration_method_id import IntegrationMethodID

__all__ = ["CommandConnectParams", "Location"]


class CommandConnectParams(TypedDict, total=False):
    method_id: Required[Annotated[IntegrationMethodID, PropertyInfo(alias="methodID")]]

    label: Optional[str]

    location: Optional[Location]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
