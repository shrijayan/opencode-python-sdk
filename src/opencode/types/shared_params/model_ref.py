# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .provider_id import ProviderID

__all__ = ["ModelRef"]


class ModelRef(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    id: Required[str]

    provider_id: Required[Annotated[ProviderID, PropertyInfo(alias="providerID")]]

    variant: str
