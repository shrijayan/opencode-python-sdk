# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .prompt_file_attachment import PromptFileAttachment
from .prompt_agent_attachment import PromptAgentAttachment
from .prompt_skill_attachment import PromptSkillAttachment

__all__ = ["SessionInboxUserPayload"]


class SessionInboxUserPayload(BaseModel):
    text: str

    agents: Optional[List[PromptAgentAttachment]] = None

    files: Optional[List[PromptFileAttachment]] = None

    metadata: Optional[Dict[str, object]] = None

    skills: Optional[List[PromptSkillAttachment]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
