# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .integration_env_method import IntegrationEnvMethod
from .integration_key_method import IntegrationKeyMethod
from .integration_o_auth_method import IntegrationOAuthMethod
from .integration_command_method import IntegrationCommandMethod
from .integration_external_method import IntegrationExternalMethod

__all__ = ["IntegrationMethod"]

IntegrationMethod: TypeAlias = Union[
    IntegrationOAuthMethod,
    IntegrationCommandMethod,
    IntegrationKeyMethod,
    IntegrationExternalMethod,
    IntegrationEnvMethod,
]
