from __future__ import annotations

from enum import Enum


class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return self.value  # type: ignore

    def __repr__(self) -> str:
        return str(self)


class SecuritySchemeType(BaseEnum):
    apiKey = "apiKey"
    http = "http"
    oauth2 = "oauth2"
    mutualTLS = "mutualTLS"
    openIdConnect = "openIdConnect"


class APIKeyIn(BaseEnum):
    query = "query"
    header = "header"
    cookie = "cookie"


class Header(BaseEnum):
    authorization = "Authorization"
