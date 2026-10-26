# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .worktree_directory import WorktreeDirectory

__all__ = ["WorktreeList"]

WorktreeList: TypeAlias = List[WorktreeDirectory]
