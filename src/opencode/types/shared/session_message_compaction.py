# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .session_message_compaction_failed import SessionMessageCompactionFailed
from .session_message_compaction_running import SessionMessageCompactionRunning
from .session_message_compaction_completed import SessionMessageCompactionCompleted

__all__ = ["SessionMessageCompaction"]

SessionMessageCompaction: TypeAlias = Union[
    SessionMessageCompactionRunning, SessionMessageCompactionCompleted, SessionMessageCompactionFailed
]
