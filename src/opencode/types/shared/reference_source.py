# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .reference_git_source import ReferenceGitSource
from .reference_local_source import ReferenceLocalSource

__all__ = ["ReferenceSource"]

ReferenceSource: TypeAlias = Union[ReferenceLocalSource, ReferenceGitSource]
