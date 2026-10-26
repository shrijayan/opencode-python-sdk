"""The OpenCode clients: Ferrule's generated clients with this SDK's own features.

Custom code, never regenerated. ``opencode.Opencode`` and ``opencode.AsyncOpencode`` are these
subclasses; ``opencode._client`` holds the generated ones they extend. On top of the generated
client they add:

- ``directory``: the default project directory, sent as the ``location`` of every request that
  does not pass its own;
- ``transport``: an ``httpx`` transport for the client's own connection pool (such as
  :class:`opencode.testing.FakeServer`);
- ``events`` (one shared event stream), ``rpc(Definition)`` (typed plugin RPCs), ``fake()``,
  ``from_service()`` and ``wait_until_ready()``;
- typed errors: a response whose body carries a known ``_tag`` raises its own class.
"""

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, cast
from typing_extensions import Self, override

import httpx

from .._rpc import TypedRpcResource, AsyncTypedRpcResource
from .._types import NOT_GIVEN, NotGiven
from .._client import Opencode as _Opencode, AsyncOpencode as _AsyncOpencode
from .._compat import cached_property
from .._errors import tagged_status_error
from .._events import EventHub, AsyncEventHub
from ._support import DEFAULT_USERNAME
from .._service import (
    Version,
    EnsureReason,
    ServiceError,
    ensure as ensure_service,
    discover as discover_service,
    async_ensure,
    async_discover,
)
from ._resources import Pty, Session, AsyncPty, AsyncSession, Experimental, AsyncExperimental
from .._exceptions import APIStatusError

if TYPE_CHECKING:
    from collections.abc import Mapping, Callable, Iterable, Sequence

    from .._models import FinalRequestOptions
    from ..testing import FakeServer

__all__ = ["FAKE_BASE_URL", "AsyncOpencode", "Opencode"]

FAKE_BASE_URL = "http://opencode.fake"
"""Base URL of clients made by ``Opencode.fake()``."""


def _with_location(options: FinalRequestOptions, directory: str | None) -> FinalRequestOptions:
    """Send ``directory`` as the request's ``location`` unless the call passed one, and leave out
    ``order`` when a page is fetched by ``cursor``: the server rejects both together (the cursor
    already encodes the direction), and the next page keeps the first request's parameters."""
    params = options.params
    if not isinstance(params, dict):
        return options
    query = cast("dict[str, object]", params)
    if "cursor" in query and "order" in query:
        query = {key: value for key, value in query.items() if key != "order"}
    if directory is not None and "location" not in query:
        query = {**query, "location": {"directory": directory}}
    options.params = query
    return options


def _directory(value: str | os.PathLike[str] | None) -> str | None:
    return None if value is None else os.fspath(value)


