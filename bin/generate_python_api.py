"""Reproducing `bin/generate-python-api.js` in python.

Lowers the barrier for who can fix schema gen issues (One language is easier than 2).

## Notes
- May want to pull in `jsonschema`/`fastjsonschema` as an inline script dep
"""

from __future__ import annotations

import keyword
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence

Schema: TypeAlias = dict[str, Any]
"""An item in the `"definitions"` field of the schema.

Uses the variable name `def` in JS, but reserved keyword here.
"""

_GROUP_1 = r"\g<1>"
_GROUP_2 = r"\g<2>"
_CAMEL_PATTERN = re.compile(r"([a-z0-9])([A-Z])")
_CAMEL_REPL = rf"{_GROUP_1}_{_GROUP_2}"


def camel_case_to_snake(name: str) -> str:
    return name if not name else _CAMEL_PATTERN.sub(_CAMEL_REPL, name).lower()


def ident(name: str) -> str:
    """Python identifier for a schema (camelCase) name, keyword-safe."""
    s = camel_case_to_snake(name)
    return f"{s}_" if s in PYTHON_KEYWORDS else s


def docline(desc: str, fallback: str = "") -> str:
    """First sentence of a schema description, with markdown links stripped and escaped for a docstring."""
    # NOTE: man, this is complicated
    text = desc or fallback
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", _GROUP_1, text)  # [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", _GROUP_1, text)  # [text][ref] -> text
    text = re.sub(r"\[(\d+)\]", "", text)  # bare footnote [1] -> (removed)
    text = re.sub(r"\[([^\]]+)\]", _GROUP_1, text)  # [text] shortcut -> text
    text = re.sub(r"\s+", " ", text).strip()

    first: str = next(iter(re.split(r"(?<=\.)\s", text)), fallback)
    text = re.sub(r"\\", "\\\\", first)
    return re.sub(r'"', '\\"\\"\\"', text)


def is_boolean_attr(schema: Schema) -> bool:
    """Return True if the attribute schema admits a boolean (so it gets a `= True` default)."""
    opts: Iterable[dict[str, Any]] = schema.get("anyOf") or schema.get("oneOf") or (schema,)
    return any(o.get("type") == "boolean" for o in opts)


@dataclass
class MarkInfo:
    mark: str
    props: dict[str, dict[str, Any]]
    description: str


def mark_info(schema: Schema) -> MarkInfo | None:
    """Extract a mark's const name and unioned channel properties from a def.

    Handles both flat defs and `anyOf` intersection defs (e.g. densityX).
    """
    props: dict[str, dict[str, Any]]
    desc: str = schema.get("description", "")
    if (
        (props := schema.get("properties", {}))
        and props.get("mark")
        and (const := props["mark"].get("const"))
    ):
        return MarkInfo(const, props, desc)
    branches: Sequence[dict[str, dict[str, dict[str, Any] | Any]]] = schema.get("anyOf", ())
    consts = set[str]()
    props = {}

    for b in branches:
        if c := b.get("properties", {}).get("mark", {}).get("const", ""):
            consts.add(c)
            props.update(b["properties"])
    if len(consts) != 1:
        return None
    return MarkInfo(consts.pop(), props, desc)


PYTHON_KEYWORDS = frozenset(keyword.kwlist)

BIN_DIR = Path(__file__).parent
ROOT_DIR = BIN_DIR.parent
PACKAGES_DIR = ROOT_DIR / "packages"
VGPLOT_DIR = PACKAGES_DIR / "vgplot"
SCHEMA_PATH = VGPLOT_DIR / "spec/dist/mosaic-schema.json"
OUT_DIR = VGPLOT_DIR / "vgplot-python/vgplot/_generated"
SPEC_GEN_DIR = VGPLOT_DIR / "spec/src/generated"

EXCLUDE_ATTRS = frozenset(("margins",))
"""Attributes handled by special hand-written helpers (not simple value directives)."""


HEADER = (
    "# DO NOT EDIT. Generated from the Mosaic JSON schema by bin/generate_python_api.py.\n"
    "# Regenerate with: <TODO>\n"
)
