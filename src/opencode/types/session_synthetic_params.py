# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .shared_params.session_message_id import SessionMessageID
from .shared_params.session_inbox_delivery import SessionInboxDelivery

__all__ = ["SessionSyntheticParams"]


class SessionSyntheticParams(TypedDict, total=False):
    text: Required[str]

    id: Optional[SessionMessageID]

    delivery: Optional[SessionInboxDelivery]

    description: Optional[str]

    metadata: Dict[str, object]

    resume: Optional[bool]
