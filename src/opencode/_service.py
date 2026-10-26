"""Find, start and stop the local OpenCode background service (``opencode serve --service``).

A port of ``packages/client/src/promise/service.ts`` and its helpers from the OpenCode TypeScript client. The
registration file written by the service is the whole discovery contract: it names the URL, PID, version and
password of the one service that owns it.

The API is a set of module functions (``discover``, ``ensure``, ``stop``, ``headers``) with ``async_`` twins,
because the operations share no state between calls: a class would only be a namespace, and the module already is
one. ``from opencode import service`` gives the same ``service.ensure()`` spelling as the TypeScript ``Service``
object.
"""

from __future__ import annotations

import base64
import contextlib
import json
import logging
import os
import shutil
import signal
import subprocess
import sys
import threading
import time
import uuid
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal, TypeAlias, cast

import httpx
from anyio import sleep as _async_sleep

from ._exceptions import OpencodeError
from .lib._support import DEFAULT_USERNAME

__all__ = [
    "BasicAuth",
    "Endpoint",
    "EnsureReason",
    "PtyMode",
    "ServiceError",
    "Version",
    "async_discover",
    "async_ensure",
    "async_stop",
    "default_file",
    "discover",
    "ensure",
    "headers",
    "stop",
]

log = logging.getLogger("opencode")
_sleep = time.sleep

EnsureReason: TypeAlias = Literal["missing", "version-mismatch"]
"""Why :func:`ensure` starts a new service process."""

Version: TypeAlias = str | Callable[[str], bool]
"""A required exact service version, or a predicate that accepts compatible versions."""

PtyMode: TypeAlias = Literal["clear", "handoff"]
"""How :func:`stop` treats persistent terminals."""

_STDERR_LIMIT = 8 * 1024
_HANDOFF_TTL_MS = 30_000


class ServiceError(OpencodeError):
    """The local service could not be found, started or stopped."""


@dataclass(frozen=True)
class BasicAuth:
    """HTTP basic credentials of a local service."""

    username: str
    """Basic auth user name, always ``opencode``."""
    password: str = field(repr=False)
    """The service's private password. Hidden from ``repr`` so it stays out of logs."""


@dataclass(frozen=True)
class Endpoint:
    """Connection details of a local OpenCode service.

    Pass it to :meth:`opencode.Opencode.from_service`, or use ``url`` and :func:`headers` with any HTTP client.
    """

    url: str
    """Base URL of the service."""
    auth: BasicAuth | None = None
    """Credentials the service requires, or ``None`` when it runs without a password."""


@dataclass(frozen=True)
class _Info:
    url: str
    pid: int
    id: str | None = None
    version: str | None = None
    password: str | None = field(default=None, repr=False)


@dataclass(frozen=True)
class _LocalService:
    info: _Info
    endpoint: Endpoint
    version: str | None
    state: Literal["ready", "waiting", "failed"]
    compatible: bool


@dataclass(frozen=True)
class _Probe:
    service: _LocalService | None = None
    timed_out: bool = False


@dataclass(frozen=True)
class _Registration:
    info: _Info | None = None
    service: _LocalService | None = None
    timed_out: bool = False


@dataclass(frozen=True)
class _Timing:
    # Seconds. A freshly spawned service registers in ~250 ms, so the poll cadence is a large share of the time a
    # client waits for it.
    poll_interval: float = 0.025
    request_timeout: float = 2.0
    spawn_delay: float = 5.0
    max_spawn_delay: float = 30.0
    timeout: float = 120.0
    stop_poll_interval: float = 0.05
    stop_poll_attempts: int = 100


# Tests replace this to keep the lifecycle fast; it is not part of the public signature, as in TypeScript.
_TIMING = _Timing()


def default_file() -> Path:
    """The default registration file, ``$XDG_STATE_HOME/opencode/service.json``.

    ``XDG_STATE_HOME`` defaults to ``~/.local/state`` on every platform, as in OpenCode itself.
    """
    state = os.environ.get("XDG_STATE_HOME")
    return Path(state if state is not None else Path.home() / ".local" / "state") / "opencode" / "service.json"


