# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PermissionSource"]


class PermissionSource(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    type: Required[Literal["tool"]]
