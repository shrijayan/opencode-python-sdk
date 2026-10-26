# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .provider_id import ProviderID
from .config_model import ConfigModel
from .provider_compatibility import ProviderCompatibility
from .config_provider_settings import ConfigProviderSettings

__all__ = ["ConfigProvider"]


class ConfigProvider(BaseModel):
    body: Optional[Dict[str, object]] = None

    canonical: Optional[ProviderID] = None

    compatibility: Optional[ProviderCompatibility] = None

    env: Optional[List[str]] = None

    headers: Optional[Dict[str, str]] = None

    models: Optional[Dict[str, ConfigModel]] = None

    name: Optional[str] = None

    package: Optional[str] = None

    settings: Optional[ConfigProviderSettings] = None

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
