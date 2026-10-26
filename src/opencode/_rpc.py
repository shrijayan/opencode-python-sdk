"""Typed calls to plugin RPCs.

A plugin registers an RPC with an id, methods and events. Declare the same shape once as a class, then call it
through ``client.rpc(Definition)``, the counterpart of ``client.rpc(definition)`` in the official TypeScript client::

    from pydantic import BaseModel
    from opencode import RpcDefinition, rpc_event, rpc_method


    class AddInput(BaseModel):
        amount: int


    class Total(BaseModel):
        total: int


    class Counter(RpcDefinition, id="counter"):
        add = rpc_method(AddInput, Total)
        reset = rpc_method(None, Total)
        changed = rpc_event(Total)


    counter = client.rpc(Counter)
    print(counter.call(Counter.add, AddInput(amount=2)).total)
    with counter.subscribe(Counter.changed) as changes:
        for change in changes:
            print(change.data.total)

Inputs are validated and serialized, and outputs and event data validated, with pydantic, so any type pydantic
accepts works: models, dataclasses, ``TypedDict``, ``list[int]``. RPC failures raise :class:`RpcCallError`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Generic, TypeVar, cast, overload

import pydantic
from typing_extensions import Self

from ._errors import RpcError, RpcInternalError
from ._exceptions import OpencodeError
from ._types import NOT_GIVEN, NotGiven
from .lib._support import type_adapter, validation_summary
from .resources.rpc import AsyncRpcResource, RpcResource

if TYPE_CHECKING:
    from collections.abc import Mapping
    from types import TracebackType

    from .lib._client import AsyncOpencode, Opencode
    from ._events import AsyncSubscription, Subscription
    from ._types import Headers
    from .lib._support import Timeout
    from .lib._support import Location
    from .types import RpcEvent

__all__ = [
    "AsyncRpcClient",
    "AsyncRpcEvents",
    "RpcCallError",
    "RpcCallInternalError",
    "RpcClient",
    "RpcDefinition",
    "RpcEventDefinition",
    "RpcEventPayload",
    "RpcEvents",
    "RpcMethod",
    "rpc_event",
    "rpc_method",
]

_D = TypeVar("_D", bound="RpcDefinition")
_I = TypeVar("_I")
_O = TypeVar("_O")
_T = TypeVar("_T")


class RpcCallError(OpencodeError):
    """A plugin RPC method failed (the server answered with ``RpcError``).

    Attributes:
        rpc_id: The RPC that was called.
        method: The method that was called.
        type: The error type the plugin reported, for example ``"not_found"``.
        message: The error message.
        data: Error details, validated against the method's ``errors`` declaration when it names this type.
    """

    def __init__(self, rpc_id: str, method: str, type: str, message: str, data: object = None) -> None:
        super().__init__(f"{rpc_id}.{method} failed with {type}: {message}")
        self.rpc_id = rpc_id
        self.method = method
        self.type = type
        self.message = message
        self.data = data


class RpcCallInternalError(RpcCallError):
    """The plugin RPC crashed or returned output that does not match its declaration.

    ``type`` is ``"rpc.internal"`` or ``"rpc.invalid_output"``. Output this client cannot validate against the
    method's declared output type is also reported as ``"rpc.invalid_output"``.
    """


class RpcMethod(Generic[_I, _O]):
    """One method of an :class:`RpcDefinition`. Create it with :func:`rpc_method`."""

    name: str

    def __init__(self, input: Any, output: Any, *, name: str | None, errors: Mapping[str, Any] | None) -> None:
        self.input = input
        self.output = output
        self.errors = dict(errors or {})
        if name is not None:
            self.name = name

    def __set_name__(self, owner: type, name: str) -> None:
        if not hasattr(self, "name"):
            self.name = name

    def encode(self, value: _I) -> object:
        """Validates ``value`` against the input type and returns its JSON form."""
        if self.input is None:
            return NOT_GIVEN if value is None else value
        adapter = type_adapter(self.input)
        return adapter.dump_python(adapter.validate_python(value), mode="json", by_alias=True)

    def decode(self, rpc_id: str, value: object) -> _O:
        """Validates a method's output."""
        if self.output is None:
            return cast("_O", None)
        try:
            return cast("_O", type_adapter(self.output).validate_python(value))
        except pydantic.ValidationError as exc:
            raise RpcCallInternalError(rpc_id, self.name, "rpc.invalid_output", validation_summary(exc), value) from exc

    def error(self, rpc_id: str, exc: RpcError | RpcInternalError) -> RpcCallError:
        """Maps a transport error to :class:`RpcCallError`, decoding declared error data."""
        body = exc.error
        data: object = body.data
        if body.type in self.errors and data is not None:
            try:
                data = type_adapter(self.errors[body.type]).validate_python(data)
            except pydantic.ValidationError:
                data = body.data
        cls = RpcCallInternalError if isinstance(exc, RpcInternalError) else RpcCallError
        return cls(rpc_id, self.name, body.type, body.message, data)


