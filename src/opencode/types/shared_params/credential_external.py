# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .integration_method_id import IntegrationMethodID

__all__ = ["CredentialExternal"]


class CredentialExternal(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    method_id: Required[Annotated[IntegrationMethodID, PropertyInfo(alias="methodID")]]

    type: Required[Literal["external"]]

    metadata: Dict[str, object]
