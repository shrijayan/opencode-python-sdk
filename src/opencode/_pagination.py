"""Cursor pagination.

OpenCode list endpoints return ``{"data": [...], "cursor": {"previous": ..., "next": ...}}``. A page iterates over
every item of every following page, fetching lazily::

    for message in client.message.list("ses_..."):
        ...

Use :meth:`SyncCursorPage.iter_pages` or the cursor properties for manual control.
"""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING, Any, Generic, TypeVar

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Generator, Iterator

    from ._base_client import AsyncAPIClient, RequestOptions, SyncAPIClient

__all__ = ["AsyncCursorPage", "AsyncPaginator", "SyncCursorPage"]

_T = TypeVar("_T")


def _page_parts(payload: Any) -> tuple[list[Any], str | None, str | None]:
    cursor = payload.cursor
    return list(payload.data), getattr(cursor, "next", None), getattr(cursor, "previous", None)


def _follow(options: RequestOptions, cursor: str) -> RequestOptions:
    query = {key: value for key, value in options.query.items() if key != "order"}
    # The server rejects `order` together with a cursor: the cursor already encodes the direction.
    query["cursor"] = cursor
    return dataclasses.replace(options, query=query)


class _PageBase(Generic[_T]):
    data: list[_T]
    """Items on this page."""
    next_cursor: str | None
    """Cursor for the following page, or ``None`` on the last page."""
    previous_cursor: str | None
    """Cursor for the preceding page, or ``None`` on the first page."""

    def __init__(
        self, *, data: list[_T], next_cursor: str | None, previous_cursor: str | None, options: RequestOptions
    ) -> None:
        self.data = data
        self.next_cursor = next_cursor
        self.previous_cursor = previous_cursor
        self._options = options

    def has_next_page(self) -> bool:
        return bool(self.next_cursor)

    def __len__(self) -> int:
        return len(self.data)


class SyncCursorPage(_PageBase[_T]):
    """One page of results. Iterating it walks this page and every page after it."""

    def __init__(
        self,
        *,
        client: SyncAPIClient,
        data: list[_T],
        next_cursor: str | None,
        previous_cursor: str | None,
        options: RequestOptions,
        response_type: Any,
    ) -> None:
        super().__init__(data=data, next_cursor=next_cursor, previous_cursor=previous_cursor, options=options)
        self._client = client
        self._response_type = response_type

    @classmethod
    def fetch(cls, client: SyncAPIClient, options: RequestOptions, response_type: Any) -> SyncCursorPage[Any]:
        payload = client.request(options, response_type=response_type)
        return cls.build(client, options, response_type, payload)

    @classmethod
    def build(
        cls, client: SyncAPIClient, options: RequestOptions, response_type: Any, payload: Any
    ) -> SyncCursorPage[Any]:
        """Builds a page from an already parsed response."""
        data, next_cursor, previous_cursor = _page_parts(payload)
        return cls(
            client=client,
            data=data,
            next_cursor=next_cursor,
            previous_cursor=previous_cursor,
            options=options,
            response_type=response_type,
        )

    def next_page(self) -> SyncCursorPage[_T]:
        """Fetches the following page. Raises ``StopIteration`` on the last page."""
        if not self.next_cursor:
            raise StopIteration("No more pages")
        return SyncCursorPage.fetch(self._client, _follow(self._options, self.next_cursor), self._response_type)

    def previous_page(self) -> SyncCursorPage[_T]:
        """Fetches the preceding page. Raises ``StopIteration`` on the first page."""
        if not self.previous_cursor:
            raise StopIteration("No previous page")
        return SyncCursorPage.fetch(self._client, _follow(self._options, self.previous_cursor), self._response_type)

    def iter_pages(self) -> Generator[SyncCursorPage[_T], None, None]:
        """Yields this page and then each following page."""
        page: SyncCursorPage[_T] = self
        yield page
        while page.has_next_page():
            page = page.next_page()
            yield page

    def __iter__(self) -> Iterator[_T]:
        for page in self.iter_pages():
            yield from page.data


class AsyncCursorPage(_PageBase[_T]):
    """One page of results. ``async for`` walks this page and every page after it."""

    def __init__(
        self,
        *,
        client: AsyncAPIClient,
        data: list[_T],
        next_cursor: str | None,
        previous_cursor: str | None,
        options: RequestOptions,
        response_type: Any,
    ) -> None:
        super().__init__(data=data, next_cursor=next_cursor, previous_cursor=previous_cursor, options=options)
        self._client = client
        self._response_type = response_type

    @classmethod
    async def fetch(cls, client: AsyncAPIClient, options: RequestOptions, response_type: Any) -> AsyncCursorPage[Any]:
        payload = await client.request(options, response_type=response_type)
        return cls.build(client, options, response_type, payload)

    @classmethod
    def build(
        cls, client: AsyncAPIClient, options: RequestOptions, response_type: Any, payload: Any
    ) -> AsyncCursorPage[Any]:
        """Builds a page from an already parsed response."""
        data, next_cursor, previous_cursor = _page_parts(payload)
        return cls(
            client=client,
            data=data,
            next_cursor=next_cursor,
            previous_cursor=previous_cursor,
            options=options,
            response_type=response_type,
        )

    async def next_page(self) -> AsyncCursorPage[_T]:
        """Fetches the following page. Raises ``StopAsyncIteration`` on the last page."""
        if not self.next_cursor:
            raise StopAsyncIteration("No more pages")
        return await AsyncCursorPage.fetch(self._client, _follow(self._options, self.next_cursor), self._response_type)

    async def previous_page(self) -> AsyncCursorPage[_T]:
        """Fetches the preceding page. Raises ``StopAsyncIteration`` on the first page."""
        if not self.previous_cursor:
            raise StopAsyncIteration("No previous page")
        return await AsyncCursorPage.fetch(
            self._client, _follow(self._options, self.previous_cursor), self._response_type
        )

    async def iter_pages(self) -> AsyncIterator[AsyncCursorPage[_T]]:
        """Yields this page and then each following page."""
        page: AsyncCursorPage[_T] = self
        yield page
        while page.has_next_page():
            page = await page.next_page()
            yield page

    async def __aiter__(self) -> AsyncIterator[_T]:
        async for page in self.iter_pages():
            for item in page.data:
                yield item


class AsyncPaginator(Generic[_T]):
    """Returned by async list methods.

    ``await`` it for the first page, or ``async for`` over it to walk every item across pages.
    """

    def __init__(self, client: AsyncAPIClient, options: RequestOptions, response_type: Any) -> None:
        self._client = client
        self._options = options
        self._response_type = response_type

    def __await__(self) -> Generator[Any, None, AsyncCursorPage[_T]]:
        return AsyncCursorPage.fetch(self._client, self._options, self._response_type).__await__()

    async def __aiter__(self) -> AsyncIterator[_T]:
        page: AsyncCursorPage[_T] = await self
        async for item in page:
            yield item