class RpcEventDefinition(Generic[_T]):
    """One event of an :class:`RpcDefinition`. Create it with :func:`rpc_event`."""

    name: str

    def __init__(self, data: Any, *, name: str | None) -> None:
        self.data = data
        if name is not None:
            self.name = name

    def __set_name__(self, owner: type, name: str) -> None:
        if not hasattr(self, "name"):
            self.name = name

    def parse(self, event: RpcEvent) -> RpcEventPayload[_T]:
        """Validates the data of a raw RPC event of this kind.

        Raises:
            pydantic.ValidationError: The data does not match the declared type.
        """
        data = cast("_T", type_adapter(self.data).validate_python(event.data))
        return RpcEventPayload(name=self.name, data=data, event=event)


@overload
def rpc_method(
    input: None, output: type[_O], *, name: str | None = None, errors: Mapping[str, Any] | None = None
) -> RpcMethod[None, _O]: ...
@overload
def rpc_method(
    input: type[_I], output: type[_O], *, name: str | None = None, errors: Mapping[str, Any] | None = None
) -> RpcMethod[_I, _O]: ...
def rpc_method(
    input: Any, output: Any, *, name: str | None = None, errors: Mapping[str, Any] | None = None
) -> RpcMethod[Any, Any]:
    """Declares an RPC method on an :class:`RpcDefinition`.

    Args:
        input: The input type, or ``None`` for a method without input.
        output: The output type. Use ``type(None)`` for a method that returns nothing.
        name: The method name on the server. Defaults to the attribute name.
        errors: Data types of the errors the method declares, by error type. Matching error data is validated
            into these types on :attr:`RpcCallError.data`.
    """
    return RpcMethod(input, output, name=name, errors=errors)


def rpc_event(data: type[_T], *, name: str | None = None) -> RpcEventDefinition[_T]:
    """Declares an RPC event on an :class:`RpcDefinition`.

    Args:
        data: The type of the event's ``data``.
        name: The event name on the server. Defaults to the attribute name.
    """
    return RpcEventDefinition(data, name=name)