def headers(endpoint: Endpoint) -> dict[str, str] | None:
    """The ``Authorization`` header for ``endpoint``, or ``None`` when it needs no credentials."""
    if endpoint.auth is None:
        return None
    return {"authorization": _basic(endpoint.auth.username, endpoint.auth.password)}


def _basic(username: str, password: str) -> str:
    return "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()


def _file(file: str | os.PathLike[str] | None) -> Path:
    return Path(file) if file is not None else default_file()


def _now_ms() -> float:
    return time.time() * 1000


# --- versions and probing (service-version.ts, service-probe.ts) ---


def _matches_version(version: str | None, required: Version | None) -> bool:
    if required is None:
        return True
    if version is None:
        return False
    if callable(required):
        return required(version)
    return version == required


@dataclass(frozen=True)
class _Decision:
    tag: Literal["reuse", "wait", "replace", "fail"]
    pty: PtyMode = "clear"
    error: str = ""


def _decide(service: _LocalService, required: Version | None) -> _Decision:
    if not _matches_version(service.version, required):
        return _Decision("replace", pty="handoff" if service.state == "ready" else "clear")
    if not service.compatible:
        return _Decision(
            "fail",
            error="Background service uses an incompatible health protocol. "
            "Update this client or explicitly restart the service.",
        )
    if service.state == "ready":
        return _Decision("reuse")
    if service.state == "failed":
        return _Decision("fail", error="Background service failed to start")
    return _Decision("wait")


def _same(left: _Info, right: _Info) -> bool:
    return left.id == right.id and left.version == right.version and left.url == right.url and left.pid == right.pid


def _endpoint(info: _Info) -> Endpoint:
    return Endpoint(info.url, None if info.password is None else BasicAuth(DEFAULT_USERNAME, info.password))


def _decode_server_info(body: object) -> tuple[str, int] | None:
    if not isinstance(body, dict):
        return None
    data = cast("dict[str, object]", body)
    version, pid = data.get("version"), data.get("pid")
    if not isinstance(version, str):
        return None
    if isinstance(pid, bool) or not isinstance(pid, (int, float)) or pid != int(pid) or pid < 0:
        return None
    return version, int(pid)


def _classify(info: _Info, status: int, body: object) -> _Probe:
    endpoint = _endpoint(info)
    # A missing health endpoint identifies protocol incompatibility, not an older version. Only an unmet version
    # requirement lets ensure replace this owner.
    if status == 404:
        return _Probe(_LocalService(info, endpoint, info.version, "ready", compatible=False))
    decoded = _decode_server_info(body)
    if decoded is None:
        return _Probe()
    version, pid = decoded
    if pid != info.pid:
        return _Probe()
    if info.version is not None and version != info.version:
        return _Probe()
    state: Literal["ready", "waiting", "failed"] = (
        "ready" if 200 <= status < 300 else "failed" if status == 500 else "waiting"
    )
    return _Probe(_LocalService(info, endpoint, version, state, compatible=True))


def _info_url(info: _Info) -> httpx.URL:
    return httpx.URL(info.url).join("/api/info")


def _probe(info: _Info, timeout: float) -> _Probe:
    # The service is local: ignore proxy variables, as Node's fetch in the TypeScript client does.
    try:
        with httpx.Client(timeout=timeout, trust_env=False) as http:
            response = http.get(_info_url(info), headers=headers(_endpoint(info)))
            body: object = None if response.status_code == 404 else response.json()
    except httpx.TimeoutException:
        return _Probe(timed_out=True)
    except (httpx.HTTPError, ValueError):
        return _Probe()
    return _classify(info, response.status_code, body)


async def _async_probe(info: _Info, timeout: float) -> _Probe:
    try:
        async with httpx.AsyncClient(timeout=timeout, trust_env=False) as http:
            response = await http.get(_info_url(info), headers=headers(_endpoint(info)))
            body: object = None if response.status_code == 404 else response.json()
    except httpx.TimeoutException:
        return _Probe(timed_out=True)
    except (httpx.HTTPError, ValueError):
        return _Probe()
    return _classify(info, response.status_code, body)


