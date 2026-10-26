# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .session_message_idle import SessionMessageIdle
from .session_message_user import SessionMessageUser
from .session_message_shell import SessionMessageShell
from .session_message_skill import SessionMessageSkill
from .session_message_system import SessionMessageSystem
from .session_message_assistant import SessionMessageAssistant
from .session_message_synthetic import SessionMessageSynthetic
from .session_message_compaction import SessionMessageCompaction
from .session_message_agent_selected import SessionMessageAgentSelected
from .session_message_model_selected import SessionMessageModelSelected
from .session_message_location_switched import SessionMessageLocationSwitched

__all__ = ["SessionMessageInfo"]

SessionMessageInfo: TypeAlias = Union[
    SessionMessageAgentSelected,
    SessionMessageModelSelected,
    SessionMessageLocationSwitched,
    SessionMessageUser,
    SessionMessageSynthetic,
    SessionMessageSystem,
    SessionMessageSkill,
    SessionMessageShell,
    SessionMessageAssistant,
    SessionMessageCompaction,
    SessionMessageIdle,
]
