from __future__ import annotations

from typing import Any, Dict, List, TypeVar, runtime_checkable

from pydantic import DirectoryPath, validate_call
from typing_extensions import Protocol


@runtime_checkable
class TemplateProtocol(Protocol):  # pragma: no cover
    def make_response(self, **context: Dict[str, Any] | None) -> str: ...


TP = TypeVar("TP", bound=TemplateProtocol, covariant=True)


@runtime_checkable
class TemplateEngineProtocol(Protocol[TP]):  # pragma: no cover
    @validate_call
    def __init__(self, directory: DirectoryPath | List[DirectoryPath]) -> None: ...

    def get_template(self, template_name: str) -> TP: ...
