from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from .external_documentation import ExternalDocumentation


class Tag(BaseModel):
    """Adds metadata to a single tag that is used by the [Operation
    Object](https://spec.openapis.org/oas/v3.1.0#operationObject).

    It is not mandatory to have a Tag Object per tag defined in the
    Operation Object instances.
    """

    name: str
    """
    **REQUIRED**. The name of the tag.
    """

    description: str | None = None
    """
    A short description for the tag.
    [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    """

    externalDocs: ExternalDocumentation | None = None
    """
    Additional external documentation for this tag.
    """
    model_config = ConfigDict(
        extra="ignore",
        json_schema_extra={"examples": [{"name": "pet", "description": "Pets operations"}]},
    )
