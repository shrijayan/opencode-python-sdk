# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .provider_encoding import ProviderEncoding
from .provider_transport import ProviderTransport
from .provider_compaction import ProviderCompaction

__all__ = ["ProviderSettings"]


class ProviderSettings(BaseModel):
    chunk_timeout: Union[Literal[False], float, None] = FieldInfo(alias="chunkTimeout", default=None)

    compaction: Optional[ProviderCompaction] = None

    encoding: Optional[ProviderEncoding] = None

    header_timeout: Union[Literal[False], float, None] = FieldInfo(alias="headerTimeout", default=None)

    timeout: Union[Literal[False], float, None] = None

    transport: Optional[ProviderTransport] = None

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
