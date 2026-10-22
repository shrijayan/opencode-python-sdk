# Use the background service

OpenCode can run one shared background server per user, `opencode serve --service`. It registers itself in
`$XDG_STATE_HOME/opencode/service.json` (default `~/.local/state/opencode/service.json`) with its URL, PID, version
and password. `Opencode.from_service()` connects to it, starting it first if it is not running:

```python
from opencode import Opencode

with Opencode.from_service(version="2.1.2") as client:  # (1)!
    print(client.server.info().version)
```

1. Optional. A service running another version is stopped and replaced. `version` can also be a predicate,
   such as `lambda v: v.startswith("2.")`.

Pass `start=False` to only connect to a running service; it raises `ServiceError` when there is none.

## Without a client

```python
from opencode import service

endpoint = service.discover()  # an Endpoint, or None; never starts anything
endpoint = service.ensure()  # starts the service when needed
service.headers(endpoint)  # {"authorization": "Basic ..."} for other HTTP clients
service.stop(pty="handoff")  # hand persistent terminals to the next service
```

Several processes may call `ensure()` at once: each starts at most two attempts, the service's own lock picks a
winner, and every caller gets the same service. It gives up after 120 seconds with a `ServiceError` that includes
the end of the failed process's stderr.

## Async

`await AsyncOpencode.from_service()`, `service.async_discover()`, `service.async_ensure()` and
`service.async_stop()` take the same arguments.

These helpers follow the TypeScript client's `Service` from `@opencode-ai/client`.
