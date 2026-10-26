# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.config_entry import ConfigEntry

__all__ = ["ConfigGetResponse"]

ConfigGetResponse: TypeAlias = List[ConfigEntry]
