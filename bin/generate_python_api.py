# /// script
# requires-python = ">=3.14"
# ///
"""Reproducing `bin/generate-python-api.js` in python.

Lowers the barrier for who can fix schema gen issues (One language is easier than 2).
"""

# ruff: file-ignore[print]
from __future__ import annotations

import json
import re
from collections import deque
from dataclasses import dataclass, field
from keyword import iskeyword as is_keyword
from operator import attrgetter, itemgetter
from pathlib import Path
from typing import TYPE_CHECKING, Any, ClassVar, Final, Literal as L, TypedDict

if TYPE_CHECKING:
    from collections.abc import Collection, Iterable, Iterator, Sequence


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

BIN_DIR = Path(__file__).parent
ROOT_DIR = BIN_DIR.parent
PACKAGES_DIR = ROOT_DIR / "packages"
VGPLOT_DIR = PACKAGES_DIR / "vgplot"
SCHEMA_PATH = VGPLOT_DIR / "spec/dist/mosaic-schema.json"
OUT_DIR = VGPLOT_DIR / "vgplot-python/vgplot/_generated"
SPEC_GEN_DIR = VGPLOT_DIR / "spec/src/generated"

EXCLUDE_ATTRS = frozenset(("margins",))
"""Attributes handled by special hand-written helpers (not simple value directives)."""

INDENT: Final = " " * 4
EMPTY: Final = ""
LB, RB = "{", "}"
NL: Final = "\n"
UNSET: Final = "UNSET"
KWDS: Final = "options"
ANN_DICT = "dict[str, Any]"

HEADER = (
    f"# DO NOT EDIT. Generated from the Mosaic JSON schema by bin/generate_python_api.py.{NL}"
    f"# Regenerate with: pnpm generate:python-api-py{NL}"
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

join = ",".join
"""Join strings using a comma separator."""


def write_lines(target: Path, lines: str | Iterable[str]) -> None:
    """Write `lines` to `target`."""
    lines = (NL.join(lines) if not isinstance(lines, str) else lines) + NL
    target.touch()
    target.write_text(lines, "utf8", newline=NL)


def py_identifier(name: str) -> str:
    if not name:
        msg = "Cannot create an identifier from an empty string"
        raise TypeError(msg)
    s = _CAMEL_PATTERN.sub(_CAMEL_REPL, name).lower()
    if is_keyword(s):
        url = "https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords"
        msg = (
            f"Cannot use {s!r} as an identifier as it is a Python keyword.{NL}"
            f"Hint: try picking a different name?{NL}See also: {url}"
        )
        raise SyntaxError(msg)
    return s


def docline(desc: str, fallback: str = EMPTY) -> str:
    """First sentence of a schema description, with markdown links stripped and escaped for a docstring."""
    # NOTE: man, this is complicated
    text = desc or fallback
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", _GROUP_1, text)  # [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\[[^\]]*\]", _GROUP_1, text)  # [text][ref] -> text
    text = re.sub(r"\[(\d+)\]", EMPTY, text)  # bare footnote [1] -> (removed)
    text = re.sub(r"\[([^\]]+)\]", _GROUP_1, text)  # [text] shortcut -> text
    text = re.sub(r"\s+", " ", text).strip()

    first: str = next(iter(re.split(r"(?<=\.)\s", text)), fallback)
    text = re.sub(r"\\", "\\\\", first)
    text = re.sub(r'"', '\\"\\"\\"', text)
    return f'"""{text}"""'


@dataclass
class MarkInfo:
    mark: str
    props: dict[str, Schema]
    description: str


def mark_info(schema: Schema) -> MarkInfo | None:
    """Extract a mark's const name and unioned channel properties from a def.

    Handles both flat defs and `anyOf` intersection defs (e.g. densityX).
    """
    desc = schema.get("description", EMPTY)
    if (props := schema.get("properties", {})) and (const := props.get("mark", {}).get("const")):
        return MarkInfo(const, props, desc)
    branches = schema.get("anyOf", ())
    consts = set[str]()
    props = {}

    for b in branches:
        if c := b.get("properties", {}).get("mark", {}).get("const", EMPTY):
            consts.add(c)
            props.update(b["properties"])
    if len(consts) != 1:
        return None
    return MarkInfo(consts.pop(), props, desc)


type AbsoluteName = L[
    "typing",
    "vgplot._types",
    "vgplot.plot",
    "vgplot._generated.marks",
    "vgplot._generated.attributes",
    "vgplot._generated.encodings",
]
"""[Absolute name][1] of the module.

[1]: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
"""


@dataclass
class Module:
    name: L["attributes", "encodings", "marks", "__init__"]
    deps: dict[AbsoluteName, Sequence[str]]
    exports: deque[str] = field(default_factory=deque)
    BASE_HEADER: ClassVar = (
        f"# DO NOT EDIT. Generated from the Mosaic JSON schema by bin/generate_python_api.py.{NL}"
        f"# Regenerate with: pnpm generate:python-api-py{NL}"
    )

    @property
    def path(self) -> Path:
        return OUT_DIR / f"{self.name}.py"

    def iter_header(self) -> Iterator[str]:
        yield self.BASE_HEADER
        for module, names in self.deps.items():
            yield f"from {module} import {join(names)}"

    def render_exports(self) -> str:
        return f"__all__ = {tuple(self.exports)!r}"


