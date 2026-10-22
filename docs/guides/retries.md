# Retries and timeouts

## Retries

The client retries twice by default, with exponential backoff and jitter, and honors `Retry-After` up to 60 seconds.
Which requests are retried depends on whether they may already have run:

| Method | Retried on |
| --- | --- |
| `GET`, `PUT`, `DELETE` | Connection errors, 408, 429, 500, 502, 503, 504 |
| `POST`, `PATCH` | Only when the request cannot have run: connection could not be opened, 429, 503 |

So a prompt is never sent twice because a response was slow.

```python
client = Opencode(max_retries=5)
client.with_options(max_retries=0).session.prompt(session_id, text="...")
```

## Timeouts

The default is 10 minutes overall with a 10 second connect timeout. Set it per client, per derived client, or per
call. A float is seconds; an `httpx.Timeout` gives full control.

```python
import httpx

client = Opencode(timeout=30.0)
client.with_options(timeout=None).session.wait(session_id)  # (1)!
client.session.get("ses_...", timeout=5.0)  # (2)!
client = Opencode(timeout=httpx.Timeout(60.0, connect=2.0))
```

1. `with_options` returns a client that shares the connection pool. `None` waits forever.
2. Per call.

Event streams apply only the connect timeout unless you pass one, because they stay open between events. A timed-out
request raises `APITimeoutError`.
