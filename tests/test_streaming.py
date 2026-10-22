from __future__ import annotations

import httpx
import pytest
import respx

from opencode import APIResponseValidationError, AsyncOpencode, Opencode
from opencode._streaming import _Decoder, _LineSplitter
from opencode.types import ServerConnectedEvent, UnknownEvent

CONNECTED = '{"type":"server.connected","id":"evt_1","created":1,"data":{}}'


def _sse(*blocks: str) -> bytes:
    return "".join(blocks).encode()


def test_line_splitter_handles_every_newline_style_across_chunks() -> None:
    splitter = _LineSplitter()
    lines = [*splitter.feed("a\r"), *splitter.feed("\nb\rc\nd"), *splitter.feed("e\r\n"), *splitter.flush()]
    assert lines == ["a", "b", "c", "de", ""]


def test_decoder_joins_multiline_data_and_ignores_comments() -> None:
    decoder = _Decoder()
    events = [decoder.feed_line(line) for line in [": keepalive", "event: x", "data: one", "data:two", "id: 7", ""]]
    event = events[-1]
    assert event is not None
    assert (event.data, event.event, event.id) == ("one\ntwo", "x", "7")
    assert all(item is None for item in events[:-1])


def test_sync_stream_yields_typed_events(client: Opencode, mock_api: respx.MockRouter) -> None:
    body = _sse(": hi\n\n", f"data: {CONNECTED}\n\n", 'data: {"type":"brand.new","id":"e","created":1}\n\n')
    route = mock_api.get("/api/event").respond(headers={"content-type": "text/event-stream"}, content=body)
    with client.event.subscribe() as events:
        received = list(events)
    assert isinstance(received[0], ServerConnectedEvent)
    assert isinstance(received[1], UnknownEvent)
    assert route.calls.last.request.headers["Accept"] == "text/event-stream"


def test_stream_rejects_wrong_content_type(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").respond(json={"not": "a stream"})
    with pytest.raises(APIResponseValidationError, match="event stream"):
        client.event.subscribe()


def test_stream_reports_malformed_event(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").respond(headers={"content-type": "text/event-stream"}, content=b"data: {oops\n\n")
    with pytest.raises(APIResponseValidationError, match="Malformed"), client.event.subscribe() as events:
        list(events)


def test_stream_has_no_read_timeout_by_default(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/event").respond(headers={"content-type": "text/event-stream"}, content=b"")
    client.event.subscribe().close()
    timeout = route.calls.last.request.extensions["timeout"]
    assert timeout["read"] is None
    assert timeout["connect"] == 10.0


@pytest.mark.anyio
async def test_async_stream(async_client: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").respond(
        headers={"content-type": "text/event-stream"}, content=_sse(f"data: {CONNECTED}\r\n\r\n")
    )
    async with await async_client.event.subscribe() as events:
        received = [event async for event in events]
    assert [event.type for event in received] == ["server.connected"]


def test_stream_error_status_raises(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/event").mock(
        return_value=httpx.Response(401, json={"_tag": "UnauthorizedError", "message": "no"})
    )
    with pytest.raises(Exception, match="no"):
        client.event.subscribe()
