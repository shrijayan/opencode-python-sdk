"""PTY WebSocket attach against an in-process fake server."""

from __future__ import annotations

import sys
import json
import struct
import threading
from typing import Any
from dataclasses import field, dataclass
from urllib.parse import parse_qs, urlsplit
from collections.abc import Iterator

import httpx
import respx
import pytest
from websockets.http11 import Request, Response
from websockets.sync.server import Server, ServerConnection, serve
from websockets.datastructures import Headers

from opencode import Opencode, AsyncOpencode, PtyConnectionError

PASSWORD = "test-password"
TICKET = "ticket-1"


@dataclass
class Fake:
    """Records what the client sent and decides how the fake server behaves."""

    close_code: int = 1000
    refuse: bool = False
    paths: list[str] = field(default_factory=list)
    queries: list[dict[str, list[str]]] = field(default_factory=list)
    headers: list[Headers] = field(default_factory=list)
    received: list[bytes | str] = field(default_factory=list)


def _handler(fake: Fake) -> Any:
    def handle(ws: ServerConnection) -> None:
        assert ws.request is not None
        path = urlsplit(ws.request.path).path
        if fake.close_code != 1000:
            ws.close(fake.close_code, "session not found")
            return
        if "persistent-pty" in path:
            ws.send(
                json.dumps({"type": "attached", "info": {"size": {"cols": 80, "rows": 24}}, "replay": {"endOffset": 0}})
            )
            ws.send(b"replay")
            ws.send(json.dumps({"type": "replay_complete", "endOffset": 6}))
        else:
            ws.send("replay")
            ws.send(b"\x00" + json.dumps({"cursor": 6}).encode())
        for message in ws:
            fake.received.append(message)
            if "persistent-pty" in path:
                assert isinstance(message, bytes)
                kind, cols, rows = struct.unpack(">BHH", message[:5])
                if kind == 0:
                    ws.send(json.dumps({"type": "resized", "cols": cols, "rows": rows}))
                    continue
                payload = message[5:]
            else:
                payload = message.encode() if isinstance(message, str) else message
            if payload == b"exit\n":
                ws.close(1000)
                return
            ws.send(payload if "persistent-pty" in path else payload.decode())

    return handle


def _process_request(fake: Fake) -> Any:
    def process(ws: ServerConnection, request: Request) -> Response | None:
        split = urlsplit(request.path)
        fake.paths.append(split.path)
        fake.queries.append(parse_qs(split.query))
        fake.headers.append(request.headers)
        if fake.refuse:
            return ws.respond(403, "forbidden\n")
        return None

    return process


@pytest.fixture
def fake() -> Fake:
    return Fake()


@pytest.fixture
def ws_server(fake: Fake) -> Iterator[str]:
    server: Server = serve(_handler(fake), "127.0.0.1", 0, process_request=_process_request(fake))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.socket.getsockname()[:2]
    try:
        yield f"http://{host}:{port}"
    finally:
        server.shutdown()
        thread.join()


@pytest.fixture
def api(ws_server: str) -> Iterator[respx.MockRouter]:
    with respx.mock(base_url=ws_server, assert_all_called=False) as router:
        router.post("/api/pty/pty_1/connect-token").respond(
            json={"location": {"directory": "/repo"}, "data": {"ticket": TICKET, "expires_in": 60}}
        )
        router.post("/api/experimental/persistent-pty/pty_1/connect-token").respond(
            json={"data": {"ticket": TICKET, "expires_in": 60}}
        )
        yield router


def test_pty_attach_round_trip(ws_server: str, api: respx.MockRouter, fake: Fake) -> None:
    update = api.put("/api/pty/pty_1").respond(
        json={
            "location": {"directory": "/repo"},
            "data": {
                "id": "pty_1",
                "title": "t",
                "command": "bash",
                "args": [],
                "cwd": "/repo",
                "status": "running",
                "pid": 1,
            },
        }
    )
    with (
        Opencode(base_url=ws_server, password=PASSWORD, directory="/repo") as client,
        client.pty.attach("pty_1", cursor=3) as term,
    ):
        assert term.recv(timeout=5) == b"replay"
        term.send("echo hi\n")
        assert term.recv(timeout=5) == b"echo hi\n"
        assert term.cursor == 6
        term.resize(120, 40)
        term.send(b"exit\n")
        assert list(term) == []
        assert term.close_code == 1000
    assert api.calls[0].request.headers["x-opencode-ticket"] == "1"
    assert json.loads(update.calls[0].request.content) == {"size": {"rows": 40, "cols": 120}}
    assert fake.paths == ["/api/pty/pty_1/connect"]
    assert fake.queries[0] == {"location[directory]": ["/repo"], "cursor": ["3"], "ticket": [TICKET]}
    assert fake.headers[0]["Authorization"].startswith("Basic ")
    assert fake.received == ["echo hi\n", b"exit\n"]


