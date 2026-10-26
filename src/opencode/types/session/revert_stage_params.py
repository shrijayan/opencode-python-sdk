# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.session_message_id import SessionMessageID

__all__ = ["RevertStageParams"]


class RevertStageParams(TypedDict, total=False):
    message_id: Required[Annotated[SessionMessageID, PropertyInfo(alias="messageID")]]

    files: Optional[bool]
