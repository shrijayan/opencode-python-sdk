# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .model_ref import ModelRef
from .money_usd import MoneyUSD
from .token_usage_info import TokenUsageInfo
from .session_message_id import SessionMessageID
from .session_message_native4 import SessionMessageNative4

__all__ = ["SessionMessageCompactionCompleted", "Time"]


class Time(BaseModel):
    created: float

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


class SessionMessageCompactionCompleted(BaseModel):
    id: SessionMessageID

    reason: Literal["auto", "manual"]

    status: Literal["completed"]

    summary: str

    time: Time

    type: Literal["compaction"]

    cost: Optional[MoneyUSD] = None

    metadata: Optional[Dict[str, object]] = None

    model: Optional[ModelRef] = None

    native: Optional[SessionMessageNative4] = None

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
