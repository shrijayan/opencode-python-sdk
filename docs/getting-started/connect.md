# Connect to a server

Start a server with the CLI, then point a client at it:

```bash
OPENCODE_PASSWORD=secret opencode serve --port 4096
```

```python
from opencode import Opencode

client = Opencode("http://127.0.0.1:4096", password="secret")
print(client.server.info().version)
```

## Environment variables

`base_url` and `password` fall back to environment variables, so the shortest form is `Opencode()`.

| Argument | Variable |
| --- | --- |
| `base_url` | `OPENCODE_BASE_URL` |
| `password` | `OPENCODE_PASSWORD`, then `OPENCODE_SERVER_PASSWORD` |

`OPENCODE_PASSWORD` is the same variable the OpenCode CLI reads. Pass `password=""` to send no credentials.

## Closing the client

The client owns an `httpx.Client` connection pool. Use it as a context manager, or call `close()`:

```python
with Opencode() as client:
    client.agent.list()
```

## Calling the API

Methods mirror the official TypeScript client: `client.<group>.<operation>()`, in `snake_case`. Path parameters are
positional; everything else is keyword-only.

```python
client.session.get("ses_...")
client.session.prompt("ses_...", text="Fix the failing test", resume=True)
client.session.revert.stage("ses_...", message_id="msg_...")
client.mcp.list()
```

Every method is listed under [Resources](../reference/resources.md).

### Optional and null arguments

The server distinguishes a field that is absent from a field set to `null`. Optional arguments default to
`NOT_GIVEN` and are left out of the request; passing `None` sends `null`.

```python
client.session.update("ses_...", title="New title")  # (1)!
client.session.list(parent_id=None)  # (2)!
```

1. Sends `{"title": "New title"}`.
2. Sends `parentID=null`, which returns only root sessions.
