# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared.event_seq import EventSeq

__all__ = ["SessionLogParams"]


class SessionLogParams(TypedDict, total=False):
    after: Optional[EventSeq]

    follow: Optional[bool]
