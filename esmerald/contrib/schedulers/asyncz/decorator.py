from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, cast

from asyncz.triggers.types import TriggerType

from esmerald.contrib.schedulers.asyncz.config import Task


def scheduler(
    *,
    name: str | None = None,
    trigger: TriggerType | None = None,
    id: str | None = None,
    mistrigger_grace_time: int | None = None,
    coalesce: bool | None = None,
    max_instances: int | None = None,
    next_run_time: datetime | None = None,
    store: str | None = "default",
    executor: str | None = "default",
    replace_existing: bool = True,
    extra_args: Any | None = None,
    extra_kwargs: Dict[str, Any] | None = None,
    is_enabled: bool = True,
) -> Task:

    def wrapper(func: Any) -> Task:
        task = Task(
            name=name,
            trigger=trigger,
            id=id,
            mistrigger_grace_time=mistrigger_grace_time,
            coalesce=coalesce,
            max_instances=max_instances,
            next_run_time=next_run_time,
            store=store,
            executor=executor,
            replace_existing=replace_existing,
            args=extra_args,
            kwargs=extra_kwargs,
            is_enabled=is_enabled,
        )
        task.fn = func
        return task

    return cast(Task, wrapper)
