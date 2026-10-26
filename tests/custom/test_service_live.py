"""The service lifecycle against a real `opencode serve --service`, in temporary XDG directories.

Run with `uv run pytest -m live`. Skipped when the opencode CLI is not installed.
"""

from __future__ import annotations

import json
import shutil
import socket
from pathlib import Path

import pytest

from opencode import API_VERSION, Opencode, AsyncOpencode, service

pytestmark = [
    pytest.mark.live,
    pytest.mark.skipif(shutil.which("opencode") is None, reason="opencode CLI is not installed"),
]


def _sandbox(root: Path) -> tuple[Path, dict[str, str]]:
    # The service must never see, reuse or stop the developer's real background service.
    env = {
        name: str(root / name.lower())
        for name in ("XDG_DATA_HOME", "XDG_CONFIG_HOME", "XDG_STATE_HOME", "XDG_CACHE_HOME")
    }
    env["OPENCODE_CONFIG_PROJECT_DISABLE"] = "1"
    env["OPENCODE_DISABLE_CLAUDE_CODE"] = "1"
    # The service binds a fixed managed port, which a real service on this machine may hold. Give it a free one.
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
    config = Path(env["XDG_CONFIG_HOME"]) / "opencode" / "service.json"
    config.parent.mkdir(parents=True)
    config.write_text(json.dumps({"port": port}))
    return Path(env["XDG_STATE_HOME"]) / "opencode" / "service.json", env


def test_service_lifecycle(tmp_path: Path) -> None:
    file, env = _sandbox(tmp_path)
    assert service.discover(file) is None
    reasons: list[str] = []
    try:
        endpoint = service.ensure(file, env=env, on_start=lambda reason, _: reasons.append(reason))
        assert reasons == ["missing"]
        assert file.exists()
        assert service.discover(file, API_VERSION) == endpoint
        assert service.ensure(file, env=env) == endpoint
        with Opencode.from_service(start=False, file=file) as client:
            assert client.server.info().version == API_VERSION
    finally:
        service.stop(file, pty="handoff")
    assert not file.exists()
    assert service.discover(file) is None


@pytest.mark.anyio
async def test_async_service_lifecycle(tmp_path: Path) -> None:
    file, env = _sandbox(tmp_path)
    try:
        async with await AsyncOpencode.from_service(file=file, env=env) as client:
            assert (await client.server.info()).version == API_VERSION
    finally:
        await service.async_stop(file)
    assert not file.exists()
