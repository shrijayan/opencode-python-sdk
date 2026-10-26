# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .project_id import ProjectID
from .relative_path import RelativePath
from .location_public_ref import LocationPublicRef

__all__ = ["SessionInboxMovePayload"]


class SessionInboxMovePayload(BaseModel):
    location: LocationPublicRef

    project_id: ProjectID = FieldInfo(alias="projectID")

    subpath: Optional[RelativePath] = None

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
