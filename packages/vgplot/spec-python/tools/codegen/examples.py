"""Generating examples from specs.

## Ref
- [prepare-examples.js]
- [Yaml] (authored in yaml)
- [JSON]
- [TypeScript]
- [Python]

[prepare-examples.js]: https://github.com/dangotbanned/mosaic/blob/c35ab3a1213a55c15579f275fc1fb8e60d283616/bin/prepare-examples.js
[Yaml]: https://github.com/dangotbanned/mosaic/blob/c35ab3a1213a55c15579f275fc1fb8e60d283616/specs/yaml/aeromagnetic-survey.yaml
[JSON]: https://github.com/dangotbanned/mosaic/blob/c35ab3a1213a55c15579f275fc1fb8e60d283616/specs/json/aeromagnetic-survey.json
[TypeScript]: https://github.com/dangotbanned/mosaic/blob/c35ab3a1213a55c15579f275fc1fb8e60d283616/specs/ts/aeromagnetic-survey.ts
[Python]: https://github.com/dangotbanned/mosaic/blob/c35ab3a1213a55c15579f275fc1fb8e60d283616/specs/python/aeromagnetic-survey.py
"""

from __future__ import annotations

import functools
from collections.abc import Iterator, Sequence
from itertools import chain
from typing import TYPE_CHECKING, Any, Final, Literal as L, LiteralString as LS

import fs
import msgspec
from typing_extensions import TypedDict

from tools.codegen import markdown
from tools.common import (
    PyIdentifierSnake,
    ensure_type,
    fix_ambiguous_unicode_characters,
    into_repl_map,
)
from tools.ident import py_identifier_snake
from tools.models.base import FrozenHashableStruct, Struct
from tools.serde import read_yaml_untyped

if TYPE_CHECKING:
    from collections.abc import Callable, Mapping
    from pathlib import Path

    from mosaic_spec._gen import params as p


type Lit = bool | int | float | str | None
type JsonIn = Lit | list[JsonIn] | dict[str, JsonIn]
type JsonOut = Lit | ParamRef | list[JsonOut] | tuple[JsonOut, ...] | dict[str, JsonOut]
type Incomplete = Any


class _Meta(TypedDict, total=False):
    title: str
    description: str
    credit: str


class _Config(TypedDict, total=False):
    extensions: str | list[str]


type _DataInline = list[dict[str, Any]]
"""DataArray"""

type _DataDef = dict[str, Any]
"""csv, file, json, json objects, parquet, spatial, table."""

type _DataQuery = str
"""target for NewType"""


class _YamlSpec(TypedDict, total=False, extra_items=JsonIn):
    meta: _Meta
    config: _Config
    data: dict[str, _DataInline | _DataDef | _DataQuery]
    params: dict[str, p.ParamDefinition]
    """All of these are identical to python version."""
    plotDefaults: dict[str, JsonIn]


class DataOther(Struct):
    inner: _DataInline | _DataDef

    def __repr__(self) -> str:
        return self.inner.__str__()


class DataQuery(Struct):
    sql: str

    def __repr__(self) -> str:
        return f"ms.DataQuery({self.sql!r})"


class Datasets(Struct):
    inner: dict[str, DataQuery | DataOther] = msgspec.field(default_factory=dict)

    @staticmethod
    def extract(converted: dict[str, JsonOut]) -> Datasets:
        data: dict[str, Any] = ensure_type(converted.pop("data", {}), dict)
        if not data:
            return Datasets()
        return Datasets(
            {k: (DataQuery(v) if isinstance(v, str) else DataOther(v)) for k, v in data.items()}
        )

    def __bool__(self) -> bool:
        return bool(self.inner)

    def section(self) -> Iterator[tuple[str, Any]]:
        if self:
            yield "data", self.inner


class ParamRef(FrozenHashableStruct, kw_only=False):
    ref: str

    def __repr__(self) -> str:
        return f"ms.ParamRef({self.ref!r})"


type Selection = dict[str, bool | ParamRef | list[ParamRef] | str]
type ParamValue = p.ParamLiteral | list[ParamRef | p.ParamLiteral]
type Param = Mapping[L["value"], ParamValue]
type ParamDef = Param | p.ParamDate | ParamValue | Selection


class Params(Struct):
    inner: dict[PyIdentifierSnake, ParamDef] = msgspec.field(default_factory=dict)

    @staticmethod
    def extract(spec: _YamlSpec) -> Params:
        if not (params := spec.pop("params", {})):
            return Params()
        inner = {py_identifier_snake(name): _param_def(param) for name, param in params.items()}
        return Params(inner)

    def __bool__(self) -> bool:
        return bool(self.inner)

    def section(self) -> Iterator[tuple[str, Any]]:
        if self:
            yield "params", self.inner


def _param_def(param: p.ParamDefinition) -> ParamDef:
    if isinstance(param, (_STOP, Sequence)):
        return _param_value(param)
    if "date" in param:
        return param
    if "value" in param:
        return {"value": _param_value(param["value"])}
    return param_selection(param)


def _param_value(obj: p.ParamValue) -> ParamValue:
    if not isinstance(obj, _STOP):
        return [
            _param_ref(item) if isinstance(item, str) and item.startswith("$") else item
            for item in obj
        ]
    return obj


@functools.cache
def _param_ref(name: str) -> ParamRef:
    return ParamRef(f"${py_identifier_snake(name.removeprefix('$'))}")


@functools.lru_cache(maxsize=128)
def _str_or_param_ref(string: str) -> str | ParamRef:
    if string.startswith("$") and " " not in string:
        # `" "` is checked to guard against sql queries that *happen to* start with a param ref
        return _param_ref(string)
    return string


