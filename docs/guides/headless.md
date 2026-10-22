# Running agents headless

The common embedded use of OpenCode is: start the server, wait until the agents you configured have loaded, run
one prompt per unit of work, and read the result. Two helpers cover that on both clients.

## Wait until the server is ready

Agents load and MCP servers connect in the background after `opencode serve` starts listening, so the first
requests can arrive before your agent exists. `wait_until_ready` polls until everything you name is there:

```python
client.wait_until_ready(agents=["reviewer"], mcp_servers=["github"], timeout=60)
```

It treats connection errors and `503` answers as "still booting". After `timeout` seconds it raises
`TimeoutError` naming what is still missing.

## Run a prompt to completion

```python
from opencode.types import ModelRef

result = client.session.run(
    "Review the staged changes",
    agent="reviewer",
    model=ModelRef(provider_id="anthropic", id="claude-sonnet-5-5"),
    timeout=600,
)
print(result.outcome)  # "succeeded", "failed" or "interrupted"
print(result.text)  # text of the last assistant message
print(result.cost, result.tokens.input, result.tokens.output)
```

`run` creates a session with the agent and model, sends the prompt, blocks on `session.wait` until the session is
idle, then returns a [`opencode.lib.RunResult`](../reference/testing.md#opencode.lib.RunResult):

- `messages`: the messages this run added, oldest first, starting with the prompt
- `text`, `outcome`, `error`: the final answer and how the run ended
- `cost`, `tokens`: usage of this run; `session.cost` and `session.tokens` are the session totals

Set `model` together with `agent` when creating a session: otherwise the session can run on a different model
than the agent's.

Pass `session_id=` to continue a session. `agent` and `model` then switch the session before the prompt, and
`messages` holds only the new messages.

### Interrupts

If waiting ends early, through `KeyboardInterrupt`, cancelling the task (async), the `timeout`, or a connection
error, `run` calls `session.interrupt` before re-raising, so the agent does not keep running on the server.

### Files

`files` takes `PromptInputFileAttachment`s. Images and other inline content can be `data:` URLs:

```python
import base64
from opencode.types import PromptInputFileAttachment

png = base64.b64encode(open("screenshot.png", "rb").read()).decode()
client.session.run(
    "What is wrong in this screenshot?",
    files=[PromptInputFileAttachment(uri=f"data:image/png;base64,{png}", name="screenshot.png")],
)
```

## Async

The same helpers exist on `AsyncOpencode`:

```python
async with AsyncOpencode(url, password=password) as client:
    await client.wait_until_ready(agents=["build"])
    result = await client.session.run("Summarize README.md", agent="build")
```
