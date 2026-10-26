# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.shared import GenerateTextResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_text(self, client: Opencode) -> None:
        generate = client.generate.text(
            prompt="prompt",
        )
        assert_matches_type(GenerateTextResponse, generate, path=["response"])

    @parametrize
    def test_method_text_with_all_params(self, client: Opencode) -> None:
        generate = client.generate.text(
            prompt="prompt",
            model={},
        )
        assert_matches_type(GenerateTextResponse, generate, path=["response"])

    @parametrize
    def test_raw_response_text(self, client: Opencode) -> None:
        response = client.generate.with_raw_response.text(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateTextResponse, generate, path=["response"])

    @parametrize
    def test_streaming_response_text(self, client: Opencode) -> None:
        with client.generate.with_streaming_response.text(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateTextResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_text(self, async_client: AsyncOpencode) -> None:
        generate = await async_client.generate.text(
            prompt="prompt",
        )
        assert_matches_type(GenerateTextResponse, generate, path=["response"])

    @parametrize
    async def test_method_text_with_all_params(self, async_client: AsyncOpencode) -> None:
        generate = await async_client.generate.text(
            prompt="prompt",
            model={},
        )
        assert_matches_type(GenerateTextResponse, generate, path=["response"])

    @parametrize
    async def test_raw_response_text(self, async_client: AsyncOpencode) -> None:
        response = await async_client.generate.with_raw_response.text(
            prompt="prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateTextResponse, generate, path=["response"])

    @parametrize
    async def test_streaming_response_text(self, async_client: AsyncOpencode) -> None:
        async with async_client.generate.with_streaming_response.text(
            prompt="prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateTextResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True
