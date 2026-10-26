# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .agent_id import AgentID
from ..._models import BaseModel
from .model_ref import ModelRef
from .money_usd import MoneyUSD
from .snapshot_id import SnapshotID
from .relative_path import RelativePath
from .token_usage_info import TokenUsageInfo
from .session_message_id import SessionMessageID
from .session_message_native3 import SessionMessageNative3
from .session_structured_error import SessionStructuredError
from .session_message_assistant_text import SessionMessageAssistantText
from .session_message_assistant_tool import SessionMessageAssistantTool
from .session_message_assistant_retry import SessionMessageAssistantRetry
from .session_message_assistant_reasoning import SessionMessageAssistantReasoning

__all__ = ["SessionMessageAssistant", "Content", "Time", "Snapshot"]

Content: TypeAlias = Union[SessionMessageAssistantText, SessionMessageAssistantReasoning, SessionMessageAssistantTool]


class Time(BaseModel):
    created: float

    completed: Optional[float] = None

    streamed: Optional[float] = None

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


class Snapshot(BaseModel):
    end: Optional[SnapshotID] = None

    files: Optional[List[RelativePath]] = None

    start: Optional[SnapshotID] = None

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


class SessionMessageAssistant(BaseModel):
    id: SessionMessageID

    agent: AgentID

    content: List[Content]

    model: ModelRef

    time: Time

    type: Literal["assistant"]

    cost: Optional[MoneyUSD] = None

    error: Optional[SessionStructuredError] = None

    finish: Optional[Literal["stop", "length", "tool-calls", "content-filter", "error", "unknown"]] = None

    metadata: Optional[Dict[str, object]] = None

    native: Optional[SessionMessageNative3] = None

    raw_finish: Optional[str] = FieldInfo(alias="rawFinish", default=None)

    retry: Optional[SessionMessageAssistantRetry] = None

    snapshot: Optional[Snapshot] = None

    tokens: Optional[TokenUsageInfo] = None

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
