# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .form_value import FormValue

__all__ = ["FormAnswer"]

FormAnswer: TypeAlias = Dict[str, FormValue]
