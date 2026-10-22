# Interactive terminals

`client.pty.attach()` opens an interactive connection to a server-side PTY over a WebSocket. It needs the `pty`
extra:

```bash
pip install "opencode-python-sdk[pty]"
```

```python
pty = client.pty.create(command="/bin/sh").data
with client.pty.attach(pty.id) as term:  # (1)!
    term.resize(120, 40)
    term.send("echo hi\n")
    for chunk in term:  # (2)!
        print(chunk.decode(errors="replace"), end="")
```

1. Closing the connection leaves the PTY running; remove it with `client.pty.remove(pty.id)`.
2. Output arrives as `bytes` until the shell exits.

`recv(timeout=...)` reads one chunk and returns `None` once the terminal has ended. `term.cursor` is the output
position to pass as `cursor=` when you reattach; `cursor=-1` skips the replay of earlier output.

## Persistent terminals

Persistent terminals belong to a session and survive server restarts *(experimental)*:

```python
info = client.experimental.persistent_pty.create(session.id, command="/bin/sh", args=[], title="sh", env={})
with client.experimental.persistent_pty.attach(info.id, role="controller", on_event=print) as term:
    term.send("ls\n")
    print(term.recv(timeout=5))
```

`role="observer"` watches without sending input, `takeover=True` takes control from another controller, and
`attachment_id` identifies this client across reconnects. `on_event` receives the JSON events (`attached`,
`replay_complete`, `resized`, `controller_changed`, ...).

## Async

The async client returns `AsyncPtyConnection`, which needs asyncio:

```python
async with await client.pty.attach(pty.id) as term:
    await term.send("echo hi\n")
    async for chunk in term:
        ...
```

## Errors

A refused handshake (bad ticket, unknown PTY) or an abnormal close raises `PtyConnectionError`, with `status` for the
HTTP status and `code` / `reason` for the close frame (`4404` means the terminal was not found, has exited or is
unavailable). The same error explains how to install the extra when `websockets` is missing.

[`examples/terminal.py`](https://github.com/shrijayan/opencode-python-sdk/blob/main/examples/terminal.py) bridges
your local terminal to a remote shell.
