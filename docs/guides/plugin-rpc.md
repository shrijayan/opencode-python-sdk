# Plugin RPC

Declare a plugin RPC once as a class, then call it with typed inputs and outputs:

```python
from pydantic import BaseModel
from opencode import RpcCallError, RpcDefinition, rpc_event, rpc_method


class AddInput(BaseModel):
    amount: int


class Total(BaseModel):
    total: int


class Counter(RpcDefinition, id="counter"):
    add = rpc_method(AddInput, Total)
    reset = rpc_method(None, Total)
    changed = rpc_event(Total)


counter = client.rpc(Counter)
try:
    print(counter.call(Counter.add, AddInput(amount=2)).total)
except RpcCallError as error:
    print(error.type, error.message, error.data)

with counter.subscribe(Counter.changed) as changes:  # only rpc.counter.changed, with validated data
    for change in changes:
        print(change.data.total)
```

Any type pydantic validates works for inputs, outputs and event data. `rpc_method(..., errors={"not_found": Model})`
validates the `data` of declared errors. Failures raise `RpcCallError`; crashes and outputs that do not match the
declared type raise `RpcCallInternalError`. `counter.events()` yields every raw event of the RPC. The untyped
`client.rpc.call(rpc_id, method, input=...)` is still available.


## Async

The async client returns `AsyncRpcClient`, with the same methods:

```python
counter = client.rpc(Counter)
total = await counter.call(Counter.add, AddInput(amount=2))
async with counter.subscribe(Counter.changed) as changes:
    async for change in changes:
        print(change.data.total)
```

RPC events travel on the [shared event stream](events.md#shared-event-stream), so they share its delivery rules.
