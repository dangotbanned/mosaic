"""A limited representation of Python's type system & data model.

## Important
- No classes
- No objects
- No functions/methods/operators
- No AST
- Strictly, things that can be used in the generation of modules containing `TypedDict`s

## Loose structure
- `.definition` is the string representing the defining statement or suite
    - Like `"definitions"` this appears only once
- `.value` is the string representing a type expression (`[Ty]`])
    - Like `"$ref"`, this can appear multiple times
- `.expr` holds a `TypeExpr[Ty]` or a `TypeQualifier[Ty]`
"""

from __future__ import annotations

import typing as t
from pathlib import Path  # ruff: ignore[typing-only-standard-library-import]
from typing import LiteralString as LS  # ruff: ignore[camelcase-imported-as-acronym]

import msgspec

from tools import fs
from tools.models.base import Struct


@t.final
class Module(Struct):
    """A representation of a Python module.

    This is a stripped down version of [griffe.Module](https://mkdocstrings.github.io/griffe/reference/api/models/module/#griffe.Module).
    """

    name: str
    filepath: Path
    parent: Module | None = None

    @property
    def is_init_module(self) -> bool:
        return self.filepath.stem == "__init__"

    @property
    def is_package(self) -> bool:
        return (not self.parent) and self.is_init_module

    @property
    def is_subpackage(self) -> bool:
        return bool(self.parent) and self.is_init_module

    @property
    def canonical_path(self) -> str:
        if self.parent is None:
            return self.name
        return f"{self.parent.canonical_path}.{self.name}"

    @staticmethod
    def mosaic_spec() -> Module:
        """Return the (root) package."""
        return Module("mosaic_spec", fs.MOSAIC_SPEC_INIT)


class _Tagged(
    msgspec.Struct,
    tag=True,
    tag_field="tag_field",
    omit_defaults=True,
    repr_omit_defaults=True,
    frozen=True,
): ...


@t.final
class TypeExpr[Ty: LS = LS](_Tagged, frozen=True):
    """A representation of a type expression."""

    value: Ty

    def __str__(self) -> str:
        return self.value


@t.final
class Lit[Members: LS](_Tagged, frozen=True):
    # technically accepts more than `str`, but mosaic-spec doesnt use anything else
    members: tuple[Members, ...]

    @property
    def value(self) -> LS:
        return f"Literal[{','.join(self.members)}]"

    def __str__(self) -> LS:
        return self.value


class TypeQualifier[Ty: LS = LS](_Tagged, frozen=True):
    """A type expression wrapped with a [qualifier][1].

    [1]: https://typing.python.org/en/latest/spec/qualifiers.html#type-qualifiers
    """

    expr: TypeExpr[Ty]

    @property
    def value(self) -> str:
        return self.expr.value

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.expr}]"


@t.final
class Required[Ty: LS = LS](TypeQualifier[Ty], frozen=True):
    """Marks a Field as required."""


@t.final
class NotRequired[Ty: LS = LS](TypeQualifier[Ty], frozen=True):
    """Marks a Field as not required."""


@t.final
class ReadOnly[Ty: LS = LS](TypeQualifier[Ty], frozen=True):
    """Marks `extra_items` as read-only.

    I was hoping to avoid ReadOnly, limiting it to resolving this kind of error:

    > *"TypedDict `Closed1Extra1` must preserve mutable extra items from base `Extra1`"*
    """


