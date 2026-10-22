"""`DefaultAioHttpClient` against a real aiohttp server. Skipped unless the ``aiohttp`` extra is installed."""

from __future__ import annotations

import asyncio
import importlib
import sys
from collections.abc import AsyncIterator, Awaitable, Callable

import pytest

from opencode import APITimeoutError, AsyncOpencode, DefaultAioHttpClient
from opencode.types import ServerConnectedEvent

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
CONNECTED = '{"type":"server.connected","id":"evt_1","created":1,"data":{}}'


def test_missing_extra_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(sys.modules, "httpx_aiohttp", None)
    module = importlib.reload(importlib.import_module("opencode._aiohttp"))
    try:
        with pytest.raises(RuntimeError, match=r"opencode-python-sdk\[aiohttp\]"):
            module.DefaultAioHttpClient()
    finally:
        monkeypatch.undo()
        importlib.reload(module)


@pytest.fixture
async def server_url() -> AsyncIterator[str]:
    pytest.importorskip("httpx_aiohttp")
    from aiohttp import web
    from aiohttp.test_utils import TestServer

    attempts = {"retry": 0}

    async def session(request: web.Request) -> web.Response:
        body = await request.json()
        return web.json_response({"data": {**SESSION, "title": body["title"]}})

    async def flaky(request: web.Request) -> web.Response:
        attempts["retry"] += 1
        if attempts["retry"] == 1:
            return web.json_response({"_tag": "UnknownError", "message": "busy"}, status=503)
        return web.json_response({"data": {**SESSION, "title": "retried"}})

    async def slow(request: web.Request) -> web.Response:
        await asyncio.sleep(5)
        return web.json_response({"data": SESSION})

    async def events(request: web.Request) -> web.StreamResponse:
        response = web.StreamResponse(headers={"Content-Type": "text/event-stream"})
        await response.prepare(request)
        await response.write(b": hi\n\n")
        # Split one event across writes to check the decoder reassembles aiohttp's chunks.
        await response.write(f"data: {CONNECTED[:20]}".encode())
        await response.write(f"{CONNECTED[20:]}\n\n".encode())
        await response.write_eof()
        return response

    modes = {"retry": flaky, "slow": slow}

    # The retry and timeout cases reuse the session route, picked by a header.
    @web.middleware
    async def switch(
        request: web.Request, handler: Callable[[web.Request], Awaitable[web.StreamResponse]]
    ) -> web.StreamResponse:
        mode = request.headers.get("X-Test-Mode")
        return await modes[mode](request) if mode else await handler(request)

    app = web.Application(middlewares=[switch])
    app.router.add_post("/api/session", session)
    app.router.add_get("/api/event", events)
    server = TestServer(app, host="127.0.0.1")
    await server.start_server()
    try:
        yield str(server.make_url("/"))
    finally:
        await server.close()


async def test_request_and_body(server_url: str) -> None:
    async with DefaultAioHttpClient() as http, AsyncOpencode(server_url, password="", http_client=http) as client:
        session = await client.session.create(title="Hello")
    assert session.title == "Hello"


async def test_event_stream(server_url: str) -> None:
    async with DefaultAioHttpClient() as http, AsyncOpencode(server_url, password="", http_client=http) as client:  # noqa: SIM117
        async with await client.event.subscribe() as stream:
            received = [event async for event in stream]
    assert len(received) == 1
    assert isinstance(received[0], ServerConnectedEvent)


async def test_retries_server_errors(server_url: str) -> None:
    async with (
        DefaultAioHttpClient() as http,
        AsyncOpencode(
            server_url, password="", http_client=http, max_retries=2, default_headers={"X-Test-Mode": "retry"}
        ) as client,
    ):
        session = await client.session.create(title="ignored")
    assert session.title == "retried"


async def test_timeout(server_url: str) -> None:
    async with (
        DefaultAioHttpClient() as http,
        AsyncOpencode(
            server_url,
            password="",
            http_client=http,
            max_retries=0,
            timeout=0.2,
            default_headers={"X-Test-Mode": "slow"},
        ) as client,
    ):
        with pytest.raises(APITimeoutError):
            await client.session.create(title="slow")
