# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared.session_message_id import SessionMessageID
from .shared.session_inbox_delivery import SessionInboxDelivery

__all__ = ["SessionCompactParams"]


class SessionCompactParams(TypedDict, total=False):
    id: Optional[SessionMessageID]

    delivery: Optional[SessionInboxDelivery]
