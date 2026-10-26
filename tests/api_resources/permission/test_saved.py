# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.shared import PermissionSavedInfo
from opencode.types.permission import SavedListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSaved:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        saved = client.permission.saved.update(
            id={},
        )
        assert_matches_type(PermissionSavedInfo, saved, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Opencode) -> None:
        saved = client.permission.saved.update(
            id={},
            action="action",
            resource="resource",
        )
        assert_matches_type(PermissionSavedInfo, saved, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.permission.saved.with_raw_response.update(
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved = response.parse()
        assert_matches_type(PermissionSavedInfo, saved, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.permission.saved.with_streaming_response.update(
            id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved = response.parse()
            assert_matches_type(PermissionSavedInfo, saved, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.permission.saved.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        saved = client.permission.saved.list()
        assert_matches_type(SavedListResponse, saved, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        saved = client.permission.saved.list(
            project_id={},
        )
        assert_matches_type(SavedListResponse, saved, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.permission.saved.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved = response.parse()
        assert_matches_type(SavedListResponse, saved, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.permission.saved.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved = response.parse()
            assert_matches_type(SavedListResponse, saved, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove(self, client: Opencode) -> None:
        saved = client.permission.saved.remove(
            {},
        )
        assert saved is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.permission.saved.with_raw_response.remove(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved = response.parse()
        assert saved is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.permission.saved.with_streaming_response.remove(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved = response.parse()
            assert saved is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.permission.saved.with_raw_response.remove(
                "",
            )


class TestAsyncSaved:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        saved = await async_client.permission.saved.update(
            id={},
        )
        assert_matches_type(PermissionSavedInfo, saved, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencode) -> None:
        saved = await async_client.permission.saved.update(
            id={},
            action="action",
            resource="resource",
        )
        assert_matches_type(PermissionSavedInfo, saved, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.permission.saved.with_raw_response.update(
            id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved = await response.parse()
        assert_matches_type(PermissionSavedInfo, saved, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.permission.saved.with_streaming_response.update(
            id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved = await response.parse()
            assert_matches_type(PermissionSavedInfo, saved, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.permission.saved.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        saved = await async_client.permission.saved.list()
        assert_matches_type(SavedListResponse, saved, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        saved = await async_client.permission.saved.list(
            project_id={},
        )
        assert_matches_type(SavedListResponse, saved, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.permission.saved.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved = await response.parse()
        assert_matches_type(SavedListResponse, saved, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.permission.saved.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved = await response.parse()
            assert_matches_type(SavedListResponse, saved, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencode) -> None:
        saved = await async_client.permission.saved.remove(
            {},
        )
        assert saved is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.permission.saved.with_raw_response.remove(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved = await response.parse()
        assert saved is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.permission.saved.with_streaming_response.remove(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved = await response.parse()
            assert saved is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.permission.saved.with_raw_response.remove(
                "",
            )
