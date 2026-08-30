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
from typing import TYPE_CHECKING, Any, Final, LiteralString as LS, Self

from typing_extensions import TypedDict

from tools.codegen import markdown
from tools.codegen.convert import KEYS_REPLACE, py_identifier_snake
from tools.codegen.docstrings import doc
from tools.models.mosaic import _fix_ambiguous_unicode_characters
from tools.serde import read_yaml_untyped

if TYPE_CHECKING:
    from pathlib import Path

type Lit = bool | int | float | str | None
type JsonIn = Lit | list[JsonIn] | dict[str, JsonIn]
type JsonOut = Lit | list[JsonOut] | tuple[JsonOut, ...] | dict[str, JsonOut]


class _Meta(TypedDict, total=False):
    title: str
    description: str
    credit: str


class _Config(TypedDict, total=False):
    extensions: str | list[str]


class YamlSpec(TypedDict, total=False, extra_items=JsonIn):
    meta: _Meta
    config: _Config
    data: dict[str, JsonIn]
    params: dict[str, JsonIn]
    plotDefaults: dict[str, JsonIn]


_GET_KEY = KEYS_REPLACE.get


@functools.cache
def _py_name(s: str, /) -> str:
    return _GET_KEY(s) or py_identifier_snake(s)


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


def _translate(obj: JsonIn | Any, /) -> JsonOut:
    # micro-opt
    _stop = _STOP
    _list: Final = list
    if isinstance(obj, _stop):
        return obj
    if isinstance(obj, _list):
        return [_translate(el) for el in obj]
    if _LIST_AS_TUPLE.isdisjoint(obj):
        return {_py_name(k): _translate(v) for k, v in obj.items()}
    return {
        k_: (
            tuple(_translate(el) for el in v)
            if k_ in _LIST_AS_TUPLE and isinstance(v, _list)
            else [_translate(el) for el in v]
            if isinstance(v, _list)
            else _translate(v)
        )
        for k, v in obj.items()
        if (k_ := _py_name(k))
    }


type Title = str
type Description = str


class Example:
    title: Title
    description: Description
    source: Path
    converted: dict[str, JsonOut]
    type: LS
    """Symbol from `mosaic_spec` to use as an annotation."""

    @classmethod
    def _extract_doc_components(cls, spec: YamlSpec, source: Path) -> tuple[Title, Description]:
        if not (meta := spec.pop("meta", {})) or not (title := meta.pop("title", "")):
            parts, *rest = source.stem.split("-")
            title = " ".join((parts.title(), *rest))
        else:
            title = _fix_ambiguous_unicode_characters(title.removesuffix("."))
        title = f"{title}."
        if description := meta.pop("description", ""):
            description = description.strip()
            if credit := (meta.pop("credit", "").strip()):
                description = f"{description}\n\n## Credit\n{credit}"
        elif credit := (meta.pop("credit", "").strip()):
            description = f"## Credit\n{credit}"
        else:
            return title, "*Missing description*"
        return title, _fix_ambiguous_unicode_characters(description)

    @classmethod
    def from_path(cls, source: Path) -> Self:
        # NOTE: `extra_items` isn't supported in msgspec (iirc)
        spec: YamlSpec = read_yaml_untyped(source)
        self = cls.__new__(cls)
        self.source = source
        self.title, self.description = cls._extract_doc_components(spec, source)
        self.converted = {_py_name(k): _translate(v) for k, v in spec.items()}
        if "plot" in self.converted:
            self.type = "spec.Plot"
        elif "vconcat" in self.converted:
            self.type = "spec.VConcat"
        elif "hconcat" in self.converted:
            self.type = "spec.HConcat"
        elif "input" in self.converted and self.converted["input"] == "table":
            self.type = "spec.Table"
        else:
            self.type = "Spec"
        return self

    def render_test_module(self) -> str:
        s = markdown.fix(f"{self.title}\n\n{self.description}")
        docstring = doc(s)
        return TEMPLATE_TEST_MODULE.format(doc=docstring, content=self.converted, type=self.type)


TEMPLATE_TEST_MODULE: Final = """\
{doc}
from __future__ import annotations

import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.{type} = {content}
"""
