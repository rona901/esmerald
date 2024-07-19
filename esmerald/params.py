from __future__ import annotations

from typing import Any, Callable, Dict, List

from pydantic.dataclasses import dataclass
from pydantic.fields import AliasChoices, AliasPath, FieldInfo

from esmerald.enums import EncodingType, ParamType
from esmerald.typing import Undefined
from esmerald.utils.constants import IS_DEPENDENCY, SKIP_VALIDATION

_PyUndefined: Any = Undefined


class Param(FieldInfo):
    in_: ParamType

    def __init__(
        self,
        default: Any = _PyUndefined,
        *,
        allow_none: bool | None = True,
        default_factory: Callable[..., Any] | None = _PyUndefined,
        annotation: Any | None = None,
        alias: str | None = None,
        alias_priority: int | None = _PyUndefined,
        value_type: Any = _PyUndefined,
        header: str | None = None,
        cookie: str | None = None,
        query: str | None = None,
        path: str | None = None,
        content_encoding: str | None = None,
        required: bool = True,
        title: str | None = None,
        description: str | None = None,
        gt: float | None = None,
        ge: float | None = None,
        lt: float | None = None,
        le: float | None = None,
        multiple_of: float | None = _PyUndefined,
        allow_inf_nan: bool | None = _PyUndefined,
        min_length: int | None = None,
        max_length: int | None = None,
        max_digits: int | None = _PyUndefined,
        strict: bool | None = _PyUndefined,
        pattern: str | None = None,
        examples: List[Any] | None = None,
        deprecated: bool | None = None,
        include_in_schema: bool = True,
        validation_alias: str | AliasPath | AliasChoices | None = None,
        discriminator: str | None = None,
        frozen: bool | None = None,
        validate_default: bool = True,
        init_var: bool = True,
        kw_only: bool = True,
    ) -> None:
        self.deprecated = deprecated
        self.examples = examples
        self.include_in_schema = include_in_schema
        self.allow_none = allow_none

        extra: Dict[str, Any] = {}
        extra.update(header=header)
        extra.update(cookie=cookie)
        extra.update(query=query)
        extra.update(path=path)
        extra.update(required=required)
        extra.update(content_encoding=content_encoding)
        extra.update(value_type=value_type)
        extra.update(examples=self.examples)
        extra.update(deprecated=self.deprecated)
        extra.update(include_in_schema=self.include_in_schema)
        extra.update(allow_none=self.allow_none)

        super().__init__(
            annotation=annotation,
            default=default,
            default_factory=default_factory,
            alias=alias,
            alias_priority=alias_priority,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            multiple_of=multiple_of,
            min_length=min_length,
            max_length=max_length,
            pattern=pattern,
            examples=examples,
            allow_inf_nan=allow_inf_nan,
            json_schema_extra=extra,
            validate_default=validate_default,
            validation_alias=validation_alias,
            discriminator=discriminator,
            max_digits=max_digits,
            strict=strict,
            frozen=frozen,
            init_var=init_var,
            kw_only=kw_only,
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(annotation={self.annotation}, default={self.default})"


class Header(Param):
    in_ = ParamType.HEADER

    def __init__(
        self,
        *,
        default: Any = _PyUndefined,
        allow_none: bool | None = True,
        default_factory: Callable[..., Any] | None = _PyUndefined,
        annotation: Any | None = None,
        alias: str | None = None,
        alias_priority: int | None = _PyUndefined,
        value: str | None = None,
        value_type: Any = _PyUndefined,
        content_encoding: str | None = None,
        required: bool = True,
        title: str | None = None,
        description: str | None = None,
        gt: float | None = None,
        ge: float | None = None,
        lt: float | None = None,
        le: float | None = None,
        multiple_of: float | None = _PyUndefined,
        allow_inf_nan: bool | None = _PyUndefined,
        min_length: int | None = None,
        max_length: int | None = None,
        max_digits: int | None = _PyUndefined,
        strict: bool | None = _PyUndefined,
        pattern: str | None = None,
        examples: List[Any] | None = None,
        deprecated: bool | None = None,
        include_in_schema: bool = True,
        validation_alias: str | AliasPath | AliasChoices | None = None,
        discriminator: str | None = None,
        frozen: bool | None = None,
        validate_default: bool = True,
        init_var: bool = True,
        kw_only: bool = True,
    ) -> None:
        super().__init__(
            default=default,
            allow_none=allow_none,
            default_factory=default_factory,
            annotation=annotation,
            header=value,
            alias=alias,
            alias_priority=alias_priority,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            multiple_of=multiple_of,
            allow_inf_nan=allow_inf_nan,
            min_length=min_length,
            max_length=max_length,
            max_digits=max_digits,
            strict=strict,
            pattern=pattern,
            required=required,
            content_encoding=content_encoding,
            value_type=value_type,
            examples=examples,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            validate_default=validate_default,
            validation_alias=validation_alias,
            discriminator=discriminator,
            frozen=frozen,
            init_var=init_var,
            kw_only=kw_only,
        )


class Cookie(Param):
    in_ = ParamType.COOKIE

    def __init__(
        self,
        default: Any = _PyUndefined,
        *,
        allow_none: bool | None = True,
        default_factory: Callable[..., Any] | None = _PyUndefined,
        annotation: Any | None = None,
        alias: str | None = None,
        alias_priority: int | None = _PyUndefined,
        value_type: Any = _PyUndefined,
        value: str | None = None,
        content_encoding: str | None = None,
        required: bool = True,
        title: str | None = None,
        description: str | None = None,
        gt: float | None = None,
        ge: float | None = None,
        lt: float | None = None,
        le: float | None = None,
        multiple_of: float | None = _PyUndefined,
        allow_inf_nan: bool | None = _PyUndefined,
        min_length: int | None = None,
        max_length: int | None = None,
        max_digits: int | None = _PyUndefined,
        strict: bool | None = _PyUndefined,
        pattern: str | None = None,
        examples: List[Any] | None = None,
        deprecated: bool | None = None,
        include_in_schema: bool = True,
        validation_alias: str | AliasPath | AliasChoices | None = None,
        discriminator: str | None = None,
        frozen: bool | None = None,
        validate_default: bool = True,
        init_var: bool = True,
        kw_only: bool = True,
    ) -> None:
        super().__init__(
            default=default,
            allow_none=allow_none,
            default_factory=default_factory,
            annotation=annotation,
            cookie=value,
            alias=alias,
            alias_priority=alias_priority,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            multiple_of=multiple_of,
            allow_inf_nan=allow_inf_nan,
            min_length=min_length,
            max_length=max_length,
            max_digits=max_digits,
            strict=strict,
            pattern=pattern,
            required=required,
            content_encoding=content_encoding,
            value_type=value_type,
            examples=examples,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            validate_default=validate_default,
            validation_alias=validation_alias,
            discriminator=discriminator,
            frozen=frozen,
            init_var=init_var,
            kw_only=kw_only,
        )


class Query(Param):
    in_ = ParamType.QUERY

    def __init__(
        self,
        default: Any = _PyUndefined,
        *,
        allow_none: bool | None = True,
        default_factory: Callable[..., Any] | None = _PyUndefined,
        annotation: Any | None = None,
        alias: str | None = None,
        alias_priority: int | None = _PyUndefined,
        value_type: Any = _PyUndefined,
        value: str | None = None,
        content_encoding: str | None = None,
        required: bool = True,
        title: str | None = None,
        description: str | None = None,
        gt: float | None = None,
        ge: float | None = None,
        lt: float | None = None,
        le: float | None = None,
        multiple_of: float | None = _PyUndefined,
        allow_inf_nan: bool | None = _PyUndefined,
        min_length: int | None = None,
        max_length: int | None = None,
        max_digits: int | None = _PyUndefined,
        strict: bool | None = _PyUndefined,
        pattern: str | None = None,
        examples: List[Any] | None = None,
        deprecated: bool | None = None,
        include_in_schema: bool = True,
        validation_alias: str | AliasPath | AliasChoices | None = None,
        discriminator: str | None = None,
        frozen: bool | None = None,
        validate_default: bool = True,
        init_var: bool = True,
        kw_only: bool = True,
    ) -> None:
        super().__init__(
            default=default,
            allow_none=allow_none,
            default_factory=default_factory,
            annotation=annotation,
            query=value,
            alias=alias,
            alias_priority=alias_priority,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            multiple_of=multiple_of,
            allow_inf_nan=allow_inf_nan,
            min_length=min_length,
            max_length=max_length,
            max_digits=max_digits,
            strict=strict,
            pattern=pattern,
            required=required,
            content_encoding=content_encoding,
            value_type=value_type,
            examples=examples,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            validate_default=validate_default,
            validation_alias=validation_alias,
            discriminator=discriminator,
            frozen=frozen,
            init_var=init_var,
            kw_only=kw_only,
        )


class Path(Param):
    in_ = ParamType.PATH

    def __init__(
        self,
        default: Any = _PyUndefined,
        *,
        allow_none: bool | None = True,
        default_factory: Callable[..., Any] | None = _PyUndefined,
        annotation: Any | None = None,
        value_type: Any = _PyUndefined,
        content_encoding: str | None = None,
        required: bool = True,
        title: str | None = None,
        description: str | None = None,
        gt: float | None = None,
        ge: float | None = None,
        lt: float | None = None,
        le: float | None = None,
        min_length: int | None = None,
        max_length: int | None = None,
        max_digits: int | None = _PyUndefined,
        strict: bool | None = _PyUndefined,
        pattern: str | None = None,
        examples: List[Any] | None = None,
        deprecated: bool | None = None,
        include_in_schema: bool = True,
        validation_alias: str | AliasPath | AliasChoices | None = None,
        discriminator: str | None = None,
        frozen: bool | None = None,
        validate_default: bool = True,
        init_var: bool = True,
        kw_only: bool = True,
    ) -> None:
        super().__init__(
            default=default,
            allow_none=allow_none,
            default_factory=default_factory,
            annotation=annotation,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            max_digits=max_digits,
            strict=strict,
            pattern=pattern,
            required=required,
            content_encoding=content_encoding,
            value_type=value_type,
            examples=examples,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            validate_default=validate_default,
            validation_alias=validation_alias,
            discriminator=discriminator,
            frozen=frozen,
            init_var=init_var,
            kw_only=kw_only,
        )


class Body(FieldInfo):
    def __init__(
        self,
        default: Any = _PyUndefined,
        *,
        allow_none: bool | None = True,
        default_factory: Callable[..., Any] | None = _PyUndefined,
        annotation: Any | None = None,
        media_type: str | EncodingType = EncodingType.JSON,
        content_encoding: str | None = None,
        title: str | None = None,
        alias: str | None = None,
        alias_priority: int | None = _PyUndefined,
        description: str | None = None,
        embed: bool | None = None,
        gt: float | None = None,
        ge: float | None = None,
        lt: float | None = None,
        le: float | None = None,
        multiple_of: float | None = _PyUndefined,
        allow_inf_nan: bool | None = _PyUndefined,
        max_digits: int | None = _PyUndefined,
        strict: bool | None = _PyUndefined,
        min_length: int | None = None,
        max_length: int | None = None,
        pattern: str | None = None,
        examples: List[Any] | None = None,
        validation_alias: str | AliasPath | AliasChoices | None = None,
        discriminator: str | None = None,
        frozen: bool | None = None,
        validate_default: bool = True,
        init_var: bool = True,
        kw_only: bool = True,
        include_in_schema: bool = True,
    ) -> None:
        extra: Dict[str, Any] = {}
        self.media_type = media_type
        self.content_encoding = content_encoding
        self.examples = examples
        self.allow_none = allow_none
        self.include_in_schema = include_in_schema

        extra.update(media_type=self.media_type)
        extra.update(content_encoding=self.content_encoding)
        extra.update(embed=embed)
        extra.update(allow_none=allow_none)

        super().__init__(
            default=default,
            default_factory=default_factory,
            annotation=annotation,
            title=title,
            alias=alias,
            alias_priority=alias_priority,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            multiple_of=multiple_of,
            max_digits=max_digits,
            allow_inf_nan=allow_inf_nan,
            min_length=min_length,
            max_length=max_length,
            pattern=pattern,
            json_schema_extra=extra,
            validate_default=validate_default,
            validation_alias=validation_alias,
            discriminator=discriminator,
            frozen=frozen,
            init_var=init_var,
            strict=strict,
            kw_only=kw_only,
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(annotation={self.annotation}, default={self.default})"


class Form(Body):
    def __init__(
        self,
        default: Any = _PyUndefined,
        *,
        annotation: Any | None = None,
        default_factory: Callable[..., Any] | None = _PyUndefined,
        allow_none: bool | None = True,
        media_type: str | EncodingType = EncodingType.URL_ENCODED,
        content_encoding: str | None = None,
        alias: str | None = None,
        alias_priority: int | None = _PyUndefined,
        title: str | None = None,
        description: str | None = None,
        gt: float | None = None,
        ge: float | None = None,
        lt: float | None = None,
        le: float | None = None,
        min_length: int | None = None,
        max_length: int | None = None,
        pattern: str | None = None,
        examples: List[Any] | None = None,
        validation_alias: str | AliasPath | AliasChoices | None = None,
        discriminator: str | None = None,
        max_digits: int | None = _PyUndefined,
        strict: bool | None = _PyUndefined,
        frozen: bool | None = None,
        validate_default: bool = True,
        init_var: bool = True,
        kw_only: bool = True,
        include_in_schema: bool = True,
    ) -> None:
        super().__init__(
            default=default,
            annotation=annotation,
            allow_none=allow_none,
            default_factory=default_factory,
            embed=True,
            media_type=media_type,
            content_encoding=content_encoding,
            alias=alias,
            alias_priority=alias_priority,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            pattern=pattern,
            examples=examples,
            validate_default=validate_default,
            validation_alias=validation_alias,
            discriminator=discriminator,
            frozen=frozen,
            init_var=init_var,
            kw_only=kw_only,
            include_in_schema=include_in_schema,
            max_digits=max_digits,
            strict=strict,
        )


class File(Form):
    def __init__(
        self,
        default: Any = _PyUndefined,
        *,
        annotation: Any | None = None,
        allow_none: bool | None = True,
        default_factory: Callable[..., Any] | None = _PyUndefined,
        media_type: str | EncodingType = EncodingType.MULTI_PART,
        content_encoding: str | None = None,
        alias: str | None = None,
        alias_priority: int | None = _PyUndefined,
        title: str | None = None,
        description: str | None = None,
        gt: float | None = None,
        ge: float | None = None,
        lt: float | None = None,
        le: float | None = None,
        min_length: int | None = None,
        max_length: int | None = None,
        pattern: str | None = None,
        examples: List[Any] | None = None,
        validation_alias: str | AliasPath | AliasChoices | None = None,
        discriminator: str | None = None,
        max_digits: int | None = _PyUndefined,
        strict: bool | None = _PyUndefined,
        frozen: bool | None = None,
        validate_default: bool = True,
        init_var: bool = True,
        kw_only: bool = True,
        include_in_schema: bool = True,
    ) -> None:
        super().__init__(
            default=default,
            annotation=annotation,
            allow_none=allow_none,
            default_factory=default_factory,
            media_type=media_type,
            content_encoding=content_encoding,
            alias=alias,
            alias_priority=alias_priority,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            pattern=pattern,
            examples=examples,
            validate_default=validate_default,
            validation_alias=validation_alias,
            discriminator=discriminator,
            max_digits=max_digits,
            strict=strict,
            frozen=frozen,
            init_var=init_var,
            kw_only=kw_only,
            include_in_schema=include_in_schema,
        )


class Injects(FieldInfo):
    """
    Creates a FieldInfo class with extra parameters.
    This is used for dependencies and to inject them.

    **Example**

    ```python
    @get(dependencies={"value": Inject(lambda: 13)})
    def myview(value: Injects()):
        return {"value": value}
    ```
    """

    def __init__(
        self,
        default: Any = Undefined,
        skip_validation: bool = False,
        allow_none: bool = True,
    ) -> None:
        self.allow_none = allow_none
        self.extra: Dict[str, Any] = {
            IS_DEPENDENCY: True,
            SKIP_VALIDATION: skip_validation,
            "allow_none": self.allow_none,
        }
        super().__init__(default=default, json_schema_extra=self.extra)


@dataclass
class DirectInject:  # pragma: no cover
    def __init__(
        self,
        dependency: Callable[..., Any] | None = None,
        *,
        use_cache: bool = True,
        allow_none: bool = True,
    ) -> None:
        self.dependency = dependency
        self.use_cache = use_cache
        self.allow_none = allow_none

    def __hash__(self) -> int:
        values: Dict[str, Any] = {}
        for key, value in self.__dict__.items():
            values[key] = None
            if isinstance(value, (list, set)):
                values[key] = tuple(value)
            else:
                values[key] = value
        return hash((type(self),) + tuple(values))
