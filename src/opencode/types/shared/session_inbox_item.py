# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .session_inbox_delivery import SessionInboxDelivery
from .session_inbox_user_payload import SessionInboxUserPayload
from .session_inbox_move_payload1 import SessionInboxMovePayload1
from .session_inbox_synthetic_payload import SessionInboxSyntheticPayload
from .session_inbox_compaction_payload import SessionInboxCompactionPayload

__all__ = [
    "SessionInboxItem",
    "SessionInboxItemVariant0",
    "SessionInboxItemVariant1",
    "SessionInboxItemVariant2",
    "SessionInboxItemVariant3",
]


class SessionInboxItemVariant0(BaseModel):
    delivery: SessionInboxDelivery

    payload: SessionInboxUserPayload

    type: Literal["user"]

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


class SessionInboxItemVariant1(BaseModel):
    delivery: SessionInboxDelivery

    payload: SessionInboxSyntheticPayload

    type: Literal["synthetic"]

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


class SessionInboxItemVariant2(BaseModel):
    delivery: SessionInboxDelivery

    payload: SessionInboxCompactionPayload

    type: Literal["compaction"]

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


class SessionInboxItemVariant3(BaseModel):
    delivery: SessionInboxDelivery

    payload: SessionInboxMovePayload1

    type: Literal["move"]

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


SessionInboxItem: TypeAlias = Union[
    SessionInboxItemVariant0, SessionInboxItemVariant1, SessionInboxItemVariant2, SessionInboxItemVariant3
]
