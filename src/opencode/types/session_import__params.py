# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .shared.session_info import SessionInfo
from .shared.location_public_ref import LocationPublicRef

__all__ = ["SessionImportParams"]


class SessionImportParams(TypedDict, total=False):
    info: Required[SessionInfo]

    messages: Required[Iterable[object]]

    location: Optional[LocationPublicRef]
