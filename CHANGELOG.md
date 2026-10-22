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

## 0.1.0

First release, generated from OpenCode 2.1.2: sync and async clients for all 142 operations, typed models and
events, typed errors, pagination, event streams, retries, and the `OpencodeServer` launcher.
