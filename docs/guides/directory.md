# The project directory

An OpenCode server can serve several projects. Most endpoints take a `location` that says which one a request is
about. Set a default once on the client:

```python
client = Opencode("http://127.0.0.1:4096", directory="/path/to/repo")
client.agent.list()  # (1)!
client.agent.list(location={"directory": "/other"})  # (2)!
```

1. Sent with `location` = `/path/to/repo`.
2. A per-call `location` overrides the default.

Without a default, the server uses its own working directory. With `OpencodeServer`, that is `cwd`; you can also pass
`directory=` to `server.client()`.

```python
with OpencodeServer(cwd="/repos/api") as server:
    api = server.client()
    web = server.client(directory="/repos/web")
```
