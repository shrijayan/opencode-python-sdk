# Events and streaming

`client.event.subscribe()` opens a server-sent event stream of everything happening on the server.

```python
with client.event.subscribe() as events:  # (1)!
    for event in events:
        print(event.type)
```

1. The context manager closes the HTTP connection when you stop reading.

Events are typed (`SessionCreatedEvent`, `SessionTextDeltaEvent` and so on; see [Events](../reference/types/events.md)).
Narrow them with `match`:

```python
from opencode.types import SessionTextDeltaEvent, SessionIdleEvent

with client.event.subscribe() as events:
    for event in events:
        match event:
            case SessionTextDeltaEvent():
                print(event.to_dict())
            case SessionIdleEvent():
                break
            case _:
                pass
```

Event types this client version does not know arrive as `UnknownEvent`, with all their fields kept.

## Timeouts

Streams only apply the connect timeout by default, because they stay open between events. Pass `timeout=` to bound
a stream.

## Delivery

The event stream is volatile by contract. A slow consumer overflows and fails the stream, and events sent while you
are disconnected are lost. Keep the loop body fast, and after reconnecting, read current state (for example with
`client.message.list`) rather than assuming you saw every event.

## Async

```python
async with await client.event.subscribe() as events:
    async for event in events:
        print(event.type)
```

## Shared event stream

`client.events` shares one connection among every subscriber, like `client.event` in the TypeScript client. The
connection opens with the first subscriber and closes when the last one leaves. Each subscriber has its own queue of
up to 4096 events; one that falls further behind fails with `EventOverflowError` without affecting the others. The
latest `server.connected` event is replayed to subscribers that join later.

```python
from opencode.types import SessionIdleEvent

with client.events.of_type(SessionIdleEvent).for_session(session.id) as idle:
    client.session.prompt(session.id, text="Hello")
    event = idle.get(timeout=300)  # typed as SessionIdleEvent
```

- Filters chain: `of_type(*classes)` narrows the yielded type, `for_session(id)` keeps one session's events, and
  `where(predicate)` takes any test. Entering the `with` block joins the stream, so nothing published after that is
  missed.
- `subscribe(on_activity=callback)` calls `callback` for every chunk received, keepalive comments included, as a
  liveness signal.
- `close()` (or leaving the `with` block) ends the subscription, also from another thread. In async code, cancel a wait
  with `anyio.fail_after`, `asyncio.timeout` or a trio cancel scope; the subscription stays usable.
- Reconnection is opt-in: `EventHub(client, reconnect=True)` (or `AsyncEventHub`, or a `Reconnect(...)` policy) reopens
  the connection with exponential backoff after connection errors, 5xx and 429. Subscribers see `server.connected`
  once. **The stream is volatile** (see [Delivery](#delivery)): events published while disconnected are lost, so re-read state through the API
  after a reconnect when it matters.

The async hub works the same way under asyncio and trio:

```python
async with client.events.for_session(session.id) as events:
    async for event in events:
        print(event.type)
```

`client.event.subscribe()` still opens a dedicated connection.

Typed plugin RPC events are covered in the [plugin RPC guide](plugin-rpc.md).
