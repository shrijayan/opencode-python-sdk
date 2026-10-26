# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.form_answer import FormAnswer

__all__ = ["FormReplyParams"]


class FormReplyParams(TypedDict, total=False):
    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    answer: Required[FormAnswer]
