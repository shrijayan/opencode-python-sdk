from __future__ import annotations

import pytest
import respx

from opencode import AsyncOpencode, Opencode


def _page(ids: list[str], next_cursor: str | None) -> dict[str, object]:
    return {
        "data": [{"type": "user", "id": item, "time": {"created": 1}, "text": item} for item in ids],
        "cursor": {"previous": None, "next": next_cursor},
    }


def test_iterates_across_pages_and_drops_order(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/session/ses_1/message").mock(
        side_effect=[
            respx.MockResponse(json=_page(["a", "b"], "c1")),
            respx.MockResponse(json=_page(["c"], None)),
        ]
    )
    page = client.message.list("ses_1", order="desc", limit=2)
    assert [message.id for message in page] == ["a", "b", "c"]
    first, second = route.calls[0].request.url.params, route.calls[1].request.url.params
    assert first["order"] == "desc"
    assert "order" not in second
    assert second["cursor"] == "c1"
    assert second["limit"] == "2"


def test_manual_page_control(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1/message").mock(
        side_effect=[respx.MockResponse(json=_page(["a"], "c1")), respx.MockResponse(json=_page(["b"], None))]
    )
    page = client.message.list("ses_1")
    assert page.has_next_page()
    following = page.get_next_page()
    assert [message.id for message in following.data] == ["b"]
    assert not following.has_next_page()
    with pytest.raises(RuntimeError):
        following.get_next_page()


@pytest.mark.anyio
async def test_async_paginator(async_client: AsyncOpencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1/message").mock(
        side_effect=[
            respx.MockResponse(json=_page(["a"], "c1")),
            respx.MockResponse(json=_page(["b"], None)),
            respx.MockResponse(json=_page(["a"], "c1")),
        ]
    )
    ids = [message.id async for message in async_client.message.list("ses_1")]
    assert ids == ["a", "b"]
    first = await async_client.message.list("ses_1")
    assert first.cursor is not None
    assert first.cursor.next == "c1"
