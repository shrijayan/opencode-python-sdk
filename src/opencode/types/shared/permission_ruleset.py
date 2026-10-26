# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .permission_rule import PermissionRule

__all__ = ["PermissionRuleset"]

PermissionRuleset: TypeAlias = List[PermissionRule]
