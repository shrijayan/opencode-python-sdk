# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.integration import OauthStatusResponse, OauthConnectResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOauth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cancel(self, client: Opencode) -> None:
        oauth = client.integration.oauth.cancel(
            attempt_id={},
            integration_id={},
        )
        assert oauth is None

    @parametrize
    def test_method_cancel_with_all_params(self, client: Opencode) -> None:
        oauth = client.integration.oauth.cancel(
            attempt_id={},
            integration_id={},
            location={
                "directory": "string",
            },
        )
        assert oauth is None

    @parametrize
    def test_raw_response_cancel(self, client: Opencode) -> None:
        response = client.integration.oauth.with_raw_response.cancel(
            attempt_id={},
            integration_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert oauth is None

    @parametrize
    def test_streaming_response_cancel(self, client: Opencode) -> None:
        with client.integration.oauth.with_streaming_response.cancel(
            attempt_id={},
            integration_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.oauth.with_raw_response.cancel(
                attempt_id={},
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.integration.oauth.with_raw_response.cancel(
                attempt_id="",
                integration_id={},
            )

    @parametrize
    def test_method_complete(self, client: Opencode) -> None:
        oauth = client.integration.oauth.complete(
            attempt_id={},
            integration_id={},
        )
        assert oauth is None

    @parametrize
    def test_method_complete_with_all_params(self, client: Opencode) -> None:
        oauth = client.integration.oauth.complete(
            attempt_id={},
            integration_id={},
            code="code",
            location={
                "directory": "string",
            },
        )
        assert oauth is None

    @parametrize
    def test_raw_response_complete(self, client: Opencode) -> None:
        response = client.integration.oauth.with_raw_response.complete(
            attempt_id={},
            integration_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert oauth is None

    @parametrize
    def test_streaming_response_complete(self, client: Opencode) -> None:
        with client.integration.oauth.with_streaming_response.complete(
            attempt_id={},
            integration_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_complete(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.oauth.with_raw_response.complete(
                attempt_id={},
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.integration.oauth.with_raw_response.complete(
                attempt_id="",
                integration_id={},
            )

    @parametrize
    def test_method_connect(self, client: Opencode) -> None:
        oauth = client.integration.oauth.connect(
            integration_id={},
            method_id={},
        )
        assert_matches_type(OauthConnectResponse, oauth, path=["response"])

    @parametrize
    def test_method_connect_with_all_params(self, client: Opencode) -> None:
        oauth = client.integration.oauth.connect(
            integration_id={},
            method_id={},
            answer={},
            label="label",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(OauthConnectResponse, oauth, path=["response"])

    @parametrize
    def test_raw_response_connect(self, client: Opencode) -> None:
        response = client.integration.oauth.with_raw_response.connect(
            integration_id={},
            method_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OauthConnectResponse, oauth, path=["response"])

    @parametrize
    def test_streaming_response_connect(self, client: Opencode) -> None:
        with client.integration.oauth.with_streaming_response.connect(
            integration_id={},
            method_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OauthConnectResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_connect(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.oauth.with_raw_response.connect(
                integration_id="",
                method_id={},
            )

    @parametrize
    def test_method_status(self, client: Opencode) -> None:
        oauth = client.integration.oauth.status(
            attempt_id={},
            integration_id={},
        )
        assert_matches_type(OauthStatusResponse, oauth, path=["response"])

    @parametrize
    def test_method_status_with_all_params(self, client: Opencode) -> None:
        oauth = client.integration.oauth.status(
            attempt_id={},
            integration_id={},
            location={
                "directory": "string",
            },
        )
        assert_matches_type(OauthStatusResponse, oauth, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: Opencode) -> None:
        response = client.integration.oauth.with_raw_response.status(
            attempt_id={},
            integration_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OauthStatusResponse, oauth, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: Opencode) -> None:
        with client.integration.oauth.with_streaming_response.status(
            attempt_id={},
            integration_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OauthStatusResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.integration.oauth.with_raw_response.status(
                attempt_id={},
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.integration.oauth.with_raw_response.status(
                attempt_id="",
                integration_id={},
            )


class TestAsyncOauth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpencode) -> None:
        oauth = await async_client.integration.oauth.cancel(
            attempt_id={},
            integration_id={},
        )
        assert oauth is None

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncOpencode) -> None:
        oauth = await async_client.integration.oauth.cancel(
            attempt_id={},
            integration_id={},
            location={
                "directory": "string",
            },
        )
        assert oauth is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.oauth.with_raw_response.cancel(
            attempt_id={},
            integration_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert oauth is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.oauth.with_streaming_response.cancel(
            attempt_id={},
            integration_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.oauth.with_raw_response.cancel(
                attempt_id={},
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.integration.oauth.with_raw_response.cancel(
                attempt_id="",
                integration_id={},
            )

    @parametrize
    async def test_method_complete(self, async_client: AsyncOpencode) -> None:
        oauth = await async_client.integration.oauth.complete(
            attempt_id={},
            integration_id={},
        )
        assert oauth is None

    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncOpencode) -> None:
        oauth = await async_client.integration.oauth.complete(
            attempt_id={},
            integration_id={},
            code="code",
            location={
                "directory": "string",
            },
        )
        assert oauth is None

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.oauth.with_raw_response.complete(
            attempt_id={},
            integration_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert oauth is None

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.oauth.with_streaming_response.complete(
            attempt_id={},
            integration_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.oauth.with_raw_response.complete(
                attempt_id={},
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.integration.oauth.with_raw_response.complete(
                attempt_id="",
                integration_id={},
            )

    @parametrize
    async def test_method_connect(self, async_client: AsyncOpencode) -> None:
        oauth = await async_client.integration.oauth.connect(
            integration_id={},
            method_id={},
        )
        assert_matches_type(OauthConnectResponse, oauth, path=["response"])

    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncOpencode) -> None:
        oauth = await async_client.integration.oauth.connect(
            integration_id={},
            method_id={},
            answer={},
            label="label",
            location={
                "directory": "string",
            },
        )
        assert_matches_type(OauthConnectResponse, oauth, path=["response"])

    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.oauth.with_raw_response.connect(
            integration_id={},
            method_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OauthConnectResponse, oauth, path=["response"])

    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.oauth.with_streaming_response.connect(
            integration_id={},
            method_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OauthConnectResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_connect(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.oauth.with_raw_response.connect(
                integration_id="",
                method_id={},
            )

    @parametrize
    async def test_method_status(self, async_client: AsyncOpencode) -> None:
        oauth = await async_client.integration.oauth.status(
            attempt_id={},
            integration_id={},
        )
        assert_matches_type(OauthStatusResponse, oauth, path=["response"])

    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncOpencode) -> None:
        oauth = await async_client.integration.oauth.status(
            attempt_id={},
            integration_id={},
            location={
                "directory": "string",
            },
        )
        assert_matches_type(OauthStatusResponse, oauth, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncOpencode) -> None:
        response = await async_client.integration.oauth.with_raw_response.status(
            attempt_id={},
            integration_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OauthStatusResponse, oauth, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncOpencode) -> None:
        async with async_client.integration.oauth.with_streaming_response.status(
            attempt_id={},
            integration_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OauthStatusResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.integration.oauth.with_raw_response.status(
                attempt_id={},
                integration_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.integration.oauth.with_raw_response.status(
                attempt_id="",
                integration_id={},
            )
