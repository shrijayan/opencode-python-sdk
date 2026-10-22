from __future__ import annotations

import base64
import json

import httpx
import pytest
import respx

from opencode import (
    NOT_GIVEN,
    APIConnectionError,
    APIResponseValidationError,
    APITimeoutError,
    InternalServerError,
    NotFoundError,
    Opencode,
    OpencodeError,
    RateLimitError,
    SessionNotFoundError,
)
from opencode.types import ModelRef, SessionMessageUser

from .conftest import BASE_URL, PASSWORD

SESSION = {
    "id": "ses_1",
    "projectID": "prj_1",
    "cost": 0,
    "tokens": {"input": 0, "output": 0, "reasoning": 0, "cache": {"read": 0, "write": 0}},
    "time": {"created": 1, "updated": 1},
    "title": "Hello",
    "location": {"directory": "/repo"},
}
AGENTS: dict[str, object] = {"location": {"directory": "/repo"}, "data": []}


def _auth(username: str = "opencode", password: str = PASSWORD) -> str:
    return "Basic " + base64.b64encode(f"{username}:{password}".encode()).decode()


def test_sends_basic_auth_and_user_agent(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/agent").respond(json=AGENTS)
    client.agent.list()
    request = route.calls.last.request
    assert request.headers["Authorization"] == _auth()
    assert request.headers["User-Agent"].startswith("opencode-python/")


def test_password_from_environment(monkeypatch: pytest.MonkeyPatch, mock_api: respx.MockRouter) -> None:
    monkeypatch.setenv("OPENCODE_PASSWORD", "from-env")
    route = mock_api.get("/api/agent").respond(json=AGENTS)
    with Opencode(BASE_URL) as client:
        client.agent.list()
    assert route.calls.last.request.headers["Authorization"] == _auth(password="from-env")


def test_empty_password_disables_auth(monkeypatch: pytest.MonkeyPatch, mock_api: respx.MockRouter) -> None:
    monkeypatch.setenv("OPENCODE_PASSWORD", "from-env")
    route = mock_api.get("/api/agent").respond(json=AGENTS)
    with Opencode(BASE_URL, password="") as client:
        client.agent.list()
    assert "Authorization" not in route.calls.last.request.headers


def test_missing_base_url_explains_how_to_fix(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENCODE_BASE_URL", raising=False)
    with pytest.raises(OpencodeError, match="OPENCODE_BASE_URL"):
        Opencode()


def test_repr_never_contains_password(client: Opencode) -> None:
    assert PASSWORD not in repr(client)


def test_base_url_path_prefix_is_kept() -> None:
    with respx.mock() as router:
        route = router.get("http://proxy.test/opencode/api/agent").respond(json=AGENTS)
        with Opencode("http://proxy.test/opencode", password="") as client:
            client.agent.list()
        assert route.called


def test_body_omits_not_given_and_sends_explicit_null(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/session").respond(json={"data": SESSION})
    session = client.session.create(title=None, model=ModelRef(id="m", provider_id="p"))
    assert session.id == "ses_1"
    assert json.loads(route.calls.last.request.content) == {"title": None, "model": {"id": "m", "providerID": "p"}}


def test_path_and_query_parameters(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/session/ses%2F1/interrupt").respond(json={"interrupted": True})
    client.session.interrupt("ses/1", resume=False)
    assert route.calls.last.request.url.params["resume"] == "false"


def test_default_directory_becomes_location(mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/agent").respond(json=AGENTS)
    with Opencode(BASE_URL, password="", directory="/repo") as client:
        client.agent.list()
        client.agent.list(location={"directory": "/other"})  # type: ignore[arg-type]
    assert route.calls[0].request.url.params["location[directory]"] == "/repo"
    assert route.calls[1].request.url.params["location[directory]"] == "/other"


def test_extra_options_are_merged(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/session").respond(json={"data": SESSION})
    client.session.create(
        title="t", extra_headers={"X-Trace": "1"}, extra_query={"debug": True}, extra_body={"experimental": 1}
    )
    request = route.calls.last.request
    assert request.headers["X-Trace"] == "1"
    assert request.url.params["debug"] == "true"
    assert json.loads(request.content) == {"title": "t", "experimental": 1}


def test_unwraps_data_envelope_into_model(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/session/ses_1/prompt").respond(
        json={
            "data": {
                "id": "msg_1",
                "sessionID": "ses_1",
                "time": {"created": 1},
                "type": "user",
                "payload": {"text": "hi"},
                "delivery": "steer",
            }
        }
    )
    result = client.session.prompt("ses_1", text="hi")
    assert result.id == "msg_1"


def test_tagged_error_maps_to_specific_class(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_9").respond(
        404, json={"_tag": "SessionNotFoundError", "sessionID": "ses_9", "message": "Session not found: ses_9"}
    )
    with pytest.raises(SessionNotFoundError) as caught:
        client.session.get("ses_9")
    error = caught.value
    assert isinstance(error, NotFoundError)
    assert error.status_code == 404
    assert error.error.session_id == "ses_9"
    assert "Session not found" in str(error)


def test_unknown_tag_falls_back_to_status_class(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_9").respond(404, json={"_tag": "BrandNewError", "message": "nope"})
    with pytest.raises(NotFoundError) as caught:
        client.session.get("ses_9")
    assert caught.value.error_tag == "BrandNewError"


def test_get_retries_transient_status(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/agent").mock(
        side_effect=[httpx.Response(502), httpx.Response(503), httpx.Response(200, json=AGENTS)]
    )
    client.agent.list()
    assert route.call_count == 3


def test_retries_are_bounded(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/agent").respond(500, json={"_tag": "UnknownError", "message": "boom"})
    with pytest.raises(InternalServerError):
        client.agent.list()
    assert route.call_count == 3


def test_post_is_not_retried_after_server_error(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/session/ses_1/prompt").respond(500, json={"message": "boom"})
    with pytest.raises(InternalServerError):
        client.session.prompt("ses_1", text="hi")
    assert route.call_count == 1


def test_post_is_retried_after_rate_limit(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/session").mock(
        side_effect=[httpx.Response(429, headers={"retry-after": "0"}), httpx.Response(200, json={"data": SESSION})]
    )
    client.session.create(title="t")
    assert route.call_count == 2


def test_post_rate_limit_raises_after_retries(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.post("/api/session").respond(429, json={"message": "slow down"})
    with pytest.raises(RateLimitError):
        client.session.create(title="t")


def test_connect_errors_are_retried_even_for_post(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/session").mock(
        side_effect=[httpx.ConnectError("refused"), httpx.Response(200, json={"data": SESSION})]
    )
    client.session.create(title="t")
    assert route.call_count == 2


def test_read_timeout_on_post_is_not_retried(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.post("/api/session").mock(side_effect=httpx.ReadTimeout("slow"))
    with pytest.raises(APITimeoutError):
        client.session.create(title="t")
    assert route.call_count == 1


def test_connection_error_after_retries(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/agent").mock(side_effect=httpx.ConnectError("refused"))
    with pytest.raises(APIConnectionError):
        client.agent.list()


def test_invalid_response_does_not_echo_values(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1").respond(json={"data": {"id": 12345, "secretField": "token-abc"}})
    with pytest.raises(APIResponseValidationError) as caught:
        client.session.get("ses_1")
    assert "token-abc" not in str(caught.value)


def test_binary_response(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/fs/read/src/a%20b.py").respond(content=b"print(1)\n")
    assert client.file.read(path="src/a b.py") == b"print(1)\n"


def test_void_response(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.delete("/api/session/ses_1").respond(204)
    assert client.session.remove("ses_1") is None


def test_with_options_shares_pool_and_overrides(client: Opencode, mock_api: respx.MockRouter) -> None:
    route = mock_api.get("/api/agent").respond(json=AGENTS)
    other = client.with_options(directory="/elsewhere", max_retries=0)
    other.agent.list()
    assert other._http is client._http
    assert route.calls.last.request.url.params["location[directory]"] == "/elsewhere"
    assert route.calls.last.request.headers["Authorization"] == _auth()


def test_not_given_is_falsy_singleton() -> None:
    assert not NOT_GIVEN
    assert repr(NOT_GIVEN) == "NOT_GIVEN"
    assert type(NOT_GIVEN)() is NOT_GIVEN


def test_message_list_returns_typed_union(client: Opencode, mock_api: respx.MockRouter) -> None:
    mock_api.get("/api/session/ses_1/message").respond(
        json={
            "data": [{"type": "user", "id": "msg_1", "time": {"created": 1}, "text": "hi"}],
            "cursor": {"previous": None, "next": None},
        }
    )
    messages = list(client.message.list("ses_1"))
    assert isinstance(messages[0], SessionMessageUser)
