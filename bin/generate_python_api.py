# /// script
# requires-python = ">=3.14"
# ///
"""Reproducing `bin/generate-python-api.js` in python.

Lowers the barrier for who can fix schema gen issues (One language is easier than 2).
"""

# ruff: file-ignore[print]
from __future__ import annotations

import json
import keyword
import re
from collections import deque
from dataclasses import dataclass
from operator import attrgetter, itemgetter
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final, LiteralString, TypedDict

if TYPE_CHECKING:
    from collections.abc import Collection, Iterable, Iterator


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

TRANSFORM_ARGS: Final = {
    "argmax": ("col", "by"),
    "argmin": ("col", "by"),
    "quantile": ("col", "p"),
    "lag": ("col", "offset", "default"),
    "lead": ("col", "offset", "default"),
    "nth_value": ("col", "offset"),
    "ntile": ("buckets",),
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


_POUND_DEFS = "#/definitions/"
LB, RB = "{", "}"


def generate_transforms(definitions: Definitions) -> list[str]:
    # NOTE: The whole `transform-keys.js` thing looks like a hallucination
    root = "Transform"
    transforms = {}
    for kind_ref in definitions[root].get("anyOf", ()):
        # `ColumnTransform, AggregateTransform, WindowTransform`
        kind_def = definitions.get(kind_ref.get("$ref", "").removeprefix(_POUND_DEFS), {})

        for member_ref in kind_def.get("anyOf", ()):
            member_name = member_ref.get("$ref", "").removeprefix(_POUND_DEFS)
            # `Bin", Column, ...`
            # `Argmax, Argmin, ...`
            # `RowNumber, Rank, ...`
            transforms[member_name] = definitions.get(member_name, {})

    out = [
        HEADER,
        "from typing import Any",
        "",
        "from vgplot._types import UNSET, TransformArg",
        "",
        "",
        "def _transform(name: str, args: tuple[Any, ...], options: dict[str, Any]) -> dict[str, Any]:",
        "    vals = [a for a in args if a is not UNSET]",
        '    value: Any = vals[0] if len(vals) == 1 else vals or ""',
        "    return {name: value, **options}",
        "",
        "",
    ]
    export_names = []
    for _, schema in sorted(transforms.items(), key=itemgetter(0)):
        props = schema.get("properties", {})
        key = next(iter(schema.get("required", ())))
        fn_name = ident(key)
        export_names.append(fn_name)
        min_, max_ = arg_range(props[key])
        # not sure why this slicing was there?
        args = TRANSFORM_ARGS.get(key, ("col",))[:max_]

        params = [
            f"{a}: TransformArg{'' if i < min_ else ' | UNSET = UNSET'}" for i, a in enumerate(args)
        ]
        body = (
            f"    return {LB}{key!r}: None, **options{RB}"
            if not max_
            else f"    return _transform({key!r}, {args!r}, options)"
        )
        params.append("**options: Any")
        out.extend(
            (
                f"def {fn_name}({','.join(params)}) -> dict[str, Any]:",
                f"    {docline(schema.get('description', ''), f'The {key} transform.')}",
                body,
                "",
                "",
            )
        )

    out.append(f"__all__ = {tuple(export_names)!r}")
    write_lines(OUT_DIR / "encodings.py", out)
    return export_names


def arg_range(schema: Schema) -> tuple[int, int]:
    """Positional-argument range [min, max] admitted by a transform key schema."""
    if (schema.get("anyOf")) is None:
        return schema["minItems"], schema["maxItems"]

    def _flatten_min_max(s: Schema) -> Iterator[tuple[int, int]]:
        for sub in s.get("anyOf", ()):
            if sub.get("anyOf", ()):
                yield from _flatten_min_max(sub)
            elif (min_ := sub.get("minItems")) is not None and (
                max_ := sub.get("maxItems")
            ) is not None:
                yield (min_, max_)

    mins, maxs = zip(*_flatten_min_max(schema), strict=True)
    return min(mins), max(maxs)


type AbsoluteName = LiteralString
"""[Absolute name][1] of the module.

[1]: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
"""


def write_init(exports: dict[AbsoluteName, Collection[str]]) -> None:
    out = deque([HEADER])
    names_all = deque()
    for module, export_names in exports.items():
        out.append(f"from {module} import {','.join(export_names)}")
        names_all.extend(export_names)

    out.append(f"__all__ = {tuple(names_all)!r}")
    write_lines(OUT_DIR / "__init__.py", out)


def main() -> None:
    with SCHEMA_PATH.open(encoding="utf-8") as fd:
        schema: dict[str, Any] = json.load(fd)
    definitions: Definitions = schema["definitions"]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SPEC_GEN_DIR.mkdir(parents=True, exist_ok=True)

    mark_names = generate_marks(definitions.values())
    attr_names = generate_attributes(definitions["PlotAttributes"])
    enc_names = generate_transforms(definitions)
    write_init(
        {
            "vgplot._generated.marks": mark_names,
            "vgplot._generated.attributes": attr_names,
            "vgplot._generated.encodings": enc_names,
        }
    )
    print(
        f"Generated {len(mark_names)} marks + {len(attr_names)} attributes + {len(enc_names)} encodings -> vgplot/_generated/"
    )


if __name__ == "__main__":
    main()
