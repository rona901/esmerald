from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    AsyncGenerator,
    AsyncIterable,
    AsyncIterator,
    Callable,
    Dict,
    Generator,
    Iterable,
    Iterator,
    Type,
)

from lilya.responses import StreamingResponse  # noqa
from typing_extensions import Annotated, Doc

from esmerald.datastructures.base import ResponseContainer  # noqa
from esmerald.enums import MediaType

if TYPE_CHECKING:  # pragma: no cover
    from esmerald.applications import Esmerald


class Stream(ResponseContainer[StreamingResponse]):
    iterator: Annotated[
        Iterator[str | bytes] | AsyncIterator[str | bytes] | AsyncGenerator[str | bytes, Any] | Callable[[], AsyncGenerator[str | bytes, Any]] | Callable[[], Generator[str | bytes, Any, Any]],
        Doc(
            """
            Any iterable function.
            """
        ),
    ]

    def to_response(
        self,
        headers: Dict[str, Any],
        media_type: MediaType | str,
        status_code: int,
        app: Type[Esmerald],
    ) -> StreamingResponse:  # pragma: no cover
        return StreamingResponse(
            background=self.background,
            content=(
                self.iterator
                if isinstance(self.iterator, (Iterable, AsyncIterable))
                else self.iterator()
            ),
            headers=headers,
            media_type=media_type,
            status_code=status_code,
        )
