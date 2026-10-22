from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Any

from typing_extensions import Self

from ._base_client import AsyncAPIClient, SyncAPIClient
from ._constants import DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT, DEFAULT_USERNAME
from ._events import AsyncEventHub, EventHub
from ._rpc import AsyncTypedRpcResource, TypedRpcResource
from ._types import NOT_GIVEN, NotGiven, Timeout
from .resources import AsyncResources, SyncResources

if TYPE_CHECKING:
    import os
    from collections.abc import Iterable, Mapping

    import httpx

    from .testing import FakeServer

__all__ = ["AsyncOpencode", "Opencode"]

FAKE_BASE_URL = "http://opencode.fake"
"""Base URL of clients made by ``Opencode.fake()``."""


class Opencode(SyncAPIClient, SyncResources):
    """Synchronous client for an OpenCode server.

    Args:
        base_url: Server URL, for example ``http://127.0.0.1:4096``. Defaults to ``OPENCODE_BASE_URL``.
        password: Server password. Defaults to ``OPENCODE_PASSWORD``, then ``OPENCODE_SERVER_PASSWORD``. Pass ``""``
            to send no credentials.
        username: Basic auth user name. The OpenCode server uses ``opencode``.
        directory: Default project directory. Sent as the ``location`` of every request that accepts one, unless
            the call passes its own ``location``.
        timeout: Default timeout in seconds, or an ``httpx.Timeout``. Event streams only apply the connect timeout.
        max_retries: Retries for connection failures and transient statuses. Requests that may have changed state
            on the server are only retried when the server refused them before acting (429 and 503).
        default_headers: Headers sent with every request.
        default_query: Query parameters sent with every request.
        http_client: A preconfigured ``httpx.Client`` (proxies, custom transports, event hooks). The caller keeps
            ownership and must close it.
        transport: An ``httpx`` transport for the client's own connection pool, such as
            :class:`opencode.testing.FakeServer`. Cannot be combined with ``http_client``.

    Example::

        from opencode import Opencode

        with Opencode("http://127.0.0.1:4096", password="...") as client:
            for agent in client.agent.list():
                print(agent.id)
    """

    def __init__(
        self,
        base_url: str | httpx.URL | None = None,
        *,
        password: str | None = None,
        username: str = DEFAULT_USERNAME,
        directory: str | os.PathLike[str] | None = None,
        timeout: Timeout = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        http_client: httpx.Client | None = None,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        super().__init__(
            base_url=base_url,
            password=password,
            username=username,
            directory=directory,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
            transport=transport,
        )

    @cached_property
    def events(self) -> EventHub:
        """The shared event stream: one connection for every subscriber. See :class:`opencode.EventHub`."""
        return EventHub(self)

    @cached_property
    def rpc(self) -> TypedRpcResource:
        """Plugin RPC calls: ``client.rpc.call(...)``, or ``client.rpc(Definition)`` for typed access."""
        return TypedRpcResource(self)

    @classmethod
    def fake(cls, server: FakeServer | None = None, **kwargs: Any) -> Self:
        """Returns a client wired to an in-process :class:`opencode.testing.FakeServer`, for tests.

        Pass your own ``server`` to configure replies and inspect requests; other arguments go to the constructor.
        """
        from .testing import FakeServer

        kwargs.setdefault("password", "")
        return cls(FAKE_BASE_URL, transport=server if server is not None else FakeServer(), **kwargs)

    def wait_until_ready(
        self, *, agents: Iterable[str] = (), mcp_servers: Iterable[str] = (), timeout: float = 60
    ) -> None:
        """Blocks until the server answers, the named ``agents`` are listed and the named ``mcp_servers`` are
        connected.

        Agents load asynchronously after the server starts, so call this before creating sessions on a freshly
        booted server. Connection errors and 503s while the server boots count as not ready yet.

        Raises:
          TimeoutError: Something was still missing after ``timeout`` seconds. The message names it.
        """
        from .lib._ready import wait_until_ready

        wait_until_ready(self, agents=agents, mcp_servers=mcp_servers, timeout=timeout)

    def with_options(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        password: str | NotGiven | None = NOT_GIVEN,
        directory: str | os.PathLike[str] | NotGiven | None = NOT_GIVEN,
        timeout: Timeout | NotGiven = NOT_GIVEN,
        max_retries: int | None = None,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
    ) -> Self:
        """Returns a client with some options changed. It shares this client's connection pool.

        ``default_headers`` and ``default_query`` are merged over the current values.
        """
        client = type(self)(
            base_url=base_url or self.base_url,
            password=self.password or "" if isinstance(password, NotGiven) else password,
            username=self.username,
            directory=self.directory if isinstance(directory, NotGiven) else directory,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            max_retries=self.max_retries if max_retries is None else max_retries,
            default_headers={**self._default_headers, **(default_headers or {})},
            default_query={**self._default_query, **(default_query or {})},
            http_client=self._http,
        )
        return client


class AsyncOpencode(AsyncAPIClient, AsyncResources):
    """Asynchronous client for an OpenCode server. Works with asyncio and trio.

    Takes the same arguments as :class:`Opencode`; ``http_client`` is an ``httpx.AsyncClient``.

    Example::

        from opencode import AsyncOpencode

        async with AsyncOpencode("http://127.0.0.1:4096", password="...") as client:
            for agent in await client.agent.list():
                print(agent.id)
    """

    def __init__(
        self,
        base_url: str | httpx.URL | None = None,
        *,
        password: str | None = None,
        username: str = DEFAULT_USERNAME,
        directory: str | os.PathLike[str] | None = None,
        timeout: Timeout = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        http_client: httpx.AsyncClient | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        super().__init__(
            base_url=base_url,
            password=password,
            username=username,
            directory=directory,
            timeout=timeout,
            max_retries=max_retries,
            default_headers=default_headers,
            default_query=default_query,
            http_client=http_client,
            transport=transport,
        )

    @cached_property
    def events(self) -> AsyncEventHub:
        """The shared event stream: one connection for every subscriber. See :class:`opencode.AsyncEventHub`."""
        return AsyncEventHub(self)

    @cached_property
    def rpc(self) -> AsyncTypedRpcResource:
        """Plugin RPC calls: ``client.rpc.call(...)``, or ``client.rpc(Definition)`` for typed access."""
        return AsyncTypedRpcResource(self)

    @classmethod
    def fake(cls, server: FakeServer | None = None, **kwargs: Any) -> Self:
        """Returns a client wired to an in-process :class:`opencode.testing.FakeServer`, for tests.

        Pass your own ``server`` to configure replies and inspect requests; other arguments go to the constructor.
        """
        from .testing import FakeServer

        kwargs.setdefault("password", "")
        return cls(FAKE_BASE_URL, transport=server if server is not None else FakeServer(), **kwargs)

    async def wait_until_ready(
        self, *, agents: Iterable[str] = (), mcp_servers: Iterable[str] = (), timeout: float = 60
    ) -> None:
        """Blocks until the server answers, the named ``agents`` are listed and the named ``mcp_servers`` are
        connected.

        Agents load asynchronously after the server starts, so call this before creating sessions on a freshly
        booted server. Connection errors and 503s while the server boots count as not ready yet.

        Raises:
          TimeoutError: Something was still missing after ``timeout`` seconds. The message names it.
        """
        from .lib._ready import async_wait_until_ready

        await async_wait_until_ready(self, agents=agents, mcp_servers=mcp_servers, timeout=timeout)

    def with_options(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        password: str | NotGiven | None = NOT_GIVEN,
        directory: str | os.PathLike[str] | NotGiven | None = NOT_GIVEN,
        timeout: Timeout | NotGiven = NOT_GIVEN,
        max_retries: int | None = None,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
    ) -> Self:
        """Returns a client with some options changed. It shares this client's connection pool.

        ``default_headers`` and ``default_query`` are merged over the current values.
        """
        client = type(self)(
            base_url=base_url or self.base_url,
            password=self.password or "" if isinstance(password, NotGiven) else password,
            username=self.username,
            directory=self.directory if isinstance(directory, NotGiven) else directory,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            max_retries=self.max_retries if max_retries is None else max_retries,
            default_headers={**self._default_headers, **(default_headers or {})},
            default_query={**self._default_query, **(default_query or {})},
            http_client=self._http,
        )
        return client
