# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from .form_id import FormID
from ..._models import BaseModel
from .form_state import FormState
from .form_fields import FormFields
from .form_metadata import FormMetadata

__all__ = ["FormDetail"]


class FormDetail(BaseModel):
    id: FormID

    fields: FormFields

    session_id: str = FieldInfo(alias="sessionID")

    state: FormState

    title: str

    metadata: Optional[FormMetadata] = None

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
