from __future__ import annotations

import json

import pytest
import respx

from opencode import AsyncOpencode, SessionBusyError

pytestmark = pytest.mark.anyio

SESSION = {
    "id": "ses_1",
    "projectID": "prj_1",
    "cost": 0,
    "tokens": {"input": 0, "output": 0, "reasoning": 0, "cache": {"read": 0, "write": 0}},
    "time": {"created": 1, "updated": 1},
    "title": "Hello",
    "location": {"directory": "/repo"},
}


@pytest.fixture(params=["asyncio", "trio"])
def anyio_backend(request: pytest.FixtureRequest) -> str:
    return str(request.param)


async def test_async_request_and_body(mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/session").respond(json={"data": SESSION})
    async with AsyncOpencode("http://opencode.test", password="") as client:
        session = await client.session.create(title="Hello")
    assert session.title == "Hello"
    assert json.loads(route.calls.last.request.content) == {"title": "Hello"}


async def test_async_tagged_error(mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/session/ses_1/prompt").respond(
        409, json={"_tag": "SessionBusyError", "sessionID": "ses_1", "message": "busy"}
    )
    async with AsyncOpencode("http://opencode.test", password="") as client:
        with pytest.raises(SessionBusyError):
            await client.session.prompt("ses_1", text="hi")


async def test_async_retry(mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/agent").mock(
        side_effect=[respx.MockResponse(503), respx.MockResponse(json={"location": {"directory": "/"}, "data": []})]
    )
    async with AsyncOpencode("http://opencode.test", password="") as client:
        await client.agent.list()
    assert route.call_count == 2
