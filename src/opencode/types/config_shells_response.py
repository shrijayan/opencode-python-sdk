# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.config_shell_option import ConfigShellOption

__all__ = ["ConfigShellsResponse"]

ConfigShellsResponse: TypeAlias = List[ConfigShellOption]
