from __future__ import annotations

from collections.abc import AsyncIterator, Iterator

import pytest
import respx

from opencode import AsyncOpencode, Opencode

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
    with Opencode(BASE_URL, password=PASSWORD, max_retries=2) as instance:
        yield instance


@pytest.fixture
async def async_client(mock_api: respx.MockRouter) -> AsyncIterator[AsyncOpencode]:
    async with AsyncOpencode(BASE_URL, password=PASSWORD, max_retries=2) as instance:
        yield instance


@pytest.fixture(autouse=True)
def _no_retry_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    """Retries back off with real sleeps; skip them so tests stay fast."""

    async def instant(_: float) -> None:
        return None

    monkeypatch.setattr("opencode._base_client.time.sleep", lambda _: None)
    monkeypatch.setattr("opencode._base_client.anyio.sleep", instant)
