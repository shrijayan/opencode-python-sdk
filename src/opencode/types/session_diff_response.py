# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.file_diff_info import FileDiffInfo

__all__ = ["SessionDiffResponse"]

SessionDiffResponse: TypeAlias = List[FileDiffInfo]
