from __future__ import annotations

from typing import Any, Literal

from esmerald.openapi.enums import APIKeyIn, SecuritySchemeType
from esmerald.openapi.security.base import HTTPBase


class APIKeyInQuery(HTTPBase):
    def __init__(
        self,
        *,
        type_: Literal[
            "apiKey", "http", "mutualTLS", "oauth2", "openIdConnect"
        ] = SecuritySchemeType.apiKey.value,
        scheme_name: str | None = None,
        description: str | None = None,
        in_: Literal["query", "header", "cookie"] | None = APIKeyIn.query.value,
        name: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(
            type_=type_,
            description=description,
            name=name,
            in_=in_,
            scheme_name=scheme_name or self.__class__.__name__,
            **kwargs,
        )


class APIKeyInHeader(HTTPBase):
    def __init__(
        self,
        *,
        type_: Literal[
            "apiKey", "http", "mutualTLS", "oauth2", "openIdConnect"
        ] = SecuritySchemeType.apiKey.value,
        scheme_name: str | None = None,
        description: str | None = None,
        in_: Literal["query", "header", "cookie"] | None = APIKeyIn.header.value,
        name: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(
            type_=type_,
            description=description,
            name=name,
            in_=in_,
            scheme_name=scheme_name or self.__class__.__name__,
            **kwargs,
        )


class APIKeyInCookie(HTTPBase):
    def __init__(
        self,
        *,
        type_: Literal[
            "apiKey", "http", "mutualTLS", "oauth2", "openIdConnect"
        ] = SecuritySchemeType.apiKey.value,
        scheme_name: str | None = None,
        description: str | None = None,
        in_: Literal["query", "header", "cookie"] | None = APIKeyIn.cookie.value,
        name: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(
            type_=type_,
            description=description,
            name=name,
            in_=in_,
            scheme_name=scheme_name or self.__class__.__name__,
            **kwargs,
        )
