# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "msgspec>=0.21.1",
# ]
# ///
"""Transform `packages/vgplot/spec/dist/mosaic-schema.json` for use in python."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Final

from scripts import fs

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping

    from scripts._json_schema import JsonSchema


SCHEMA_IN = fs.SPEC / "dist/mosaic-schema.json"
SCHEMA_OUT = fs.SPEC_PYTHON / "schema" / SCHEMA_IN.name


KEYS_REMAP: Final = {"as": "bind", "from": "source", "for": "plot"}
"""Keys that collide with [`keyword.kwlist`][], but must be preserved."""

KEYS_EXCLUDE: Final = frozenset(("$schema",))
"""Keys to entirely ignore in the output.

Excluding `"$schema"` avoids all usage of the more limited [functional-syntax].

[functional-syntax]: https://typing.python.org/en/latest/spec/typeddict.html#functional-syntax.
"""


def read_schema(path: str | Path) -> JsonSchema:
    import msgspec

    with Path(path).open(encoding="utf8") as fd:
        schema: JsonSchema = msgspec.json.decode(fd.read())
        return schema


def write_schema(path: str | Path, schema: JsonSchema) -> None:
    import json

    path = Path(path)
    path.touch()
    with path.open("w", encoding="utf8", newline="\n") as fd:
        json.dump(schema, fd, separators=(",", ":"))


def replace_schema_keys(root: JsonSchema) -> JsonSchema:
    definitions = dict(_recursive_replace(root.get("definitions", {})))
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
    schema = read_schema(SCHEMA_IN)
    replaced = replace_schema_keys(schema)
    write_schema(SCHEMA_OUT, replaced)
    print(f"Generated python schema at: {SCHEMA_OUT.relative_to(fs.SPEC_PYTHON).as_posix()}")
