# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.migration import V1StatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_status(self, client: Opencode) -> None:
        v1 = client.migration.v1.status()
        assert_matches_type(V1StatusResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Opencode) -> None:
        response = client.migration.v1.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1StatusResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Opencode) -> None:
        with client.migration.v1.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1StatusResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_status(self, async_client: AsyncOpencode) -> None:
        v1 = await async_client.migration.v1.status()
        assert_matches_type(V1StatusResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncOpencode) -> None:
        response = await async_client.migration.v1.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1StatusResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncOpencode) -> None:
        async with async_client.migration.v1.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1StatusResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
