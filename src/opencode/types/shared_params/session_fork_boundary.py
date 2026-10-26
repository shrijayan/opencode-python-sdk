# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .session_message_id import SessionMessageID

__all__ = ["SessionForkBoundary", "SessionForkBoundaryVariant0", "SessionForkBoundaryVariant1"]


class SessionForkBoundaryVariant0(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    message_id: Required[Annotated[SessionMessageID, PropertyInfo(alias="messageID")]]

    type: Required[Literal["before"]]


class SessionForkBoundaryVariant1(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    message_id: Required[Annotated[SessionMessageID, PropertyInfo(alias="messageID")]]

    type: Required[Literal["through"]]


SessionForkBoundary: TypeAlias = Union[SessionForkBoundaryVariant0, SessionForkBoundaryVariant1]
