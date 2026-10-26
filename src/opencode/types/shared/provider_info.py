# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .provider_id import ProviderID
from .integration_id import IntegrationID
from .provider_settings import ProviderSettings
from .provider_compatibility import ProviderCompatibility

__all__ = ["ProviderInfo"]


class ProviderInfo(BaseModel):
    id: ProviderID

    activation: Literal["auto", "enabled", "disabled"]

    name: str

    package: str

    body: Optional[Dict[str, object]] = None

    canonical: Optional[ProviderID] = None

    compatibility: Optional[ProviderCompatibility] = None

    headers: Optional[Dict[str, str]] = None

    integration_id: Optional[IntegrationID] = FieldInfo(alias="integrationID", default=None)

    settings: Optional[ProviderSettings] = None

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
