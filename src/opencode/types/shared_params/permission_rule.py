# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .permission_effect import PermissionEffect

__all__ = ["PermissionRule"]


class PermissionRule(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    action: Required[str]

    effect: Required[PermissionEffect]

    resource: Required[str]
