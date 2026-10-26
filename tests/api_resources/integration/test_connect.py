# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnect:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_external(self, client: Opencode) -> None:
        connect = client.integration.connect.external(
            integration_id="integrationID",
            method_id="methodID",
        )
        assert connect is None

    @parametrize
    def test_method_external_with_all_params(self, client: Opencode) -> None:
        connect = client.integration.connect.external(
            integration_id="integrationID",
            method_id="methodID",
            answer={},
            label="label",
            location={
                "directory": "string",
            },
        )
        assert connect is None

    @parametrize
    def test_raw_response_external(self, client: Opencode) -> None:
        response = client.integration.connect.with_raw_response.external(
            integration_id="integrationID",
            method_id="methodID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert connect is None

    @parametrize
    def test_streaming_response_external(self, client: Opencode) -> None:
        with client.integration.connect.with_streaming_response.external(
            integration_id="integrationID",
            method_id="methodID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert connect is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_external(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.connect.with_raw_response.external(
                integration_id="",
                method_id="methodID",
            )

    @parametrize
    def test_method_key(self, client: Opencode) -> None:
        connect = client.integration.connect.key(
            integration_id="integrationID",
            key="key",
        )
        assert connect is None

    @parametrize
    def test_method_key_with_all_params(self, client: Opencode) -> None:
        connect = client.integration.connect.key(
            integration_id="integrationID",
            key="key",
            answer={},
            label="label",
            location={
                "directory": "string",
            },
        )
        assert connect is None

    @parametrize
    def test_raw_response_key(self, client: Opencode) -> None:
        response = client.integration.connect.with_raw_response.key(
            integration_id="integrationID",
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = response.parse()
        assert connect is None

    @parametrize
    def test_streaming_response_key(self, client: Opencode) -> None:
        with client.integration.connect.with_streaming_response.key(
            integration_id="integrationID",
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = response.parse()
            assert connect is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_key(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.connect.with_raw_response.key(
                integration_id="",
                key="key",
            )


class TestAsyncConnect:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_external(self, async_client: AsyncOpencode) -> None:
        connect = await async_client.integration.connect.external(
            integration_id="integrationID",
            method_id="methodID",
        )
        assert connect is None

    @parametrize
    async def test_method_external_with_all_params(self, async_client: AsyncOpencode) -> None:
        connect = await async_client.integration.connect.external(
            integration_id="integrationID",
            method_id="methodID",
            answer={},
            label="label",
            location={
                "directory": "string",
            },
        )
        assert connect is None

    @parametrize
    async def test_raw_response_external(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.connect.with_raw_response.external(
            integration_id="integrationID",
            method_id="methodID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert connect is None

    @parametrize
    async def test_streaming_response_external(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.connect.with_streaming_response.external(
            integration_id="integrationID",
            method_id="methodID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert connect is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_external(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.connect.with_raw_response.external(
                integration_id="",
                method_id="methodID",
            )

    @parametrize
    async def test_method_key(self, async_client: AsyncOpencode) -> None:
        connect = await async_client.integration.connect.key(
            integration_id="integrationID",
            key="key",
        )
        assert connect is None

    @parametrize
    async def test_method_key_with_all_params(self, async_client: AsyncOpencode) -> None:
        connect = await async_client.integration.connect.key(
            integration_id="integrationID",
            key="key",
            answer={},
            label="label",
            location={
                "directory": "string",
            },
        )
        assert connect is None

    @parametrize
    async def test_raw_response_key(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.connect.with_raw_response.key(
            integration_id="integrationID",
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connect = await response.parse()
        assert connect is None

    @parametrize
    async def test_streaming_response_key(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.connect.with_streaming_response.key(
            integration_id="integrationID",
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connect = await response.parse()
            assert connect is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_key(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.connect.with_raw_response.key(
                integration_id="",
                key="key",
            )
