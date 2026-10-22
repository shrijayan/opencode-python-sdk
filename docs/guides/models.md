# Models and unions

Responses are [pydantic](https://docs.pydantic.dev) v2 models, defined in `opencode.types`. Attributes are
`snake_case`; the wire names stay available as aliases, so a model validates server JSON and serializes back to it
unchanged.

```python
from opencode.types import ModelRef

session = client.session.create(model=ModelRef(id="claude-sonnet-5-5", provider_id="anthropic"))
session.project_id  # (1)!
session.to_dict()  # (2)!
session.to_json(indent=2)
```

1. Attribute access in `snake_case`.
2. `{"id": "...", "projectID": "...", ...}`: wire names, unset fields left out.

Requests accept either model instances or plain dicts with wire names.

## Discriminated unions

Unions are discriminated on their `type` field, so `isinstance` and `match` narrow them, and type checkers follow:

```python
from opencode.types import SessionMessageAssistant, SessionMessageUser

for message in client.message.list(session.id):
    match message:
        case SessionMessageUser(text=text):
            print("user:", text)
        case SessionMessageAssistant():
            print("assistant replied")
        case _:
            pass  # (1)!
```

1. Always keep a fallback arm: it also catches variants added by newer servers.

## Forward compatibility

A client generated from an older contract keeps working against a newer server:

- **New fields** are kept on the model and available as attributes and through `model_extra`.
- **New enum values** are accepted as plain strings.
- **New union variants** are parsed into an `Unknown...` fallback model with all their fields, rather than failing.
- **New event types** arrive as `UnknownEvent`.

Validation errors on a response are raised as `APIResponseValidationError`, and report field locations and reasons
without values.