# --- registration file ---


def _read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _parse_info(value: object) -> _Info | None:
    if not isinstance(value, dict):
        return None
    data = cast("dict[str, object]", value)
    url, pid = data.get("url"), data.get("pid")
    if not isinstance(url, str) or isinstance(pid, bool) or not isinstance(pid, int):
        return None

    def text(key: str) -> str | None:
        item = data.get(key)
        return item if isinstance(item, str) else None

    return _Info(url=url, pid=pid, id=text("id"), version=text("version"), password=text("password"))


def _read(file: Path) -> _Info | None:
    return _parse_info(_read_json(file))


def _registered(file: Path, timeout: float) -> _Registration:
    info = _read(file)
    if info is None:
        return _Registration()
    probe = _probe(info, timeout)
    return _Registration(info, probe.service, probe.timed_out)


async def _async_registered(file: Path, timeout: float) -> _Registration:
    info = _read(file)
    if info is None:
        return _Registration()
    probe = await _async_probe(info, timeout)
    return _Registration(info, probe.service, probe.timed_out)


def _discovered(registration: _Registration, version: Version | None) -> Endpoint | None:
    found = registration.service
    if found is None or found.state != "ready" or not found.compatible:
        return None
    if not _matches_version(found.version, version):
        return None
    return found.endpoint


# --- persistent terminal handoff (pty-handoff.ts) ---


@dataclass(frozen=True)
class _Source:
    pid: int
    url: str
    id: str | None = None


@dataclass(frozen=True)
class _Sidecar:
    source: _Source
    handoff: dict[str, Any] | None
    expires_at: float


def _sidecar_path(file: Path) -> Path:
    return file.with_name(file.name + ".pty-handoff")


def _is_handoff(value: object) -> bool:
    if not isinstance(value, dict):
        return False
    data = cast("dict[str, object]", value)
    expires = data.get("expiresAt")
    return (
        isinstance(data.get("directory"), str)
        and isinstance(data.get("instanceID"), str)
        and isinstance(data.get("ticket"), str)
        and _is_number(expires)
    )


def _is_number(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and value == value
        and abs(value) != float("inf")
    )


def _read_sidecar(file: Path) -> _Sidecar | None:
    value = _read_json(_sidecar_path(file))
    if not isinstance(value, dict):
        return None
    data = cast("dict[str, object]", value)
    if "source" not in data or "handoff" not in data:
        return None
    source = data["source"]
    if not isinstance(source, dict):
        return None
    src = cast("dict[str, object]", source)
    pid, url, id_ = src.get("pid"), src.get("url"), src.get("id")
    if not _is_number(pid) or not isinstance(url, str):
        return None
    if "id" in src and not isinstance(id_, str):
        return None
    handoff = data["handoff"]
    if handoff is not None and not _is_handoff(handoff):
        return None
    expires = data.get("expiresAt")
    if not _is_number(expires):
        return None
    return _Sidecar(
        _Source(pid=cast("int", pid), url=url, id=id_ if isinstance(id_, str) else None),
        cast("dict[str, Any] | None", handoff),
        cast("float", expires),
    )


def _same_source(source: _Source, info: _Info) -> bool:
    return source.id == info.id and source.pid == info.pid and source.url == info.url


def _fresh_for(record: _Sidecar | None, info: _Info) -> bool:
    return record is not None and record.expires_at > _now_ms() and _same_source(record.source, info)


def _parse_handoff(body: object) -> dict[str, Any] | None:
    if not isinstance(body, dict) or "handoff" not in body:
        raise ValueError("Invalid persistent terminal handoff response")
    handoff = cast("dict[str, object]", body)["handoff"]
    if handoff is None:
        return None
    if not _is_handoff(handoff) or cast("dict[str, Any]", handoff)["expiresAt"] <= _now_ms():
        raise ValueError("Invalid or expired persistent terminal handoff")
    return cast("dict[str, Any]", handoff)


