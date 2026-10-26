# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["RpcCallParams", "Location"]


class RpcCallParams(TypedDict, total=False):
    rpc_id: Required[Annotated[str, PropertyInfo(alias="rpcID")]]

    input: object

    location: Optional[Location]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
