from __future__ import annotations

import json
import sys
import time
from collections.abc import Iterator
from dataclasses import replace
from pathlib import Path

import httpx
import pytest
import respx

from opencode import AsyncOpencode, Endpoint, Opencode, ServiceError, _service as impl, service

FAKE = str(Path(__file__).with_name("fake_service.py"))
URL = "http://127.0.0.1:4999"


@pytest.fixture
def file(tmp_path: Path) -> Path:
    return tmp_path / "state" / "opencode" / "service.json"


@pytest.fixture(autouse=True)
def _fast_timing(monkeypatch: pytest.MonkeyPatch) -> None:
    timing = replace(impl._TIMING, spawn_delay=0.5, max_spawn_delay=1.0, timeout=20.0, stop_poll_interval=0.02)
    monkeypatch.setattr(impl, "_TIMING", timing)


def register(file: Path, **fields: object) -> None:
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(json.dumps({"url": URL, "pid": 1234, "version": "2.1.2", "password": "pw", **fields}))


def fake(file: Path, version: str, mode: str = "serve") -> list[str]:
    return [sys.executable, FAKE, str(file), version, mode]


@pytest.fixture
def cleanup(file: Path) -> Iterator[None]:
    yield
    service.stop(file)


def test_headers_and_default_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    assert service.headers(Endpoint(URL)) is None
    assert service.headers(Endpoint(URL, service.BasicAuth("opencode", "pw"))) == {
        "authorization": "Basic b3BlbmNvZGU6cHc="
    }
    monkeypatch.setenv("XDG_STATE_HOME", str(tmp_path))
    assert service.default_file() == tmp_path / "opencode" / "service.json"
    monkeypatch.delenv("XDG_STATE_HOME")
    assert service.default_file() == Path.home() / ".local" / "state" / "opencode" / "service.json"


def test_discover_without_registration(file: Path) -> None:
    assert service.discover(file) is None
    file.parent.mkdir(parents=True)
    file.write_text("{not json")
    assert service.discover(file) is None


@pytest.mark.parametrize(
    ("status", "body", "version", "found"),
    [
        (200, {"version": "2.1.2", "pid": 1234}, None, True),
        (200, {"version": "2.1.2", "pid": 1234}, "2.1.2", True),
        (200, {"version": "2.1.2", "pid": 1234}, "2.0.0", False),
        (200, {"version": "2.1.2", "pid": 1234}, lambda v: v.startswith("2."), True),
        (200, {"version": "2.1.2", "pid": 99}, None, False),  # another process answered on that port
        (200, {"version": "2.0.0", "pid": 1234}, None, False),  # registration and server disagree
        (200, {"pid": 1234}, None, False),
        (503, {"version": "2.1.2", "pid": 1234}, None, False),  # still starting
        (404, None, None, False),  # incompatible health protocol
    ],
)
def test_discover_classifies_health(
    file: Path, status: int, body: object, version: service.Version | None, found: bool
) -> None:
    register(file)
    with respx.mock() as router:
        route = router.get(f"{URL}/api/info").respond(status, json=body)
        endpoint = service.discover(file, version)
    assert route.calls.last.request.headers["authorization"] == "Basic b3BlbmNvZGU6cHc="
    assert endpoint == (Endpoint(URL, service.BasicAuth("opencode", "pw")) if found else None)


def test_discover_without_password(file: Path) -> None:
    register(file, password=None)
    with respx.mock() as router:
        route = router.get(f"{URL}/api/info").respond(200, json={"version": "2.1.2", "pid": 1234})
        assert service.discover(file) == Endpoint(URL)
    assert "authorization" not in route.calls.last.request.headers


def test_ensure_reuses_and_clears_foreign_handoff(file: Path) -> None:
    register(file, id="new")
    sidecar = file.with_name("service.json.pty-handoff")
    sidecar.write_text(json.dumps({"source": {"id": "old", "pid": 1, "url": URL}, "handoff": None, "expiresAt": 1e15}))
    started: list[str] = []
    with respx.mock() as router:
        router.get(f"{URL}/api/info").respond(200, json={"version": "2.1.2", "pid": 1234})
        endpoint = service.ensure(file, "2.1.2", on_start=lambda reason, _: started.append(reason))
    assert endpoint.url == URL
    assert started == []
    assert not sidecar.exists()


