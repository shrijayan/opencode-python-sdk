# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.session_message_id import SessionMessageID

__all__ = ["SessionShellParams"]


class SessionShellParams(TypedDict, total=False):
    command: Required[str]

    id: Optional[SessionMessageID]
