from __future__ import annotations

import httpx

DEFAULT_TIMEOUT = httpx.Timeout(timeout=600.0, connect=10.0)
"""Ten minutes overall with a ten second connect timeout. Agent operations can run for a long time."""

DEFAULT_MAX_RETRIES = 2
INITIAL_RETRY_DELAY = 0.5
MAX_RETRY_DELAY = 8.0
MAX_RETRY_AFTER = 60.0
"""A ``Retry-After`` above this many seconds is not honored; the request fails instead of stalling."""

DEFAULT_CONNECTION_LIMITS = httpx.Limits(max_connections=100, max_keepalive_connections=20, keepalive_expiry=30.0)

DEFAULT_USERNAME = "opencode"
"""The Basic auth user name the OpenCode server expects."""

BASE_URL_ENV = "OPENCODE_BASE_URL"
PASSWORD_ENVS = ("OPENCODE_PASSWORD", "OPENCODE_SERVER_PASSWORD")
"""Password variables, in the order the OpenCode CLI reads them."""

IDEMPOTENT_METHODS = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE"})
RETRYABLE_STATUSES = frozenset({408, 429, 500, 502, 503, 504})
"""Statuses retried for idempotent requests."""
RETRYABLE_STATUSES_UNSAFE = frozenset({429, 503})
"""Statuses retried for non-idempotent requests: the server refused the request before acting on it."""
