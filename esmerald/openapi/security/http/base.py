from __future__ import annotations

from typing import Any, Literal

from esmerald.openapi.enums import APIKeyIn, Header, SecuritySchemeType
from esmerald.openapi.security.base import HTTPBase


class Basic(HTTPBase):
    def __init__(
        self,
        *,
        type_: Literal[
            "apiKey", "http", "mutualTLS", "oauth2", "openIdConnect"
        ] = SecuritySchemeType.http.value,
        bearerFormat: str | None = None,
        scheme_name: str | None = None,
        description: str | None = None,
        in_: Literal["query", "header", "cookie"] | None = APIKeyIn.header.value,
        name: str | None = None,
        scheme: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(
            type_=type_,
            bearerFormat=bearerFormat,
            description=description,
            name=name or "Basic",
            in_=in_,
            scheme=scheme or "basic",
            scheme_name=scheme_name or self.__class__.__name__,
            **kwargs,
        )


class Bearer(HTTPBase):
    def __init__(
        self,
        *,
        type_: Literal[
            "apiKey", "http", "mutualTLS", "oauth2", "openIdConnect"
        ] = SecuritySchemeType.http.value,
        bearerFormat: str | None = None,
        scheme_name: str | None = None,
        description: str | None = None,
        in_: Literal["query", "header", "cookie"] | None = APIKeyIn.header.value,
        name: str | None = None,
        scheme: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(
            type_=type_,
            bearerFormat=bearerFormat,
            description=description,
            name=name or Header.authorization,
            in_=in_,
            scheme=scheme or "bearer",
            scheme_name=scheme_name or self.__class__.__name__,
            **kwargs,
        )


class Digest(HTTPBase):
    def __init__(
        self,
        *,
        type_: Literal[
            "apiKey", "http", "mutualTLS", "oauth2", "openIdConnect"
        ] = SecuritySchemeType.http.value,
        bearerFormat: str | None = None,
        scheme_name: str | None = None,
        description: str | None = None,
        in_: Literal["query", "header", "cookie"] | None = APIKeyIn.header.value,
        name: str | None = None,
        scheme: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(
            type_=type_,
            bearerFormat=bearerFormat,
            description=description,
            name=name or Header.authorization,
            in_=in_,
            scheme=scheme or "digest",
            scheme_name=scheme_name or self.__class__.__name__,
            **kwargs,
        )
