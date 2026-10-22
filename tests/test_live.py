"""End-to-end tests against a real `opencode serve`. They make no model calls.

Run with `uv run pytest -m live`. They are skipped when the opencode CLI is not installed.
"""

from __future__ import annotations

import shutil
from collections.abc import Iterator
from pathlib import Path

import pytest

from opencode import AsyncOpencodeServer, Opencode, OpencodeServer, SessionNotFoundError
from opencode.types import ServerConnectedEvent

pytestmark = [
    pytest.mark.live,
    pytest.mark.skipif(shutil.which("opencode") is None, reason="opencode CLI is not installed"),
]


def _sandbox_env(root: Path) -> dict[str, str]:
    # Keep the test server away from the developer's real sessions and settings.
    return {
        name: str(root / name.lower())
        for name in ("XDG_DATA_HOME", "XDG_CONFIG_HOME", "XDG_STATE_HOME", "XDG_CACHE_HOME")
    }


@pytest.fixture(scope="module")
def server(tmp_path_factory: pytest.TempPathFactory) -> Iterator[OpencodeServer]:
    root = tmp_path_factory.mktemp("opencode")
    project = root / "project"
    project.mkdir()
    with OpencodeServer(cwd=project, isolated=True, env=_sandbox_env(root)) as running:
        yield running


@pytest.fixture
def client(server: OpencodeServer) -> Iterator[Opencode]:
    with server.client() as instance:
        yield instance


def test_server_info(client: Opencode) -> None:
    info = client.server.info()
    assert info.version
    assert info.pid > 0


def test_session_lifecycle(client: Opencode) -> None:
    session = client.session.create(title="live test")
    assert client.session.get(session.id).title == "live test"
    assert any(item.id == session.id for item in client.session.list(limit=50))
    assert list(client.message.list(session.id)) == []
    client.session.remove(session.id)
    with pytest.raises(SessionNotFoundError) as caught:
        client.session.get(session.id)
    assert caught.value.error.session_id == session.id


def test_queue_prompt_without_running(client: Opencode) -> None:
    session = client.session.create(title="queued")
    queued = client.session.prompt(session.id, text="hello", resume=False)
    assert queued.type == "user"
    client.session.remove(session.id)


def test_event_stream_connects(client: Opencode) -> None:
    with client.event.subscribe() as events:
        first = next(iter(events))
    assert isinstance(first, ServerConnectedEvent)


def test_wrong_password_is_rejected(server: OpencodeServer) -> None:
    from opencode import UnauthorizedError

    with Opencode(server.url, password="wrong", max_retries=0) as client, pytest.raises(UnauthorizedError):
        client.server.info()


@pytest.mark.anyio
async def test_async_server(tmp_path: Path) -> None:
    running = AsyncOpencodeServer(cwd=tmp_path, isolated=True, env=_sandbox_env(tmp_path))
    async with running, running.client() as client:
        info = await client.server.info()
    assert info.version
    assert not running.running
