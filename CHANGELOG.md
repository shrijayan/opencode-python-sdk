# Changelog

Releases are published automatically on every merge to `main`. Release notes for each version are on the
[GitHub releases page](https://github.com/shrijayan/opencode-python-sdk/releases).

## Unreleased

- `client.events`: a shared event stream with one connection for all subscribers, bounded per-subscriber queues,
  `server.connected` replay, `of_type` / `for_session` / `where` filters, `on_activity` keepalive hook, cancellation,
  and opt-in reconnection with backoff (`EventHub(client, reconnect=True)`).
- `client.rpc(Definition)`: typed plugin RPC calls and event subscriptions declared with `RpcDefinition`,
  `rpc_method` and `rpc_event`; RPC failures raise `RpcCallError` / `RpcCallInternalError`.
- `Stream.on_activity` and `Stream.interrupt()`.
- `OPENCODE_LOG=debug|info` sends the `opencode` logger to stderr at that level.
- `client.copy(...)`, an alias of `client.with_options(...)`; documented that copies share the connection pool
  and do not close it.
- `DefaultAioHttpClient`: an optional aiohttp transport for `AsyncOpencode`, installed with the `aiohttp` extra
  (`pip install 'opencode-python-sdk[aiohttp]'`) and passed as `http_client=`.
- `.with_raw_response` and `.with_streaming_response` on every resource (sync and async): return an
  `APIResponse` / `AsyncAPIResponse` with `headers`, `status_code`, `http_response`, `request`, `text`, `json()`,
  `iter_bytes()` / `iter_lines()` and `parse()` for the usual typed value.
- `client.get` / `post` / `put` / `patch` / `delete` for endpoints the client has no method for.

## 0.1.0

First release, generated from OpenCode 2.1.2: sync and async clients for all 142 operations, typed models and
events, typed errors, pagination, event streams, retries, and the `OpencodeServer` launcher.
