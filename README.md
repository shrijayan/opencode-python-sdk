# opencode

Typed Python client for the [OpenCode](https://github.com/anomalyco/opencode) 2.x server API.

> **Unofficial, community-maintained.** This package is not affiliated with or endorsed by the OpenCode team.
> If the OpenCode maintainers would like to take it over, we are happy to transfer ownership of this
> repository and the `opencode` name on PyPI. Open an issue or reach out and we will hand it over.

## Status

Early development. See the [design doc](docs/design.html) for the plan.

Tracks the OpenCode 2.x API, generated from the upstream spec at
[`packages/protocol/openapi.json`](https://github.com/anomalyco/opencode/blob/dev/packages/protocol/openapi.json).
Related upstream discussion: [anomalyco/opencode#54300](https://github.com/anomalyco/opencode/issues/54300).

## Install

```bash
pip install opencode
```

## Usage

```python
from opencode import Opencode

client = Opencode(base_url="http://127.0.0.1:4096", password="...")

session = client.session.create(agent="build", model="anthropic/claude-sonnet-5-5")
client.session.prompt(session.id, text="Summarise this repository")
client.experimental.session.wait(session.id)

for message in client.session.message.list(session.id):
    print(message.role, message.text)
```

An async client with the same method names is available as `AsyncOpencode`.

## License

MIT
