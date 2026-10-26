# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .form_when import FormWhen
from .form_option import FormOption

__all__ = ["FormStringField"]


class FormStringField(BaseModel):
    key: str

    type: Literal["string"]

    custom: Optional[bool] = None

    default: Optional[str] = None

    description: Optional[str] = None

    format: Optional[Literal["email", "uri", "date", "date-time"]] = None

    hidden: Optional[bool] = None

    max_length: Optional[int] = FieldInfo(alias="maxLength", default=None)

    min_length: Optional[int] = FieldInfo(alias="minLength", default=None)

    options: Optional[List[FormOption]] = None

    pattern: Optional[str] = None

    placeholder: Optional[str] = None

    required: Optional[bool] = None

    title: Optional[str] = None

    when: Optional[List[FormWhen]] = None

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
