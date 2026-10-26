# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .form_number_field import FormNumberField
from .form_string_field import FormStringField
from .form_boolean_field import FormBooleanField
from .form_integer_field import FormIntegerField
from .form_external_field import FormExternalField
from .form_multiselect_field import FormMultiselectField

__all__ = ["FormField"]

FormField: TypeAlias = Union[
    FormStringField, FormNumberField, FormIntegerField, FormBooleanField, FormMultiselectField, FormExternalField
]
