# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .project_id import ProjectID
from .project_vcs import ProjectVcs
from .project_icon import ProjectIcon
from .project_time import ProjectTime
from .absolute_path import AbsolutePath
from .project_commands import ProjectCommands

__all__ = ["Project"]


class Project(BaseModel):
    id: ProjectID

    canonical: AbsolutePath

    sandboxes: List[str]

    time: ProjectTime

    commands: Optional[ProjectCommands] = None

    icon: Optional[ProjectIcon] = None

    name: Optional[str] = None

    vcs: Optional[ProjectVcs] = None

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