@pytest.mark.parametrize(
    ("status", "body", "message"),
    [(404, None, "incompatible health protocol"), (500, {"version": "2.1.2", "pid": 1234}, "failed to start")],
)
def test_ensure_fails_on_unusable_service(file: Path, status: int, body: object, message: str) -> None:
    register(file)
    with respx.mock() as router:
        router.get(f"{URL}/api/info").respond(status, json=body)
        with pytest.raises(ServiceError, match=message):
            service.ensure(file, command=["false-command-never-run"])


def test_ensure_starts_missing_service_and_stop_removes_it(file: Path) -> None:
    started: list[tuple[str, str | None]] = []
    endpoint = service.ensure(file, command=fake(file, "1.0.0"), on_start=lambda *args: started.append(args))
    assert started == [("missing", None)]
    assert endpoint.auth is None  # the fake runs without a password
    assert service.discover(file, "1.0.0") == endpoint
    # A second call reuses the running service.
    assert service.ensure(file, command=fake(file, "1.0.0")) == endpoint
    pid = json.loads(file.read_text())["pid"]

    service.stop(file)
    assert not file.exists()
    assert impl._stopped(pid)
    assert service.discover(file) is None
    service.stop(file)  # nothing registered: a no-op


@pytest.mark.usefixtures("cleanup")
def test_ensure_replaces_version_mismatch_with_handoff(file: Path) -> None:
    first = service.ensure(file, command=fake(file, "1.0.0"))
    started: list[tuple[str, str | None]] = []
    second = service.ensure(file, "2.0.0", command=fake(file, "2.0.0"), on_start=lambda *args: started.append(args))
    assert started == [("version-mismatch", "1.0.0")]
    assert second.url != first.url
    # The handoff the old service published was adopted, then cleared once the new owner was ready.
    assert not file.with_name("service.json.pty-handoff").exists()


def test_ensure_reports_startup_failure(file: Path) -> None:
    with pytest.raises(ServiceError, match=r"exited with code 1\nfake service: boom"):
        service.ensure(file, command=fake(file, "1.0.0", "fail"))