@t.final
class TypeVar(_Tagged, frozen=True):
    """A representation of a TypeVar."""

    # - skipping default,
    # = skipping {co,contra}variance
    #   - use `infer_variance` iff there's a use-case
    name: str
    bound: TypeExpr | None = None
    constraints: tuple[TypeExpr, ...] = ()

    @property
    def definition(self) -> str:
        value = str(bound) if (bound := self.bound) else ", ".join(map(str, self.constraints))
        return f"{self.name} = TypeVar({self.name!r}, {value})"

    @property
    def value(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.definition


# NOTE: This would include {ParamSpec,TypeVarTuple}, but doubt they'll be needed
type TypeParam = TypeVar


@t.final
class TypeAlias[Ty: LS = LS](_Tagged, frozen=True):
    """A representation of a TypeAliasType."""

    name: str
    expr: TypeExpr[Ty]
    type_params: tuple[TypeParam, ...] = ()

    @property
    def definition(self) -> str:
        params = ""
        if type_params := self.type_params:
            params = f", ({','.join(tp.value for tp in type_params)})"
        return f"{self.name} = TypeAliasType({self.name!r}{params})"

    @property
    def value(self) -> str:
        return self.name


@t.final
class Field[Name: LS = LS, Ty: LS = LS](_Tagged, frozen=True):
    """A representation of an entry in a TypedDict."""

    name: Name
    expr: TypeExpr[Ty] | Required[Ty] | NotRequired[Ty]
    doc: str = ""

    def is_required(self) -> bool:
        return self.expr.__class__ is Required


def field[Name: LS = LS, Ty: LS = LS](name: Name, value: Ty, doc: str = "") -> Field[Name, Ty]:
    return Field[Name, Ty](name, TypeExpr(value), doc)


tp_expr = TypeExpr("int")
field_a = Field("a", tp_expr)

TE_BUILTINS = (
    TypeExpr("str"),
    TypeExpr("bool"),
    TypeExpr("float"),
    TypeExpr("int"),
    TypeExpr("None"),
)
TE_TYPING = TypeExpr("Any")


MAP_PRIMITIVE: t.Final = {
    "boolean": TypeExpr("bool"),
    "integer": TypeExpr("int"),
    "null": TypeExpr("None"),
    "number": TypeExpr("float"),
    "string": TypeExpr("str"),
}


class _SpecialForm(_Tagged, frozen=True): ...


@t.final
class _TypedDictSF(_SpecialForm, frozen=True):
    @property
    def value(self) -> t.Literal["TypedDict"]:
        return "TypedDict"


_TYPED_DICT: t.Final = _TypedDictSF()
"""Represents using the *symbol* `TypedDict`."""

type ValidBase = _TypedDictSF | OpenDict | ExtraDict
"""A huge simplification of what is allowed as a base class for TypedDict definitions.

The real thing is far too complex (see [typed_dict.rs][1]).

[1]: https://github.com/astral-sh/ruff/blob/7de420ecd242fdecf859c65b8ffdaaae339c9a54/crates/ty_python_semantic/src/types/typed_dict.rs
"""


@t.final
class OpenDict(_Tagged, frozen=True):
    """A representation of an open (default) TypedDict.

    https://typing.python.org/en/latest/spec/typeddict.html#openness
    """

    name: str
    fields: tuple[Field, ...]
    bases: tuple[ValidBase, ...]
    total: bool
    doc: str = ""


@t.final
class ClosedDict(_Tagged, frozen=True):
    """A representation of a closed TypedDict.

    https://typing.python.org/en/latest/spec/typeddict.html#openness
    """

    name: str
    fields: tuple[Field, ...]
    bases: tuple[ValidBase, ...]
    total: bool
    doc: str = ""


@t.final
class ExtraDict(_Tagged, frozen=True):
    """A representation of a TypedDict with [extra items][1].

    Similar to [additionalProperties][2].

    [1]: https://typing.python.org/en/latest/spec/glossary.html#term-extra-items
    [2]: https://json-schema.org/understanding-json-schema/reference/object#additionalproperties
    """

    name: str
    fields: tuple[Field, ...]
    bases: tuple[ValidBase, ...]
    total: bool
    extra_items: ReadOnly
    """Note: `extra_items` is used outside of an [annotation scope][1].

    [1]: https://docs.python.org/3/reference/executionmodel.html#annotation-scopes
    """
    doc: str = ""


def example() -> OpenDict:
    out = OpenDict(
        name="BrushStyles",
        fields=(
            field("fill", "str", "The fill color of the brush rectangle."),
            field("fill_opacity", "float", "The fill opacity of the brush rectangle."),
            field("opacity", "float", "The overall opacity of the brush rectangle."),
            field("stroke", "str", "The stroke color of the brush rectangle."),
            field("stroke_dasharray", "str", "The stroke dash array of the brush rectangle."),
            field("stroke_opacity", "float", "The stroke opacity of the brush rectangle."),
        ),
        bases=(_TYPED_DICT,),
        total=False,
        doc="Styles for rectangular selection brushes.",
    )
    return out  # ruff: ignore[unnecessary-assign]
