# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.integration import CommandStatusResponse, CommandConnectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cancel(self, client: Opencode) -> None:
        command = client.integration.command.cancel(
            attempt_id="attemptID",
            integration_id="integrationID",
        )
        assert command is None

    @parametrize
    def test_method_cancel_with_all_params(self, client: Opencode) -> None:
        command = client.integration.command.cancel(
            attempt_id="attemptID",
            integration_id="integrationID",
            location={
                "directory": "string",
            },
        )
        assert command is None

    @parametrize
    def test_raw_response_cancel(self, client: Opencode) -> None:
        response = client.integration.command.with_raw_response.cancel(
            attempt_id="attemptID",
            integration_id="integrationID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert command is None

    @parametrize
    def test_streaming_response_cancel(self, client: Opencode) -> None:
        with client.integration.command.with_streaming_response.cancel(
            attempt_id="attemptID",
            integration_id="integrationID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert command is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.command.with_raw_response.cancel(
                attempt_id="attemptID",
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.integration.command.with_raw_response.cancel(
                attempt_id="",
                integration_id="integrationID",
            )

    @parametrize
    def test_method_connect(self, client: Opencode) -> None:
        command = client.integration.command.connect(
            integration_id="integrationID",
            method_id="methodID",
        )
        assert_matches_type(CommandConnectResponse, command, path=["response"])

    @parametrize
    def test_method_connect_with_all_params(self, client: Opencode) -> None:
        command = client.integration.command.connect(
            integration_id="integrationID",
            method_id="methodID",
            label="label",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(CommandConnectResponse, command, path=["response"])

    @parametrize
    def test_raw_response_connect(self, client: Opencode) -> None:
        response = client.integration.command.with_raw_response.connect(
            integration_id="integrationID",
            method_id="methodID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(CommandConnectResponse, command, path=["response"])

    @parametrize
    def test_streaming_response_connect(self, client: Opencode) -> None:
        with client.integration.command.with_streaming_response.connect(
            integration_id="integrationID",
            method_id="methodID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(CommandConnectResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_connect(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.command.with_raw_response.connect(
                integration_id="",
                method_id="methodID",
            )

    @parametrize
    def test_method_status(self, client: Opencode) -> None:
        command = client.integration.command.status(
            attempt_id="attemptID",
            integration_id="integrationID",
        )
        assert_matches_type(CommandStatusResponse, command, path=["response"])

    @parametrize
    def test_method_status_with_all_params(self, client: Opencode) -> None:
        command = client.integration.command.status(
            attempt_id="attemptID",
            integration_id="integrationID",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(CommandStatusResponse, command, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Opencode) -> None:
        response = client.integration.command.with_raw_response.status(
            attempt_id="attemptID",
            integration_id="integrationID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(CommandStatusResponse, command, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Opencode) -> None:
        with client.integration.command.with_streaming_response.status(
            attempt_id="attemptID",
            integration_id="integrationID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(CommandStatusResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.command.with_raw_response.status(
                attempt_id="attemptID",
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.integration.command.with_raw_response.status(
                attempt_id="",
                integration_id="integrationID",
            )


class TestAsyncCommand:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpencode) -> None:
        command = await async_client.integration.command.cancel(
            attempt_id="attemptID",
            integration_id="integrationID",
        )
        assert command is None

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncOpencode) -> None:
        command = await async_client.integration.command.cancel(
            attempt_id="attemptID",
            integration_id="integrationID",
            location={
                "directory": "string",
            },
        )
        assert command is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.command.with_raw_response.cancel(
            attempt_id="attemptID",
            integration_id="integrationID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert command is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.command.with_streaming_response.cancel(
            attempt_id="attemptID",
            integration_id="integrationID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert command is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.command.with_raw_response.cancel(
                attempt_id="attemptID",
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.integration.command.with_raw_response.cancel(
                attempt_id="",
                integration_id="integrationID",
            )

    @parametrize
    async def test_method_connect(self, async_client: AsyncOpencode) -> None:
        command = await async_client.integration.command.connect(
            integration_id="integrationID",
            method_id="methodID",
        )
        assert_matches_type(CommandConnectResponse, command, path=["response"])

    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncOpencode) -> None:
        command = await async_client.integration.command.connect(
            integration_id="integrationID",
            method_id="methodID",
            label="label",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(CommandConnectResponse, command, path=["response"])

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.command.with_raw_response.connect(
            integration_id="integrationID",
            method_id="methodID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(CommandConnectResponse, command, path=["response"])

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.command.with_streaming_response.connect(
            integration_id="integrationID",
            method_id="methodID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(CommandConnectResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_connect(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.command.with_raw_response.connect(
                integration_id="",
                method_id="methodID",
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncOpencode) -> None:
        command = await async_client.integration.command.status(
            attempt_id="attemptID",
            integration_id="integrationID",
        )
        assert_matches_type(CommandStatusResponse, command, path=["response"])

    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncOpencode) -> None:
        command = await async_client.integration.command.status(
            attempt_id="attemptID",
            integration_id="integrationID",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(CommandStatusResponse, command, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.command.with_raw_response.status(
            attempt_id="attemptID",
            integration_id="integrationID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(CommandStatusResponse, command, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.command.with_streaming_response.status(
            attempt_id="attemptID",
            integration_id="integrationID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(CommandStatusResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.command.with_raw_response.status(
                attempt_id="attemptID",
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.integration.command.with_raw_response.status(
                attempt_id="",
                integration_id="integrationID",
            )