def test_persistent_closed_before_attached(ws_server: str, api: respx.MockRouter, fake: Fake) -> None:
    fake.close_code = 4404
    with Opencode(base_url=ws_server, password=PASSWORD) as client, pytest.raises(PtyConnectionError) as caught:
        client.experimental.persistent_pty.attach("pty_1")
    assert caught.value.code == 4404


def test_persistent_pty_attach_frames(ws_server: str, api: respx.MockRouter, fake: Fake) -> None:
    events: list[dict[str, Any]] = []
    with Opencode(base_url=ws_server, password=PASSWORD) as client:
        term = client.experimental.persistent_pty.attach("pty_1", attachment_id="a1", on_event=events.append)
        with term:
            assert term.recv(timeout=5) == b"replay"
            assert term.attached is not None
            term.send("ls\n")
            assert term.recv(timeout=5) == b"ls\n"
            assert term.cursor == 9
            term.resize(132, 50)
            term.send("exit\n")
            assert list(term) == []
    assert [event["type"] for event in events] == ["attached", "replay_complete", "resized"]
    assert fake.queries[0] == {
        "ticket": [TICKET],
        "cursor": ["0"],
        "role": ["controller"],
        "attachment_id": ["a1"],
        "takeover": ["false"],
        "input_protocol": ["1"],
    }
    # Input frames carry the size from the attached event, then the size set by resize.
    assert fake.received == [
        struct.pack(">BHH", 1, 80, 24) + b"ls\n",
        struct.pack(">BHH", 0, 132, 50),
        struct.pack(">BHH", 1, 132, 50) + b"exit\n",
    ]


def test_not_found_close_raises(ws_server: str, api: respx.MockRouter, fake: Fake) -> None:
    fake.close_code = 4404
    with (
        Opencode(base_url=ws_server, password=PASSWORD) as client,
        client.pty.attach("pty_1") as term,
        pytest.raises(PtyConnectionError) as caught,
    ):
        term.recv(timeout=5)
    assert caught.value.code == 4404
    assert caught.value.reason == "session not found"


def test_refused_handshake_raises(ws_server: str, api: respx.MockRouter, fake: Fake) -> None:
    fake.refuse = True
    with Opencode(base_url=ws_server, password=PASSWORD) as client, pytest.raises(PtyConnectionError) as caught:
        client.pty.attach("pty_1")
    assert caught.value.status == 403


def test_missing_websockets(monkeypatch: pytest.MonkeyPatch, mock_api: respx.MockRouter, client: Opencode) -> None:
    monkeypatch.setitem(sys.modules, "websockets", None)
    with pytest.raises(PtyConnectionError, match=r"opencode-python-sdk\[pty\]"):
        client.pty.attach("pty_1")
    assert not mock_api.calls


@pytest.mark.anyio
async def test_async_pty_attach(ws_server: str, api: respx.MockRouter, fake: Fake) -> None:
    async with AsyncOpencode(base_url=ws_server, password=PASSWORD) as client:
        async with await client.pty.attach("pty_1") as term:
            assert await term.recv() == b"replay"
            await term.send("echo hi\n")
            assert await term.recv() == b"echo hi\n"
            await term.send("exit\n")
            assert [chunk async for chunk in term] == []
        async with await client.experimental.persistent_pty.attach("pty_1") as persistent:
            assert await persistent.recv() == b"replay"
            await persistent.resize(90, 20)
            await persistent.send(b"exit\n")
            assert [chunk async for chunk in persistent] == []
    assert fake.received[-1] == struct.pack(">BHH", 1, 90, 20) + b"exit\n"


def test_wss_for_https() -> None:
    from opencode._pty import _ws_url

    url = _ws_url(httpx.URL("https://example.com/base/"), "/api/pty/x/connect", {"ticket": "t"})
    assert url == "wss://example.com/base/api/pty/x/connect?ticket=t"
