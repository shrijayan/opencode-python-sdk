# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import PermissionListResponse, PermissionCreateResponse
from opencode.types.shared import PermissionRequest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPermission:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        permission = client.permission.create(
            session_id="sessionID",
            action="action",
            resources=["string"],
        )
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        permission = client.permission.create(
            session_id="sessionID",
            action="action",
            resources=["string"],
            agent="agent",
            id="id",
            metadata={"foo": {}},
            save=["string"],
            source={
                "id": "string",
                "message_id": "string",
                "type": "tool",
            },
        )
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.permission.with_raw_response.create(
            session_id="sessionID",
            action="action",
            resources=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.permission.with_streaming_response.create(
            session_id="sessionID",
            action="action",
            resources=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionCreateResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.permission.with_raw_response.create(
                session_id="",
                action="action",
                resources=["string"],
            )

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        permission = client.permission.list(
            "sessionID",
        )
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.permission.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.permission.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionListResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.permission.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        permission = client.permission.get(
            request_id="requestID",
            session_id="sessionID",
        )
        assert_matches_type(PermissionRequest, permission, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.permission.with_raw_response.get(
            request_id="requestID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionRequest, permission, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.permission.with_streaming_response.get(
            request_id="requestID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionRequest, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.permission.with_raw_response.get(
                request_id="requestID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.permission.with_raw_response.get(
                request_id="",
                session_id="sessionID",
            )

    @parametrize
    def test_method_reply(self, client: Opencode) -> None:
        permission = client.permission.reply(
            request_id="requestID",
            session_id="sessionID",
            decision="once",
        )
        assert permission is None

    @parametrize
    def test_method_reply_with_all_params(self, client: Opencode) -> None:
        permission = client.permission.reply(
            request_id="requestID",
            session_id="sessionID",
            decision="once",
            message="message",
        )
        assert permission is None

    @parametrize
    def test_raw_response_reply(self, client: Opencode) -> None:
        response = client.permission.with_raw_response.reply(
            request_id="requestID",
            session_id="sessionID",
            decision="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert permission is None

    @parametrize
    def test_streaming_response_reply(self, client: Opencode) -> None:
        with client.permission.with_streaming_response.reply(
            request_id="requestID",
            session_id="sessionID",
            decision="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert permission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reply(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.permission.with_raw_response.reply(
                request_id="requestID",
                session_id="",
                decision="once",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.permission.with_raw_response.reply(
                request_id="",
                session_id="sessionID",
                decision="once",
            )


class TestAsyncPermission:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        permission = await async_client.permission.create(
            session_id="sessionID",
            action="action",
            resources=["string"],
        )
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        permission = await async_client.permission.create(
            session_id="sessionID",
            action="action",
            resources=["string"],
            agent="agent",
            id="id",
            metadata={"foo": {}},
            save=["string"],
            source={
                "id": "string",
                "message_id": "string",
                "type": "tool",
            },
        )
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.permission.with_raw_response.create(
            session_id="sessionID",
            action="action",
            resources=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionCreateResponse, permission, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.permission.with_streaming_response.create(
            session_id="sessionID",
            action="action",
            resources=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionCreateResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.permission.with_raw_response.create(
                session_id="",
                action="action",
                resources=["string"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        permission = await async_client.permission.list(
            "sessionID",
        )
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.permission.with_raw_response.list(
            "sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionListResponse, permission, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.permission.with_streaming_response.list(
            "sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionListResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.permission.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        permission = await async_client.permission.get(
            request_id="requestID",
            session_id="sessionID",
        )
        assert_matches_type(PermissionRequest, permission, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.permission.with_raw_response.get(
            request_id="requestID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionRequest, permission, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.permission.with_streaming_response.get(
            request_id="requestID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionRequest, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.permission.with_raw_response.get(
                request_id="requestID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.permission.with_raw_response.get(
                request_id="",
                session_id="sessionID",
            )

    @parametrize
    async def test_method_reply(self, async_client: AsyncOpencode) -> None:
        permission = await async_client.permission.reply(
            request_id="requestID",
            session_id="sessionID",
            decision="once",
        )
        assert permission is None

    @parametrize
    async def test_method_reply_with_all_params(self, async_client: AsyncOpencode) -> None:
        permission = await async_client.permission.reply(
            request_id="requestID",
            session_id="sessionID",
            decision="once",
            message="message",
        )
        assert permission is None

    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncOpencode) -> None:
        response = await async_client.permission.with_raw_response.reply(
            request_id="requestID",
            session_id="sessionID",
            decision="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert permission is None

    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncOpencode) -> None:
        async with async_client.permission.with_streaming_response.reply(
            request_id="requestID",
            session_id="sessionID",
            decision="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert permission is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reply(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.permission.with_raw_response.reply(
                request_id="requestID",
                session_id="",
                decision="once",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.permission.with_raw_response.reply(
                request_id="",
                session_id="sessionID",
                decision="once",
            )
