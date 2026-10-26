# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...shared_params.session_id import SessionID

__all__ = ["EntryPutParams"]


class EntryPutParams(TypedDict, total=False):
    session_id: Required[Annotated[SessionID, PropertyInfo(alias="sessionID")]]

    value: Required[object]
