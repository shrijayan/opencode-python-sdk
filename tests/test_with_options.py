from __future__ import annotations

import pytest
import respx

from opencode import AsyncOpencode, Opencode

from .conftest import BASE_URL

AGENTS: dict[str, object] = {"location": {"directory": "/repo"}, "data": []}


@pytest.mark.parametrize("method", ["with_options", "copy"])
def test_overrides_apply_and_original_unchanged(mock_api: respx.MockRouter, method: str) -> None:
    route = mock_api.get("/api/agent").respond(json=AGENTS)
    with Opencode(
        BASE_URL, password="pw", directory="/repo", timeout=5.0, max_retries=3, default_headers={"X-A": "1"}
    ) as client:
        other = getattr(client, method)(
            password="other",
            directory="/elsewhere",
            timeout=1.0,
            max_retries=0,
            default_headers={"X-B": "2"},
            default_query={"q": "2"},
        )
        assert isinstance(other, Opencode)
        assert (other.max_retries, other.timeout, other.directory, other.password) == (0, 1.0, "/elsewhere", "other")
        other.agent.list()
        request = route.calls.last.request
        assert request.headers["X-A"] == "1"
        assert request.headers["X-B"] == "2"
        assert request.url.params["q"] == "2"
        assert request.url.params["location[directory]"] == "/elsewhere"

        assert (client.max_retries, client.timeout, client.directory, client.password) == (3, 5.0, "/repo", "pw")
        assert "X-B" not in client._default_headers


def test_base_url_override(mock_api: respx.MockRouter) -> None:
    with Opencode(BASE_URL, password="") as client:
        other = client.with_options(base_url="http://other.test")
        assert str(other.base_url).startswith("http://other.test")
        assert str(client.base_url).startswith(BASE_URL)


def test_copy_does_not_close_shared_pool(mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/agent").respond(json=AGENTS)
    client = Opencode(BASE_URL, password="")
    with client.copy(max_retries=0) as other:
        assert other._http is client._http
    assert not client._http.is_closed
    client.agent.list()
    assert route.called
    client.close()
    assert client._http.is_closed


@pytest.mark.anyio
@pytest.mark.parametrize("method", ["with_options", "copy"])
async def test_async_overrides_and_shared_pool(mock_api: respx.MockRouter, method: str) -> None:
    route = mock_api.get("/api/agent").respond(json=AGENTS)
    client = AsyncOpencode(BASE_URL, password="", directory="/repo", max_retries=3, default_headers={"X-A": "1"})
    async with getattr(client, method)(directory="/elsewhere", max_retries=0, default_headers={"X-B": "2"}) as other:
        assert isinstance(other, AsyncOpencode)
        assert other._http is client._http
        assert other.max_retries == 0
        await other.agent.list()
        request = route.calls.last.request
        assert (request.headers["X-A"], request.headers["X-B"]) == ("1", "2")
        assert request.url.params["location[directory]"] == "/elsewhere"
    assert not client._http.is_closed
    assert (client.max_retries, client.directory) == (3, "/repo")
    await client.agent.list()
    await client.close()
    assert client._http.is_closed
