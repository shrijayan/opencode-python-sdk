from __future__ import annotations

from typing import TYPE_CHECKING

from ._types import NotGiven

if TYPE_CHECKING:
    from ._client import AsyncOpencode, Opencode

__all__ = ["AsyncAPIResource", "SyncAPIResource"]


class SyncAPIResource:
    """Base class for generated resource groups of the sync client."""

    _client: Opencode

    def __init__(self, client: Opencode) -> None:
        self._client = client

    def _location(self, location: object) -> object:
        """Falls back to the client's ``directory`` for endpoints that take a ``location``."""
        return _default_location(location, self._client.directory)


class AsyncAPIResource:
    """Base class for generated resource groups of the async client."""

    _client: AsyncOpencode

    def __init__(self, client: AsyncOpencode) -> None:
        self._client = client

    def _location(self, location: object) -> object:
        """Falls back to the client's ``directory`` for endpoints that take a ``location``."""
        return _default_location(location, self._client.directory)


def _default_location(location: object, directory: str | None) -> object:
    if isinstance(location, NotGiven) and directory is not None:
        return {"directory": directory}
    return location
