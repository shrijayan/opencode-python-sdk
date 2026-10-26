# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..shared.permission_saved_info import PermissionSavedInfo

__all__ = ["SavedListResponse"]

SavedListResponse: TypeAlias = List[PermissionSavedInfo]
