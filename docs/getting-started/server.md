# Run a server from Python

`OpencodeServer` runs `opencode serve` as a child process, on a free local port with a random password, for the
lifetime of a `with` block.

```python
from opencode import OpencodeServer

server = OpencodeServer(
    cwd="/path/to/repo",  # (1)!
    isolated=True,  # (2)!
    config={"model": "anthropic/claude-sonnet-5-5"},  # (3)!
)
with server:
    client = server.client()
    print(client.server.info().version)
```

1. The server's working directory, which becomes its default project.
2. Ignore project `opencode.json`, `AGENTS.md` and Claude Code files on disk, for reproducible runs.
3. Passed to the server as `OPENCODE_CONFIG_CONTENT`.

The server runs in `--stdio` mode, so it exits when the Python process dies, even if the `with` block never
finishes. Its password reaches the child through `OPENCODE_PASSWORD`, which the server strips from the environment
its tools inherit.

## Async

`AsyncOpencodeServer` takes the same arguments:

```python
from opencode import AsyncOpencodeServer

async with AsyncOpencodeServer(cwd="/path/to/repo") as server:
    async with server.client() as client:
        await client.session.create(title="Async")
```

## When it fails to start

If `opencode` is missing or the server exits early, `ServerStartError` is raised. Its `output` attribute holds the
last lines the server printed.

```python
from opencode import OpencodeServer, ServerStartError

try:
    with OpencodeServer() as server:
        ...
except ServerStartError as error:
    print(error.output)
```

See the [`OpencodeServer` reference](../reference/server.md) for every argument.