class RpcDefinition:
    """Base class for plugin RPC declarations. Pass the RPC id as a class keyword::

        class Counter(RpcDefinition, id="counter"):
            add = rpc_method(AddInput, Total)
            changed = rpc_event(Total)

    The class is only a declaration; bind it to a client with ``client.rpc(Counter)``.
    """

    id: ClassVar[str]
    methods: ClassVar[dict[str, RpcMethod[Any, Any]]]
    events: ClassVar[dict[str, RpcEventDefinition[Any]]]

    def __init_subclass__(cls, *, id: str | None = None, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if id is not None:
            cls.id = id
        elif not hasattr(cls, "id"):
            raise TypeError(f"{cls.__name__} needs an RPC id: class {cls.__name__}(RpcDefinition, id='...')")
        methods: dict[str, RpcMethod[Any, Any]] = {}
        events: dict[str, RpcEventDefinition[Any]] = {}
        for base in reversed(cls.__mro__):
            for value in vars(base).values():
                if isinstance(value, RpcMethod):
                    methods[value.name] = value
                elif isinstance(value, RpcEventDefinition):
                    events[value.name] = value
        cls.methods = methods
        cls.events = events

    @classmethod
    def event_type(cls, event: RpcEventDefinition[Any] | str) -> str:
        """The wire ``type`` of an event of this RPC: ``rpc.<id>.<name>``."""
        return f"rpc.{cls.id}.{event if isinstance(event, str) else event.name}"


@dataclass(frozen=True)
class RpcEventPayload(Generic[_T]):
    """A plugin RPC event with validated data.

    Attributes:
        name: The event name, without the ``rpc.<id>.`` prefix.
        data: The validated event data.
        event: The raw event, with its ``id``, ``created`` time and ``location``.
    """

    name: str
    data: _T
    event: RpcEvent


def _check_method(definition: type[RpcDefinition], method: RpcMethod[Any, Any]) -> None:
    if not any(known is method for known in definition.methods.values()):
        raise ValueError(f"{getattr(method, 'name', method)!r} is not a method of {definition.__name__}")


def _check_event(definition: type[RpcDefinition], event: RpcEventDefinition[Any]) -> None:
    if not any(known is event for known in definition.events.values()):
        raise ValueError(f"{getattr(event, 'name', event)!r} is not an event of {definition.__name__}")


class RpcClient(Generic[_D]):
    """A plugin RPC bound to a synchronous client. Get one with ``client.rpc(Definition)``."""

    def __init__(self, client: Opencode, definition: type[_D]) -> None:
        self._client = client
        self.definition = definition

    @overload
    def call(
        self,
        method: RpcMethod[None, _O],
        input: None = None,
        *,
        location: Location | NotGiven | None = NOT_GIVEN,
        extra_headers: Headers | None = None,
        timeout: Timeout | NotGiven = NOT_GIVEN,
    ) -> _O: ...
    @overload
    def call(
        self,
        method: RpcMethod[_I, _O],
        input: _I,
        *,
        location: Location | NotGiven | None = NOT_GIVEN,
        extra_headers: Headers | None = None,
        timeout: Timeout | NotGiven = NOT_GIVEN,
    ) -> _O: ...
    def call(
        self,
        method: RpcMethod[Any, Any],
        input: Any = None,
        *,
        location: Location | NotGiven | None = NOT_GIVEN,
        extra_headers: Headers | None = None,
        timeout: Timeout | NotGiven = NOT_GIVEN,
    ) -> Any:
        """Calls a method of this RPC and returns its validated output.

        Raises:
            RpcCallError: The method failed.
            RpcCallInternalError: The method crashed or returned invalid output.
        """
        _check_method(self.definition, method)
        rpc_id = self.definition.id
        try:
            result = self._client.rpc.call(
                method.name,
                rpc_id=rpc_id,
                input=method.encode(input),
                location=location,
                extra_headers=extra_headers,
                timeout=timeout,
            )
        except (RpcError, RpcInternalError) as exc:
            raise method.error(rpc_id, exc) from exc
        return method.decode(rpc_id, result.output)

    def events(self) -> Subscription[RpcEvent]:
        """Subscribes to every event of this RPC, as raw events, on the client's shared event stream."""
        from .types import RpcEvent

        prefix = f"rpc.{self.definition.id}."
        return self._client.events.of_type(RpcEvent).where(lambda event: event.type.startswith(prefix))

    def subscribe(self, event: RpcEventDefinition[_T]) -> RpcEvents[_T]:
        """Subscribes to one event of this RPC, with validated data, on the client's shared event stream."""
        from .types import RpcEvent

        _check_event(self.definition, event)
        wire = self.definition.event_type(event)
        return RpcEvents(self._client.events.of_type(RpcEvent).where(lambda raw: raw.type == wire), event)


class AsyncRpcClient(Generic[_D]):
    """A plugin RPC bound to an asynchronous client. Get one with ``client.rpc(Definition)``."""

    def __init__(self, client: AsyncOpencode, definition: type[_D]) -> None:
        self._client = client
        self.definition = definition

    @overload
    async def call(
        self,
        method: RpcMethod[None, _O],
        input: None = None,
        *,
        location: Location | NotGiven | None = NOT_GIVEN,
        extra_headers: Headers | None = None,
        timeout: Timeout | NotGiven = NOT_GIVEN,
    ) -> _O: ...
    @overload
    async def call(
        self,
        method: RpcMethod[_I, _O],
        input: _I,
        *,
        location: Location | NotGiven | None = NOT_GIVEN,
        extra_headers: Headers | None = None,
        timeout: Timeout | NotGiven = NOT_GIVEN,
    ) -> _O: ...
    async def call(
        self,
        method: RpcMethod[Any, Any],
        input: Any = None,
        *,
        location: Location | NotGiven | None = NOT_GIVEN,
        extra_headers: Headers | None = None,
        timeout: Timeout | NotGiven = NOT_GIVEN,
    ) -> Any:
        """Calls a method of this RPC and returns its validated output.

        Raises:
            RpcCallError: The method failed.
            RpcCallInternalError: The method crashed or returned invalid output.
        """
        _check_method(self.definition, method)
        rpc_id = self.definition.id
        try:
            result = await self._client.rpc.call(
                method.name,
                rpc_id=rpc_id,
                input=method.encode(input),
                location=location,
                extra_headers=extra_headers,
                timeout=timeout,
            )
        except (RpcError, RpcInternalError) as exc:
            raise method.error(rpc_id, exc) from exc
        return method.decode(rpc_id, result.output)

    def events(self) -> AsyncSubscription[RpcEvent]:
        """Subscribes to every event of this RPC, as raw events, on the client's shared event stream."""
        from .types import RpcEvent

        prefix = f"rpc.{self.definition.id}."
        return self._client.events.of_type(RpcEvent).where(lambda event: event.type.startswith(prefix))

    def subscribe(self, event: RpcEventDefinition[_T]) -> AsyncRpcEvents[_T]:
        """Subscribes to one event of this RPC, with validated data, on the client's shared event stream."""
        from .types import RpcEvent

        _check_event(self.definition, event)
        wire = self.definition.event_type(event)
        return AsyncRpcEvents(self._client.events.of_type(RpcEvent).where(lambda raw: raw.type == wire), event)


class RpcEvents(Generic[_T]):
    """Events of one kind from a plugin RPC. Iterate with ``for``; close it, or use ``with``, to leave."""

    def __init__(self, source: Subscription[RpcEvent], event: RpcEventDefinition[_T]) -> None:
        self._source = source
        self._event = event

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> RpcEventPayload[_T]:
        return self._event.parse(next(self._source))

    def get(self, timeout: float | None = None) -> RpcEventPayload[_T]:
        """Returns the next event, waiting up to ``timeout`` seconds. See :meth:`Subscription.get`."""
        return self._event.parse(self._source.get(timeout))

    def close(self) -> None:
        """Leaves the shared event stream."""
        self._source.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        self.close()


class AsyncRpcEvents(Generic[_T]):
    """Events of one kind from a plugin RPC. Iterate with ``async for``; close it, or use ``async with``."""

    def __init__(self, source: AsyncSubscription[RpcEvent], event: RpcEventDefinition[_T]) -> None:
        self._source = source
        self._event = event

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> RpcEventPayload[_T]:
        return self._event.parse(await self._source.__anext__())

    async def get(self) -> RpcEventPayload[_T]:
        """Returns the next event. See :meth:`AsyncSubscription.get`."""
        return self._event.parse(await self._source.get())

    async def close(self) -> None:
        """Leaves the shared event stream."""
        await self._source.close()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self.close()


class TypedRpcResource(RpcResource):
    """``client.rpc``: the generated ``call`` plus ``client.rpc(Definition)`` for typed access."""

    def __call__(self, definition: type[_D]) -> RpcClient[_D]:
        """Binds a plugin RPC declaration to this client."""
        return RpcClient(self._client, definition)


class AsyncTypedRpcResource(AsyncRpcResource):
    """``client.rpc``: the generated ``call`` plus ``client.rpc(Definition)`` for typed access."""

    def __call__(self, definition: type[_D]) -> AsyncRpcClient[_D]:
        """Binds a plugin RPC declaration to this client."""
        return AsyncRpcClient(self._client, definition)
