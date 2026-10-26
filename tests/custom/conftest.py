from __future__ import annotations

from collections.abc import Iterator, AsyncIterator

import respx
import pytest

from opencode import Opencode, AsyncOpencode
from opencode._base_client import BaseClient

BASE_URL = "http://opencode.test"
PASSWORD = "test-password"


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
def mock_api() -> Iterator[respx.MockRouter]:
    with respx.mock(base_url=BASE_URL, assert_all_called=False) as router:
        yield router


@pytest.fixture
def client(mock_api: respx.MockRouter) -> Iterator[Opencode]:
    with Opencode(base_url=BASE_URL, password=PASSWORD, max_retries=2) as instance:
        yield instance


@pytest.fixture
async def async_client(mock_api: respx.MockRouter) -> AsyncIterator[AsyncOpencode]:
    async with AsyncOpencode(base_url=BASE_URL, password=PASSWORD, max_retries=2) as instance:
        yield instance


@pytest.fixture(autouse=True)
def _no_retry_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    """Retries back off with real sleeps; make the delay zero so tests stay fast.

    Patching ``anyio.sleep`` itself would also patch ``anyio.lowlevel.checkpoint`` on anyio
    releases that implement it as ``sleep(0)``, and a task polling with it would never yield.
    """
    monkeypatch.setattr(BaseClient, "_calculate_retry_timeout", lambda *_args, **_kwargs: 0.0)