def _publish(file: Path, info: _Info, handoff: dict[str, Any] | None) -> None:
    temporary = file.with_name(f"{file.name}.pty-handoff.{uuid.uuid4()}.tmp")
    record = {
        "source": {
            key: value for key, value in (("id", info.id), ("pid", info.pid), ("url", info.url)) if value is not None
        },
        "handoff": handoff,
        "expiresAt": handoff["expiresAt"] if handoff is not None else _now_ms() + _HANDOFF_TTL_MS,
    }
    try:
        descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump(record, stream, separators=(",", ":"))
        os.replace(temporary, _sidecar_path(file))
    finally:
        with contextlib.suppress(FileNotFoundError):
            temporary.unlink()


def _pty_url(info: _Info, action: str) -> httpx.URL:
    return httpx.URL(info.url).join(f"/api/experimental/persistent-pty/{action}")


def _pty_headers(info: _Info) -> dict[str, str] | None:
    return None if info.password is None else {"authorization": _basic(DEFAULT_USERNAME, info.password)}


def _handoff_failed(file: Path, info: _Info, cause: Exception) -> bool:
    """Whether the old service's terminals must be shut down, after a failed handoff request."""
    # Another caller may already have prepared and stopped this server.
    if _fresh_for(_read_sidecar(file), info):
        return False
    log.warning(
        "Background service cannot hand off persistent terminals; shutting them down before replacement: %s", cause
    )
    return True


def _publish_logged(file: Path, info: _Info, handoff: dict[str, Any] | None) -> None:
    try:
        _publish(file, info, handoff)
    except OSError as cause:
        log.warning("Failed to publish persistent terminal handoff: %s", cause)


def _pty_prepare(file: Path, info: _Info, timeout: float) -> None:
    # Publish the ticket before stopping its owner so every replacement contender can adopt it.
    if _fresh_for(_read_sidecar(file), info):
        return
    with httpx.Client(timeout=timeout, trust_env=False, headers=_pty_headers(info)) as http:
        try:
            response = http.post(_pty_url(info, "handoff"))
            response.raise_for_status()
            handoff = _parse_handoff(response.json())
        except (httpx.HTTPError, ValueError) as cause:
            if not _handoff_failed(file, info, cause):
                return
            with contextlib.suppress(httpx.HTTPError):
                http.post(_pty_url(info, "shutdown"))
            handoff = None
    _publish_logged(file, info, handoff)


async def _async_pty_prepare(file: Path, info: _Info, timeout: float) -> None:
    if _fresh_for(_read_sidecar(file), info):
        return
    async with httpx.AsyncClient(timeout=timeout, trust_env=False, headers=_pty_headers(info)) as http:
        try:
            response = await http.post(_pty_url(info, "handoff"))
            response.raise_for_status()
            handoff = _parse_handoff(response.json())
        except (httpx.HTTPError, ValueError) as cause:
            if not _handoff_failed(file, info, cause):
                return
            with contextlib.suppress(httpx.HTTPError):
                await http.post(_pty_url(info, "shutdown"))
            handoff = None
    _publish_logged(file, info, handoff)


def _pty_environment(file: Path, env: Mapping[str, str] | None) -> dict[str, str | None]:
    record = _read_sidecar(file)
    current = _read_json(file)
    usable = record is not None and record.expires_at > _now_ms()
    if usable and record is not None and isinstance(current, dict):
        data = cast("dict[str, object]", current)
        usable = record.source.id == data.get("id") and record.source.pid == data.get("pid")
        usable = usable and record.source.url == data.get("url")
    handoff = record.handoff if usable and record is not None else None
    return {
        **(env or {}),
        "OPENCODE_PTY_HANDOFF": None if handoff is None else json.dumps(handoff, separators=(",", ":")),
    }


def _pty_complete(file: Path, info: _Info) -> None:
    record = _read_sidecar(file)
    if record is not None and not _same_source(record.source, info):
        _pty_clear(file)


def _pty_clear(file: Path) -> None:
    with contextlib.suppress(FileNotFoundError):
        _sidecar_path(file).unlink()


# --- startup attempts (service-contender.ts) ---

