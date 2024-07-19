from __future__ import annotations

from pydantic import BaseModel


class AsyncExitConfig(BaseModel):
    """Configuration for AsyncExitMiddleware."""

    context_name: str = "esmerald_astack"
