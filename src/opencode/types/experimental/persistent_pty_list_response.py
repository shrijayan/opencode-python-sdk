# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.persistent_pty_info import PersistentPtyInfo

__all__ = ["PersistentPtyListResponse"]

PersistentPtyListResponse: TypeAlias = List[PersistentPtyInfo]
