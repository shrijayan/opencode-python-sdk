# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.credential_id import CredentialID
from .shared.integration_id import IntegrationID
from .shared.credential_value import CredentialValue

__all__ = ["CredentialCreateParams"]


class CredentialCreateParams(TypedDict, total=False):
    integration_id: Required[Annotated[IntegrationID, PropertyInfo(alias="integrationID")]]

    value: Required[CredentialValue]

    id: CredentialID

    activate: bool

    label: str
