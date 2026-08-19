"""Configuration via toml."""

from collections.abc import Mapping
from typing import Literal as L

import msgspec

from tools.models import base

type UnwrapPolicy = L["longest", "shortest", "inner", "outer"]
type DefName = str


class ReferenceUnwrap(base.FrozenStruct, frozen=True):
    """Override how each attribute is chosen when unwraping a ref.

    ## Notes
    Both `name` and `description` are resolved independently. Here they are referred to as **value**.

    - *"longest"*: pick the longest value
    - *"shortest"*: pick the shortest value
        - **note**: The default description is `""`
    - *"outer"*: use the value of the definition with a `"$ref"` field
    - *"inner"*: use the value of the definition without a `"$ref"` field

    ## Examples
    `"Curve"` does not add much value to `"CurveName"`, but it has a different name and description:

    ```py
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "definitions": {
            "Curve": {
                "$ref": "#/definitions/CurveName",
                "description": "How to interpolate between control points.",
            },
            "CurveName": {
                "description": "The built-in curve implementations.",
                "enum": ["basis", "basis-closed", "basis-open"],
                "type": "string",
            },
        },
    }
    ```

    By default, `schema` will be simplified using the `"outer"` name (`"Curve"`)
    and the `"longest"` description (`"CurveName"`)

    ```py
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "definitions": {
            "Curve": {
                "description": "How to interpolate between control points.",
                "enum": ["basis", "basis-closed", "basis-open"],
                "type": "string",
            }
        },
    }
    ```
    """

    name: UnwrapPolicy = "outer"
    description: UnwrapPolicy = "longest"


class JsonWrapperToMLIR(base.FrozenStruct, frozen=True):
    ref_unwrap: Mapping[DefName, ReferenceUnwrap] = msgspec.field(default_factory=dict)
    """Mapping from the outer ("$ref"-defining) definition name to a policy table."""


class ConvertConfig(base.FrozenStruct, frozen=True):
    """Top-level config for translation/codegen."""

    to_mlir: JsonWrapperToMLIR = msgspec.field(default_factory=JsonWrapperToMLIR)
    """Configure converting from json schema.

    Represents the first conversion stage.
    """
