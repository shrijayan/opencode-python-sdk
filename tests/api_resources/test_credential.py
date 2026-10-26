# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types import CredentialListResponse
from opencode.types.shared import CredentialEntry

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredential:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Opencode) -> None:
        credential = client.credential.create(
            integration_id="integrationID",
            value={},
        )
        assert_matches_type(CredentialEntry, credential, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Opencode) -> None:
        credential = client.credential.create(
            integration_id="integrationID",
            value={},
            activate=True,
            id="id",
            label="label",
        )
        assert_matches_type(CredentialEntry, credential, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Opencode) -> None:
        response = client.credential.with_raw_response.create(
            integration_id="integrationID",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialEntry, credential, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Opencode) -> None:
        with client.credential.with_streaming_response.create(
            integration_id="integrationID",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialEntry, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Opencode) -> None:
        credential = client.credential.update(
            credential_id="credentialID",
            label="label",
        )
        assert credential is None

    @parametrize
    def test_raw_response_update(self, client: Opencode) -> None:
        response = client.credential.with_raw_response.update(
            credential_id="credentialID",
            label="label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert credential is None

    @parametrize
    def test_streaming_response_update(self, client: Opencode) -> None:
        with client.credential.with_streaming_response.update(
            credential_id="credentialID",
            label="label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert credential is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.credential.with_raw_response.update(
                credential_id="",
                label="label",
            )

    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        credential = client.credential.list()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.credential.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.credential.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(CredentialListResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_activate(self, client: Opencode) -> None:
        credential = client.credential.activate(
            "credentialID",
        )
        assert credential is None

    @parametrize
    def test_raw_response_activate(self, client: Opencode) -> None:
        response = client.credential.with_raw_response.activate(
            "credentialID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert credential is None

    @parametrize
    def test_streaming_response_activate(self, client: Opencode) -> None:
        with client.credential.with_streaming_response.activate(
            "credentialID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert credential is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_activate(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.credential.with_raw_response.activate(
                "",
            )

    @parametrize
    def test_method_remove(self, client: Opencode) -> None:
        credential = client.credential.remove(
            "credentialID",
        )
        assert credential is None

    @parametrize
    def test_raw_response_remove(self, client: Opencode) -> None:
        response = client.credential.with_raw_response.remove(
            "credentialID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert credential is None

    @parametrize
    def test_streaming_response_remove(self, client: Opencode) -> None:
        with client.credential.with_streaming_response.remove(
            "credentialID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert credential is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            client.credential.with_raw_response.remove(
                "",
            )


class TestAsyncCredential:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncOpencode) -> None:
        credential = await async_client.credential.create(
            integration_id="integrationID",
            value={},
        )
        assert_matches_type(CredentialEntry, credential, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencode) -> None:
        credential = await async_client.credential.create(
            integration_id="integrationID",
            value={},
            activate=True,
            id="id",
            label="label",
        )
        assert_matches_type(CredentialEntry, credential, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencode) -> None:
        response = await async_client.credential.with_raw_response.create(
            integration_id="integrationID",
            value={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialEntry, credential, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencode) -> None:
        async with async_client.credential.with_streaming_response.create(
            integration_id="integrationID",
            value={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialEntry, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOpencode) -> None:
        credential = await async_client.credential.update(
            credential_id="credentialID",
            label="label",
        )
        assert credential is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencode) -> None:
        response = await async_client.credential.with_raw_response.update(
            credential_id="credentialID",
            label="label",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert credential is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencode) -> None:
        async with async_client.credential.with_streaming_response.update(
            credential_id="credentialID",
            label="label",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert credential is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.credential.with_raw_response.update(
                credential_id="",
                label="label",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        credential = await async_client.credential.list()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.credential.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(CredentialListResponse, credential, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.credential.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(CredentialListResponse, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_activate(self, async_client: AsyncOpencode) -> None:
        credential = await async_client.credential.activate(
            "credentialID",
        )
        assert credential is None

    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncOpencode) -> None:
        response = await async_client.credential.with_raw_response.activate(
            "credentialID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert credential is None

    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncOpencode) -> None:
        async with async_client.credential.with_streaming_response.activate(
            "credentialID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert credential is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_activate(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.credential.with_raw_response.activate(
                "",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencode) -> None:
        credential = await async_client.credential.remove(
            "credentialID",
        )
        assert credential is None

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencode) -> None:
        response = await async_client.credential.with_raw_response.remove(
            "credentialID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert credential is None

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencode) -> None:
        async with async_client.credential.with_streaming_response.remove(
            "credentialID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert credential is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credential_id` but received ''"):
            await async_client.credential.with_raw_response.remove(
                "",
            )
