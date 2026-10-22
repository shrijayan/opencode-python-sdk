# Sessions and prompts

A session is one conversation with an agent. The usual loop is: create a session, send a prompt, wait for the agent
to go idle, then read the messages.

```python
from opencode import Opencode

with Opencode() as client:
    session = client.session.create(title="Fix tests", agent="build")  # (1)!
    client.session.prompt(session.id, text="Fix the failing test in tests/test_api.py")
    client.session.wait(session.id)  # (2)!

    for message in client.message.list(session.id):
        print(message.type)
```

1. `agent` picks one of the server's agents; `client.agent.list()` shows them.
2. Blocks until the agent loop is idle. Long runs may exceed the default timeout; see below.

## Waiting for long runs

`wait()` uses the client's timeout (10 minutes by default). To wait as long as it takes:

```python
client.with_options(timeout=None).session.wait(session.id)
```

To react to progress instead of blocking, subscribe to [events](events.md).

## Prompt options

```python
from opencode.types import PromptInputFileAttachment

client.session.prompt(
    session.id,
    text="Review this file",
    files=[PromptInputFileAttachment(...)],  # (1)!
    resume=True,  # (2)!
)
```

1. Files, agents and skills can be attached to a prompt.
2. Resume the agent loop if it was interrupted.

## Managing sessions

| Task | Call |
| --- | --- |
| List sessions | `client.session.list()` |
| Rename | `client.session.update(session_id, title=...)` |
| Fork at a message | `client.session.fork(session_id, ...)` |
| Switch model | `client.session.switch_model(session_id, ...)` |
| Stop the agent | `client.session.interrupt(session_id)` |
| Compact history | `client.session.compact(session_id)` |
| Diff of changes | `client.session.diff(session_id)` |
| Delete | `client.session.remove(session_id)` |
| Revert changes | `client.session.revert.stage(session_id, message_id=...)` |

The full list, with arguments, is in the [`SessionResource` reference](../reference/resources.md#opencode.resources.session.SessionResource).
