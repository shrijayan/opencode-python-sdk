from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import AsyncOpencode, Opencode

__all__ = ["AsyncAPIResource", "SyncAPIResource"]


class SyncAPIResource:
    """Base class for generated resource groups of the sync client."""

    _client: Opencode

    def __init__(self, client: Opencode) -> None:
        self._client = client


class AsyncAPIResource:
    """Base class for generated resource groups of the async client."""

    _client: AsyncOpencode

    def __init__(self, client: AsyncOpencode) -> None:
        self._client = client
