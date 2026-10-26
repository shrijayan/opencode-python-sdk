# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .session_inbox_move import SessionInboxMove
from .session_inbox_user import SessionInboxUser
from .session_inbox_synthetic import SessionInboxSynthetic
from .session_inbox_compaction import SessionInboxCompaction

__all__ = ["SessionInboxInfo"]

SessionInboxInfo: TypeAlias = Union[SessionInboxUser, SessionInboxSynthetic, SessionInboxCompaction, SessionInboxMove]
