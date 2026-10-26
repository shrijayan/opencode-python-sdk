"""An in-process fake OpenCode server for your own tests.

:class:`FakeServer` is an ``httpx`` transport that answers like an OpenCode server, keeping sessions, messages and
events in memory. Plug it into a client and test code that uses the SDK without starting ``opencode serve`` or
calling a model::

    from opencode import Opencode
    from opencode.testing import FakeServer

    fake = FakeServer(reply="Done.")
    client = Opencode.fake(fake)  # or Opencode(transport=fake)

    result = client.session.run("Fix the bug", agent="build")
    assert result.text == "Done."
    assert fake.prompts == ["Fix the bug"]

It covers sessions (create, get, list, remove, switch agent or model), prompts, waiting, interrupts, messages,
agents, MCP servers, server info and the event stream. Every payload is built from the generated models, so it
has the shape the real server sends. Other routes answer ``404``. Use :meth:`FakeServer.fail` to make a route fail.
"""

from __future__ import annotations

import itertools
import json
import os
import re
import time
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from typing import Any, TypeVar

import httpx

from ._models import BaseModel
from .types import (
    AgentInfo,
    AgentListResponse,
    LocationPublicRef,
    McpListResponse,
    McpServer,
    ModelRef,
    ServerConnectedEvent,
    ServerInfo,
    SessionCreatedEvent,
    SessionIdleEvent,
    SessionInboxUser,
    SessionInfo,
    SessionInterruptResponse,
    SessionMessageAssistant,
    SessionMessageAssistantText,
    SessionMessageIdle,
    SessionMessageUser,
    TokenUsageInfo,
)

__all__ = ["DEFAULT_MODEL", "FakeServer"]

_M = TypeVar("_M", bound=BaseModel)


def _model(cls: type[_M], data: object) -> _M:
    """Validates ``data`` written with field names or wire names (``provider_id`` or ``providerID``)."""
    return cls.model_validate(data, by_alias=True, by_name=True)


DEFAULT_MODEL = _model(ModelRef, {"id": "fake-model", "provider_id": "fake"})
"""Model reported for sessions created without one."""

Reply = str | Callable[[str], str]
"""Assistant reply: fixed text, or a function from the prompt text to the reply."""


@dataclass
class _Failure:
    method: str
    path: re.Pattern[str]
    status: int
    body: object
    exception: BaseException | None
    times: int | None


