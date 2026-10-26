# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.credential_entry import CredentialEntry

__all__ = ["CredentialListResponse"]

CredentialListResponse: TypeAlias = List[CredentialEntry]
