from __future__ import annotations

from typing import Dict

from pydantic import BaseModel, ConfigDict

from .header import Header
from .link import Link
from .media_type import MediaType
from .reference import Reference


class Response(BaseModel):
    """Describes a single response from an API Operation, including design-
    time, static `links` to operations based on the response."""

    description: str
    """
    **REQUIRED**. A short description of the response.
    [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    """

    headers: Dict[str, Header | Reference] | None = None
    """
    Maps a header name to its definition.
    [RFC7230](https://tools.ietf.org/html/rfc7230#page-22) states header names are case insensitive.
    If a response header is defined with the name `"Content-Type"`, it SHALL be ignored.
    """

    content: Dict[str, MediaType] | None = None
    """
    A map containing descriptions of potential response payloads.
    The key is a media type or [media type range](https://tools.ietf.org/html/rfc7231#appendix-D)
    and the value describes it.

    For responses that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*
    """

    links: Dict[str, Link | Reference] | None = None
    """
    A map of operations links that can be followed from the response.
    The key of the map is a short name for the link,
    following the naming constraints of the names for `Component Objects <https://spec.openapis.org/oas/v3.1.0#componentsObject).
    """
    model_config = ConfigDict(
        extra="ignore",
        json_schema_extra={
            "examples": [
                {
                    "description": "A complex object array response",
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/VeryComplexType"},
                            }
                        }
                    },
                },
                {
                    "description": "A simple string response",
                    "content": {"text/plain": {"schema": {"type": "string"}}},
                },
                {
                    "description": "A simple string response",
                    "content": {"text/plain": {"schema": {"type": "string", "example": "whoa!"}}},
                    "headers": {
                        "X-Rate-Limit-Limit": {
                            "description": "The number of allowed requests in the current period",
                            "schema": {"type": "integer"},
                        },
                        "X-Rate-Limit-Remaining": {
                            "description": "The number of remaining requests in the current period",
                            "schema": {"type": "integer"},
                        },
                        "X-Rate-Limit-Reset": {
                            "description": "The number of seconds left in the current period",
                            "schema": {"type": "integer"},
                        },
                    },
                },
                {"description": "object created"},
            ]
        },
    )
