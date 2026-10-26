# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .agent_id import AgentID
from .event_id import EventID
from ..._models import BaseModel
from .event_seq import EventSeq
from .model_ref import ModelRef
from .project_id import ProjectID
from .session_id import SessionID
from .location_ref import LocationRef
from .event_version import EventVersion
from .relative_path import RelativePath
from .session_metadata import SessionMetadata
from .permission_ruleset import PermissionRuleset

__all__ = ["SessionCreatedEvent", "Data", "Durable"]


class Data(BaseModel):
    location: LocationRef

    project_id: ProjectID = FieldInfo(alias="projectID")

    session_id: SessionID = FieldInfo(alias="sessionID")

    slug: str

    version: str

    agent: Optional[AgentID] = None

    metadata: Optional[SessionMetadata] = None

    model: Optional[ModelRef] = None

    parent_id: Optional[SessionID] = FieldInfo(alias="parentID", default=None)

    permissions: Optional[PermissionRuleset] = None

    subpath: Optional[RelativePath] = None

    title: Optional[str] = None

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


class SessionCreatedEvent(BaseModel):
    id: EventID

    created: float

    data: Data

    durable: Durable

    type: Literal["session.created"]

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
