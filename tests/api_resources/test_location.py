# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.shared import LocationPublicInfo

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Opencode) -> None:
        location = client.location.get()
        assert_matches_type(LocationPublicInfo, location, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Opencode) -> None:
        location = client.location.get(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(LocationPublicInfo, location, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Opencode) -> None:
        response = client.location.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationPublicInfo, location, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Opencode) -> None:
        with client.location.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationPublicInfo, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reload(self, client: Opencode) -> None:
        location = client.location.reload()
        assert location is None

    @parametrize
    def test_raw_response_reload(self, client: Opencode) -> None:
        response = client.location.with_raw_response.reload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert location is None

    @parametrize
    def test_streaming_response_reload(self, client: Opencode) -> None:
        with client.location.with_streaming_response.reload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert location is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLocation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get(self, async_client: AsyncOpencode) -> None:
        location = await async_client.location.get()
        assert_matches_type(LocationPublicInfo, location, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncOpencode) -> None:
        location = await async_client.location.get(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(LocationPublicInfo, location, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOpencode) -> None:
        response = await async_client.location.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationPublicInfo, location, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOpencode) -> None:
        async with async_client.location.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationPublicInfo, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reload(self, async_client: AsyncOpencode) -> None:
        location = await async_client.location.reload()
        assert location is None

    @parametrize
    async def test_raw_response_reload(self, async_client: AsyncOpencode) -> None:
        response = await async_client.location.with_raw_response.reload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert location is None

    @parametrize
    async def test_streaming_response_reload(self, async_client: AsyncOpencode) -> None:
        async with async_client.location.with_streaming_response.reload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert location is None

        assert cast(Any, response.is_closed) is True
