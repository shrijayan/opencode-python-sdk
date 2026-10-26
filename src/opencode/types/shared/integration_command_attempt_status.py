# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "IntegrationCommandAttemptStatus",
    "IntegrationCommandAttemptStatusVariant0",
    "IntegrationCommandAttemptStatusVariant0Time",
    "IntegrationCommandAttemptStatusVariant1",
    "IntegrationCommandAttemptStatusVariant1Time",
    "IntegrationCommandAttemptStatusVariant2",
    "IntegrationCommandAttemptStatusVariant2Time",
    "IntegrationCommandAttemptStatusVariant3",
    "IntegrationCommandAttemptStatusVariant3Time",
]


class IntegrationCommandAttemptStatusVariant0Time(BaseModel):
    created: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    expires: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class IntegrationCommandAttemptStatusVariant0(BaseModel):
    status: Literal["pending"]

    time: IntegrationCommandAttemptStatusVariant0Time

    message: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class IntegrationCommandAttemptStatusVariant1Time(BaseModel):
    created: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    expires: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class IntegrationCommandAttemptStatusVariant1(BaseModel):
    status: Literal["complete"]

    time: IntegrationCommandAttemptStatusVariant1Time

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class IntegrationCommandAttemptStatusVariant2Time(BaseModel):
    created: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    expires: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class IntegrationCommandAttemptStatusVariant2(BaseModel):
    message: str

    status: Literal["failed"]

    time: IntegrationCommandAttemptStatusVariant2Time

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class IntegrationCommandAttemptStatusVariant3Time(BaseModel):
    created: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    expires: Union[Literal["Infinity", "-Infinity", "NaN"], float]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class IntegrationCommandAttemptStatusVariant3(BaseModel):
    status: Literal["expired"]

    time: IntegrationCommandAttemptStatusVariant3Time

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


IntegrationCommandAttemptStatus: TypeAlias = Union[
    IntegrationCommandAttemptStatusVariant0,
    IntegrationCommandAttemptStatusVariant1,
    IntegrationCommandAttemptStatusVariant2,
    IntegrationCommandAttemptStatusVariant3,
]
