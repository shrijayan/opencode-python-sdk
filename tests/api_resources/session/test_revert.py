# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.session import RevertStageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevert:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_clear(self, client: Opencode) -> None:
        revert = client.session.revert.clear(
            {},
        )
        assert revert is None

    @parametrize
    def test_raw_response_clear(self, client: Opencode) -> None:
        response = client.session.revert.with_raw_response.clear(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revert = response.parse()
        assert revert is None

    @parametrize
    def test_streaming_response_clear(self, client: Opencode) -> None:
        with client.session.revert.with_streaming_response.clear(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revert = response.parse()
            assert revert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_clear(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.revert.with_raw_response.clear(
                "",
            )

    @parametrize
    def test_method_commit(self, client: Opencode) -> None:
        revert = client.session.revert.commit(
            {},
        )
        assert revert is None

    @parametrize
    def test_raw_response_commit(self, client: Opencode) -> None:
        response = client.session.revert.with_raw_response.commit(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revert = response.parse()
        assert revert is None

    @parametrize
    def test_streaming_response_commit(self, client: Opencode) -> None:
        with client.session.revert.with_streaming_response.commit(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revert = response.parse()
            assert revert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_commit(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.revert.with_raw_response.commit(
                "",
            )

    @parametrize
    def test_method_stage(self, client: Opencode) -> None:
        revert = client.session.revert.stage(
            session_id={},
            message_id={},
        )
        assert_matches_type(RevertStageResponse, revert, path=["response"])

    @parametrize
    def test_method_stage_with_all_params(self, client: Opencode) -> None:
        revert = client.session.revert.stage(
            session_id={},
            message_id={},
            files=True,
        )
        assert_matches_type(RevertStageResponse, revert, path=["response"])

    @parametrize
    def test_raw_response_stage(self, client: Opencode) -> None:
        response = client.session.revert.with_raw_response.stage(
            session_id={},
            message_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revert = response.parse()
        assert_matches_type(RevertStageResponse, revert, path=["response"])

    @parametrize
    def test_streaming_response_stage(self, client: Opencode) -> None:
        with client.session.revert.with_streaming_response.stage(
            session_id={},
            message_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revert = response.parse()
            assert_matches_type(RevertStageResponse, revert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_stage(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.revert.with_raw_response.stage(
                session_id="",
                message_id={},
            )


class TestAsyncRevert:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_clear(self, async_client: AsyncOpencode) -> None:
        revert = await async_client.session.revert.clear(
            {},
        )
        assert revert is None

    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.revert.with_raw_response.clear(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revert = await response.parse()
        assert revert is None

    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.revert.with_streaming_response.clear(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revert = await response.parse()
            assert revert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_clear(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.revert.with_raw_response.clear(
                "",
            )

    @parametrize
    async def test_method_commit(self, async_client: AsyncOpencode) -> None:
        revert = await async_client.session.revert.commit(
            {},
        )
        assert revert is None

    @parametrize
    async def test_raw_response_commit(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.revert.with_raw_response.commit(
            {},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revert = await response.parse()
        assert revert is None

    @parametrize
    async def test_streaming_response_commit(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.revert.with_streaming_response.commit(
            {},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revert = await response.parse()
            assert revert is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_commit(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.revert.with_raw_response.commit(
                "",
            )

    @parametrize
    async def test_method_stage(self, async_client: AsyncOpencode) -> None:
        revert = await async_client.session.revert.stage(
            session_id={},
            message_id={},
        )
        assert_matches_type(RevertStageResponse, revert, path=["response"])

    @parametrize
    async def test_method_stage_with_all_params(self, async_client: AsyncOpencode) -> None:
        revert = await async_client.session.revert.stage(
            session_id={},
            message_id={},
            files=True,
        )
        assert_matches_type(RevertStageResponse, revert, path=["response"])

    @parametrize
    async def test_raw_response_stage(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.revert.with_raw_response.stage(
            session_id={},
            message_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revert = await response.parse()
        assert_matches_type(RevertStageResponse, revert, path=["response"])

    @parametrize
    async def test_streaming_response_stage(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.revert.with_streaming_response.stage(
            session_id={},
            message_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revert = await response.parse()
            assert_matches_type(RevertStageResponse, revert, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_stage(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.revert.with_raw_response.stage(
                session_id="",
                message_id={},
            )