class Opencode(_Opencode):
    """Synchronous client for an OpenCode server.

    Takes the generated client's arguments (``base_url``, ``username``, ``password``, ``timeout``,
    ``max_retries``, ``default_headers``, ``default_query``, ``http_client``) and:

    Args:
        directory: Default project directory, sent as the ``location`` of every request that does not
            pass its own.
        transport: An ``httpx`` transport for the client's own connection pool, such as
            :class:`opencode.testing.FakeServer`. Cannot be combined with ``http_client``.

    Example::

        from opencode import Opencode

        with Opencode(base_url="http://127.0.0.1:4096", password="...") as client:
            for agent in client.agent.list().data:
                print(agent.id)
    """

    directory: str | None

    def __init__(
        self,
        *,
        directory: str | os.PathLike[str] | None = None,
        transport: httpx.BaseTransport | None = None,
        **kwargs: Any,
    ) -> None:
        if transport is not None:
            if kwargs.get("http_client") is not None:
                raise ValueError("Pass either http_client or transport, not both")
            kwargs["http_client"] = httpx.Client(transport=transport)
        super().__init__(**kwargs)
        self.directory = _directory(directory)

    @override
    def _prepare_options(self, options: FinalRequestOptions) -> FinalRequestOptions:
        return _with_location(super()._prepare_options(options), self.directory)

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        return tagged_status_error(err_msg, body=body, response=response) or super()._make_status_error(
            err_msg, body=body, response=response
        )

    @override
    def copy(self, *, directory: str | os.PathLike[str] | NotGiven | None = NOT_GIVEN, **kwargs: Any) -> Self:
        """Returns a client with some options changed, sharing this client's connection pool."""
        chosen = self.directory if isinstance(directory, NotGiven) else _directory(directory)
        extra = {**kwargs.pop("_extra_kwargs", {}), "directory": chosen}
        return super().copy(_extra_kwargs=extra, **kwargs)

    with_options = copy

    @classmethod
    def from_service(
        cls,
        *,
        start: bool = True,
        file: str | os.PathLike[str] | None = None,
        version: Version | None = None,
        command: Sequence[str] | None = None,
        env: Mapping[str, str] | None = None,
        on_start: Callable[[EnsureReason, str | None], None] | None = None,
        **kwargs: Any,
    ) -> Self:
        """Connect to the local background service, starting ``opencode serve --service`` if needed.

        Uses :func:`opencode.service.ensure`, or :func:`opencode.service.discover` when ``start`` is false, and
        sends the service's password with every request. Other arguments go to the constructor.

        Raises:
            ServiceError: No matching service is running and ``start`` is false, or it could not be started.
        """
        if start:
            endpoint = ensure_service(file, version, command=command, env=env, on_start=on_start)
        else:
            found = discover_service(file, version)
            if found is None:
                raise ServiceError("No matching OpenCode background service is running")
            endpoint = found
        return cls(
            base_url=endpoint.url,
            username=DEFAULT_USERNAME if endpoint.auth is None else endpoint.auth.username,
            password=None if endpoint.auth is None else endpoint.auth.password,
            **kwargs,
        )

    @cached_property
    def events(self) -> EventHub:
        """The shared event stream: one connection for every subscriber. See :class:`opencode.EventHub`."""
        return EventHub(self)

    @cached_property
    @override
    def rpc(self) -> TypedRpcResource:  # pyright: ignore[reportIncompatibleVariableOverride]
        """Plugin RPC calls: ``client.rpc.call(...)``, or ``client.rpc(Definition)`` for typed access."""
        return TypedRpcResource(self)

    @cached_property
    @override
    def session(self) -> Session:  # pyright: ignore[reportIncompatibleVariableOverride]
        """Sessions: the generated operations and ``run``."""
        return Session(self)

    @cached_property
    @override
    def pty(self) -> Pty:  # pyright: ignore[reportIncompatibleVariableOverride]
        """Terminals: the generated operations and ``attach``."""
        return Pty(self)

    @cached_property
    @override
    def experimental(self) -> Experimental:  # pyright: ignore[reportIncompatibleVariableOverride]
        """Experimental operations; ``persistent_pty`` can ``attach``."""
        return Experimental(self)

    @classmethod
    def fake(cls, server: FakeServer | None = None, **kwargs: Any) -> Self:
        """Returns a client wired to an in-process :class:`opencode.testing.FakeServer`, for tests.

        Pass your own ``server`` to configure replies and inspect requests; other arguments go to the constructor.
        """
        from ..testing import FakeServer

        return cls(base_url=FAKE_BASE_URL, transport=server if server is not None else FakeServer(), **kwargs)

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
        from ._ready import wait_until_ready

        wait_until_ready(self, agents=agents, mcp_servers=mcp_servers, timeout=timeout)


