from __future__ import annotations

import pydantic

from opencode.types import (
    ConfigAgent,
    Event,
    ModelRef,
    PromptFileSourceInline,
    SessionMessageInfo,
    SessionMessageUser,
    UnknownEvent,
    UnknownSessionMessageInfo,
)

MESSAGES: pydantic.TypeAdapter[SessionMessageInfo] = pydantic.TypeAdapter(SessionMessageInfo)
EVENTS: pydantic.TypeAdapter[Event] = pydantic.TypeAdapter(Event)


def test_models_accept_wire_and_python_names() -> None:
    assert ModelRef.model_validate({"id": "m", "providerID": "p"}).provider_id == "p"
    assert ModelRef(id="m", provider_id="p").to_dict() == {"id": "m", "providerID": "p"}


def test_optional_fields_are_omitted_not_null() -> None:
    assert ModelRef(id="m", provider_id="p", variant=None).to_dict() == {"id": "m", "providerID": "p"}


def test_unknown_fields_are_kept() -> None:
    ref = ModelRef.model_validate({"id": "m", "providerID": "p", "newField": 1})
    assert ref.model_extra == {"newField": 1}


def test_union_tag_defaults_and_is_serialized() -> None:
    source = PromptFileSourceInline()
    assert source.to_dict() == {"type": "inline"}
    assert PromptFileSourceInline.model_validate({"type": "inline"}).to_dict() == {"type": "inline"}


def test_discriminated_union_selects_member() -> None:
    message = MESSAGES.validate_python({"type": "user", "id": "msg_1", "time": {"created": 1}, "text": "hello"})
    assert isinstance(message, SessionMessageUser)
    assert message.text == "hello"


def test_unknown_union_variant_falls_back_instead_of_failing() -> None:
    message = MESSAGES.validate_python({"type": "hologram", "id": "msg_2", "payload": [1, 2]})
    assert isinstance(message, UnknownSessionMessageInfo)
    assert message.type == "hologram"
    assert message.id == "msg_2"
    assert message.model_extra == {"payload": [1, 2]}


def test_unknown_event_type_falls_back() -> None:
    event = EVENTS.validate_python({"type": "future.thing", "id": "evt_1", "created": 1, "data": {}})
    assert isinstance(event, UnknownEvent)


def test_rpc_events_match_by_pattern() -> None:
    event = EVENTS.validate_python(
        {"type": "rpc.myplugin.ping", "id": "evt_1", "created": 1, "location": {"directory": "/r"}, "data": {}}
    )
    assert type(event).__name__ == "RpcEvent"


def test_open_enum_accepts_new_values() -> None:
    assert ConfigAgent.model_validate({"mode": "primary"}).mode == "primary"
    assert ConfigAgent.model_validate({"mode": "orchestrator"}).mode == "orchestrator"
