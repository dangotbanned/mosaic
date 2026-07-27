# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "msgspec>=0.21.1",
# ]
# ///
"""Transform `packages/vgplot/spec/dist/mosaic-schema.json` for use in python."""

# ruff: noqa: T201
from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Final

if TYPE_CHECKING:
    from collections.abc import Iterator


SCRIPTS_DIR = Path(__file__).parent
SPEC_PYTHON_DIR = SCRIPTS_DIR.parent
SCHEMA_DIR = SPEC_PYTHON_DIR / "schema"

VGPLOT_DIR = SPEC_PYTHON_DIR.parent

SCHEMA_IN = VGPLOT_DIR / "spec/dist/mosaic-schema.json"
SCHEMA_OUT = SCHEMA_DIR / SCHEMA_IN.name


KEYS_REMAP: Final = {"as": "bind", "from": "source", "for": "plot"}
"""Keys that collide with [`keyword.kwlist`][]."""


def read_schema(path: str | Path) -> dict[str, Any]:
    import msgspec

    with Path(path).open(encoding="utf8") as fd:
        schema: dict[str, Any] = msgspec.json.decode(fd.read())
        return schema


def write_schema(path: str | Path, schema: dict[str, Any]) -> None:
    import json

    path = Path(path)
    path.touch()
    with path.open("w", encoding="utf8", newline="\n") as fd:
        json.dump(schema, fd, separators=(",", ":"))


def replace_schema_keys(root: dict[str, Any]) -> dict[str, Any]:
    return dict(_recursive_replace(root))


def _recursive_replace(m: dict[str, Any]) -> Iterator[tuple[str, Any]]:
    remap = KEYS_REMAP
    for k, v in m.items():
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
    print(f"Generated python schema at: {SCHEMA_OUT.relative_to(SPEC_PYTHON_DIR).as_posix()}")
