from __future__ import annotations

from inspect import Signature
from typing import Any

from pydantic import BaseModel, ConfigDict

from esmerald.enums import MediaType


class InternalResponse(BaseModel):
    """
    Response generated for non common return types.
    """

    media_type: str | MediaType | None = None
    return_annotation: Any | None = None
    signature: Signature | None = None
    description: str | None = None
    encoding: str | None = None

    model_config = ConfigDict(extra="allow", arbitrary_types_allowed=True)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(annotation={self.media_type}, default={self.encoding})"
