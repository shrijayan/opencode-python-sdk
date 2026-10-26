# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from .shared_params.session_message_id import SessionMessageID
from .shared_params.session_inbox_delivery import SessionInboxDelivery
from .shared_params.prompt_agent_attachment import PromptAgentAttachment
from .shared_params.prompt_input_file_attachment import PromptInputFileAttachment
from .shared_params.prompt_input_skill_attachment import PromptInputSkillAttachment

__all__ = ["SessionPromptParams"]


class SessionPromptParams(TypedDict, total=False):
    text: Required[str]

    id: Optional[SessionMessageID]

    agents: Iterable[PromptAgentAttachment]

    delivery: Optional[SessionInboxDelivery]

    files: Iterable[PromptInputFileAttachment]

    metadata: Dict[str, object]

    resume: Optional[bool]

    skills: Iterable[PromptInputSkillAttachment]
