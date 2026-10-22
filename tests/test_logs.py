from __future__ import annotations

import logging
from collections.abc import Iterator

import pytest

from opencode._logs import logger, setup_logging


@pytest.fixture(autouse=True)
def _restore_logger() -> Iterator[None]:
    handlers, level = list(logger.handlers), logger.level
    yield
    logger.handlers[:] = handlers
    logger.setLevel(level)


def _env_handlers() -> list[logging.Handler]:
    return [h for h in logger.handlers if getattr(h, "_opencode_env", False)]


@pytest.mark.parametrize(
    ("value", "level"), [("debug", logging.DEBUG), ("INFO", logging.INFO), (" Debug ", logging.DEBUG)]
)
def test_opencode_log_sets_level(monkeypatch: pytest.MonkeyPatch, value: str, level: int) -> None:
    logger.handlers[:] = []
    monkeypatch.setenv("OPENCODE_LOG", value)
    setup_logging()
    setup_logging()
    assert logger.level == level
    assert len(_env_handlers()) == 1


@pytest.mark.parametrize("value", [None, "", "warning", "verbose"])
def test_opencode_log_ignored(monkeypatch: pytest.MonkeyPatch, value: str | None) -> None:
    logger.handlers[:] = []
    logger.setLevel(logging.NOTSET)
    if value is None:
        monkeypatch.delenv("OPENCODE_LOG", raising=False)
    else:
        monkeypatch.setenv("OPENCODE_LOG", value)
    setup_logging()
    assert logger.level == logging.NOTSET
    assert _env_handlers() == []
