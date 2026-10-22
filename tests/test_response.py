from __future__ import annotations

import pytest
import respx

from opencode import (
    APIResponse,
    AsyncAPIResponse,
    AsyncCursorPage,
    AsyncOpencode,
    NotFoundError,
    Opencode,
    Stream,
    SyncCursorPage,
)
from opencode.types import ServerConnectedEvent, SessionInfo

from .test_client import SESSION

CONNECTED = '{"type":"server.connected","id":"evt_1","created":1,"data":{}}'
SSE = {"content-type": "text/event-stream"}


def _page(ids: list[str], next_cursor: str | None) -> dict[str, object]:
    return {
        "data": [{"type": "user", "id": item, "time": {"created": 1}, "text": item} for item in ids],
        "cursor": {"previous": None, "next": next_cursor},
    }


def test_raw_response(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1").respond(json={"data": SESSION}, headers={"x-request-id": "req_1"})
    response = client.session.with_raw_response.get("ses_1")
    assert isinstance(response, APIResponse)
    assert response.status_code == 200
    assert response.headers["x-request-id"] == "req_1"
    assert response.request.method == "GET"
    assert response.http_response.is_success
    assert response.json() == {"data": SESSION}
    assert '"ses_1"' in response.text
    session = response.parse()
    assert isinstance(session, SessionInfo)
    assert session.id == "ses_1"
    assert response.parse() is session


def test_raw_response_void_binary_and_nested(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.delete("/api/session/ses_1/revert").respond(204)
    mock_api.get("/api/fs/read/a.txt").respond(content=b"hello")
    assert client.session.revert.with_raw_response.clear("ses_1").parse() is None
    assert client.file.with_raw_response.read("a.txt").parse() == b"hello"


def test_raw_response_still_raises_status_errors(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_9").respond(404, json={"message": "nope"})
    with pytest.raises(NotFoundError):
        client.session.with_raw_response.get("ses_9")


def test_raw_mode_does_not_leak(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1").respond(json={"data": SESSION})
    client.session.with_raw_response.get("ses_1")
    assert isinstance(client.session.get("ses_1"), SessionInfo)


def test_raw_page_parses_to_a_working_page(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1/message").mock(
        side_effect=[respx.MockResponse(json=_page(["a"], "c1")), respx.MockResponse(json=_page(["b"], None))]
    )
    response = client.message.with_raw_response.list("ses_1")
    page = response.parse()
    assert isinstance(page, SyncCursorPage)
    assert [message.id for message in page] == ["a", "b"]


def test_streaming_response(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/fs/read/a.txt").respond(content=b"line 1\nline 2\n")
    with client.file.with_streaming_response.read("a.txt") as response:
        assert not response.http_response.is_stream_consumed
        assert list(response.iter_lines()) == ["line 1", "line 2"]
    assert response.is_closed


def test_streaming_response_parse(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1").respond(json={"data": SESSION})
    with client.session.with_streaming_response.get("ses_1") as response:
        assert response.parse().id == "ses_1"


def test_raw_event_stream(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").respond(headers=SSE, content=f"data: {CONNECTED}\n\n".encode())
    response = client.event.with_raw_response.subscribe()
    assert response.headers["content-type"] == "text/event-stream"
    with response.parse() as events:
        assert isinstance(events, Stream)
        assert isinstance(next(iter(events)), ServerConnectedEvent)


@pytest.mark.anyio
async def test_async_raw_response(async_client: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1").respond(json={"data": SESSION}, headers={"x-request-id": "req_1"})
    response = await async_client.session.with_raw_response.get("ses_1")
    assert isinstance(response, AsyncAPIResponse)
    assert response.headers["x-request-id"] == "req_1"
    assert (await response.json()) == {"data": SESSION}
    assert (await response.parse()).id == "ses_1"


@pytest.mark.anyio
async def test_async_raw_page(async_client: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1/message").mock(
        side_effect=[respx.MockResponse(json=_page(["a"], "c1")), respx.MockResponse(json=_page(["b"], None))]
    )
    response = await async_client.message.with_raw_response.list("ses_1")
    page = await response.parse()
    assert isinstance(page, AsyncCursorPage)
    assert [message.id async for message in page] == ["a", "b"]


@pytest.mark.anyio
async def test_async_streaming_response(async_client: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/fs/read/a.txt").respond(content=b"hello")
    async with async_client.file.with_streaming_response.read("a.txt") as response:
        assert b"".join([chunk async for chunk in response.iter_bytes()]) == b"hello"
    assert response.is_closed
    mock_api.get("/api/session/ses_1").respond(json={"data": SESSION})
    async with async_client.session.with_streaming_response.get("ses_1") as response:
        assert (await response.parse()).id == "ses_1"


@pytest.mark.anyio
async def test_async_raw_event_stream(async_client: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").respond(headers=SSE, content=f"data: {CONNECTED}\n\n".encode())
    response = await async_client.event.with_raw_response.subscribe()
    async with await response.parse() as events:
        async for event in events:
            assert isinstance(event, ServerConnectedEvent)
            break


def test_custom_requests(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/custom").respond(json={"ok": True})
    assert client.post("/api/custom", body={"a": 1}, query={"q": "x"}, headers={"X-A": "b"}) == {"ok": True}
    request = route.calls.last.request
    assert request.content == b'{"a":1}'
    assert request.url.params["q"] == "x"
    assert request.headers["X-A"] == "b"
    mock_api.get("/api/session/ses_1").respond(json={"data": SESSION})
    assert client.get("/api/session/ses_1", cast_to=dict[str, SessionInfo])["data"].id == "ses_1"


@pytest.mark.anyio
async def test_async_custom_requests(async_client: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    mock_api.delete("/api/custom").respond(json=[1])
    assert await async_client.delete("/api/custom", cast_to=list[int]) == [1]
