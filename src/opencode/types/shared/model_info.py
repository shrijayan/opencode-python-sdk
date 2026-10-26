# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .model_cost import ModelCost
from .provider_id import ProviderID
from .model_variant import ModelVariant
from .model_settings import ModelSettings
from .model_capabilities import ModelCapabilities
from .model_compatibility import ModelCompatibility

__all__ = ["ModelInfo", "Limit", "Time"]


class Limit(BaseModel):
    context: int

    output: int

    input: Optional[int] = None

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


class Time(BaseModel):
    released: float

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


class ModelInfo(BaseModel):
    id: str

    capabilities: ModelCapabilities

    cost: List[ModelCost]

    enabled: bool

    limit: Limit

    api_model_id: str = FieldInfo(alias="modelID")

    name: str

    provider_id: ProviderID = FieldInfo(alias="providerID")

    status: Literal["alpha", "beta", "deprecated", "active"]

    time: Time

    variants: List[ModelVariant]

    body: Optional[Dict[str, object]] = None

    canonical: Optional[ProviderID] = None

    compatibility: Optional[ModelCompatibility] = None

    family: Optional[str] = None

    headers: Optional[Dict[str, str]] = None

    package: Optional[str] = None

    settings: Optional[ModelSettings] = None

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
