# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..shared_params.form_id import FormID
from ..shared_params.form_fields import FormFields
from ..shared_params.form_metadata import FormMetadata

__all__ = ["FormCreateParams"]


class FormCreateParams(TypedDict, total=False):
    fields: Required[FormFields]

    title: Required[str]

    id: Optional[FormID]

    metadata: FormMetadata