class AsyncOpencode(_AsyncOpencode):
    """Asynchronous client for an OpenCode server. Works with asyncio and trio.

    Takes the same arguments as :class:`Opencode`; ``http_client`` is an ``httpx.AsyncClient`` and
    ``transport`` an ``httpx.AsyncBaseTransport``.
    """

    directory: str | None

    def __init__(
        self,
        *,
        directory: str | os.PathLike[str] | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
        **kwargs: Any,
    ) -> None:
        if transport is not None:
            if kwargs.get("http_client") is not None:
                raise ValueError("Pass either http_client or transport, not both")
            kwargs["http_client"] = httpx.AsyncClient(transport=transport)
        super().__init__(**kwargs)
        self.directory = _directory(directory)

    @override
    async def _prepare_options(self, options: FinalRequestOptions) -> FinalRequestOptions:
        return _with_location(await super()._prepare_options(options), self.directory)

    @override
    def _make_status_error(self, err_msg: str, *, body: object, response: httpx.Response) -> APIStatusError:
        return tagged_status_error(err_msg, body=body, response=response) or super()._make_status_error(
            err_msg, body=body, response=response
        )

    @override
    def copy(self, *, directory: str | os.PathLike[str] | NotGiven | None = NOT_GIVEN, **kwargs: Any) -> Self:
        """Returns a client with some options changed, sharing this client's connection pool."""
        chosen = self.directory if isinstance(directory, NotGiven) else _directory(directory)
        extra = {**kwargs.pop("_extra_kwargs", {}), "directory": chosen}
        return super().copy(_extra_kwargs=extra, **kwargs)

    with_options = copy

    @classmethod
    async def from_service(
        cls,
        *,
        start: bool = True,
        file: str | os.PathLike[str] | None = None,
        version: Version | None = None,
        command: Sequence[str] | None = None,
        env: Mapping[str, str] | None = None,
        on_start: Callable[[EnsureReason, str | None], None] | None = None,
        **kwargs: Any,
    ) -> Self:
        """Async version of :meth:`Opencode.from_service`. Await it: ``client = await AsyncOpencode.from_service()``."""
        if start:
            endpoint = await async_ensure(file, version, command=command, env=env, on_start=on_start)
        else:
            found = await async_discover(file, version)
            if found is None:
                raise ServiceError("No matching OpenCode background service is running")
            endpoint = found
        return cls(
            base_url=endpoint.url,
            username=DEFAULT_USERNAME if endpoint.auth is None else endpoint.auth.username,
            password=None if endpoint.auth is None else endpoint.auth.password,
            **kwargs,
        )

    @cached_property
    def events(self) -> AsyncEventHub:
        """The shared event stream: one connection for every subscriber. See :class:`opencode.AsyncEventHub`."""
        return AsyncEventHub(self)

    @cached_property
    @override
    def rpc(self) -> AsyncTypedRpcResource:  # pyright: ignore[reportIncompatibleVariableOverride]
        """Plugin RPC calls: ``client.rpc.call(...)``, or ``client.rpc(Definition)`` for typed access."""
        return AsyncTypedRpcResource(self)

    @cached_property
    @override
    def session(self) -> AsyncSession:  # pyright: ignore[reportIncompatibleVariableOverride]
        """Sessions: the generated operations and ``run``."""
        return AsyncSession(self)

    @cached_property
    @override
    def pty(self) -> AsyncPty:  # pyright: ignore[reportIncompatibleVariableOverride]
        """Terminals: the generated operations and ``attach``."""
        return AsyncPty(self)

    @cached_property
    @override
    def experimental(self) -> AsyncExperimental:  # pyright: ignore[reportIncompatibleVariableOverride]
        """Experimental operations; ``persistent_pty`` can ``attach``."""
        return AsyncExperimental(self)

    @classmethod
    def fake(cls, server: FakeServer | None = None, **kwargs: Any) -> Self:
        """Returns a client wired to an in-process :class:`opencode.testing.FakeServer`, for tests."""
        from ..testing import FakeServer

        return cls(base_url=FAKE_BASE_URL, transport=server if server is not None else FakeServer(), **kwargs)

    async def wait_until_ready(
        self, *, agents: Iterable[str] = (), mcp_servers: Iterable[str] = (), timeout: float = 60
    ) -> None:
        """Async version of :meth:`Opencode.wait_until_ready`."""
        from ._ready import async_wait_until_ready

        await async_wait_until_ready(self, agents=agents, mcp_servers=mcp_servers, timeout=timeout)
