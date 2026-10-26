# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .shared_params.project_icon import ProjectIcon
from .shared_params.absolute_path import AbsolutePath
from .shared_params.project_commands import ProjectCommands

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    canonical: AbsolutePath

    commands: ProjectCommands

    icon: ProjectIcon

    name: str
