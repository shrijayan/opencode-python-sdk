# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ..shared.persistent_pty_read_result import PersistentPtyReadResult

__all__ = ["PersistentPtyReadResponse"]

PersistentPtyReadResponse: TypeAlias = Union[PersistentPtyReadResult, None]