# Detached service processes this interpreter started. Keeping them referenced until they are reaped stops
# ``subprocess`` from warning about a still-running child when the ``Popen`` object is collected.
_children: set[subprocess.Popen[bytes]] = set()


class _Contender:
    """One ``opencode serve --service`` attempt. Losers of the startup race exit with code 0."""

    def __init__(self, command: Sequence[str], env: Mapping[str, str | None]) -> None:
        merged = {**os.environ, **env}
        environment = {key: value for key, value in merged.items() if value is not None}
        executable = _resolve(command[0], environment.get("PATH", os.defpath))
        if sys.platform == "win32":  # pragma: no cover - Windows only
            self.process = subprocess.Popen(
                [executable, *command[1:]],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                env=environment,
                creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW,
            )
        else:
            self.process = subprocess.Popen(
                [executable, *command[1:]],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                env=environment,
                start_new_session=True,
            )
        _children.add(self.process)
        self._stderr: bytes = b""
        self._capture = True
        self._closed = threading.Event()
        threading.Thread(target=self._drain, name="opencode-service-stderr", daemon=True).start()

    def _drain(self) -> None:
        stream = self.process.stderr
        assert stream is not None
        with stream:
            for chunk in iter(lambda: os.read(stream.fileno(), 4096), b""):
                if self._capture:
                    self._stderr = (self._stderr + chunk)[-_STDERR_LIMIT:]
        self.process.wait()
        _children.discard(self.process)
        self._closed.set()

    @property
    def pid(self) -> int:
        return self.process.pid

    def closed(self) -> bool:
        return self._closed.is_set()

    def stderr(self) -> str:
        return self._stderr.decode("utf-8", "replace").strip()

    def release(self) -> None:
        # Keep draining so a chatty service never blocks on a full pipe, but stop keeping its output.
        self._capture = False
        self._stderr = b""

    def failure(self) -> ServiceError | None:
        code = self.process.returncode
        if code is None or code == 0:
            return None
        if code > 0 or sys.platform == "win32":
            return _startup_error(f"Server process exited with code {code}", self.stderr())
        try:
            name = signal.Signals(-code).name
        except ValueError:
            name = str(-code)
        return _startup_error(f"Server process terminated by {name}", self.stderr())


def _resolve(command: str, search_path: str) -> str:
    """Find ``command`` on ``search_path``, the child's ``PATH``, as Node's spawn does.

    ``shutil.which`` on Windows also searches the current directory first, which Node's spawn in the TypeScript
    client does not, so a planted ``opencode.exe`` there could run. A command with a directory part is used as is.

    Raises:
        FileNotFoundError: ``command`` is not on ``PATH``.
    """
    if os.path.dirname(command):
        return command
    for directory in search_path.split(os.pathsep):
        if directory and (found := shutil.which(os.path.join(directory, command))) is not None:
            return found
    # Never hand Popen a bare name: Windows CreateProcess would search the current directory for it.
    raise FileNotFoundError(f"{command!r} was not found on PATH")


def _startup_error(message: str, stderr: str) -> ServiceError:
    return ServiceError(f"{message}\n{stderr}" if stderr else message)


