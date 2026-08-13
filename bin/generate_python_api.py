# /// script
# requires-python = ">=3.14"
# ///
"""Reproducing `bin/generate-python-api.js` in python.

Lowers the barrier for who can fix schema gen issues (One language is easier than 2).

## Notes
- May want to pull in `jsonschema`/`fastjsonschema` as an inline script dep
"""

from __future__ import annotations

import json
import keyword
import re
from dataclasses import dataclass
from operator import attrgetter
from pathlib import Path
from typing import TYPE_CHECKING, Any, TypedDict

if TYPE_CHECKING:
    from collections.abc import Iterable


Schema = TypedDict(
    "Schema",
    {
        "$ref": str,  # NOTE: Identifier requires using the ugly functional form
        "properties": dict[str, "Schema"],
        "description": str,
        "anyOf": list["Schema"],
        "required": list[str],
        "type": str,
        "minItems": int,
        "maxItems": int,
    },
    total=False,
)
"""An item in the `"definitions"` field of the schema.

    Uses the variable name `def` in JS, but reserved keyword here.
"""

type Definitions = dict[str, Schema]


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

TRANSFORM_ARGS = {
    "argmax": ["col", "by"],
    "argmin": ["col", "by"],
    "quantile": ["col", "p"],
    "lag": ["col", "offset", "default"],
    "lead": ["col", "offset", "default"],
    "nth_value": ["col", "offset"],
    "ntile": ["buckets"],
}
"""Python parameter names for transforms that take more than a single column."""

_GROUP_1 = r"\g<1>"
_GROUP_2 = r"\g<2>"
_CAMEL_PATTERN = re.compile(r"([a-z0-9])([A-Z])")
_CAMEL_REPL = rf"{_GROUP_1}_{_GROUP_2}"


def write_lines(target: Path, lines: str | Iterable[str]) -> None:
    """Write `lines` to `target`."""
    lines = ("\n".join(lines) if not isinstance(lines, str) else lines) + "\n"
    target.touch()
    target.write_text(lines, "utf8", newline="\n")


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
    text = re.sub(r'"', '\\"\\"\\"', text)
    return f'"""{text}"""'


def is_boolean_attr(schema: Schema) -> bool:
    """Return True if the attribute schema admits a boolean (so it gets a `= True` default)."""
    opts = schema.get("anyOf") or (schema,)
    return any(o.get("type") == "boolean" for o in opts)


@dataclass
class MarkInfo:
    mark: str
    props: dict[str, Schema]
    description: str


def mark_info(schema: Schema) -> MarkInfo | None:
    """Extract a mark's const name and unioned channel properties from a def.

    Handles both flat defs and `anyOf` intersection defs (e.g. densityX).
    """
    desc = schema.get("description", "")
    if (props := schema.get("properties", {})) and (const := props.get("mark", {}).get("const")):
        return MarkInfo(const, props, desc)
    branches = schema.get("anyOf", ())
    consts = set[str]()
    props = {}

    for b in branches:
        if c := b.get("properties", {}).get("mark", {}).get("const", ""):
            consts.add(c)
            props.update(b["properties"])
    if len(consts) != 1:
        return None
    return MarkInfo(consts.pop(), props, desc)


def generate_marks(schemas: Iterable[Schema]) -> list[str]:
    marks = [info for s in schemas if (info := mark_info(s))]
    marks.sort(key=attrgetter("mark"))

    out = [
        HEADER,
        "from typing import Any",
        "",
        "from vgplot._types import UNSET, ChannelValue, MarkData",
        "from vgplot.plot import Mark",
        "",
        "",
        "def _mark(name: str, args: dict[str, Any]) -> Mark:",
        "    args = dict(args)",
        '    data = args.pop("data")',
        '    options = args.pop("options")',
        "    enc = {k: v for k, v in args.items() if v is not UNSET}",
        "    enc.update(options)",
        "    return Mark(name, data=data, enc=enc or None)",
        "",
        "",
    ]
    export_names = []
    pattern = re.compile(r"^[A-Za-z][A-Za-z0-9]*$")
    for m in marks:
        mark = m.mark
        fn_name = ident(mark)
        export_names.append(fn_name)
        # Channel/option properties: everything except the `mark` const, `data`,
        # and any non-identifier keys (e.g. a stray `$schema`).

        params = [
            f"    {ident(parameter)}: ChannelValue | UNSET = UNSET,"
            for parameter in m.props
            if parameter not in {"mark", "data"} and pattern.search(parameter)
        ]
        out.extend(
            (
                f"def {fn_name}(",
                "    data: MarkData = None,",
                "    *,",
                *params,
                "    **options: Any,",
                ") -> Mark:",
                f"    {docline(m.description, f'The {mark} mark.')}",
                f"    return _mark({mark!r}, locals())",
                "",
                "",
            )
        )
    out.append(f"__all__ = {tuple(export_names)!r}")
    write_lines(OUT_DIR / "marks.py", out)
    return export_names


def generate_attributes(plot_attributes: Schema) -> list[str]:
    out = [
        HEADER,
        "from vgplot._types import AttrValue",
        "from vgplot.plot import Directive",
        "",
        "",
    ]
    export_names = []
    for attr, schema in plot_attributes.get("properties", {}).items():
        if attr in EXCLUDE_ATTRS:
            continue
        fn_name = ident(attr)
        export_names.append(fn_name)
        out.extend(
            (
                f"def {fn_name}(value: AttrValue{' = True' if is_boolean_attr(schema) else ''}) -> Directive:",
                f"    {docline(schema.get('description', ''), f'The {attr} attribute.')}",
                f"    return Directive({attr!r}, value)",
                "",
                "",
            )
        )
    out.append(f"__all__ = {tuple(export_names)!r}")
    write_lines(OUT_DIR / "attributes.py", out)
    return export_names


def generate_encodings(schemas: Iterable[Schema]) -> list[str]:
    msg = f"TODO {generate_encodings.__name__}()"
    raise NotImplementedError(msg)


def arg_range(schema: Schema) -> tuple[int, int]:
    """Positional-argument range [min, max] admitted by a transform key schema."""
    msg = f"TODO {arg_range.__name__}()"
    raise NotImplementedError(msg)


def write_init() -> None:
    msg = f"TODO {write_init.__name__}()"
    raise NotImplementedError(msg)


def main() -> None:
    with SCHEMA_PATH.open(encoding="utf-8") as fd:
        schema: dict[str, Any] = json.load(fd)
    definitions: Definitions = schema["definitions"]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SPEC_GEN_DIR.mkdir(parents=True, exist_ok=True)

    _mark_names = generate_marks(definitions.values())
    _attr_names = generate_attributes(definitions["PlotAttributes"])
