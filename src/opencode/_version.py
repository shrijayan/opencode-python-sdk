from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

__title__ = "opencode"

try:
    __version__ = version("opencode-python-sdk")
except PackageNotFoundError:  # running from a source tree that is not installed
    __version__ = "0.0.0"
