# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .event_id import EventID
from ..._models import BaseModel
from .session_id import SessionID
from .location_ref import LocationRef
from .permission_id import PermissionID
from .permission_source import PermissionSource

__all__ = ["PermissionAskedEvent", "Data"]


class Data(BaseModel):
    id: PermissionID

    action: str

    resources: List[str]

    session_id: SessionID = FieldInfo(alias="sessionID")

    message: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None

    save: Optional[List[str]] = None

    source: Optional[PermissionSource] = None

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


class PermissionAskedEvent(BaseModel):
    id: EventID

    created: float

    data: Data

    type: Literal["permission.asked"]

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
