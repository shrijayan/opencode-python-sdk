# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .event_id import EventID
from ..._models import BaseModel
from .session_id import SessionID
from .location_ref import LocationRef
from .session_message_id import SessionMessageID

__all__ = ["SessionReasoningDeltaEvent", "Data"]


class Data(BaseModel):
    assistant_message_id: SessionMessageID = FieldInfo(alias="assistantMessageID")

    delta: str

    ordinal: int

    session_id: SessionID = FieldInfo(alias="sessionID")

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


class SessionReasoningDeltaEvent(BaseModel):
    id: EventID

    created: float

    data: Data

    type: Literal["session.reasoning.delta"]

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
