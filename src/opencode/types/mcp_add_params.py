# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.mcp_local_config import McpLocalConfig
from .shared_params.mcp_remote_config import McpRemoteConfig

__all__ = ["McpAddParams", "Config", "Location"]


class McpAddParams(TypedDict, total=False):
    config: Required[Config]

    location: Optional[Location]


Config: TypeAlias = Union[McpLocalConfig, McpRemoteConfig]


class LocationTyped(TypedDict, total=False):
    directory: Optional[str]


Location: TypeAlias = Union[LocationTyped, Dict[str, object]]
