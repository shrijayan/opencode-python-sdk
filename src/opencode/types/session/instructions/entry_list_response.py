# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ...shared.instruction_entry_info import InstructionEntryInfo

__all__ = ["EntryListResponse"]

EntryListResponse: TypeAlias = List[InstructionEntryInfo]
