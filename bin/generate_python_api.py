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
from textwrap import dedent
from typing import TYPE_CHECKING, Any, ClassVar, Final, Literal as L, Protocol, TypedDict

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator, Sequence


VGPLOT_DIR = Path(__file__).parent.parent / "packages" / "vgplot"
SCHEMA_PATH = VGPLOT_DIR / "spec/dist/mosaic-schema.json"
VGPLOT_PYTHON_SRC = VGPLOT_DIR / "vgplot-python/vgplot"

EMPTY: Final = ""
LB, RB = "{", "}"
NL: Final = "\n"
UNSET: Final = "UNSET"
KWDS: Final = "options"
ANN_DICT = "dict[str, Any]"
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
_CAMEL_PATTERN = re.compile(r"([a-z0-9])([A-Z])")
_CAMEL_REPL = rf"{_GROUP_1}_\g<2>"

join = ",".join
"""Join strings using a comma separator."""


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
type Line = str
"""A line of code."""

type AbsoluteName = L["typing", "vgplot._types", "vgplot.plot"]
"""[Absolute name][1] of the module.

[1]: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
"""

type ExportFn = Callable[[str | Iterable[str]], None]
"""Add name(s) to `__all__`."""


class _ModuleGenFn(Protocol):
    def __call__(self, definitions: Definitions, export: ExportFn, /) -> Iterator[Line]: ...
    @property
    def __name__(self) -> str: ...


def write_lines(target: Path, lines: Line | Iterable[Line]) -> None:
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


def _link_relative(path: Path, /) -> str:
    return path.relative_to(Path.cwd()).as_posix()


class _ModuleBase:
    _exports: deque[str]

    FILE_HEADER: ClassVar = (
        f"# DO NOT EDIT. Generated from the Mosaic JSON schema by bin/generate_python_api.py.{NL}"
        f"# Regenerate with: pnpm generate:python-api-py{NL}"
    )

    def iter_header(self) -> Iterator[Line]:
        yield self.FILE_HEADER

    def iter_imports(self) -> Iterator[Line]:
        raise NotImplementedError

    def iter_body(self, definitions: Definitions, /) -> Iterator[Line]:
        raise NotImplementedError

    def iter_exports(self) -> Iterator[Line]:
        yield f"__all__ = {tuple(self._exports)!r}"

    def iter_lines(self, definitions: Definitions, /) -> Iterator[Line]:
        yield from self.iter_header()
        yield from self.iter_imports()
        yield from self.iter_body(definitions)
        yield from self.iter_exports()


class Package(_ModuleBase):
    name: L["_generated"]
    path: Path
    _modules: deque[Module]
    _exports: deque[str]

    def __init__(self, parent_dir: Path, name: L["_generated"]) -> None:
        self.name = name
        self.path = parent_dir / name / "__init__.py"
        self._modules = deque[Module]()
        self._exports = deque[str]()

    def module[Fn: _ModuleGenFn](
        self, dependencies: dict[AbsoluteName, Sequence[str] | str] | None = None, /
    ) -> Callable[[Fn], Fn]:
        """Decorate a generator function as producing a module for this package.

        The name of the function will be used for the module name.

        Args:
            dependencies: Name(s) required for import, keyed per-module.

        ## Notes
        - The function must accept two parameters
            - `definitions`: the subschemas defined in `mosaic-schema.json`
            - `export`: a function which should be called on all names intended for export in `__all__`
        """

        def decorator(fn: Fn, /) -> Fn:
            deps = {k: ([v] if isinstance(v, str) else v) for k, v in (dependencies or {}).items()}
            self._modules.append(Module(fn.__name__, deps, fn))
            return fn

        return decorator

    def iter_imports(self) -> Iterator[Line]:
        for module in self._modules:
            names = module._exports
            self._exports.extend(names)
            yield (f"from vgplot.{self.name}.{module.name} import {join(names)}")

    def iter_body(self, _: Definitions, /) -> Iterator[Line]:
        yield from ()

    def write_modules(self, definitions: Definitions, /) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        for module in self._modules:
            target = self.path.with_stem(module.name)
            write_lines(target, module.iter_lines(definitions))
            print(f"Generated {len(module._exports)} {module.name}:\n-> {_link_relative(target)}")
        write_lines(self.path, self.iter_lines(definitions))
        print(f"Generated package {self.name}:\n-> {_link_relative(self.path)}")


@dataclass
class Module(_ModuleBase):
    name: str
    deps: dict[AbsoluteName, Sequence[str]]
    _generate: _ModuleGenFn
    _exports: deque[str] = field(default_factory=deque)

    def export(self, names: str | Iterable[str], /) -> None:
        items = self._exports
        (items.append(names) if isinstance(names, str) else items.extend(names))

    def iter_imports(self) -> Iterator[Line]:
        for module, names in self.deps.items():
            yield f"from {module} import {join(names)}"

    def iter_body(self, definitions: Definitions, /) -> Iterator[Line]:
        yield from self._generate(definitions, self.export)


