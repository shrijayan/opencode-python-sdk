"""Typed plugin RPC calls and events."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator

import respx
import pytest
from pydantic import BaseModel

from opencode import (
    Opencode,
    RpcError,
    RpcCallError,
    AsyncOpencode,
    RpcDefinition,
    RpcCallInternalError,
    rpc_event,
    rpc_method,
)
from opencode.lib import Location

from .conftest import BASE_URL, PASSWORD

SSE = {"content-type": "text/event-stream"}


class AddInput(BaseModel):
    amount: int


class Total(BaseModel):
    total: int


class Missing(BaseModel):
    key: str


class Counter(RpcDefinition, id="counter"):
    add = rpc_method(AddInput, Total, errors={"not_found": Missing})
    reset = rpc_method(None, Total, name="reset-all")
    changed = rpc_event(Total)
    cleared = rpc_event(dict[str, object])


def rpc_frame(event_type: str, data: object, n: int) -> bytes:
    payload = {"type": event_type, "id": f"evt_{n}", "created": 1, "location": {"directory": "/p"}, "data": data}
    return f"data: {json.dumps(payload)}\n\n".encode()


def test_definition_collects_methods_and_events() -> None:
    assert Counter.id == "counter"
    assert set(Counter.methods) == {"add", "reset-all"}
    assert set(Counter.events) == {"changed", "cleared"}
    assert Counter.event_type(Counter.changed) == "rpc.counter.changed"
    with pytest.raises(TypeError, match="needs an RPC id"):
        type("Nameless", (RpcDefinition,), {})


def test_call_validates_input_and_output(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/rpc/counter/add").respond(json={"output": {"total": 5}})
    result = client.rpc(Counter).call(Counter.add, AddInput(amount=2), location=Location(directory="/p"))
    assert result == Total(total=5)
    request = route.calls.last.request
    assert json.loads(request.content) == {"input": {"amount": 2}}
    assert "location" in str(request.url)


def test_call_without_input_uses_declared_name(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/rpc/counter/reset-all").respond(json={"output": {"total": 0}})
    assert client.rpc(Counter).call(Counter.reset).total == 0
    assert json.loads(route.calls.last.request.content) == {}


def test_generated_call_still_available(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/rpc/counter/add").respond(json={"output": 1})
    assert client.rpc.call("add", rpc_id="counter", input={"amount": 1}).output == 1


def test_rpc_error_maps_to_rpc_call_error_with_typed_data(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/rpc/counter/add").respond(
        400, json={"_tag": "RpcError", "type": "not_found", "message": "no counter", "data": {"key": "k"}}
    )
    with pytest.raises(RpcCallError) as caught:
        client.rpc(Counter).call(Counter.add, AddInput(amount=1))
    error = caught.value
    assert (error.rpc_id, error.method, error.type, error.message) == ("counter", "add", "not_found", "no counter")
    assert error.data == Missing(key="k")
    assert isinstance(error.__cause__, RpcError)
    assert not isinstance(error, RpcCallInternalError)


def test_internal_error_and_invalid_output(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/rpc/counter/add")
    route.respond(500, json={"_tag": "RpcInternalError", "type": "rpc.internal", "message": "boom"})
    with pytest.raises(RpcCallInternalError, match=r"rpc\.internal: boom"):
        client.with_options(max_retries=0).rpc(Counter).call(Counter.add, AddInput(amount=1))
    route.respond(json={"output": {"total": "many"}})
    with pytest.raises(RpcCallInternalError) as caught:
        client.rpc(Counter).call(Counter.add, AddInput(amount=1))
    assert caught.value.type == "rpc.invalid_output"


def test_call_rejects_foreign_method(client: Opencode) -> None:
    class Other(RpcDefinition, id="other"):
        add = rpc_method(AddInput, Total)

    with pytest.raises(ValueError, match="not a method of Counter"):
        client.rpc(Counter).call(Other.add, AddInput(amount=1))
    with pytest.raises(ValueError, match="not an event of Counter"):
        client.rpc(Counter).subscribe(rpc_event(Total))


def test_subscribe_filters_and_validates_events(client: Opencode, mock_api: respx.MockRouter) -> None:
    body = (
        rpc_frame("rpc.counter.changed", {"total": 1}, 1)
        + rpc_frame("rpc.other.changed", {"total": 2}, 2)
        + rpc_frame("rpc.counter.cleared", {}, 3)
        + rpc_frame("rpc.counter.changed", {"total": 3}, 4)
    )
    mock_api.get("/api/event").respond(headers=SSE, content=body)
    counter = client.rpc(Counter)
    with counter.subscribe(Counter.changed) as changes:
        received = list(changes)
    assert [change.data.total for change in received] == [1, 3]
    assert received[0].name == "changed"
    assert received[0].event.id == "evt_1"
    with counter.events() as raw:
        assert [event.type for event in raw] == ["rpc.counter.changed", "rpc.counter.cleared", "rpc.counter.changed"]


@pytest.fixture
async def aclient(mock_api: respx.MockRouter) -> AsyncIterator[AsyncOpencode]:
    async with AsyncOpencode(base_url=BASE_URL, password=PASSWORD, max_retries=0) as instance:
        yield instance


@pytest.mark.anyio
async def test_async_call_and_subscribe(aclient: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/rpc/counter/add").respond(json={"output": {"total": 7}})
    counter = aclient.rpc(Counter)
    assert (await counter.call(Counter.add, AddInput(amount=7))).total == 7
    mock_api.post("/api/rpc/counter/reset-all").respond(
        400, json={"_tag": "RpcError", "type": "locked", "message": "busy"}
    )
    with pytest.raises(RpcCallError, match="locked"):
        await counter.call(Counter.reset)
    mock_api.get("/api/event").respond(headers=SSE, content=rpc_frame("rpc.counter.changed", {"total": 9}, 1))
    async with counter.subscribe(Counter.changed) as changes:
        assert [change.data.total async for change in changes] == [9]
    async with counter.events() as raw:
        assert [event.id async for event in raw] == ["evt_1"]
