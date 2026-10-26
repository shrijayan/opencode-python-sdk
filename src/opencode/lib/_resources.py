"""Generated resources with the SDK's hand-written methods mixed in.

Custom code, never regenerated: ``client.session`` gains ``run`` (and the other helpers of
:mod:`opencode.lib._session`), ``client.pty`` and ``client.experimental.persistent_pty`` gain
``attach`` (:mod:`opencode._pty`). :class:`opencode.Opencode` returns these classes.
"""

from __future__ import annotations

from .._compat import cached_property
from .._pty import AsyncPersistentPtyAttachMixin, AsyncPtyAttachMixin, PersistentPtyAttachMixin, PtyAttachMixin
from ..resources.experimental.experimental import AsyncExperimentalResource, ExperimentalResource
from ..resources.experimental.persistent_pty import AsyncPersistentPtyResource, PersistentPtyResource
from ..resources.pty.pty import AsyncPtyResource, PtyResource
from ..resources.session.session import AsyncSessionResource, SessionResource
from ._session import AsyncSessionHelpers, SessionHelpers

__all__ = [
    "AsyncExperimental",
    "AsyncPersistentPty",
    "AsyncPty",
    "AsyncSession",
    "Experimental",
    "PersistentPty",
    "Pty",
    "Session",
]


class Session(SessionHelpers, SessionResource):
    """``client.session``: the generated operations, ``run`` and the other session helpers."""


class AsyncSession(AsyncSessionHelpers, AsyncSessionResource):
    """``client.session`` of the async client."""


class Pty(PtyAttachMixin, PtyResource):
    """``client.pty``: the generated operations and ``attach``."""


class AsyncPty(AsyncPtyAttachMixin, AsyncPtyResource):
    """``client.pty`` of the async client."""


class PersistentPty(PersistentPtyAttachMixin, PersistentPtyResource):
    """``client.experimental.persistent_pty``: the generated operations and ``attach``."""


class AsyncPersistentPty(AsyncPersistentPtyAttachMixin, AsyncPersistentPtyResource):
    """``client.experimental.persistent_pty`` of the async client."""


class Experimental(ExperimentalResource):
    """``client.experimental``, whose ``persistent_pty`` can ``attach``."""

    @cached_property
    def persistent_pty(self) -> PersistentPty:  # pyright: ignore[reportIncompatibleVariableOverride]
        return PersistentPty(self._client)


class AsyncExperimental(AsyncExperimentalResource):
    """``client.experimental`` of the async client."""

    @cached_property
    def persistent_pty(self) -> AsyncPersistentPty:  # pyright: ignore[reportIncompatibleVariableOverride]
        return AsyncPersistentPty(self._client)
