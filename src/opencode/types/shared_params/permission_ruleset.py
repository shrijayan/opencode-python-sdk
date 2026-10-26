# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypeAlias

from .permission_rule import PermissionRule

__all__ = ["PermissionRuleset"]

PermissionRuleset: TypeAlias = Iterable[PermissionRule]
