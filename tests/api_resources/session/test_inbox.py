# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.session import InboxListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        inbox = client.session.inbox.update(
            inbox_id="inboxID",
            session_id="sessionID",
            delivery="steer",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.session.inbox.with_raw_response.update(
            inbox_id="inboxID",
            session_id="sessionID",
            delivery="steer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.session.inbox.with_streaming_response.update(
            inbox_id="inboxID",
            session_id="sessionID",
            delivery="steer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.inbox.with_raw_response.update(
                inbox_id="inboxID",
                session_id="",
                delivery="steer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.session.inbox.with_raw_response.update(
                inbox_id="",
                session_id="sessionID",
                delivery="steer",
            )

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        inbox = client.session.inbox.list(
            "sessionID",
        )
        assert_matches_type(InboxListResponse, inbox, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.session.inbox.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert_matches_type(InboxListResponse, inbox, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.session.inbox.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert_matches_type(InboxListResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.inbox.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: Opencode) -> None:
        inbox = client.session.inbox.cancel(
            inbox_id="inboxID",
            session_id="sessionID",
        )
        assert inbox is None

    @parametrize
    def test_raw_response_cancel(self, client: Opencode) -> None:
        response = client.session.inbox.with_raw_response.cancel(
            inbox_id="inboxID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = response.parse()
        assert inbox is None

    @parametrize
    def test_streaming_response_cancel(self, client: Opencode) -> None:
        with client.session.inbox.with_streaming_response.cancel(
            inbox_id="inboxID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.inbox.with_raw_response.cancel(
                inbox_id="inboxID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            client.session.inbox.with_raw_response.cancel(
                inbox_id="",
                session_id="sessionID",
            )


class TestAsyncInbox:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        inbox = await async_client.session.inbox.update(
            inbox_id="inboxID",
            session_id="sessionID",
            delivery="steer",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.inbox.with_raw_response.update(
            inbox_id="inboxID",
            session_id="sessionID",
            delivery="steer",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.inbox.with_streaming_response.update(
            inbox_id="inboxID",
            session_id="sessionID",
            delivery="steer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.inbox.with_raw_response.update(
                inbox_id="inboxID",
                session_id="",
                delivery="steer",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.session.inbox.with_raw_response.update(
                inbox_id="",
                session_id="sessionID",
                delivery="steer",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        inbox = await async_client.session.inbox.list(
            "sessionID",
        )
        assert_matches_type(InboxListResponse, inbox, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.inbox.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert_matches_type(InboxListResponse, inbox, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.inbox.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert_matches_type(InboxListResponse, inbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.inbox.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpencode) -> None:
        inbox = await async_client.session.inbox.cancel(
            inbox_id="inboxID",
            session_id="sessionID",
        )
        assert inbox is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.inbox.with_raw_response.cancel(
            inbox_id="inboxID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbox = await response.parse()
        assert inbox is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.inbox.with_streaming_response.cancel(
            inbox_id="inboxID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbox = await response.parse()
            assert inbox is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.inbox.with_raw_response.cancel(
                inbox_id="inboxID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `inbox_id` but received ''"):
            await async_client.session.inbox.with_raw_response.cancel(
                inbox_id="",
                session_id="sessionID",
            )
