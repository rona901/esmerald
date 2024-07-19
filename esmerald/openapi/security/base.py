from __future__ import annotations

from typing import Any, Literal

from pydantic import AnyUrl, ConfigDict

from esmerald.openapi.models import SecurityScheme


class HTTPBase(SecurityScheme):
    """
    Base for all HTTP security headers.
    """

    model_config = ConfigDict(extra="allow", arbitrary_types_allowed=True)

    def __init__(
        self,
        *,
        type_: Literal["apiKey", "http", "mutualTLS", "oauth2", "openIdConnect"] | None = None,
        bearerFormat: str | None = None,
        scheme_name: str | None = None,
        description: str | None = None,
        in_: Literal["query", "header", "cookie"] | None = None,
        name: str | None = None,
        scheme: str | None = None,
        openIdConnectUrl: AnyUrl | str | None = None,
        **kwargs: Any,
    ):
        super().__init__(  # type: ignore
            type=type_,
            bearerFormat=bearerFormat,
            description=description,
            name=name,
            security_scheme_in=in_,
            scheme_name=scheme_name,
            scheme=scheme,
            openIdConnectUrl=openIdConnectUrl,
            **kwargs,
        )
