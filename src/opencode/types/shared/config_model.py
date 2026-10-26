# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .config_model_cost import ConfigModelCost
from .model_compatibility import ModelCompatibility
from .config_model_settings import ConfigModelSettings
from .config_model_capabilities import ConfigModelCapabilities

__all__ = ["ConfigModel", "Cost", "Limit", "Variant"]

Cost: TypeAlias = Union[ConfigModelCost, List[ConfigModelCost]]


class Limit(BaseModel):
    context: Optional[int] = None

    input: Optional[int] = None

    output: Optional[int] = None

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


class Variant(BaseModel):
    id: str

    body: Optional[Dict[str, object]] = None

    headers: Optional[Dict[str, str]] = None

    settings: Optional[ConfigModelSettings] = None

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


class ConfigModel(BaseModel):
    body: Optional[Dict[str, object]] = None

    capabilities: Optional[ConfigModelCapabilities] = None

    compatibility: Optional[ModelCompatibility] = None

    cost: Optional[Cost] = None

    disabled: Optional[bool] = None

    family: Optional[str] = None

    headers: Optional[Dict[str, str]] = None

    limit: Optional[Limit] = None

    api_model_id: Optional[str] = FieldInfo(alias="modelID", default=None)

    name: Optional[str] = None

    package: Optional[str] = None

    release_date: Optional[str] = FieldInfo(alias="releaseDate", default=None)
    """Release date as YYYY-MM-DD or YYYY-MM"""

    settings: Optional[ConfigModelSettings] = None

    variants: Optional[List[Variant]] = None

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
