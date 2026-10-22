# How it's built

Most of this package is generated. The models, resources, error classes and `api.md` come from OpenCode's own
contract; the transport, retries, streaming, pagination and server launcher are written by hand.

```text
@opencode/protocol (npm) ──bun codegen/extract──▶ spec/contract.json ──python -m codegen──▶ src/opencode
```

## 1. Extract the contract

`codegen/extract/extract.ts` loads `ClientApi` from the published `@opencode/protocol` package, the same Effect
`HttpApi` definition the official TypeScript client is built from. It exports every endpoint with its inputs,
outputs and declared errors, and every schema as JSON Schema, into `spec/contract.json`.

Because the contract comes from the server's source of truth rather than a hand-written OpenAPI file, method names
and request shapes match the TypeScript client exactly.

## 2. Generate Python

`python -m codegen` reads the contract and writes:

| Output | What it contains |
| --- | --- |
| `src/opencode/types/` | pydantic models for every schema, discriminated unions with `Unknown...` fallbacks, open enums |
| `src/opencode/resources/` | A sync and an async class per API group, with typed arguments and docstrings |
| `src/opencode/_errors.py` | An exception class for every declared server error |
| `api.md` | The method table |

## 3. Hand-written runtime

| Module | Responsibility |
| --- | --- |
| `_base_client.py` | Request building, auth, retries with backoff, timeouts |
| `_pagination.py` | Cursor pages and the async paginator |
| `_streaming.py` | Server-sent event decoding |
| `_server.py` | `OpencodeServer` |
| `_models.py`, `_types.py` | Model base class, `NOT_GIVEN`, open enums |

## Keeping it current

Generated code is committed. CI regenerates it and fails if anything changed, so the committed code always matches
`spec/contract.json`. A nightly workflow checks for new `@opencode/protocol` releases and opens a pull request with
the regenerated client. See [Contributing](contributing.md) for running it locally.
