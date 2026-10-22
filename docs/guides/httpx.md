# Advanced httpx config

The client is built on [httpx](https://www.python-httpx.org). Pass your own `httpx.Client` (or `httpx.AsyncClient`)
for proxies, custom CA bundles, transports or event hooks. You keep ownership and must close it.

```python
import httpx
from opencode import Opencode

client = Opencode(
    "https://opencode.internal.example.com",
    http_client=httpx.Client(proxy="http://proxy:8080", verify="/etc/ssl/ca.pem"),
    default_headers={"X-Team": "platform"},
)
```

## Per-request extras

Every method takes `extra_headers`, `extra_query` and `extra_body`, merged into that request. Use them to reach
server features this client version does not model yet.

```python
client.session.create(
    title="t",
    extra_headers={"X-Trace": "1"},
    extra_body={"future": True},
)
```

## Derived clients

`with_options()` returns a client with changed settings that shares the same connection pool:

```python
fast = client.with_options(timeout=5.0, max_retries=0)
```