def test_ensure_times_out_when_attempts_keep_losing(file: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(impl, "_TIMING", replace(impl._TIMING, timeout=1.0, spawn_delay=0.1))
    with pytest.raises(ServiceError, match="Timed out"):
        service.ensure(file, command=fake(file, "1.0.0", "lose"))


def test_ensure_rejects_bad_commands(file: Path) -> None:
    with pytest.raises(ServiceError, match="Missing service command"):
        service.ensure(file, command=[])
    with pytest.raises(ServiceError, match="Failed to start server"):
        service.ensure(file, command=[str(file.parent / "does-not-exist")])


def test_unresponsive_service_is_replaced(file: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    register(file, pid=2**22 + 12345)  # a PID that is not running
    started: list[str] = []
    calls = 0

    def probe(info: impl._Info, timeout: float) -> impl._Probe:
        nonlocal calls
        calls += 1
        return impl._Probe(timed_out=True)

    monkeypatch.setattr(impl, "_probe", probe)
    monkeypatch.setattr(impl, "_TIMING", replace(impl._TIMING, timeout=1.0))
    with pytest.raises(ServiceError, match="Timed out"):
        service.ensure(file, command=fake(file, "1.0.0", "lose"), on_start=lambda reason, _: started.append(reason))
    assert started == ["missing"]
    assert calls >= 3
    assert not file.exists()  # the unresponsive registration was removed


def test_pty_environment_passes_fresh_matching_handoff(file: Path) -> None:
    register(file, id="a")
    handoff = {"directory": "/x", "instanceID": "i", "ticket": "t", "expiresAt": time.time() * 1000 + 60_000}
    sidecar = file.with_name("service.json.pty-handoff")
    sidecar.write_text(
        json.dumps({"source": {"id": "a", "pid": 1234, "url": URL}, "handoff": handoff, "expiresAt": 1e15})
    )
    env = impl._pty_environment(file, {"EXTRA": "1"})
    assert env["EXTRA"] == "1"
    assert json.loads(env["OPENCODE_PTY_HANDOFF"] or "") == handoff
    register(file, id="b")  # a different owner registered since
    assert impl._pty_environment(file, None)["OPENCODE_PTY_HANDOFF"] is None


def test_stop_handoff_publishes_ticket(file: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    register(file, id="a", pid=2**22 + 12345)
    handoff = {"directory": "/x", "instanceID": "i", "ticket": "t", "expiresAt": time.time() * 1000 + 60_000}
    with respx.mock() as router:
        router.post(f"{URL}/api/experimental/persistent-pty/handoff").respond(200, json={"handoff": handoff})
        service.stop(file, pty="handoff")
    record = json.loads(file.with_name("service.json.pty-handoff").read_text())
    assert record == {
        "source": {"id": "a", "pid": 2**22 + 12345, "url": URL},
        "handoff": handoff,
        "expiresAt": handoff["expiresAt"],
    }
    assert not file.exists()


def test_stop_handoff_failure_shuts_terminals_down(file: Path) -> None:
    register(file, pid=2**22 + 12345)
    with respx.mock() as router:
        router.post(f"{URL}/api/experimental/persistent-pty/handoff").respond(503)
        shutdown = router.post(f"{URL}/api/experimental/persistent-pty/shutdown").respond(204)
        service.stop(file, pty="handoff")
    assert shutdown.called
    record = json.loads(file.with_name("service.json.pty-handoff").read_text())
    assert record["handoff"] is None


def test_from_service(file: Path) -> None:
    with pytest.raises(ServiceError, match="No matching"):
        Opencode.from_service(start=False, file=file)
    register(file)
    with respx.mock() as router:
        router.get(f"{URL}/api/info").respond(200, json={"version": "2.1.2", "pid": 1234})
        with Opencode.from_service(file=file) as client:
            assert str(client.base_url).rstrip("/") == URL
            assert client.password == "pw"
    register(file, password=None)
    with respx.mock() as router:
        router.get(f"{URL}/api/info").respond(200, json={"version": "2.1.2", "pid": 1234})
        with Opencode.from_service(start=False, file=file) as client:
            assert not client.password


@pytest.mark.anyio
async def test_async_lifecycle(file: Path) -> None:
    assert await service.async_discover(file) is None
    endpoint = await service.async_ensure(file, command=fake(file, "1.0.0"))
    assert await service.async_discover(file) == endpoint
    async with await AsyncOpencode.from_service(start=False, file=file) as client:
        assert not client.password
    async with httpx.AsyncClient(trust_env=False) as http:  # CI runners may set proxy variables
        response = await http.get(f"{endpoint.url}/api/info", headers=service.headers(endpoint))
        assert response.json()["version"] == "1.0.0"
    second = await service.async_ensure(file, "2.0.0", command=fake(file, "2.0.0"))
    assert second != endpoint
    await service.async_stop(file, pty="handoff")
    assert not file.exists()


@pytest.mark.anyio
async def test_async_from_service_raises_when_missing(file: Path) -> None:
    with pytest.raises(ServiceError):
        await AsyncOpencode.from_service(start=False, file=file)
    with pytest.raises(ServiceError, match="exited with code 1"):
        await AsyncOpencode.from_service(file=file, command=fake(file, "1.0.0", "fail"))


def test_probe_timeout_is_reported(file: Path) -> None:
    register(file)
    with respx.mock() as router:
        router.get(f"{URL}/api/info").mock(side_effect=httpx.ConnectTimeout("slow"))
        registration = impl._registered(file, 0.1)
    assert registration.timed_out
    assert registration.service is None


def test_resolve_searches_path_only(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    bin_dir, cwd = tmp_path / "bin", tmp_path / "cwd"
    bin_dir.mkdir()
    cwd.mkdir()
    name = "tool.exe" if sys.platform == "win32" else "tool"
    for folder in (bin_dir, cwd):
        (folder / name).write_text("")
        (folder / name).chmod(0o755)
    monkeypatch.chdir(cwd)
    assert Path(impl._resolve("tool", str(bin_dir))).parent == bin_dir
    with pytest.raises(FileNotFoundError, match="not found on PATH"):
        impl._resolve("tool", "")  # the copy in the current directory is never used
    assert impl._resolve(str(cwd / name), "") == str(cwd / name)
