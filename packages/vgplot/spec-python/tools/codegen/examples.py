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
import re
from typing import TYPE_CHECKING, Any, Final, Self

from typing_extensions import TypedDict

from tools.codegen.convert import KEYS_REPLACE
from tools.codegen.docstrings import doc
from tools.models.mosaic import _fix_ambiguous_unicode_characters
from tools.serde import read_yaml

if TYPE_CHECKING:
    from pathlib import Path

type Lit = bool | int | float | str | None
type Json = Lit | list[Json] | dict[str, Json]

# `msgspec` hits an error with the correct recursive type:
#   `RecursionError: Stack overflow (used 1952 kB) while analyzing a type`
type _JsonNoRecursion = (
    Lit | list[Lit | list[Any] | dict[str, Any]] | dict[str, Lit | list[Any] | dict[str, Any]]
)
type JsonSpec = dict[str, Json]


class _Meta(TypedDict, total=False):
    title: str
    description: str
    credit: str


class _Config(TypedDict, total=False):
    extensions: str | list[str]


class YamlSpec(TypedDict, total=False, extra_items=_JsonNoRecursion):
    meta: _Meta
    config: _Config
    data: dict[str, _JsonNoRecursion]
    params: dict[str, _JsonNoRecursion]
    plotDefaults: dict[str, _JsonNoRecursion]


_GROUP_1 = r"\g<1>"
_GROUP_2 = r"\g<2>"
_REPL_SNAKE = rf"{_GROUP_1}_{_GROUP_2}"
_PATTERN_UPPER_LOWER = re.compile(r"([A-Z]+)([A-Z][a-z])")
_PATTERN_LOWER_UPPER = re.compile(r"([a-z])([A-Z])")


def _pascal_to_snake_case(s: str) -> str:
    """Convert a PascalCase string to snake_case.

    Adapted from https://github.com/pydantic/pydantic/blob/f7a9b73517afecf25bf898e3b5f591dffe669778/pydantic/alias_generators.py#L43-L62
    """
    # Handle the sequence of uppercase letters followed by a lowercase letter
    snake = _PATTERN_UPPER_LOWER.sub(_REPL_SNAKE, s)
    # Insert an underscore between a lowercase letter and an uppercase letter
    return _PATTERN_LOWER_UPPER.sub(_REPL_SNAKE, snake).lower()


_GET_KEY = KEYS_REPLACE.get


@functools.cache
def _py_name(s: str, /) -> str:
    return _GET_KEY(s) or _pascal_to_snake_case(s)


@functools.singledispatch
def _from_json(obj: Json, /) -> Json:
    return obj


@_from_json.register(list)
def _(obj: list[Json], /) -> list[Json]:
    return [_from_json(el) for el in obj]


@_from_json.register(dict)
def _(obj: dict[str, Json], /) -> dict[str, Json]:
    return {_py_name(k): _from_json(v) for k, v in obj.items()}


class Example:
    title: str
    description: str
    source: Path
    converted: dict[str, Json]

    @classmethod
    def _extract_meta(cls, spec: YamlSpec) -> tuple[str, str]:
        if meta := spec.pop("meta", None):
            description = meta.pop("description", "")
            if credit := meta.pop("credit", None):
                if description:
                    description = f"{description}\n\n## Credit\n{credit}"
                else:
                    description = f"## Credit\n{credit}"

            # NOTE: Missing cases may want to use file name
            return _fix_ambiguous_unicode_characters(
                meta.pop("title", "TODO: missing title")
            ), _fix_ambiguous_unicode_characters(description)
        return "TODO: missing meta", ""

    @classmethod
    def from_path(cls, source: Path) -> Self:

        # NOTE: `extra_items` isn't supported in msgspec (iirc)
        spec: YamlSpec = read_yaml(source, Any)
        self = cls.__new__(cls)
        self.source = source
        self.title, self.description = cls._extract_meta(spec)
        self.converted = {_py_name(k): _from_json(v) for k, v in spec.items()}
        return self

    def render(self) -> str:
        return TEMPLATE.format(
            doc=doc(f"{self.title.removesuffix('.')}.\n\n{self.description}\n"),
            content=self.converted,
        )


TEMPLATE: Final = """\
{doc}
from __future__ import annotations

import mosaic_spec as ms


def test_infer() -> None:
    _spec: ms.Spec = {content}

"""
