# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .config_document import ConfigDocument
from .config_directory import ConfigDirectory

__all__ = ["ConfigEntry"]

ConfigEntry: TypeAlias = Union[ConfigDocument, ConfigDirectory]
