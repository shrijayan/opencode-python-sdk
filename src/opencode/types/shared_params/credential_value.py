# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .credential_key import CredentialKey
from .credential_o_auth import CredentialOAuth
from .credential_external import CredentialExternal

__all__ = ["CredentialValue"]

CredentialValue: TypeAlias = Union[CredentialOAuth, CredentialKey, CredentialExternal]
