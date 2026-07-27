"""Stubs for [json-schema draft-07](http://json-schema.org/draft-07/schema#)."""

# NOTE: DO NOT EDIT.
# Regenerate with: uv run datamodel-codegen --profile=draft-07 && pnpm run lint

from collections.abc import Mapping, Sequence
from typing import Any, Literal, NotRequired, TypedDict

type NonNegativeInteger = int

class NonNegativeIntegerDefault0(TypedDict): ...

type Primitive = Literal["array", "boolean", "integer", "null", "number", "object", "string"]

type StringArray = Sequence[str]

type SchemaArray = Sequence[CoreSchemaMetaSchema]

JsonSchema = TypedDict(
    "JsonSchema",
    {
        "$id": NotRequired[str],
        "$schema": NotRequired[str],
        "$ref": NotRequired[str],
        "$comment": NotRequired[str],
        "title": NotRequired[str],
        "description": NotRequired[str],
        "default": NotRequired[Any],
        "readOnly": NotRequired[bool],
        "writeOnly": NotRequired[bool],
        "examples": NotRequired[Sequence[Any]],
        "multipleOf": NotRequired[float],
        "maximum": NotRequired[float],
        "exclusiveMaximum": NotRequired[float],
        "minimum": NotRequired[float],
        "exclusiveMinimum": NotRequired[float],
        "maxLength": NotRequired[NonNegativeInteger],
        "minLength": NotRequired[NonNegativeIntegerDefault0],
        "pattern": NotRequired[str],
        "additionalItems": NotRequired[CoreSchemaMetaSchema],
        "items": NotRequired[CoreSchemaMetaSchema | SchemaArray],
        "maxItems": NotRequired[NonNegativeInteger],
        "minItems": NotRequired[NonNegativeIntegerDefault0],
        "uniqueItems": NotRequired[bool],
        "contains": NotRequired[CoreSchemaMetaSchema],
        "maxProperties": NotRequired[NonNegativeInteger],
        "minProperties": NotRequired[NonNegativeIntegerDefault0],
        "required": NotRequired[StringArray],
        "additionalProperties": NotRequired[CoreSchemaMetaSchema],
        "definitions": NotRequired[Mapping[str, CoreSchemaMetaSchema]],
        "properties": NotRequired[Mapping[str, CoreSchemaMetaSchema]],
        "patternProperties": NotRequired[Mapping[str, CoreSchemaMetaSchema]],
        "dependencies": NotRequired[Mapping[str, CoreSchemaMetaSchema | StringArray]],
        "propertyNames": NotRequired[CoreSchemaMetaSchema],
        "const": NotRequired[Any],
        "enum": NotRequired[Sequence[Any]],
        "type": NotRequired[Primitive | Sequence[Primitive]],
        "format": NotRequired[str],
        "contentMediaType": NotRequired[str],
        "contentEncoding": NotRequired[str],
        "if": NotRequired[CoreSchemaMetaSchema],
        "then": NotRequired[CoreSchemaMetaSchema],
        "else": NotRequired[CoreSchemaMetaSchema],
        "allOf": NotRequired[SchemaArray],
        "anyOf": NotRequired[SchemaArray],
        "oneOf": NotRequired[SchemaArray],
        "not": NotRequired[CoreSchemaMetaSchema],
    },
)

type CoreSchemaMetaSchema = JsonSchema | bool