@dataclass
class _Pool:
    """The startup attempts of one ``ensure`` call: at most two alive, the first failure remembered."""

    timing: _Timing
    contenders: list[_Contender] = field(default_factory=cast("Callable[[], list[_Contender]]", list))
    failure: ServiceError | None = None
    spawn_delay: float = 0.0
    last_spawn: float | None = None

    def __post_init__(self) -> None:
        self.spawn_delay = self.timing.spawn_delay

    def service_answered(self) -> None:
        self.spawn_delay = self.timing.spawn_delay

    def evict(self, pid: int) -> None:
        for item in list(self.contenders):
            if item.pid == pid or item.closed():
                item.release()
                self.contenders.remove(item)
        self.failure = None
        self.last_spawn = None

    def recruit_now(self) -> None:
        self.last_spawn = time.monotonic() - self.spawn_delay

    def reap(self) -> ServiceError | None:
        finished = [item for item in self.contenders if item.closed()]
        if self.failure is None:
            self.failure = next((error for item in finished if (error := item.failure()) is not None), None)
        if any(item.process.returncode == 0 for item in finished):
            self.spawn_delay = min(self.spawn_delay * 2, self.timing.max_spawn_delay)
        for item in finished:
            self.contenders.remove(item)
        return self.failure if not self.contenders else None

    def should_recruit(self, registered: bool) -> bool:
        if self.last_spawn is None and registered:
            self.last_spawn = time.monotonic()
        # Keep one candidate plus one lock probe for pre-lock stalls. After a failure, let the survivors finish
        # without recruiting replacements that could hide the error indefinitely.
        since = float("inf") if self.last_spawn is None else time.monotonic() - self.last_spawn
        return self.failure is None and len(self.contenders) < 2 and since >= self.spawn_delay

    def add(self, contender: _Contender) -> None:
        self.contenders.append(contender)
        self.last_spawn = time.monotonic()

    def release_all(self) -> None:
        for contender in self.contenders:
            contender.release()


# --- stopping processes ---


def _signal(pid: int, sig: int) -> None:
    with contextlib.suppress(OSError):
        os.kill(pid, sig)


def _stopped(pid: int) -> bool:
    if sys.platform == "win32":
        return not _windows_alive(pid)
    try:
        os.kill(pid, 0)
    except OSError:
        return True
    return False


def _windows_alive(pid: int) -> bool:  # pragma: no cover - Windows only
    import ctypes

    kernel32: Any = getattr(ctypes, "windll").kernel32  # noqa: B009 - only defined on Windows
    handle = kernel32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
    if not handle:
        return False
    try:
        code = ctypes.c_ulong()
        kernel32.GetExitCodeProcess(handle, ctypes.byref(code))
        return bool(code.value == 259)  # STILL_ACTIVE
    finally:
        kernel32.CloseHandle(handle)


_KILL = getattr(signal, "SIGKILL", signal.SIGTERM)


def _terminate_steps(file: Path, info: _Info) -> bool:
    current = _read(file)
    if current is None or not _same(current, info):
        return False
    _signal(info.pid, signal.SIGTERM)
    return True


def _remove_if_same(file: Path, info: _Info) -> None:
    latest = _read(file)
    if latest is None or not _same(latest, info):
        return
    with contextlib.suppress(FileNotFoundError):
        file.unlink()


def _wait_until_stopped(pid: int, timing: _Timing) -> bool:
    for attempt in range(timing.stop_poll_attempts + 1):
        if _stopped(pid):
            return True
        if attempt < timing.stop_poll_attempts:
            _sleep(timing.stop_poll_interval)
    return False


async def _async_wait_until_stopped(pid: int, timing: _Timing) -> bool:
    for attempt in range(timing.stop_poll_attempts + 1):
        if _stopped(pid):
            return True
        if attempt < timing.stop_poll_attempts:
            await _async_sleep(timing.stop_poll_interval)
    return False


def _terminate(file: Path, info: _Info, timing: _Timing) -> None:
    if not _terminate_steps(file, info):
        return
    # The registration can disappear or change hands before this process exits. Only the PID we signalled can
    # tell us whether it has stopped, so escalate based on that process.
    if not _wait_until_stopped(info.pid, timing):
        _signal(info.pid, _KILL)
        if not _wait_until_stopped(info.pid, timing):
            raise ServiceError(f"Server process {info.pid} is still running")
    _remove_if_same(file, info)


async def _async_terminate(file: Path, info: _Info, timing: _Timing) -> None:
    if not _terminate_steps(file, info):
        return
    if not await _async_wait_until_stopped(info.pid, timing):
        _signal(info.pid, _KILL)
        if not await _async_wait_until_stopped(info.pid, timing):
            raise ServiceError(f"Server process {info.pid} is still running")
    _remove_if_same(file, info)


# --- public operations ---


