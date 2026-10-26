# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.credential_id import CredentialID
from .shared_params.integration_id import IntegrationID
from .shared_params.credential_value import CredentialValue

__all__ = ["CredentialCreateParams"]


class CredentialCreateParams(TypedDict, total=False):
    integration_id: Required[Annotated[IntegrationID, PropertyInfo(alias="integrationID")]]

    value: Required[CredentialValue]

    id: CredentialID

    activate: bool

    label: str
