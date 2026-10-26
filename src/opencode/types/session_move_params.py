# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .shared.absolute_path import AbsolutePath
from .shared.session_inbox_delivery import SessionInboxDelivery

__all__ = ["SessionMoveParams"]


class SessionMoveParams(TypedDict, total=False):
    directory: Required[AbsolutePath]

    delivery: Optional[SessionInboxDelivery]
