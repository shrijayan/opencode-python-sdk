"""Optional aiohttp-backed HTTP client for `AsyncOpencode`.

Install the extra with ``pip install 'opencode-python-sdk[aiohttp]'`` and pass the client in::

    async with AsyncOpencode(http_client=DefaultAioHttpClient()) as client:
        ...

The SDK still speaks httpx: ``httpx-aiohttp`` swaps the transport underneath, so retries, timeouts and event
streams behave the same. aiohttp only runs on asyncio, so this client does not work under trio.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

import httpx

from . import _constants as constants

if TYPE_CHECKING:
    _Base = httpx.AsyncClient
else:
    try:
        from httpx_aiohttp import HttpxAiohttpClient as _Base
    except ImportError:  # pragma: no cover - only without the extra
        _Base = httpx.AsyncClient


class DefaultAioHttpClient(_Base):
    """aiohttp-backed `httpx.AsyncClient` with the SDK's default connection limits and redirect handling.

    Pass it to `AsyncOpencode` as ``http_client``. Keyword arguments go to `httpx.AsyncClient`. The SDK does not
    close a client it was given, so close it yourself (``async with`` it) when you are done. Creating one without
    the ``aiohttp`` extra installed raises `RuntimeError`.
    """

    def __init__(self, **kwargs: Any) -> None:
        if _Base is httpx.AsyncClient:
            raise RuntimeError(
                "DefaultAioHttpClient needs the aiohttp extra: pip install 'opencode-python-sdk[aiohttp]'"
            )
        kwargs.setdefault("limits", constants.DEFAULT_CONNECTION_LIMITS)
        kwargs.setdefault("follow_redirects", True)
        super().__init__(**kwargs)
