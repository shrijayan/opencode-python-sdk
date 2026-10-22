# opencode-python-sdk

[![CI](https://github.com/shrijayan/opencode-python-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/shrijayan/opencode-python-sdk/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/opencode-python-sdk.svg)](https://pypi.org/project/opencode-python-sdk/)
[![Docs](https://img.shields.io/badge/docs-shrijayan.github.io-d9730d)](https://shrijayan.github.io/opencode-python-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/opencode-python-sdk.svg)](https://pypi.org/project/opencode-python-sdk/)

Typed Python client for the [OpenCode](https://github.com/anomalyco/opencode) 2.x server API.

**Documentation: <https://shrijayan.github.io/opencode-python-sdk/>**

> **Unofficial, community-maintained.** This package is not affiliated with or endorsed by the OpenCode team.
> If the OpenCode maintainers want to take it over, we are happy to transfer this repository and the `opencode-python-sdk`
> name on PyPI. Open an issue and we will hand it over.

- **Complete.** All 142 operations of the OpenCode 2.1 API, sync and async, with typed models for every request,
  response and event (96 event types).
- **Generated from the source of truth.** The contract is exported from the same Effect `HttpApi` the official
  TypeScript client is built from, so method names and request shapes match it exactly.
- **Safe to run in production.** Retries only when a request cannot have changed server state, bounded backoff that
  honors `Retry-After`, typed errors for every declared server error, and timeouts on everything.
- **Forward compatible.** New fields, enum values, union variants and event types from newer servers are kept, not
  rejected, so an older client keeps working after a server upgrade.
- **Batteries included.** Starts and stops `opencode serve` for you, auto-paginates lists, and streams events.

## Install

```bash
pip install opencode-python-sdk
```

The package imports as `opencode`. Requires Python 3.10 or newer. To start a server from Python, install the [OpenCode CLI](https://opencode.ai) too.

## Quick start

```python
from opencode import OpencodeServer

with OpencodeServer(cwd="/path/to/repo") as server, server.client() as client:
    session = client.session.create(title="Review")
    client.session.prompt(session.id, text="Summarize the open TODOs in this repository")
    client.session.wait(session.id)

    for message in client.message.list(session.id):
        print(message.type)
```

To connect to a server that is already running:

```python
from opencode import Opencode

client = Opencode("http://127.0.0.1:4096", password="...")
print(client.server.info().version)
```

`base_url` and `password` default to the `OPENCODE_BASE_URL` and `OPENCODE_PASSWORD` environment variables. The
password variable is the same one the OpenCode CLI reads.

## Async

`AsyncOpencode` has the same methods. It works with asyncio and trio.

```python
import asyncio

from opencode import AsyncOpencode


async def main() -> None:
    async with AsyncOpencode("http://127.0.0.1:4096", password="...") as client:
        session = await client.session.create(title="Async")
        await client.session.prompt(session.id, text="Hello")

        async for message in client.message.list(session.id):
            print(message.type)


asyncio.run(main())
```

## Calling the API

Methods mirror the official TypeScript client: `client.<group>.<operation>()`, with names in `snake_case`. Path
parameters are positional; everything else is keyword-only.

```python
client.session.get("ses_...")
client.session.prompt("ses_...", text="Fix the failing test", resume=True)
client.session.revert.stage("ses_...", message_id="msg_...")
client.mcp.list()
```

The full list is in [api.md](api.md).

### Optional and null arguments

The server distinguishes a field that is absent from a field set to `null`. Optional arguments default to
`NOT_GIVEN` and are left out of the request; passing `None` sends `null`:

```python
client.session.update("ses_...", title="New title")  # sends {"title": "New title"}
client.session.list(parent_id=None)  # only root sessions: parentID=null
```

### Models

Responses are [pydantic](https://docs.pydantic.dev) models. Attributes are `snake_case`; the wire names stay
available as aliases, so a model validates server JSON and serializes back to it unchanged.

```python
from opencode.types import ModelRef

session = client.session.create(model=ModelRef(id="claude-sonnet-5-5", provider_id="anthropic"))
session.project_id  # attribute access
session.to_dict()  # {"id": "...", "projectID": "...", ...}
```

Unions are discriminated, so `isinstance` and `match` narrow them:

```python
from opencode.types import SessionMessageAssistant, SessionMessageUser

for message in client.message.list(session.id):
    match message:
        case SessionMessageUser(text=text):
            print("user:", text)
        case SessionMessageAssistant():
            print("assistant replied")
        case _:
            pass  # includes variants added by newer servers
```

### Project directory

Most endpoints take a `location`. Set a default for the client once:

```python
client = Opencode("http://127.0.0.1:4096", directory="/path/to/repo")
client.agent.list()  # uses /path/to/repo
client.agent.list(location={"directory": "/other"})  # per call
```

## Pagination

List endpoints with cursors return a page. Iterating it fetches the following pages as needed.

```python
for session in client.session.list(limit=50):
    print(session.title)

page = client.session.list(limit=50)
page.data  # this page only
page.has_next_page()
next_page = page.next_page()
```

Async list methods return a paginator: `await` it for the first page, or `async for` over every item.

## Events

```python
with client.event.subscribe() as events:
    for event in events:
        print(event.type)
```

Events are typed (`SessionCreatedEvent`, `SessionTextDeltaEvent`, and so on). Event types this client version does
not know arrive as `UnknownEvent` with all their fields kept. Streams apply only the connect timeout by default, since
they stay open between events.

### Shared event stream

`client.events` shares one connection among every subscriber, like `client.event` in the TypeScript client. The
connection opens with the first subscriber and closes when the last one leaves. Each subscriber has its own queue of
up to 4096 events; one that falls further behind fails with `EventOverflowError` without affecting the others. The
latest `server.connected` event is replayed to subscribers that join later.

```python
from opencode.types import SessionIdleEvent

with client.events.of_type(SessionIdleEvent).for_session(session.id) as idle:
    client.session.prompt(session.id, text="Hello")
    event = idle.get(timeout=300)  # typed as SessionIdleEvent
```

- Filters chain: `of_type(*classes)` narrows the yielded type, `for_session(id)` keeps one session's events, and
  `where(predicate)` takes any test. Entering the `with` block joins the stream, so nothing published after that is
  missed.
- `subscribe(on_activity=callback)` calls `callback` for every chunk received, keepalive comments included, as a
  liveness signal.
- `close()` (or leaving the `with` block) ends the subscription, also from another thread. In async code, cancel a wait
  with `anyio.fail_after`, `asyncio.timeout` or a trio cancel scope; the subscription stays usable.
- Reconnection is opt-in: `EventHub(client, reconnect=True)` (or `AsyncEventHub`, or a `Reconnect(...)` policy) reopens
  the connection with exponential backoff after connection errors, 5xx and 429. Subscribers see `server.connected`
  once. **The stream is volatile**: events published while disconnected are lost, so re-read state through the API
  after a reconnect when it matters.

The async hub works the same way under asyncio and trio:

```python
async with client.events.for_session(session.id) as events:
    async for event in events:
        print(event.type)
```

`client.event.subscribe()` still opens a dedicated connection.

### Plugin RPC

Declare a plugin RPC once as a class, then call it with typed inputs and outputs:

```python
from pydantic import BaseModel
from opencode import RpcCallError, RpcDefinition, rpc_event, rpc_method


class AddInput(BaseModel):
    amount: int


class Total(BaseModel):
    total: int


class Counter(RpcDefinition, id="counter"):
    add = rpc_method(AddInput, Total)
    reset = rpc_method(None, Total)
    changed = rpc_event(Total)


counter = client.rpc(Counter)
try:
    print(counter.call(Counter.add, AddInput(amount=2)).total)
except RpcCallError as error:
    print(error.type, error.message, error.data)

with counter.subscribe(Counter.changed) as changes:  # only rpc.counter.changed, with validated data
    for change in changes:
        print(change.data.total)
```

Any type pydantic validates works for inputs, outputs and event data. `rpc_method(..., errors={"not_found": Model})`
validates the `data` of declared errors. Failures raise `RpcCallError`; crashes and outputs that do not match the
declared type raise `RpcCallInternalError`. `counter.events()` yields every raw event of the RPC. The untyped
`client.rpc.call(rpc_id, method, input=...)` is still available.

## Terminals

`client.pty.attach()` opens an interactive connection to a PTY over a WebSocket. It needs the `pty` extra:
`pip install "opencode-python-sdk[pty]"`.

```python
pty = client.pty.create(command="/bin/sh").data
with client.pty.attach(pty.id) as term:
    term.resize(120, 40)
    term.send("echo hi\n")
    for chunk in term:  # output bytes, until the shell exits
        print(chunk.decode(errors="replace"), end="")
```

`recv(timeout=...)` reads one chunk and returns `None` once the terminal has ended. `term.cursor` holds the output
position to pass as `cursor=` when reattaching; `cursor=-1` skips the replay of earlier output. Persistent terminals
work the same way through `client.experimental.persistent_pty.attach(pty_id, role=..., takeover=...)`. The async
client returns `AsyncPtyConnection` (asyncio only): `async with await client.pty.attach(...) as term`. A connection
the server refuses or closes abnormally raises `PtyConnectionError`. See
[`examples/terminal.py`](examples/terminal.py) for a full TTY bridge.

## Errors

Every error derives from `opencode.OpencodeError`. Errors the server declares are raised as their own class, with a
typed body:

```python
import opencode

try:
    client.session.get("ses_missing")
except opencode.SessionNotFoundError as error:
    print(error.error.session_id, error.status_code)
except opencode.NotFoundError:
    ...  # any other 404
except opencode.APIConnectionError:
    ...  # server unreachable
```

| Status | Class |
| --- | --- |
| 400 | `BadRequestError` |
| 401 | `AuthenticationError` |
| 403 | `PermissionDeniedError` |
| 404 | `NotFoundError` |
| 409 | `ConflictError` |
| 413 | `ContentTooLargeError` |
| 429 | `RateLimitError` |
| 5xx | `InternalServerError` |
| No response | `APIConnectionError`, `APITimeoutError` |
| Unexpected body | `APIResponseValidationError` |

## Retries and timeouts

The client retries twice by default, with exponential backoff and jitter, and honors `Retry-After` up to 60 seconds.

- `GET`, `PUT` and `DELETE` are retried on connection errors and on 408, 429, 500, 502, 503 and 504.
- `POST` and `PATCH` are retried only when the request cannot have run: when the connection could not be opened, or
  on 429 and 503. A prompt is never sent twice because a response was slow.

```python
client = Opencode(max_retries=5, timeout=30.0)
client.with_options(timeout=None).session.wait(session.id)  # wait as long as it takes
client.session.get("ses_...", timeout=5.0)  # per call
```

The default timeout is 10 minutes with a 10 second connect timeout.

`with_options` (alias `copy`) returns a client with some options changed: `timeout`, `max_retries`, `base_url`,
`password`, `directory`, `default_headers` and `default_query` (headers and query are merged over the current
ones). The copy shares the original's connection pool, and closing it leaves the pool open.

```python
client.with_options(max_retries=0).session.create()  # no retries for this call
scoped = client.with_options(directory="/other/repo", default_headers={"X-Trace": "1"})
```

## Running an agent headless

`client.session.run` does the usual "prompt an agent and wait" round trip in one call: it creates a session (or
reuses `session_id`), sends the prompt, blocks until the session is idle, and returns the new messages with the
final text and usage. `client.wait_until_ready` waits until agents and MCP servers have loaded, which happens
asynchronously after the server boots. Both have async versions on `AsyncOpencode`.

```python
from opencode import Opencode
from opencode.types import ModelRef, PromptInputFileAttachment

with Opencode("http://127.0.0.1:4096", password="...") as client:
    client.wait_until_ready(agents=["reviewer"], mcp_servers=["github"], timeout=60)
    result = client.session.run(
        "Review the attached diff",
        agent="reviewer",
        model=ModelRef(provider_id="anthropic", id="claude-sonnet-5-5"),  # set it with the agent
        files=[PromptInputFileAttachment(uri="data:text/plain;base64,...", name="diff.patch")],
        timeout=600,
    )
    print(result.outcome, result.text)
    print(result.cost, result.tokens.input, result.tokens.output)  # this run; result.session has the totals
```

If the wait ends early (Ctrl-C, task cancellation, `timeout`, a connection error), `run` interrupts the session
on the server before re-raising, so the agent does not keep running unattended.

## Testing your code

`opencode.testing.FakeServer` is an in-process fake of the server: an `httpx` transport that keeps sessions,
messages and events in memory and answers with the same payloads as the real server. No process, no model.

```python
from opencode import Opencode
from opencode.testing import FakeServer


def test_summarize() -> None:
    fake = FakeServer(reply=lambda prompt: f"summary of {prompt!r}")
    client = Opencode.fake(fake)  # same as Opencode(transport=fake)

    assert client.session.run("README").text == "summary of 'README'"
    assert fake.prompts == ["README"]
```

`fake.fail(method, path_regex, status=..., exception=...)` injects errors, `fake.add_agent(..., after_polls=n)`
and `fake.set_mcp_status(...)` simulate slow boots, and `fake.requests` records every request. Routes the fake
does not implement answer `404`.

## Running a server

`OpencodeServer` runs `opencode serve` as a child process on a free local port with a random password:

```python
from opencode import OpencodeServer

server = OpencodeServer(
    cwd="/path/to/repo",
    isolated=True,  # ignore project opencode.json, AGENTS.md and Claude Code files
    config={"model": "anthropic/claude-sonnet-5-5"},  # passed as OPENCODE_CONFIG_CONTENT
)
with server:
    client = server.client()
    ...
```

The server runs in `--stdio` mode, so it also exits when the Python process dies. `AsyncOpencodeServer` is the
async equivalent.

### The background service

OpenCode can also run one shared background server per user (`opencode serve --service`), which registers itself in
`$XDG_STATE_HOME/opencode/service.json`. `Opencode.from_service()` connects to it, starting it first if it is not
running:

```python
from opencode import Opencode, service

with Opencode.from_service(version="2.1.2") as client:  # replaces a service running another version
    print(client.server.info().version)

endpoint = service.discover()  # an Endpoint, or None; never starts anything
service.stop(pty="handoff")  # hand persistent terminals to the next service instead of closing them
```

`service.ensure()` returns the `Endpoint` (URL and credentials) without creating a client, and `service.headers()`
gives its `Authorization` header for other HTTP clients. Concurrent callers are safe: they race to start the service
and all get the one that won. `await AsyncOpencode.from_service()`, `service.async_discover()`,
`service.async_ensure()` and `service.async_stop()` are the async equivalents.

## Advanced

```python
import httpx

from opencode import Opencode

client = Opencode(
    "https://opencode.internal.example.com",
    http_client=httpx.Client(proxy="http://proxy:8080", verify="/etc/ssl/ca.pem"),
    default_headers={"X-Team": "platform"},
)

client.session.create(title="t", extra_headers={"X-Trace": "1"}, extra_body={"future": True})
```

Logs go to the `opencode` logger. `logging.getLogger("opencode").setLevel(logging.DEBUG)` shows every request and
retry; credentials are never logged. Set `OPENCODE_LOG=debug` (or `info`) to have the SDK attach a stderr handler at
that level on import, without touching your own logging config.

## Versioning

| `opencode-python-sdk` (this package) | OpenCode server |
| --- | --- |
| 0.1.x | 2.1.x |

`opencode.API_VERSION` is the server version the client was generated from. The package follows semantic
versioning and releases automatically on every merge to `main`; until 1.0, minor versions may contain breaking
changes. See the [releases page](https://github.com/shrijayan/opencode-python-sdk/releases).

## How it is built

```
@opencode/protocol (npm)  ──bun codegen/extract──▶  spec/contract.json  ──python -m codegen──▶  src/opencode
```

1. `codegen/extract/extract.ts` loads `ClientApi` from the published `@opencode/protocol` package and exports
   every endpoint, its inputs, outputs and declared errors, and every schema as JSON Schema.
2. `python -m codegen` turns the contract into pydantic models (`opencode/types`), resources
   (`opencode/resources`), error classes (`opencode/_errors.py`) and [api.md](api.md).
3. The transport, retries, streaming, pagination and server launcher are written by hand.

Generated code is committed. CI regenerates it and fails if anything changed. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
