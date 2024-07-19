from __future__ import annotations

from pydantic import AnyUrl, BaseModel, ConfigDict, EmailStr


class Contact(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        json_schema_extra={
            "examples": [
                {
                    "name": "API Support",
                    "url": "http://www.example.com/support",
                    "email": "support@example.com",
                }
            ]
        },
    )
    """Contact information for the exposed API."""

    name: str | None = None
    """
    The identifying name of the contact person/organization.
    """

    url: AnyUrl | None = None
    """
    The URL pointing to the contact information.
    MUST be in the form of a URL.
    """

    email: EmailStr | str | None = None
    """
    The email address of the contact person/organization.
    MUST be in the form of an email address.
    """