class FakeServer(httpx.MockTransport):
    """An in-memory OpenCode server, usable as the ``transport`` of :class:`opencode.Opencode` and
    :class:`opencode.AsyncOpencode`.

    Args:
        reply: What the assistant answers to each prompt: text, or a function of the prompt text.
        agents: Agent ids :meth:`opencode.Opencode.agent.list` reports. Add more later with :meth:`add_agent`.
        mcp_servers: MCP server names mapped to their status (``connected``, ``pending``, ``failed``, ...).
        directory: Project directory reported as every session's location.
        cost: Cost in USD reported for each assistant reply.
        tokens: Input and output tokens reported for each assistant reply.

    Attributes:
        sessions: Sessions by id.
        messages: Messages of each session, oldest first.
        events: Events the stream replays after ``server.connected``.
        requests: Every request received, in order.
    """

    def __init__(
        self,
        *,
        reply: Reply = "OK",
        agents: Iterable[str] = ("build", "plan"),
        mcp_servers: Mapping[str, str] | None = None,
        directory: str = "/fake/project",
        cost: float = 0.001,
        tokens: tuple[int, int] = (10, 5),
    ) -> None:
        super().__init__(self._handle)
        self.reply: Reply = reply
        self.directory = directory
        self.cost = cost
        self.tokens = tokens
        self.sessions: dict[str, SessionInfo] = {}
        self.messages: dict[str, list[BaseModel]] = {}
        self.inbox: dict[str, list[SessionInboxUser]] = {}
        self.events: list[BaseModel] = []
        self.requests: list[httpx.Request] = []
        self._agents: list[tuple[str, int]] = [(agent, 0) for agent in agents]
        self._mcp: dict[str, tuple[str, int]] = {name: (status, 0) for name, status in (mcp_servers or {}).items()}
        self._polls = {"agent": 0, "mcp": 0}
        self._failures: list[_Failure] = []
        self._ids = itertools.count(1)

    # -- configuration --------------------------------------------------------------------------------------

    def add_agent(self, agent: str, *, after_polls: int = 0) -> None:
        """Lists ``agent`` once ``GET /api/agent`` has been called ``after_polls`` more times, like an agent that
        loads after boot."""
        self._agents.append((agent, self._polls["agent"] + after_polls))

    def set_mcp_status(self, name: str, status: str = "connected", *, after_polls: int = 0) -> None:
        """Reports MCP server ``name`` with ``status`` once ``GET /api/mcp`` has been called ``after_polls`` more
        times."""
        self._mcp[name] = (status, self._polls["mcp"] + after_polls)

    def fail(
        self,
        method: str,
        path: str,
        *,
        status: int = 500,
        body: object = None,
        exception: BaseException | None = None,
        times: int | None = 1,
    ) -> None:
        """Makes matching requests fail.

        Args:
            method: HTTP method, such as ``POST``.
            path: Regular expression matched against the whole request path, such as ``/api/session/[^/]+/prompt``.
            status: Status of the error response.
            body: JSON error body. Defaults to an untagged body, so the error class follows ``status``.
            exception: Raise this from the transport instead of answering, for example ``httpx.ConnectError(...)``
                or ``KeyboardInterrupt()``.
            times: How many requests fail; ``None`` for all of them.
        """
        if body is None:
            body = {"message": f"Injected failure ({status})"}
        self._failures.append(_Failure(method.upper(), re.compile(path), status, body, exception, times))

    @property
    def prompts(self) -> list[str]:
        """Text of every prompt received, in order."""
        texts: list[str] = []
        for request in self.requests:
            if request.method == "POST" and request.url.path.endswith("/prompt"):
                texts.append(json.loads(request.content)["text"])
        return texts

    # -- helpers --------------------------------------------------------------------------------------------

    def _id(self, prefix: str) -> str:
        return f"{prefix}_{next(self._ids):026d}"

    @staticmethod
    def _now() -> float:
        return float(time.time_ns() // 1_000_000)

    @property
    def _location(self) -> LocationPublicRef:
        return LocationPublicRef(directory=self.directory)

    def _session(self, session_id: str) -> SessionInfo:
        try:
            return self.sessions[session_id]
        except KeyError:
            raise _ErrorResponse(
                404,
                {
                    "_tag": "SessionNotFoundError",
                    "sessionID": session_id,
                    "message": f"Session not found: {session_id}",
                },
            ) from None

    @staticmethod
    def _body(request: httpx.Request) -> dict[str, Any]:
        if not request.content:
            return {}
        try:
            payload = json.loads(request.content)
        except ValueError:
            raise _invalid("Request body is not JSON") from None
        if not isinstance(payload, dict):
            raise _invalid("Request body must be an object")
        return dict(payload)  # pyright: ignore[reportUnknownArgumentType]

    def _record(self, event: BaseModel) -> None:
        self.events.append(event)

    def _run(self, session: SessionInfo, text: str) -> None:
        """Answers one prompt synchronously: assistant reply, idle marker, usage, events."""
        reply = self.reply(text) if callable(self.reply) else self.reply
        now = self._now()
        input_tokens, output_tokens = self.tokens
        usage = {"input": input_tokens, "output": output_tokens, "reasoning": 0, "cache": {"read": 0, "write": 0}}
        self.messages[session.id] += [
            _model(SessionMessageAssistant, 
                {
                    "id": self._id("msg"),
                    "type": "assistant",
                    "time": {"created": now, "completed": now},
                    "agent": session.agent or "build",
                    "model": (session.model or DEFAULT_MODEL).to_dict(),
                    "content": [SessionMessageAssistantText(type="text", text=reply).to_dict()],
                    "finish": "stop",
                    "cost": self.cost,
                    "tokens": usage,
                }
            ),
            _model(SessionMessageIdle, 
                {"id": self._id("msg"), "type": "idle", "time": {"created": now}, "outcome": "succeeded"}
            ),
        ]
        session.cost += self.cost
        session.tokens = _model(TokenUsageInfo, 
            {
                "input": session.tokens.input + input_tokens,
                "output": session.tokens.output + output_tokens,
                "reasoning": session.tokens.reasoning,
                "cache": session.tokens.cache.to_dict(),
            }
        )
        session.outcome = "succeeded"
        session.time.updated = session.time.idle = now
        self._record(
            _model(SessionIdleEvent, 
                {"id": self._id("evt"), "created": now, "type": "session.idle", "data": {"sessionID": session.id}}
            )
        )

    # -- routes ---------------------------------------------------------------------------------------------

    def _server_info(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        info = _model(ServerInfo, 
            {
                "version": "fake",
                "pid": os.getpid(),
                "urls": [str(request.url.copy_with(path="/"))],
                "paths": {"tmp": "/tmp"},
            }
        )
        return _json(info)

    def _agent_list(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        self._polls["agent"] += 1
        visible = [agent for agent, after in self._agents if self._polls["agent"] > after]
        agents = [
            _model(AgentInfo, 
                {
                    "id": agent,
                    "name": agent,
                    "mode": "primary",
                    "hidden": False,
                    "request": {"settings": {}, "headers": {}, "body": {}},
                    "permissions": [],
                }
            )
            for agent in dict.fromkeys(visible)
        ]
        return _json(AgentListResponse(location=self._location, data=agents))

    def _mcp_list(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        self._polls["mcp"] += 1
        servers = [
            _model(McpServer, 
                {"name": name, "status": _mcp_status(status if self._polls["mcp"] > after else "pending")}
            )
            for name, (status, after) in self._mcp.items()
        ]
        return _json(McpListResponse(location=self._location, data=servers))

    def _session_create(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        body = self._body(request)
        now = self._now()
        session_id = body.get("id") or self._id("ses")
        if session_id in self.sessions:
            raise _ErrorResponse(409, {"_tag": "ConflictError", "message": f"Session already exists: {session_id}"})
        session = _model(SessionInfo, 
            {
                "id": session_id,
                "parentID": body.get("parentID"),
                "projectID": "prj_fake",
                "agent": body.get("agent"),
                "model": body.get("model") or DEFAULT_MODEL.to_dict(),
                "cost": 0,
                "tokens": {"input": 0, "output": 0, "reasoning": 0, "cache": {"read": 0, "write": 0}},
                "time": {"created": now, "updated": now},
                "title": body.get("title"),
                "metadata": body.get("metadata"),
                "location": self._location.to_dict(),
            }
        )
        self.sessions[session.id] = session
        self.messages[session.id] = []
        self.inbox[session.id] = []
        self._record(
            _model(SessionCreatedEvent, 
                {
                    "id": self._id("evt"),
                    "created": now,
                    "type": "session.created",
                    "durable": {"aggregate_id": session.id, "seq": 0, "version": 1},
                    "data": {
                        "sessionID": session.id,
                        "projectID": session.project_id,
                        "location": {"directory": self.directory},
                        "slug": session.id,
                        "title": session.title,
                        "agent": session.agent,
                        "version": "fake",
                    },
                }
            )
        )
        return _json({"data": session.to_dict()})

    def _session_list(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        sessions = list(self.sessions.values())
        return _page(request, [session.to_dict() for session in sessions], newest_first_default=True)

    def _session_get(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        return _json({"data": self._session(match["id"]).to_dict()})

    def _session_remove(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        self._session(match["id"])
        del self.sessions[match["id"]]
        self.messages.pop(match["id"], None)
        self.inbox.pop(match["id"], None)
        return httpx.Response(204)

    def _session_agent(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        session = self._session(match["id"])
        agent = self._body(request).get("agent")
        if not isinstance(agent, str):
            raise _invalid("agent is required", field="agent")
        session.agent = agent
        return httpx.Response(204)

    def _session_model(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        session = self._session(match["id"])
        session.model = _model(ModelRef, self._body(request).get("model"))
        return httpx.Response(204)

    def _session_prompt(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        session = self._session(match["id"])
        body = self._body(request)
        text = body.get("text")
        if not isinstance(text, str):
            raise _invalid("text is required", field="text")
        now = self._now()
        message_id = body.get("id") or self._id("msg")
        payload = {key: body[key] for key in ("text", "files", "agents", "skills", "metadata") if key in body}
        queued = _model(SessionInboxUser, 
            {
                "id": message_id,
                "sessionID": session.id,
                "time": {"created": now},
                "type": "user",
                "payload": payload,
                "delivery": body.get("delivery") or "queue",
            }
        )
        if body.get("resume") is False:
            self.inbox[session.id].append(queued)
        else:
            self.messages[session.id].append(
                _model(SessionMessageUser, 
                    {
                        "id": message_id,
                        "type": "user",
                        "time": {"created": now},
                        "text": text,
                        "metadata": body.get("metadata"),
                    }
                )
            )
            self._run(session, text)
        return _json({"data": queued.to_dict()})

    def _session_wait(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        self._session(match["id"])
        return httpx.Response(204)

    def _session_interrupt(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        self._session(match["id"])
        return _json(SessionInterruptResponse(interrupted=False))

    def _message_list(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        self._session(match["id"])
        wanted = request.url.params.get("type")
        items = [
            m.to_dict() for m in self.messages[match["id"]] if wanted is None or getattr(m, "type", None) == wanted
        ]
        return _page(request, items, newest_first_default=False)

    def _event_stream(self, request: httpx.Request, match: re.Match[str]) -> httpx.Response:
        connected = _model(ServerConnectedEvent, {"id": self._id("evt"), "type": "server.connected", "data": {}})
        chunks = [f"data: {json.dumps(event.to_dict())}\n\n" for event in [connected, *self.events]]
        return httpx.Response(200, headers={"content-type": "text/event-stream"}, content="".join(chunks).encode())

    _ROUTES: tuple[tuple[str, str, Callable[..., httpx.Response]], ...] = (
        ("GET", r"/api/info", _server_info),
        ("GET", r"/api/agent", _agent_list),
        ("GET", r"/api/mcp", _mcp_list),
        ("GET", r"/api/event", _event_stream),
        ("POST", r"/api/session", _session_create),
        ("GET", r"/api/session", _session_list),
        ("GET", r"/api/session/(?P<id>[^/]+)", _session_get),
        ("DELETE", r"/api/session/(?P<id>[^/]+)", _session_remove),
        ("POST", r"/api/session/(?P<id>[^/]+)/agent", _session_agent),
        ("POST", r"/api/session/(?P<id>[^/]+)/model", _session_model),
        ("POST", r"/api/session/(?P<id>[^/]+)/prompt", _session_prompt),
        ("POST", r"/api/session/(?P<id>[^/]+)/interrupt", _session_interrupt),
        ("GET", r"/api/session/(?P<id>[^/]+)/message", _message_list),
        ("POST", r"/api/experimental/session/(?P<id>[^/]+)/wait", _session_wait),
    )

    def _handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        path = request.url.path
        for failure in self._failures:
            if failure.method == request.method and failure.path.fullmatch(path) and failure.times != 0:
                if failure.times is not None:
                    failure.times -= 1
                if failure.exception is not None:
                    raise failure.exception
                return httpx.Response(failure.status, json=failure.body)
        for method, pattern, handler in self._ROUTES:
            match = re.fullmatch(pattern, path)
            if match and method == request.method:
                try:
                    return handler(self, request, match)
                except _ErrorResponse as error:
                    return httpx.Response(error.status, json=error.body)
        return httpx.Response(
            404, json={"_tag": "NotFoundError", "message": f"FakeServer does not implement {request.method} {path}"}
        )


class _ErrorResponse(Exception):
    def __init__(self, status: int, body: dict[str, object]) -> None:
        super().__init__(body.get("message"))
        self.status = status
        self.body = body


def _mcp_status(status: str) -> dict[str, object]:
    if status == "failed":
        return {"status": status, "error": "Fake MCP server failed to start"}
    return {"status": status}


def _invalid(message: str, *, field: str | None = None) -> _ErrorResponse:
    return _ErrorResponse(400, {"_tag": "InvalidRequestError", "message": message, "field": field})


def _json(payload: BaseModel | dict[str, Any]) -> httpx.Response:
    return httpx.Response(200, json=payload.to_dict() if isinstance(payload, BaseModel) else payload)


def _page(request: httpx.Request, items: list[dict[str, Any]], *, newest_first_default: bool) -> httpx.Response:
    """Cursor pagination over ``items`` (oldest first). Cursors encode the order and offset, like the server's."""
    params = request.url.params
    cursor = params.get("cursor")
    if cursor is not None:
        if "order" in params:
            return httpx.Response(
                400, json={"_tag": "InvalidRequestError", "message": "order cannot be combined with cursor"}
            )
        order, _, offset_text = cursor.partition(":")
        if order not in ("asc", "desc") or not offset_text.isdigit():
            return httpx.Response(400, json={"_tag": "InvalidCursorError", "message": f"Invalid cursor: {cursor}"})
        offset = int(offset_text)
    else:
        order = params.get("order") or ("desc" if newest_first_default else "asc")
        offset = 0
    limit = int(params.get("limit") or 50)
    ordered = list(reversed(items)) if order == "desc" else items
    data = ordered[offset : offset + limit]
    end = offset + len(data)
    return httpx.Response(
        200,
        json={
            "data": data,
            "cursor": {
                "previous": f"{order}:{max(offset - limit, 0)}" if offset > 0 else None,
                "next": f"{order}:{end}" if end < len(ordered) else None,
            },
        },
    )
