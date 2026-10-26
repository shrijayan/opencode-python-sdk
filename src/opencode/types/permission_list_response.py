# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.permission_request import PermissionRequest

__all__ = ["PermissionListResponse"]

PermissionListResponse: TypeAlias = List[PermissionRequest]