generated = Package(VGPLOT_PYTHON_SRC, "_generated")


@generated.module(
    {"typing": "Any", "vgplot._types": [UNSET, "ChannelValue", "MarkData"], "vgplot.plot": "Mark"}
)
def marks(definitions: Definitions, export: ExportFn, /) -> Iterator[Line]:
    schemas = definitions.values()
    yield dedent(f"""\
    def _mark(name: str, args: {ANN_DICT}) -> Mark:
        args = dict(args)
        data = args.pop("data")
        {KWDS} = args.pop("{KWDS}")
        enc = {LB}k: v for k, v in args.items() if v is not {UNSET}{RB}
        enc.update({KWDS})
        return Mark(name, data=data, enc=enc or None)""")
    exclude = frozenset(("mark", "data", "$schema"))
    for m in sorted((info for s in schemas if (info := mark_info(s))), key=attrgetter("mark")):
        mark = m.mark
        fn_name = py_identifier(mark)
        export(fn_name)
        props = (py_identifier(p) for p in m.props if p not in exclude)
        yield dedent(f"""\
        def {fn_name}(data: MarkData = None, *, {join(f"{p}: ChannelValue | {UNSET} = {UNSET}" for p in props)}, **{KWDS}: Any) -> Mark:
            {docline(m.description, f"The {mark} mark.")}
            return _mark({mark!r}, locals())""")


@generated.module({"vgplot._types": "AttrValue", "vgplot.plot": "Directive"})
def attributes(definitions: Definitions, export: ExportFn, /) -> Iterator[Line]:
    for attr, schema in definitions["PlotAttributes"].get("properties", {}).items():
        if attr == "margins":
            continue  # hand-written helper
        fn_name = py_identifier(attr)
        export(fn_name)
        is_boolean_attr = any(o.get("type") == "boolean" for o in schema.get("anyOf", (schema,)))
        yield dedent(f"""\
        def {fn_name}(value: AttrValue{" = True" if is_boolean_attr else EMPTY}) -> Directive:
            {docline(schema.get("description", EMPTY), f"The {attr} attribute.")}
            return Directive({attr!r}, value)""")


@generated.module(
    {"typing": "Any", "vgplot._types": [UNSET, "TransformArg"], "vgplot.plot": "Mark"}
)
def encodings(definitions: Definitions, export: ExportFn, /) -> Iterator[Line]:
    # NOTE: The whole `transform-keys.js` thing looks like a hallucination
    yield dedent(f"""\
    def _transform(name: str, args: tuple[Any, ...], {KWDS}: {ANN_DICT}) -> {ANN_DICT}:
        vals = [a for a in args if a is not {UNSET}]
        value: Any = vals[0] if len(vals) == 1 else vals or ''
        return {LB}name: value, **{KWDS}{RB}""")
    for _, schema in sorted(_iter_transform_defs(definitions), key=itemgetter(0)):
        props = schema.get("properties", {})
        discriminator_name = next(iter(schema.get("required", ())))
        discriminator = props[discriminator_name]
        description = discriminator.get("description", EMPTY)
        fn_name = py_identifier(discriminator_name)
        export(fn_name)
        min_, max_ = _arg_range(discriminator)
        params: list[str] = []
        if max_:
            args = TRANSFORM_ARGS.get(discriminator_name, ("col",))
            params = [
                f"{a}: TransformArg{EMPTY if i < min_ else f' | {UNSET} = {UNSET}'}"
                for i, a in enumerate(args)
            ]
            body = f"return _transform({discriminator_name!r}, ({join(args)},), {KWDS})"
        else:
            body = f"return {LB}{discriminator_name!r}: None, **{KWDS}{RB}"
        params.append(f"**{KWDS}: Any")
        yield dedent(f"""\
        def {fn_name}({join(params)}) -> {ANN_DICT}:
            {docline(description, f"The {discriminator_name} transform.")}
            {body}""")


def _iter_transform_defs(definitions: Definitions) -> Iterator[tuple[str, Schema]]:
    hash_defs = "#/definitions/"
    for kind_ref in definitions["Transform"].get("anyOf", ()):
        kind_def = definitions.get(kind_ref.get("$ref", EMPTY).removeprefix(hash_defs), {})
        for member_ref in kind_def.get("anyOf", ()):
            name = member_ref.get("$ref", EMPTY).removeprefix(hash_defs)
            yield name, definitions.get(name, {})


def _arg_range(schema: Schema) -> tuple[int, int]:
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


def main() -> None:
    with SCHEMA_PATH.open(encoding="utf-8") as fd:
        schema: dict[str, Any] = json.load(fd)
    definitions: Definitions = schema["definitions"]
    generated.write_modules(definitions)


if __name__ == "__main__":
    main()
