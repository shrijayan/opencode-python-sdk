# Testing with the fake server

`opencode.testing.FakeServer` lets you test code that uses the SDK without starting `opencode serve` or calling
a model. It is an `httpx` transport (an `httpx.MockTransport`) that keeps sessions, messages and events in
memory and answers with payloads built from the generated models.

```python
from opencode import Opencode
from opencode.testing import FakeServer


def test_review() -> None:
    fake = FakeServer(reply=lambda prompt: "LGTM" if "diff" in prompt else "?")
    client = Opencode.fake(fake)  # same as Opencode(transport=fake)

    result = client.session.run("Review this diff", agent="build")

    assert result.text == "LGTM"
    assert fake.prompts == ["Review this diff"]
```

`AsyncOpencode.fake(fake)` works the same way.

## What it implements

Server info, agents, MCP servers, the event stream, and sessions: create, get, list, remove, switch agent or
model, prompt (with `resume=False` queueing the prompt without running it), wait, interrupt and messages, with
cursor pagination. Each prompt gets an assistant reply, an idle marker, cost and token usage. Other routes
answer `404` with a message naming the route.

## Simulating a slow boot

```python
fake = FakeServer(agents=["build"])
fake.add_agent("reviewer", after_polls=3)  # listed from the 4th GET /api/agent
fake.set_mcp_status("github", "connected", after_polls=2)
Opencode.fake(fake).wait_until_ready(agents=["reviewer"], mcp_servers=["github"])
```

## Injecting failures

```python
fake.fail(
    "POST",
    r"/api/session/.+/prompt",
    status=409,
    body={"_tag": "SessionBusyError", "sessionID": "ses_1", "message": "busy"},
)
fake.fail("GET", "/api/info", exception=httpx.ConnectError("refused"), times=2)
```

`path` is a regular expression matched against the whole path. `times=None` fails every matching request.

## Inspecting state

`fake.requests` records every `httpx.Request`; `fake.sessions`, `fake.messages`, `fake.inbox` and `fake.events`
hold the server state and can be changed directly.
