# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.session_id import SessionID
from .shared_params.permission_reply import PermissionReply

__all__ = ["PermissionReplyParams"]


class PermissionReplyParams(TypedDict, total=False):
    session_id: Required[Annotated[SessionID, PropertyInfo(alias="sessionID")]]

    decision: Required[PermissionReply]

    message: Optional[str]