def discover(file: str | os.PathLike[str] | None = None, version: Version | None = None) -> Endpoint | None:
    """Find a healthy, compatible local service without starting one.

    Args:
        file: Registration file. Defaults to :func:`default_file`.
        version: Required exact version, or a predicate on the service version.

    Returns:
        The service endpoint, or ``None`` when no ready service with a matching version is registered.
    """
    return _discovered(_registered(_file(file), _TIMING.request_timeout), version)


async def async_discover(file: str | os.PathLike[str] | None = None, version: Version | None = None) -> Endpoint | None:
    """Async version of :func:`discover`."""
    return _discovered(await _async_registered(_file(file), _TIMING.request_timeout), version)


@dataclass
class _Ensure:
    """State and decisions shared by the sync and async ``ensure`` loops."""

    file: Path
    version: Version | None
    command: Sequence[str]
    env: Mapping[str, str] | None
    on_start: Callable[[EnsureReason, str | None], None] | None
    timing: _Timing
    pool: _Pool
    deadline: float
    timeouts: tuple[_Info, int] | None = None
    announced: bool = False

    def announce(self, reason: EnsureReason, previous_version: str | None = None) -> None:
        if self.announced:
            return
        self.announced = True
        if self.on_start is not None:
            self.on_start(reason, previous_version)

    def check_deadline(self) -> None:
        if time.monotonic() >= self.deadline:
            raise self.pool.failure or ServiceError("Timed out waiting for the background service to start")

    def unresponsive(self, registration: _Registration) -> _Info | None:
        """The registered owner to replace after three consecutive timed-out probes."""
        info = registration.info
        if not registration.timed_out or info is None:
            self.timeouts = None
            return None
        count = self.timeouts[1] + 1 if self.timeouts is not None and _same(self.timeouts[0], info) else 1
        self.timeouts = (info, count)
        if count < 3:
            return None
        self.announce("missing")
        log.warning("Background service is unresponsive; recovery cannot preserve persistent terminals")
        _pty_clear(self.file)
        return info

    def recovered(self, info: _Info) -> None:
        self.pool.evict(info.pid)
        self.pool.recruit_now()
        self.timeouts = None

    def spawn(self) -> None:
        if not self.command:
            raise ServiceError("Missing service command")
        try:
            contender = _Contender(self.command, _pty_environment(self.file, self.env))
        except OSError as cause:
            raise ServiceError("Failed to start server") from cause
        self.pool.add(contender)

    def no_answer(self, registration: _Registration) -> None:
        failed = self.pool.reap()
        if failed is not None:
            raise failed
        if self.pool.should_recruit(registration.info is not None):
            self.announce("missing")
            self.spawn()


def _ensure_state(
    file: str | os.PathLike[str] | None,
    version: Version | None,
    command: Sequence[str] | None,
    env: Mapping[str, str] | None,
    on_start: Callable[[EnsureReason, str | None], None] | None,
) -> _Ensure:
    timing = _TIMING
    return _Ensure(
        file=_file(file),
        version=version,
        command=command if command is not None else ("opencode", "serve", "--service"),
        env=env,
        on_start=on_start,
        timing=timing,
        pool=_Pool(timing),
        deadline=time.monotonic() + timing.timeout,
    )


