# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.session_message_id import SessionMessageID

__all__ = ["SessionDiffParams"]


class SessionDiffParams(TypedDict, total=False):
    context: Optional[int]
    """Unchanged lines around each hunk. Omit for full-file patches."""

    from_: Annotated[Optional[SessionMessageID], PropertyInfo(alias="from")]
    """User message whose turn to diff.

    Defaults to the turn of the newest user message.
    """

    to: Optional[SessionMessageID]
    """Later user message whose turn ends the range.

    Defaults to the turn of `from` alone.
    """