def param_selection(obj: p.Selection) -> Selection:
    out: Selection = {}
    if "cross" in obj:
        out["cross"] = obj["cross"]
    if "empty" in obj:
        out["empty"] = obj["empty"]
    if "include" in obj:
        include = obj["include"]
        out["include"] = (
            _param_ref(include)
            if isinstance(include, str)
            else [_param_ref(item) for item in include]
        )
    out["select"] = obj["select"]
    return out


class Doc(Struct):
    title: str
    description: str

    @staticmethod
    def extract(spec: _YamlSpec, source: Path) -> Doc:
        if not (meta := spec.pop("meta", {})) or not (title := meta.pop("title", "")):
            parts, *rest = source.stem.split("-")
            title = " ".join((parts.title(), *rest))
        else:
            title = fix_ambiguous_unicode_characters(title.removesuffix("."))
        title = f"{title}."
        if description := meta.pop("description", ""):
            description = description.strip()
            if credit := (meta.pop("credit", "").strip()):
                description = f"{description}\n\n## Credit\n{credit}"
        elif credit := (meta.pop("credit", "").strip()):
            description = f"## Credit\n{credit}"
        else:
            return Doc(title, "*Missing description*")
        return Doc(title, fix_ambiguous_unicode_characters(description))

    def render(self) -> str:
        return f'"""{markdown.fix(f"{self.title}\n\n{self.description}")}"""'


class Example(Struct):
    doc: Doc
    source: Path
    converted: dict[str, JsonOut]
    data: Datasets
    params: Params

    @property
    def type(self) -> LS:
        """Symbol from `mosaic_spec` to use as an annotation."""
        if "plot" in self.converted:
            return "spec.Plot"
        if "vconcat" in self.converted:
            return "spec.VConcat"
        if "hconcat" in self.converted:
            return "spec.HConcat"
        if "input" in self.converted and self.converted["input"] == "table":
            return "spec.Table"
        return "Spec"

    def render_test_module(self) -> str:
        optional = dict(chain.from_iterable(part.section() for part in (self.data, self.params)))
        content = {**optional, **self.converted} if optional else self.converted
        return TEMPLATE_TEST_MODULE.format(doc=self.doc.render(), content=content, type=self.type)

    def target_path(self, target_dir: Path) -> Path:
        # kebab-case module names cannot be imported
        valid_stem = self.source.stem.replace("-", "_")
        target = target_dir / f"test_{valid_stem}.py"
        target.touch()
        return target


def py_name(rename_fields: Mapping[str, str], /) -> Callable[[str], str]:
    get = into_repl_map(rename_fields)

    def name(s: str, /) -> str:
        return get(s) or py_identifier_snake(s)

    return functools.cache(name)


class ExamplesGenerator:
    def __init__(
        self, source_dir: Path, target_dir: Path, rename_fields: Mapping[str, str]
    ) -> None:
        self.source_dir: Path = source_dir
        self.target_dir: Path = target_dir
        self.rename: Callable[[str], str] = py_name(rename_fields)

    def generate_examples(self) -> None:
        for source in fs.iter_dir(self.source_dir, ".yaml"):
            spec = read_yaml_untyped(source)
            example = self.example(spec, source)
            target = example.target_path(self.target_dir)
            content = example.render_test_module()
            fs.write_lines(target, content, "Generated example")

    def example(self, spec: _YamlSpec, source: Path) -> Example:
        doc = Doc.extract(spec, source)
        params = Params.extract(spec)
        rename = self.rename
        translate = self._translate_inner
        converted = {rename(k): translate(v) for k, v in spec.items()}
        data = Datasets.extract(converted)
        return Example(doc, source, converted, data, params)

    def _translate_inner(self, obj: JsonIn | Any, /) -> JsonOut:
        _stop = _STOP
        _list: Final = list
        rename = self.rename
        translate = self._translate_inner
        if isinstance(obj, _stop):
            if isinstance(obj, str):
                return _str_or_param_ref(obj)
            return obj
        if isinstance(obj, _list):
            return [translate(el) for el in obj]
        if _LIST_AS_TUPLE.isdisjoint(obj):
            return {rename(k): translate(v) for k, v in obj.items()}
        return {
            k_: (
                tuple(translate(el) for el in v)
                if k_ in _LIST_AS_TUPLE and isinstance(v, _list)
                else [translate(el) for el in v]
                if isinstance(v, _list)
                else translate(v)
            )
            for k, v in obj.items()
            if (k_ := rename(k))
        }


_LIST_AS_TUPLE: Final = frozenset(
    (
        "argmax",
        "argmin",
        "avg",
        "bin",
        "centroid",
        "centroid_x",
        "centroid_y",
        "column",
        "count",
        "date_day",
        "date_month_day",
        "first",
        "first_value",
        "geojson",
        "groups",
        "last",
        "last_value",
        "limit",
        "max",
        "median",
        "min",
        "mode",
        "ntile",
        "origin",
        "product",
        "projection_parallels",
        "projection_rotate",
        "quantile",
        "range",
        "rows",
        "stddev",
        "stddev_pop",
        "sum",
        "var_pop",
        "variance",
    )
)
"""Keys that are typed as fixed-length tuples.

When deserializing, they will be a `list` and therefore produce typing yells.
"""

_STOP: Final = bool, int, float, str, type(None)

TEMPLATE_TEST_MODULE: Final = """\
{doc}
from __future__ import annotations

import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.{type} = {content}
"""
