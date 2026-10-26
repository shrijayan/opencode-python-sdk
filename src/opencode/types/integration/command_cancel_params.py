# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.integration_id import IntegrationID

__all__ = ["CommandCancelParams", "Location"]


class CommandCancelParams(TypedDict, total=False):
    integration_id: Required[Annotated[IntegrationID, PropertyInfo(alias="integrationID")]]

    location: Optional[Location]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
