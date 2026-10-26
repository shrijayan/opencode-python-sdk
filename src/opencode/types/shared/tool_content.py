# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .tool_file_content import ToolFileContent
from .tool_text_content import ToolTextContent

__all__ = ["ToolContent"]

ToolContent: TypeAlias = Union[ToolTextContent, ToolFileContent]
