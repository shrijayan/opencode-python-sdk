"""Generated resources with the SDK's hand-written methods mixed in.

Custom code, never regenerated: ``client.session`` gains ``run`` (and the other helpers of
:mod:`opencode.lib._session`), ``client.pty`` and ``client.experimental.persistent_pty`` gain
``attach`` (:mod:`opencode._pty`). :class:`opencode.Opencode` returns these classes.
"""

from __future__ import annotations

from typing_extensions import override

from .._pty import PtyAttachMixin, AsyncPtyAttachMixin, PersistentPtyAttachMixin, AsyncPersistentPtyAttachMixin
from .._compat import cached_property
from ._session import SessionHelpers, AsyncSessionHelpers
from ..resources.pty.pty import PtyResource, AsyncPtyResource
from ..resources.session.session import SessionResource, AsyncSessionResource
from ..resources.experimental.experimental import ExperimentalResource, AsyncExperimentalResource
from ..resources.experimental.persistent_pty import PersistentPtyResource, AsyncPersistentPtyResource

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
    @override
    def persistent_pty(self) -> PersistentPty:  # pyright: ignore[reportIncompatibleVariableOverride]
        return PersistentPty(self._client)


class AsyncExperimental(AsyncExperimentalResource):
    """``client.experimental`` of the async client."""

    @cached_property
    @override
    def persistent_pty(self) -> AsyncPersistentPty:  # pyright: ignore[reportIncompatibleVariableOverride]
        return AsyncPersistentPty(self._client)
