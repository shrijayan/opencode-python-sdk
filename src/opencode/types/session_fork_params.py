# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.session_message_id import SessionMessageID

__all__ = ["SessionForkParams"]


class SessionForkParams(TypedDict, total=False):
    before: Optional[SessionMessageID]
