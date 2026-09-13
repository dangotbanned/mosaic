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
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Final, LiteralString as LS

import fs
from typing_extensions import TypedDict

from tools.codegen import markdown
from tools.codegen.convert import py_identifier_snake
from tools.common import fix_ambiguous_unicode_characters, into_repl_map
from tools.serde import read_yaml_untyped

if TYPE_CHECKING:
    from collections.abc import Callable, Mapping
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


def py_name(rename_fields: Mapping[str, str], /) -> Callable[[str], str]:
    get = into_repl_map(rename_fields)

    def name(s: str, /) -> str:
        return get(s) or py_identifier_snake(s)

    return functools.cache(name)


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


type Title = str
type Description = str


def _extract_doc_components(spec: YamlSpec, source: Path) -> tuple[Title, Description]:
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
        return title, "*Missing description*"
    return title, fix_ambiguous_unicode_characters(description)


@dataclass
class Example:
    title: Title
    description: Description
    source: Path
    converted: dict[str, JsonOut]

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
        s = markdown.fix(f"{self.title}\n\n{self.description}")
        return TEMPLATE_TEST_MODULE.format(doc=f'"""{s}"""', content=self.converted, type=self.type)

    def target_path(self, target_dir: Path) -> Path:
        # kebab-case module names cannot be imported
        valid_stem = self.source.stem.replace("-", "_")
        target = target_dir / f"test_{valid_stem}.py"
        target.touch()
        return target


class ExamplesGenerator:
    def __init__(
        self, source_dir: Path, target_dir: Path, rename_fields: Mapping[str, str]
    ) -> None:
        self.source_dir: Path = source_dir
        self.target_dir: Path = target_dir
        self.rename: Callable[[str], str] = py_name(rename_fields)

    def generate(self) -> None:
        for source in fs.iter_dir(self.source_dir, ".yaml"):
            spec: YamlSpec = read_yaml_untyped(source)
            example = self._translate(spec, source)
            target = example.target_path(self.target_dir)
            content = example.render_test_module()
            fs.write_lines(target, content, "Generated example")

    def _translate(self, spec: YamlSpec, source: Path) -> Example:
        title, description = _extract_doc_components(spec, source)
        _py_name = self.rename
        _translate = self._translate_inner
        converted = {_py_name(k): _translate(v) for k, v in spec.items()}
        return Example(title, description, source, converted)

    def _translate_inner(self, obj: JsonIn | Any, /) -> JsonOut:
        _stop = _STOP
        _list: Final = list
        _py_name = self.rename
        _translate = self._translate_inner
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


TEMPLATE_TEST_MODULE: Final = """\
{doc}
from __future__ import annotations

import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.{type} = {content}
"""
