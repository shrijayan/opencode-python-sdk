# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .session_message_native2 import SessionMessageNative2
from .session_message_tool_state_error import SessionMessageToolStateError
from .session_message_tool_state_running import SessionMessageToolStateRunning
from .session_message_tool_state_completed import SessionMessageToolStateCompleted
from .session_message_tool_state_streaming import SessionMessageToolStateStreaming

__all__ = ["SessionMessageAssistantTool", "State", "Time"]

State: TypeAlias = Union[
    SessionMessageToolStateStreaming,
    SessionMessageToolStateRunning,
    SessionMessageToolStateCompleted,
    SessionMessageToolStateError,
]


class Time(BaseModel):
    created: float

    completed: Optional[float] = None

    ran: Optional[float] = None

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


class SessionMessageAssistantTool(BaseModel):
    id: str

    name: str

    state: State

    time: Time

    type: Literal["tool"]

    executed: Optional[bool] = None

    native: Optional[SessionMessageNative2] = None

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
