"""``OPENCODE_LOG`` support: configure the ``opencode`` logger from the environment."""

from __future__ import annotations

import logging
import os

logger = logging.getLogger("opencode")

_LEVELS = {"debug": logging.DEBUG, "info": logging.INFO}


def setup_logging() -> None:
    """Attach a stderr handler to the ``opencode`` logger when ``OPENCODE_LOG`` is ``debug`` or ``info``.

    Does nothing when the variable is unset or has any other value. The OpenCode CLI reads
    ``OPENCODE_LOG_LEVEL``, not ``OPENCODE_LOG``, so the two do not clash.
    """
    level = _LEVELS.get(os.environ.get("OPENCODE_LOG", "").strip().lower())
    if level is None:
        return
    if not any(getattr(h, "_opencode_env", False) for h in logger.handlers):
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("[%(asctime)s - %(name)s:%(lineno)d - %(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
        )
        handler._opencode_env = True  # type: ignore[attr-defined]
        logger.addHandler(handler)
    logger.setLevel(level)
