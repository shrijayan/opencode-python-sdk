# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .connection_env_info import ConnectionEnvInfo
from .connection_credential_info import ConnectionCredentialInfo

__all__ = ["ConnectionInfo"]

ConnectionInfo: TypeAlias = Union[ConnectionCredentialInfo, ConnectionEnvInfo]
