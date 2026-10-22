from __future__ import annotations

import pytest

from opencode import NOT_GIVEN
from opencode._qs import encode_path, encode_path_segment, encode_query, to_jsonable
from opencode.types import Location, ModelRef


def test_query_matches_typescript_client_rules() -> None:
    pairs = encode_query(
        {
            "limit": 20,
            "archived": False,
            "parentID": None,
            "skip": NOT_GIVEN,
            "type": ["user", "assistant"],
            "location": {"directory": "/repo"},
        }
    )
    assert pairs == [
        ("limit", "20"),
        ("archived", "false"),
        ("parentID", "null"),
        ("type", "user"),
        ("type", "assistant"),
        ("location[directory]", "/repo"),
    ]


def test_query_serializes_models_by_wire_name() -> None:
    assert encode_query({"location": Location(directory="/srv/app")}) == [("location[directory]", "/srv/app")]


def test_path_segment_escapes_reserved_characters() -> None:
    assert encode_path_segment("a/b?c#d") == "a%2Fb%3Fc%23d"


@pytest.mark.parametrize("value", [".", ".."])
def test_path_segment_encodes_dot_segments(value: str) -> None:
    assert "." not in encode_path_segment(value)


def test_empty_path_segment_is_rejected() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        encode_path_segment("")


def test_wildcard_path_keeps_separators_but_not_traversal() -> None:
    assert encode_path("src/my file.py") == "src/my%20file.py"
    assert encode_path("../etc/passwd") == "%2E%2E/etc/passwd"


def test_to_jsonable_drops_not_given_and_uses_aliases() -> None:
    value = to_jsonable({"model": ModelRef(id="claude", provider_id="anthropic"), "skip": NOT_GIVEN, "raw": b"hi"})
    assert value == {"model": {"id": "claude", "providerID": "anthropic"}, "raw": "aGk="}
