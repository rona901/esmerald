from __future__ import annotations

from typing import Any, Dict, runtime_checkable

from lilya.types import ASGIApp
from typing_extensions import Protocol


@runtime_checkable
class ExtensionProtocol(Protocol):  # pragma: no cover
    def __init__(self, app: ASGIApp | None = None, **kwargs: Dict[Any, Any]): ...

    def extend(self, **kwargs: Any) -> None: ...
