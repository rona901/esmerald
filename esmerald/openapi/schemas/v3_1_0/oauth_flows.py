from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from .oauth_flow import OAuthFlow


class OAuthFlows(BaseModel):
    """Allows configuration of the supported OAuth Flows."""

    implicit: OAuthFlow | None = None
    """
    Configuration for the OAuth Implicit flow
    """

    password: OAuthFlow | None = None
    """
    Configuration for the OAuth Resource Owner Password flow
    """

    clientCredentials: OAuthFlow | None = None
    """
    Configuration for the OAuth Client Credentials flow.

    Previously called `application` in OpenAPI 2.0.
    """

    authorizationCode: OAuthFlow | None = None
    """
    Configuration for the OAuth Authorization Code flow.

    Previously called `accessCode` in OpenAPI 2.0.
    """

    model_config = ConfigDict(extra="ignore")
