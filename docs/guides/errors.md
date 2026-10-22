# Errors

Every exception derives from `opencode.OpencodeError`. Errors the server declares are raised as their own class,
with a typed body on `.error`:

```python
import opencode

try:
    client.session.get("ses_missing")
except opencode.SessionNotFoundError as error:  # (1)!
    print(error.error.session_id, error.status_code)
except opencode.NotFoundError:  # (2)!
    ...
except opencode.APIConnectionError:  # (3)!
    ...
```

1. A declared error: `error.error` is a typed `SessionNotFoundErrorBody`.
2. Any other 404.
3. The server could not be reached, or the request timed out.

## Hierarchy

```text
OpencodeError
├── ServerStartError                 OpencodeServer could not start
└── APIError
    ├── APIConnectionError           no response
    │   └── APITimeoutError
    ├── APIResponseValidationError   unexpected response body
    └── APIStatusError               any non-2xx response
        ├── BadRequestError          400
        ├── AuthenticationError      401
        ├── PermissionDeniedError    403
        ├── NotFoundError            404
        ├── ConflictError            409
        ├── ContentTooLargeError     413
        ├── UnprocessableEntityError 422
        ├── RateLimitError           429
        └── InternalServerError      5xx
            ├── NotImplementedServerError   501
            └── ServiceUnavailableError     503
```

Declared errors such as `SessionNotFoundError` or `SessionBusyError` subclass the status class that matches their
HTTP status, so catching `NotFoundError` also catches `SessionNotFoundError`. Each declared error is documented on
the method that can raise it, under **Raises**. The full list is in the [exceptions reference](../reference/exceptions.md).

## What an `APIStatusError` carries

| Attribute | Value |
| --- | --- |
| `status_code` | The HTTP status |
| `response` | The `httpx.Response` |
| `request` | The `httpx.Request` |
| `body` | The decoded JSON body, or text |
| `error_tag` | The server's `_tag`, which may be one this client does not know yet |
| `request_id` | The `x-request-id` header, when the server sends one |
