# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["CursorPageCursor", "SyncCursorPage", "AsyncCursorPage"]

_T = TypeVar("_T")


class CursorPageCursor(BaseModel):
    next: Optional[str] = None


class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    cursor: Optional[CursorPageCursor] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next = None
        if self.cursor is not None:
            if self.cursor.next is not None:
                next = self.cursor.next
        if not next:
            return None

        return PageInfo(params={"cursor": next})


class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    cursor: Optional[CursorPageCursor] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next = None
        if self.cursor is not None:
            if self.cursor.next is not None:
                next = self.cursor.next
        if not next:
            return None

        return PageInfo(params={"cursor": next})