def ensure(
    file: str | os.PathLike[str] | None = None,
    version: Version | None = None,
    *,
    command: Sequence[str] | None = None,
    env: Mapping[str, str] | None = None,
    on_start: Callable[[EnsureReason, str | None], None] | None = None,
) -> Endpoint:
    """Return a healthy local service, starting ``opencode serve --service`` when none is running.

    A registered service whose version does not satisfy ``version`` is stopped and replaced; its persistent
    terminals are handed off to the replacement when it is ready. Several processes may call this at once: each
    starts at most two attempts, the service's own lock picks one winner, and the losers exit cleanly. Gives up
    after 120 seconds.

    Args:
        file: Registration file. Defaults to :func:`default_file`.
        version: Required exact version, or a predicate on the service version.
        command: Service command and arguments. Defaults to ``opencode serve --service``.
        env: Variables added to the inherited environment of a started service.
        on_start: Called once, before the first process is started, with the reason and, for
            ``"version-mismatch"``, the version being replaced.

    Raises:
        ServiceError: The service failed to start, uses an incompatible protocol, or did not answer in time.
    """
    state = _ensure_state(file, version, command, env, on_start)
    try:
        while True:
            state.check_deadline()
            registration = _registered(state.file, state.timing.request_timeout)
            stale = state.unresponsive(registration)
            if stale is not None:
                _terminate(state.file, stale, state.timing)
                state.recovered(stale)

            service = registration.service
            if service is not None:
                state.pool.service_answered()
                decision = _decide(service, state.version)
                if decision.tag == "fail":
                    raise ServiceError(decision.error)
                if decision.tag == "reuse":
                    _pty_complete(state.file, service.info)
                    return service.endpoint
                if decision.tag == "replace":
                    state.announce("version-mismatch", service.version)
                    if service.state != "ready":
                        log.warning("Background service is not ready; replacement cannot preserve persistent terminals")
                    with contextlib.suppress(Exception):
                        stop(state.file, pty=decision.pty)
                    state.pool.evict(service.info.pid)
            else:
                state.no_answer(registration)
            _sleep(state.timing.poll_interval)
    finally:
        state.pool.release_all()


async def async_ensure(
    file: str | os.PathLike[str] | None = None,
    version: Version | None = None,
    *,
    command: Sequence[str] | None = None,
    env: Mapping[str, str] | None = None,
    on_start: Callable[[EnsureReason, str | None], None] | None = None,
) -> Endpoint:
    """Async version of :func:`ensure`."""
    state = _ensure_state(file, version, command, env, on_start)
    try:
        while True:
            state.check_deadline()
            registration = await _async_registered(state.file, state.timing.request_timeout)
            stale = state.unresponsive(registration)
            if stale is not None:
                await _async_terminate(state.file, stale, state.timing)
                state.recovered(stale)

            service = registration.service
            if service is not None:
                state.pool.service_answered()
                decision = _decide(service, state.version)
                if decision.tag == "fail":
                    raise ServiceError(decision.error)
                if decision.tag == "reuse":
                    _pty_complete(state.file, service.info)
                    return service.endpoint
                if decision.tag == "replace":
                    state.announce("version-mismatch", service.version)
                    if service.state != "ready":
                        log.warning("Background service is not ready; replacement cannot preserve persistent terminals")
                    with contextlib.suppress(Exception):
                        await async_stop(state.file, pty=decision.pty)
                    state.pool.evict(service.info.pid)
            else:
                state.no_answer(registration)
            await _async_sleep(state.timing.poll_interval)
    finally:
        state.pool.release_all()


def stop(file: str | os.PathLike[str] | None = None, *, pty: PtyMode = "clear") -> None:
    """Stop the registered local service and remove its registration.

    Args:
        file: Registration file. Defaults to :func:`default_file`.
        pty: ``"clear"`` shuts persistent terminals down with the service. ``"handoff"`` first asks the service
            for a handoff ticket that the next service started by :func:`ensure` adopts. The handoff is best
            effort and never keeps the old service running.

    Raises:
        ServiceError: The process was still running after ``SIGTERM`` and ``SIGKILL``.
    """
    path = _file(file)
    info = _read(path)
    try:
        if pty == "handoff" and info is not None:
            _pty_prepare(path, info, _TIMING.request_timeout)
        else:
            _pty_clear(path)
    except Exception as cause:
        log.warning("Failed to prepare persistent terminals for replacement: %s", cause)
    if info is not None:
        _terminate(path, info, _TIMING)


async def async_stop(file: str | os.PathLike[str] | None = None, *, pty: PtyMode = "clear") -> None:
    """Async version of :func:`stop`."""
    path = _file(file)
    info = _read(path)
    try:
        if pty == "handoff" and info is not None:
            await _async_pty_prepare(path, info, _TIMING.request_timeout)
        else:
            _pty_clear(path)
    except Exception as cause:
        log.warning("Failed to prepare persistent terminals for replacement: %s", cause)
    if info is not None:
        await _async_terminate(path, info, _TIMING)