def generate_marks(schemas: Iterable[Schema]) -> deque[str]:
    marks = [info for s in schemas if (info := mark_info(s))]
    marks.sort(key=attrgetter("mark"))
    module = Module(
        "marks",
        {
            "typing": ["Any"],
            "vgplot._types": [UNSET, "ChannelValue", "MarkData"],
            "vgplot.plot": ["Mark"],
        },
    )

    out = deque(
        (
            f"def _mark(name: str, args: {ANN_DICT}) -> Mark:",
            f"{INDENT}args = dict(args)",
            f'{INDENT}data = args.pop("data")',
            f'{INDENT}{KWDS} = args.pop("{KWDS}")',
            f"{INDENT}enc = {LB}k: v for k, v in args.items() if v is not {UNSET}{RB}",
            f"{INDENT}enc.update({KWDS})",
            f"{INDENT}return Mark(name, data=data, enc=enc or None)",
        )
    )

    for m in marks:
        mark = m.mark
        fn_name = py_identifier(mark)
        module.exports.append(fn_name)
        params = [
            f"{INDENT}{py_identifier(p)}: ChannelValue | {UNSET} = {UNSET},"
            for p in m.props
            if p not in {"mark", "data", "$schema"}
        ]
        out.extend(
            (
                f"def {fn_name}(",
                f"{INDENT}data: MarkData = None,",
                f"{INDENT}*,",
                *params,
                f"{INDENT}**{KWDS}: Any,",
                ") -> Mark:",
                f"{INDENT}{docline(m.description, f'The {mark} mark.')}",
                f"{INDENT}return _mark({mark!r}, locals())",
            )
        )

    # TODO @dangotbanned: Keep working on this
    # The `__init__` should basically write itself when each module is kept together
    out.extendleft(module.iter_header())
    out.append(module.render_exports())
    write_lines(module.path, out)
    return module.exports


def generate_attributes(plot_attributes: Schema) -> list[str]:
    module = Module("attributes", {"vgplot._types": ["AttrValue"], "vgplot.plot": ["Directive"]})
    out: deque[str] = deque()
    export_names = []
    for attr, schema in plot_attributes.get("properties", {}).items():
        if attr in EXCLUDE_ATTRS:
            continue
        fn_name = py_identifier(attr)
        export_names.append(fn_name)
        is_boolean_attr = any(o.get("type") == "boolean" for o in schema.get("anyOf", (schema,)))
        value = f"value: AttrValue{' = True' if is_boolean_attr else EMPTY}"
        out.extend(
            (
                f"def {fn_name}({value}) -> Directive:",
                f"{INDENT}{docline(schema.get('description', EMPTY), f'The {attr} attribute.')}",
                f"{INDENT}return Directive({attr!r}, value)",
            )
        )
    out.extendleft(module.iter_header())
    # TODO @dangotbanned: Add to exports in loop, then render
    out.append(f"__all__ = {tuple(export_names)!r}")
    write_lines(module.path, out)
    return export_names


_POUND_DEFS = "#/definitions/"


def _iter_transform_defs(definitions: Definitions) -> Iterator[tuple[str, Schema]]:
    for kind_ref in definitions["Transform"].get("anyOf", ()):
        kind_def = definitions.get(kind_ref.get("$ref", EMPTY).removeprefix(_POUND_DEFS), {})
        for member_ref in kind_def.get("anyOf", ()):
            name = member_ref.get("$ref", EMPTY).removeprefix(_POUND_DEFS)
            yield name, definitions.get(name, {})


def generate_transforms(definitions: Definitions) -> list[str]:
    # NOTE: The whole `transform-keys.js` thing looks like a hallucination
    module = Module(
        "encodings",
        {"typing": ["Any"], "vgplot._types": [UNSET, "TransformArg"], "vgplot.plot": ["Mark"]},
    )
    out = deque(
        (
            f"def _transform(name: str, args: tuple[Any, ...], {KWDS}: {ANN_DICT}) -> {ANN_DICT}:",
            f"{INDENT}vals = [a for a in args if a is not {UNSET}]",
            f"{INDENT}value: Any = vals[0] if len(vals) == 1 else vals or ''",
            f"{INDENT}return {LB}name: value, **{KWDS}{RB}",
        )
    )
    export_names = []
    for _, schema in sorted(_iter_transform_defs(definitions), key=itemgetter(0)):
        props = schema.get("properties", {})
        discriminator_name = next(iter(schema.get("required", ())))
        discriminator = props[discriminator_name]
        description = discriminator.get("description", EMPTY)
        fn_name = py_identifier(discriminator_name)
        export_names.append(fn_name)
        min_, max_ = arg_range(discriminator)
        params: list[str] = []
        if max_:
            args = TRANSFORM_ARGS.get(discriminator_name, ("col",))
            params = [
                f"{a}: TransformArg{EMPTY if i < min_ else f' | {UNSET} = {UNSET}'}"
                for i, a in enumerate(args)
            ]
            body = f"{INDENT}return _transform({discriminator_name!r}, ({','.join(args)},), {KWDS})"
        else:
            body = f"{INDENT}return {LB}{discriminator_name!r}: None, **{KWDS}{RB}"
        params.append(f"**{KWDS}: Any")
        out.extend(
            (
                f"def {fn_name}({','.join(params)}) -> {ANN_DICT}:",
                f"{INDENT}{docline(description, f'The {discriminator_name} transform.')}",
                body,
            )
        )

    out.extendleft(module.iter_header())
    # TODO @dangotbanned: Add to exports in loop, then render
    out.append(f"__all__ = {tuple(export_names)!r}")
    write_lines(module.path, out)
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
    Module(
        "__init__",
        {
            "vgplot._generated.marks": mark_names,
            "vgplot._generated.attributes": attr_names,
            "vgplot._generated.encodings": enc_names,
        },
    )
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
