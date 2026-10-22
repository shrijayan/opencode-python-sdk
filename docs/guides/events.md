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
