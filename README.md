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
retry; credentials are never logged.

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
