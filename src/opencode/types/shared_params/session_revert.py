# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .snapshot_id import SnapshotID
from .file_diff_info import FileDiffInfo
from .session_message_id import SessionMessageID

__all__ = ["SessionRevert"]


class SessionRevert(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    message_id: Required[Annotated[SessionMessageID, PropertyInfo(alias="messageID")]]

    files: Iterable[FileDiffInfo]

    part_id: Annotated[str, PropertyInfo(alias="partID")]

    snapshot: SnapshotID
