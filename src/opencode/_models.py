"""Base model for every OpenCode API type."""

from __future__ import annotations

from typing import Any, ClassVar

import pydantic
from pydantic import ConfigDict
from typing_extensions import override

__all__ = ["BaseModel", "is_none"]


def is_none(value: object) -> bool:
    """Field ``exclude_if`` predicate: optional fields that are not nullable are left out instead of sent as null."""
    return value is None


class BaseModel(pydantic.BaseModel):
    """Base class for OpenCode API models.

    Attributes use ``snake_case`` while the wire format uses OpenCode's ``camelCase`` names. Models accept either
    spelling on input and always serialize to the wire names.

    Unknown fields are kept rather than rejected, so a client keeps working against a newer server. They are
    available through ``model_extra`` and attribute access.
    """

    model_config = ConfigDict(
        extra="allow",
        validate_by_name=True,
        validate_by_alias=True,
        serialize_by_alias=True,
        defer_build=True,
        protected_namespaces=(),
        use_enum_values=True,
        coerce_numbers_to_str=False,
    )

    __opencode_always_set__: ClassVar[tuple[str, ...]] = ()
    """Fields serialized even when left at their default, such as a union member's ``type`` tag."""

    @override
    def model_post_init(self, context: Any, /) -> None:
        if self.__opencode_always_set__:
            self.__pydantic_fields_set__.update(self.__opencode_always_set__)

    def to_dict(self, *, exclude_unset: bool = True) -> dict[str, Any]:
        """Returns the model as a JSON-compatible dict using wire field names."""
        return self.model_dump(mode="json", by_alias=True, exclude_unset=exclude_unset)

    def to_json(self, *, indent: int | None = None, exclude_unset: bool = True) -> str:
        """Returns the model as JSON text using wire field names."""
        return self.model_dump_json(by_alias=True, exclude_unset=exclude_unset, indent=indent)
