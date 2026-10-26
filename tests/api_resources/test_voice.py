# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode.types.shared import VoiceSessionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_session(self, client: Opencode) -> None:
        voice = client.voice.session(
            model="model",
            transport={},
        )
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    def test_method_session_with_all_params(self, client: Opencode) -> None:
        voice = client.voice.session(
            model="model",
            transport={},
            session={"foo": {}},
        )
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    def test_raw_response_session(self, client: Opencode) -> None:
        response = client.voice.with_raw_response.session(
            model="model",
            transport={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    def test_streaming_response_session(self, client: Opencode) -> None:
        with client.voice.with_streaming_response.session(
            model="model",
            transport={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceSessionResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_session(self, async_client: AsyncOpencode) -> None:
        voice = await async_client.voice.session(
            model="model",
            transport={},
        )
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    async def test_method_session_with_all_params(self, async_client: AsyncOpencode) -> None:
        voice = await async_client.voice.session(
            model="model",
            transport={},
            session={"foo": {}},
        )
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    async def test_raw_response_session(self, async_client: AsyncOpencode) -> None:
        response = await async_client.voice.with_raw_response.session(
            model="model",
            transport={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceSessionResponse, voice, path=["response"])

    @parametrize
    async def test_streaming_response_session(self, async_client: AsyncOpencode) -> None:
        async with async_client.voice.with_streaming_response.session(
            model="model",
            transport={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceSessionResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True
