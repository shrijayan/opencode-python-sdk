# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWellknown:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add(self, client: Opencode) -> None:
        wellknown = client.integration.wellknown.add(
            url="url",
        )
        assert wellknown is None

    @parametrize
    def test_method_add_with_all_params(self, client: Opencode) -> None:
        wellknown = client.integration.wellknown.add(
            url="url",
            location={
                "directory": "string",
            },
        )
        assert wellknown is None

    @parametrize
    def test_raw_response_add(self, client: Opencode) -> None:
        response = client.integration.wellknown.with_raw_response.add(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wellknown = response.parse()
        assert wellknown is None

    @parametrize
    def test_streaming_response_add(self, client: Opencode) -> None:
        with client.integration.wellknown.with_streaming_response.add(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wellknown = response.parse()
            assert wellknown is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWellknown:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add(self, async_client: AsyncOpencode) -> None:
        wellknown = await async_client.integration.wellknown.add(
            url="url",
        )
        assert wellknown is None

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncOpencode) -> None:
        wellknown = await async_client.integration.wellknown.add(
            url="url",
            location={
                "directory": "string",
            },
        )
        assert wellknown is None

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.wellknown.with_raw_response.add(
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wellknown = await response.parse()
        assert wellknown is None

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.wellknown.with_streaming_response.add(
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wellknown = await response.parse()
            assert wellknown is None

        assert cast(Any, response.is_closed) is True
