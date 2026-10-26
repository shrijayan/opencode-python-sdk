---
name: opencode
description: Use the opencode Python SDK (version 0.0.1) to call the Opencode API: client setup, authentication, one example per resource, errors and retries.
---

# opencode 0.0.1

This skill ships inside the `opencode` package, so it matches the installed version. The full method and type reference is `api.md` in the repository (https://github.com/).

## Install

```sh
pip install opencode==0.0.1
```

## Authenticate and create a client

Set `OPENCODE_PASSWORD`; the client reads it when `password` is not passed. Never hard-code the key.

```python
import os

from opencode import Opencode

client = Opencode(
    password=os.environ.get("OPENCODE_PASSWORD"),  # the default
    max_retries=2,  # the default; connection errors, 408, 409, 429 and 5xx are retried
)
```

Use `AsyncOpencode` the same way, with `await` on every call. `OPENCODE_BASE_URL` overrides the base URL.

## Examples

One call per resource; the arguments are placeholders.

### `client.agent.list` (GET /api/agent)

```python
from opencode import Opencode

client = Opencode()

agent = client.agent.list()
print(agent)
```

### `client.command.list` (GET /api/command)

```python
from opencode import Opencode

client = Opencode()

command = client.command.list()
print(command)
```

### `client.config.get` (GET /api/config)

```python
from opencode import Opencode

client = Opencode()

config = client.config.get()
print(config)
```

### `client.credential.list` (GET /api/credential)

```python
from opencode import Opencode

client = Opencode()

credential = client.credential.list()
print(credential)
```

### `client.debug.location.list` (GET /api/debug/location)

```python
from opencode import Opencode

client = Opencode()

location = client.debug.location.list()
print(location)
```

### `client.event.subscribe` (GET /api/event)

```python
from opencode import Opencode

client = Opencode()

event = client.event.subscribe()
print(event)
```

### `client.experimental.persistent_pty.handoff` (POST /api/experimental/persistent-pty/handoff)

```python
from opencode import Opencode

client = Opencode()

persistent_pty = client.experimental.persistent_pty.handoff()
print(persistent_pty)
```

### `client.file.list` (GET /api/fs/list)

```python
from opencode import Opencode

client = Opencode()

file = client.file.list()
print(file)
```

### `client.form.list` (GET /api/form)

```python
from opencode import Opencode

client = Opencode()

form = client.form.list()
print(form)
```

### `client.generate.text` (POST /api/experimental/generate)

```python
from opencode import Opencode

client = Opencode()

generate = client.generate.text(prompt="prompt")
print(generate)
```

### `client.integration.list` (GET /api/integration)

```python
from opencode import Opencode

client = Opencode()

integration = client.integration.list()
print(integration)
```

### `client.integration.wellknown.add` (POST /api/experimental/integration/wellknown)

```python
from opencode import Opencode

client = Opencode()

wellknown = client.integration.wellknown.add(url="url")
print(wellknown)
```

### `client.integration.connect.external` (POST /api/integration/{integrationID}/connect/external)

```python
from opencode import Opencode

client = Opencode()

connect = client.integration.connect.external(integration_id={}, method_id={})
print(connect)
```

### `client.integration.oauth.cancel` (DELETE /api/integration/{integrationID}/connect/oauth/{attemptID})

```python
from opencode import Opencode

client = Opencode()

oauth = client.integration.oauth.cancel(integration_id={}, attempt_id={})
print(oauth)
```

### `client.integration.command.cancel` (DELETE /api/integration/{integrationID}/connect/command/{attemptID})

```python
from opencode import Opencode

client = Opencode()

command = client.integration.command.cancel(integration_id={}, attempt_id={})
print(command)
```

### `client.location.get` (GET /api/location)

```python
from opencode import Opencode

client = Opencode()

location = client.location.get()
print(location)
```

### `client.mcp.list` (GET /api/mcp)

```python
from opencode import Opencode

client = Opencode()

mcp = client.mcp.list()
print(mcp)
```

### `client.mcp.resource.catalog` (GET /api/mcp/resource)

```python
from opencode import Opencode

client = Opencode()

resource = client.mcp.resource.catalog()
print(resource)
```

### `client.message.list` (GET /api/session/{sessionID}/message)

```python
from opencode import Opencode

client = Opencode()

message = client.message.list(session_id={})
print(message)
```

### `client.migration.v1.status` (GET /api/experimental/migration/v1)

```python
from opencode import Opencode

client = Opencode()

v1 = client.migration.v1.status()
print(v1)
```

### `client.model.list` (GET /api/model)

```python
from opencode import Opencode

client = Opencode()

model = client.model.list()
print(model)
```

### `client.permission.create` (POST /api/session/{sessionID}/permission)

```python
from opencode import Opencode

client = Opencode()

permission = client.permission.create(session_id={}, action="action", resources=["string"])
print(permission)
```

### `client.permission.request.list` (GET /api/permission/request)

```python
from opencode import Opencode

client = Opencode()

request = client.permission.request.list()
print(request)
```

### `client.permission.saved.list` (GET /api/permission/saved)

```python
from opencode import Opencode

client = Opencode()

saved = client.permission.saved.list()
print(saved)
```

### `client.plugin.list` (GET /api/plugin)

```python
from opencode import Opencode

client = Opencode()

plugin = client.plugin.list()
print(plugin)
```

### `client.project.list` (GET /api/project)

```python
from opencode import Opencode

client = Opencode()

project = client.project.list()
print(project)
```

### `client.provider.list` (GET /api/provider)

```python
from opencode import Opencode

client = Opencode()

provider = client.provider.list()
print(provider)
```

### `client.pty.create` (POST /api/pty)

```python
from opencode import Opencode

client = Opencode()

pty = client.pty.create()
print(pty)
```

### `client.pty.connect.token` (POST /api/pty/{ptyID}/connect-token)

```python
from opencode import Opencode

client = Opencode()

connect = client.pty.connect.token(pty_id={})
print(connect)
```

### `client.reference.list` (GET /api/reference)

```python
from opencode import Opencode

client = Opencode()

reference = client.reference.list()
print(reference)
```

### `client.rpc.call` (POST /api/rpc/{rpcID}/{method})

```python
from opencode import Opencode

client = Opencode()

rpc = client.rpc.call(rpc_id="rpcID", method="method")
print(rpc)
```

### `client.server.info` (GET /api/info)

```python
from opencode import Opencode

client = Opencode()

server = client.server.info()
print(server)
```

### `client.session.create` (POST /api/session)

```python
from opencode import Opencode

client = Opencode()

session = client.session.create()
print(session)
```

### `client.session.revert.clear` (DELETE /api/session/{sessionID}/revert)

```python
from opencode import Opencode

client = Opencode()

revert = client.session.revert.clear(session_id={})
print(revert)
```

### `client.session.inbox.update` (PATCH /api/session/{sessionID}/inbox/{inboxID})

```python
from opencode import Opencode

client = Opencode()

inbox = client.session.inbox.update(session_id={}, inbox_id={}, delivery={})
print(inbox)
```

### `client.session.instructions.entry.list` (GET /api/experimental/session/{sessionID}/instructions/entries)

```python
from opencode import Opencode

client = Opencode()

entry = client.session.instructions.entry.list(session_id={})
print(entry)
```

### `client.session.message.get` (GET /api/session/{sessionID}/message/{messageID})

```python
from opencode import Opencode

client = Opencode()

message = client.session.message.get(session_id={}, message_id={})
print(message)
```

### `client.session.form.create` (POST /api/session/{sessionID}/form)

```python
from opencode import Opencode

client = Opencode()

form = client.session.form.create(session_id="sessionID", fields={}, title="title")
print(form)
```

### `client.shell.list` (GET /api/shell)

```python
from opencode import Opencode

client = Opencode()

shell = client.shell.list()
print(shell)
```

### `client.skill.list` (GET /api/skill)

```python
from opencode import Opencode

client = Opencode()

skill = client.skill.list()
print(skill)
```

### `client.vcs.base` (GET /api/vcs/base)

```python
from opencode import Opencode

client = Opencode()

vcs = client.vcs.base()
print(vcs)
```

### `client.vcs.branch.list` (GET /api/vcs/branch)

```python
from opencode import Opencode

client = Opencode()

branch = client.vcs.branch.list()
print(branch)
```

### `client.voice.session` (POST /api/experimental/voice/session)

```python
from opencode import Opencode

client = Opencode()

voice = client.voice.session(model="model", transport={})
print(voice)
```

### `client.websearch.providers` (GET /api/websearch/provider)

```python
from opencode import Opencode

client = Opencode()

websearch = client.websearch.providers()
print(websearch)
```

### `client.worktree.create` (POST /api/worktree)

```python
from opencode import Opencode

client = Opencode()

worktree = client.worktree.create(project_id={})
print(worktree)
```

## Pagination

```python
from opencode import Opencode

client = Opencode()

# Iterating the page fetches the next pages as needed.
for item in client.message.list(session_id={}):
    print(item)
```

## Streaming

```python
from opencode import Opencode

client = Opencode()

stream = client.event.subscribe()
for event in stream:
    print(event)
```

## Errors

```python
import opencode
from opencode import Opencode

client = Opencode()

try:
    agent = client.agent.list()
    print(agent)
except opencode.APIConnectionError as e:
    print("The server could not be reached:", e.__cause__)
except opencode.RateLimitError:
    print("Rate limited (429); back off and retry.")
except opencode.APIStatusError as e:
    print("Non-2xx response:", e.status_code, e.response)
```

Every method also has `.with_raw_response` (headers and the raw response) and `.with_streaming_response`.
