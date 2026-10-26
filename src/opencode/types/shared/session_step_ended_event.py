# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .event_id import EventID
from ..._models import BaseModel
from .event_seq import EventSeq
from .money_usd import MoneyUSD
from .session_id import SessionID
from .snapshot_id import SnapshotID
from .location_ref import LocationRef
from .event_version import EventVersion
from .relative_path import RelativePath
from .token_usage_info import TokenUsageInfo
from .session_message_id import SessionMessageID
from .session_message_native5 import SessionMessageNative5

__all__ = ["SessionStepEndedEvent", "Data", "Durable"]


class Data(BaseModel):
    assistant_message_id: SessionMessageID = FieldInfo(alias="assistantMessageID")

    cost: MoneyUSD

    finish: Literal["stop", "length", "tool-calls", "content-filter", "error", "unknown"]

    session_id: SessionID = FieldInfo(alias="sessionID")

    tokens: TokenUsageInfo

    files: Optional[List[RelativePath]] = None

    native: Optional[SessionMessageNative5] = None

    raw_finish: Optional[str] = FieldInfo(alias="rawFinish", default=None)

    snapshot: Optional[SnapshotID] = None

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

    version: EventVersion

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


class SessionStepEndedEvent(BaseModel):
    id: EventID

    created: float

    data: Data

    durable: Durable

    type: Literal["session.step.ended"]

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
