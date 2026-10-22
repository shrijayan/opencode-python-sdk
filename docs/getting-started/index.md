# Install

```bash
pip install opencode-python-sdk
```

=== "uv"

    ```bash
    uv add opencode-python-sdk
    ```

=== "poetry"

    ```bash
    poetry add opencode-python-sdk
    ```

The distribution is called `opencode-python-sdk`; the package imports as `opencode`. It needs Python 3.10 or newer
and depends only on `httpx`, `pydantic`, `anyio` and `typing-extensions`.

```python
import opencode

print(opencode.__version__)  # this package
print(opencode.API_VERSION)  # the OpenCode server version it was generated from
```

To start a server from Python with [`OpencodeServer`](server.md), install the [OpenCode CLI](https://opencode.ai)
as well, so that `opencode` is on `PATH`.

## Next

- [Connect to a server](connect.md) that is already running.
- [Run a server from Python](server.md) for scripts, tests and embedded use.
