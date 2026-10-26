# File generated from our OpenAPI spec by Ferrule. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .model_cache_format import ModelCacheFormat
from .model_reasoning_field import ModelReasoningField
from .model_max_tokens_field import ModelMaxTokensField

__all__ = ["ProviderCompatibility"]


class ProviderCompatibility(BaseModel):
    cache_format: Optional[ModelCacheFormat] = FieldInfo(alias="cacheFormat", default=None)

    max_tokens_field: Optional[ModelMaxTokensField] = FieldInfo(alias="maxTokensField", default=None)

    reasoning_field: Optional[ModelReasoningField] = FieldInfo(alias="reasoningField", default=None)

    require_assistant_after_tool: Optional[bool] = FieldInfo(alias="requireAssistantAfterTool", default=None)

    require_finish_reason: Optional[bool] = FieldInfo(alias="requireFinishReason", default=None)

    require_reasoning: Optional[bool] = FieldInfo(alias="requireReasoning", default=None)

    stream_usage: Optional[bool] = FieldInfo(alias="streamUsage", default=None)

    supports_prompt_cache_key: Optional[bool] = FieldInfo(alias="supportsPromptCacheKey", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
