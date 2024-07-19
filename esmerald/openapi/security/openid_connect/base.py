from __future__ import annotations

from typing import Any, Literal

from pydantic import AnyUrl

from esmerald.openapi.enums import SecuritySchemeType
from esmerald.openapi.security.base import HTTPBase


class OpenIdConnect(HTTPBase):
    def __init__(
        self,
        *,
        type_: Literal[
            "apiKey", "http", "mutualTLS", "oauth2", "openIdConnect"
        ] = SecuritySchemeType.openIdConnect.value,
        openIdConnectUrl: AnyUrl | str | None = None,
        scheme_name: str | None = None,
        description: str | None = None,
        **kwargs: Any,
    ):
        super().__init__(
            type_=type_,
            description=description,
            scheme_name=scheme_name or self.__class__.__name__,
            openIdConnectUrl=openIdConnectUrl,
            **kwargs,
        )
