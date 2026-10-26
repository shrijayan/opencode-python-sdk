# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .integration_method_id import IntegrationMethodID

__all__ = ["CredentialOAuth"]


class CredentialOAuth(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    access: Required[str]

    expires: Required[int]

    method_id: Required[Annotated[IntegrationMethodID, PropertyInfo(alias="methodID")]]

    refresh: Required[str]

    type: Required[Literal["oauth"]]

    metadata: Dict[str, object]
