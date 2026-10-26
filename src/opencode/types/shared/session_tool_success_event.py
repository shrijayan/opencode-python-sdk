# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .event_id import EventID
from ..._models import BaseModel
from .event_seq import EventSeq
from .session_id import SessionID
from .location_ref import LocationRef
from .tool_content import ToolContent
from .event_version10 import EventVersion10
from .session_message_id import SessionMessageID
from .session_message_native11 import SessionMessageNative11

__all__ = ["SessionToolSuccessEvent", "Data", "Durable"]


class Data(BaseModel):
    id: str

    assistant_message_id: SessionMessageID = FieldInfo(alias="assistantMessageID")

    content: List[ToolContent]

    executed: bool

    session_id: SessionID = FieldInfo(alias="sessionID")

    metadata: Optional[Dict[str, object]] = None

    native: Optional[SessionMessageNative11] = None

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


class Durable(BaseModel):
    aggregate_id: str = FieldInfo(alias="aggregateID")

    seq: EventSeq

    version: EventVersion10

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


class SessionToolSuccessEvent(BaseModel):
    id: EventID

    created: float

    data: Data

    durable: Durable

    type: Literal["session.tool.success"]

    location: Optional[LocationRef] = None

    metadata: Optional[Dict[str, object]] = None

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
