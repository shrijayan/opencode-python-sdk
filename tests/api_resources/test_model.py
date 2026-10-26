# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import ModelListResponse, ModelDefaultResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModel:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        model = client.model.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Opencode) -> None:
        model = client.model.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.model.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.model.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_default(self, client: Opencode) -> None:
        model = client.model.default()
        assert_matches_type(ModelDefaultResponse, model, path=["response"])

    @parametrize
    def test_method_default_with_all_params(self, client: Opencode) -> None:
        model = client.model.default(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ModelDefaultResponse, model, path=["response"])

    @parametrize
    def test_raw_response_default(self, client: Opencode) -> None:
        response = client.model.with_raw_response.default()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelDefaultResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_default(self, client: Opencode) -> None:
        with client.model.with_streaming_response.default() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelDefaultResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModel:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        model = await async_client.model.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencode) -> None:
        model = await async_client.model.list(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.model.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.model.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_default(self, async_client: AsyncOpencode) -> None:
        model = await async_client.model.default()
        assert_matches_type(ModelDefaultResponse, model, path=["response"])

    @parametrize
    async def test_method_default_with_all_params(self, async_client: AsyncOpencode) -> None:
        model = await async_client.model.default(
            location={
                "directory": "string",
            },
        )
        assert_matches_type(ModelDefaultResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_default(self, async_client: AsyncOpencode) -> None:
        response = await async_client.model.with_raw_response.default()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelDefaultResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_default(self, async_client: AsyncOpencode) -> None:
        async with async_client.model.with_streaming_response.default() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelDefaultResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True
