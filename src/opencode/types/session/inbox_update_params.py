# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.session_id import SessionID
from ..shared_params.session_inbox_delivery import SessionInboxDelivery

__all__ = ["InboxUpdateParams"]


class InboxUpdateParams(TypedDict, total=False):
    session_id: Required[Annotated[SessionID, PropertyInfo(alias="sessionID")]]

    delivery: Required[SessionInboxDelivery]
