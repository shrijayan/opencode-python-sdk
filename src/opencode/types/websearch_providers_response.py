# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.location_public_ref import LocationPublicRef
from .shared.web_search_provider import WebSearchProvider

__all__ = ["WebsearchProvidersResponse"]


class WebsearchProvidersResponse(BaseModel):
    data: List[WebSearchProvider]

    location: LocationPublicRef

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
