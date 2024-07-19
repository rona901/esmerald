from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Type

from typing_extensions import Annotated, Doc

from esmerald.datastructures.base import ResponseContainer
from esmerald.enums import MediaType

if TYPE_CHECKING:  # pragma: no cover
    from esmerald.applications import Esmerald

try:
    from esmerald.responses.encoders import ORJSONResponse
except ImportError:  # pragma: no cover
    ORJSONResponse = None  # type: ignore

try:
    from esmerald.responses.encoders import UJSONResponse
except ImportError:  # pragma: no cover
    UJSONResponse = None  # type: ignore


class OrJSON(ResponseContainer[ORJSONResponse]):
    content: Annotated[
        Dict[str, Any] | None,
        Doc(
            """
            The content being sent to the response.
            """
        ),
    ] = None
    status_code: Annotated[
        int | None,
        Doc(
            """
            The status code of the response. It will default to the
            [handler](https://esmerald.dev/routing/handlers/) if none is provided.
            """
        ),
    ] = None
    media_type: Annotated[
        str,
        Doc(
            """
            The media type of the response.
            """
        ),
    ] = "application/json"

    def __init__(
        self,
        content: Dict[str, Any] | None = None,
        status_code: int | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.content = content
        self.status_code = status_code

    def to_response(
        self,
        headers: Dict[str, Any],
        media_type: MediaType | str,
        status_code: int,
        app: Type[Esmerald],
    ) -> ORJSONResponse:
        assert (
            ORJSONResponse is not None
        ), "You must install the encoders or orjson to use ORJSONResponse"
        status = self.status_code or status_code

        return ORJSONResponse(
            content=self.content,
            headers=headers,
            status_code=status,
            media_type=media_type,
            background=self.background,
        )


class UJSON(ResponseContainer[UJSONResponse]):
    content: Annotated[
        Dict[str, Any] | None,
        Doc(
            """
            The content being sent to the response.
            """
        ),
    ] = None
    status_code: Annotated[
        int | None,
        Doc(
            """
            The status code of the response. It will default to the
            [handler](https://esmerald.dev/routing/handlers/) if none is provided.
            """
        ),
    ] = None
    media_type: Annotated[
        str,
        Doc(
            """
            The media type of the response.
            """
        ),
    ] = "application/json"

    def __init__(
        self,
        content: Dict[str, Any] | None = None,
        status_code: int | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.content = content
        self.status_code = status_code

    def to_response(
        self,
        headers: Dict[str, Any],
        media_type: MediaType | str,
        status_code: int,
        app: Type[Esmerald],
    ) -> UJSONResponse:
        assert (
            UJSONResponse is not None
        ), "You must install the encoders or ujson to use UJSONResponse"
        status = self.status_code or status_code

        return UJSONResponse(
            content=self.content,
            headers=headers,
            status_code=status,
            media_type=media_type,
            background=self.background,
        )
