"""Find, start and stop the local OpenCode background service.

Example::

    from opencode import Opencode, service

    endpoint = service.ensure()  # or service.discover(), which never starts one
    print(endpoint.url)

    with Opencode.from_service() as client:
        print(client.server.info().version)

See :mod:`opencode._service` for how this follows the TypeScript client.
"""

from __future__ import annotations

from ._service import (
    BasicAuth,
    Endpoint,
    EnsureReason,
    PtyMode,
    ServiceError,
    Version,
    async_discover,
    async_ensure,
    async_stop,
    default_file,
    discover,
    ensure,
    headers,
    stop,
)

__all__ = [
    "BasicAuth",
    "Endpoint",
    "EnsureReason",
    "PtyMode",
    "ServiceError",
    "Version",
    "async_discover",
    "async_ensure",
    "async_stop",
    "default_file",
    "discover",
    "ensure",
    "headers",
    "stop",
]
