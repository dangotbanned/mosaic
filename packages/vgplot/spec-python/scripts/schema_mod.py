# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "msgspec>=0.21.1",
# ]
# ///
"""Transform `packages/vgplot/spec/dist/mosaic-schema.json` for use in python."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Final
from warnings import deprecated

# TODO @dangotbanned: Unbreak path for `../*.ipynb`
try:
    import fs
except ModuleNotFoundError:
    from scripts import fs

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping

    from scripts._json_schema import JsonSchema
    from scripts.models import InputSchema

    class Schema(JsonSchema, closed=True):
        """`dist/mosaic-schema.json`."""

        definitions: dict[str, JsonSchema]  # ty: ignore[invalid-typed-dict-field]


GENERATED_MODULE_NAME = "mosaic"

SCHEMA_IN = fs.SPEC / "dist/mosaic-schema.json"
SCHEMA_OUT = fs.SPEC_PYTHON / "schema" / f"{GENERATED_MODULE_NAME}.json"


KEYS_REMAP: Final = {"as": "bind", "from": "source", "for": "plot"}
"""Keys that collide with [`keyword.kwlist`][], but must be preserved."""

KEYS_EXCLUDE: Final = frozenset(("$schema",))
"""Keys to ignore in the output.

Excluding `"$schema"` avoids all usage of the more limited [functional-syntax].

[functional-syntax]: https://typing.python.org/en/latest/spec/typeddict.html#functional-syntax.
"""

DEFINITIONS_EXCLUDE = frozenset(("Spec",))
"""Top-level definitions to ignore in the output.

## Warning
This is very likely to break the schema if you are not careful.

- References to the definition(s) are not removed
- Every member of the set must be present
"""


@deprecated("switch to `msgspec` instead", category=None)
def read_schema(path: str | Path) -> Schema:
    import msgspec

    with Path(path).open(encoding="utf8") as fd:
        schema: Schema = msgspec.json.decode(fd.read())
        return schema


# TODO @dangotbanned: Integrate into everything else
def read_schema_typed(path: str | Path) -> InputSchema:
    import msgspec

    try:
        import models
    except ModuleNotFoundError:
        from scripts import models

    with Path(path).open(encoding="utf8") as fd:
        return msgspec.json.decode(fd.read(), type=models.InputSchema)


def write_schema(path: str | Path, schema: Schema) -> None:
    import json

    path = Path(path)
    path.touch()
    with path.open("w", encoding="utf8", newline="\n") as fd:
        json.dump(schema, fd, separators=(",", ":"))


def replace_schema_keys(root: Schema) -> Schema:
    definitions = root["definitions"]
    for exclude in DEFINITIONS_EXCLUDE:
        definitions.pop(exclude)
    definitions = dict(_recursive_replace(definitions))
    return root | {"definitions": definitions}


def _recursive_replace(m: Mapping[str, Any]) -> Iterator[tuple[str, Any]]:
    remap = KEYS_REMAP
    exclude = KEYS_EXCLUDE
    it = ((k, v) for k, v in m.items() if k not in exclude)
    for k, v in it:
        k_out = remap.get(k, k)
        if isinstance(v, dict):
            yield k_out, dict(_recursive_replace(v))
        elif isinstance(v, list):
            yield (
                k_out,
                [dict(_recursive_replace(el)) if isinstance(el, dict) else el for el in v],
            )
        else:
            yield k_out, v


if __name__ == "__main__":
    schema = read_schema(SCHEMA_IN)  # ty: ignore[deprecated]
    replaced = replace_schema_keys(schema)
    write_schema(SCHEMA_OUT, replaced)
    print(f"Generated python schema at: {fs.repo_relative_str(SCHEMA_OUT)}")
