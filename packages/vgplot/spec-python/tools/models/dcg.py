"""[datamodel-code-generator] artifacts.

[datamodel-code-generator]: https://github.com/koxudaxi/datamodel-code-generator
"""

from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING, Annotated as A, Any, ClassVar, Literal as L, Self, final, overload

import msgspec

from tools.models import base


class _FrozenStruct(msgspec.Struct, frozen=True, omit_defaults=True, repr_omit_defaults=True):
    """`frozen=True, omit_defaults=True, repr_omit_defaults=True`."""

    # NOTE: > "Frozen dataclass cannot inherit from non-frozen dataclass"
    if TYPE_CHECKING:
        __slots__ = ()
        __struct_defaults__: ClassVar[tuple[Any, ...]]
        __struct_encode_fields__: ClassVar[tuple[str, ...]]

        def __copy__(self) -> Self: ...


type ModuleName = L["css_styles", "interactors", "marks", "mosaic", "params", "transform", "typing"]
"""The stem of the module name that it was generated into."""


type TypeExpr = str
"""A string encoding a [type expression][1].

[1]: https://typing.python.org/en/latest/spec/annotations.html#type-and-annotation-expressions
"""


class EmitField(_FrozenStruct, frozen=True, kw_only=True, cache_hash=True):
    name: str = ""
    alias: str = ""
    original_name: str | None = None
    type: TypeExpr
    """The (python) type annotation as a string."""

    required: bool = False


class EmitModel(_FrozenStruct, frozen=True, kw_only=True):
    name: str
    """Name of the TypedDict."""

    module: ModuleName
    """The stem of the module name that it was generated into."""

    source_ref: str
    """URI within the schema.

    Real:

        'mosaic.json#/definitions/ColorScheme'

    Synthetic:

        'mosaic.json#/definitions/ChannelDomainSort/limit#-datamodel-code-generator-#-any...' # (+64 more)
    """

    source_path: tuple[str, ...]
    """The fragments within `source_ref` (ish).

    Real:

        ('definitions', 'ColorScheme')

    Synthetic:

        (
            "definitions",
            "ChannelDomainSort",
            "limit#-datamodel-code-generator-#-anyOf-#-special-#",
            "1#-datamodel-code-generator-#-array-#-special-#",
            "0",
        )
    """

    title: str | None = None
    """Only used twice?

    - Lo -> lo
    - Y1 -> y1
    """

    fields: A[tuple[EmitField, ...], msgspec.Meta(min_length=1)]
    """All of the fields defined for the TypedDict.

    `msgspec` doesn't support `tuple[EmitField, *tuple[EmitField,  ...]]`
    """


class EmitMetadataV1(base.Struct):
    """JSON output for `--emit-model-metadata`.

    [Pinned here](https://github.com/koxudaxi/datamodel-code-generator/pull/3443)
    """

    models: list[EmitModel]

    def convert_models(self) -> Root:
        """Lower the original output into a more useful representation.

        ## Notes
        - Each output has a single name
        - `"$ref"` paths are dropped
        - Outputs are grouped by module
        - Type aliases are split from their representation as a `EmitModel` with a single null field
        """
        from itertools import groupby
        from operator import attrgetter

        it = groupby(self.models, attrgetter("module"))
        modules = {name: Module.from_emit(name, models) for name, models in it}
        return Root(modules)


@final
class Field(_FrozenStruct, frozen=True, kw_only=True, cache_hash=True):
    """5360 fields."""

    name: str
    """895 unique names."""

    type_expr: TypeExpr
    """219 unique types.

    Or 207 if you unwrap `Required[...]`
    """

    required: bool = False
    """245 fields are required."""

    @classmethod
    def from_emit(cls, field: EmitField) -> Field:
        return Field(name=field.name, type_expr=field.type, required=field.required)


@final
class TypeAlias(base.Struct):
    """62 type aliases."""

    name: str
    type_expr: TypeExpr
    source_path: tuple[str, ...]

    @classmethod
    def from_emit(cls, model: EmitModel) -> TypeAlias:
        return TypeAlias(model.name, model.fields[0].type, model.source_path)


@final
class TypedDict(base.Struct):
    """172 models.

    Excludes extras from `x-base-open` and `_spec`.

    ## Ranked by number of fields
    ### Top 3

    1. `CSSStyles`: 508
    2. `Plot`: 216
    3. `PlotAttributes`: 215

    The 4th has "only" 81

    ### Field facts
    - Top 65 have >= 50 fields
    - Top 82 have >= 10 fields
        - Personally, I'd like to see as much as possible below this line
        - Major decision paralysis
    """

    name: str
    fields: tuple[Field, ...]
    source_path: tuple[str, ...]

    @classmethod
    def from_emit(cls, model: EmitModel) -> TypedDict:
        fields = tuple(Field.from_emit(fld) for fld in model.fields)
        return TypedDict(model.name, fields, model.source_path)


@final
class Module(base.Struct):
    name: ModuleName
    typed_dicts: dict[str, TypedDict]
    type_aliases: dict[str, TypeAlias]

    @classmethod
    def from_emit(cls, name: ModuleName, models: Iterable[EmitModel], /) -> Module:
        type_aliases = {}
        typed_dicts = {}
        for model in models:
            if model.fields[0].original_name is None:
                alias = TypeAlias.from_emit(model)
                type_aliases[alias.name] = alias
            else:
                typed_dict = TypedDict.from_emit(model)
                typed_dicts[typed_dict.name] = typed_dict
        return Module(name, typed_dicts, type_aliases)


if TYPE_CHECKING:
    import polars as pl


@final
class Root(base.Struct):
    modules: dict[ModuleName, Module]

    @overload
    def get(self, key: ModuleName) -> Module: ...
    @overload
    def get(self, key: tuple[ModuleName, str]) -> TypedDict | TypeAlias: ...
    def get(self, key: ModuleName | tuple[ModuleName, str]) -> Module | TypedDict | TypeAlias:
        if isinstance(key, tuple):
            module, member = key
            mod = self.modules[module]
            if td := mod.typed_dicts.get(member):
                return td
            return mod.type_aliases[member]
        return self.modules[key]

    def get_dict(self, key: str) -> TypedDict:
        for mod in self.modules.values():
            if td := mod.typed_dicts.get(key):
                return td
        raise KeyError(key)

    def iter_modules(self) -> Iterator[Module]:
        yield from self.modules.values()

    def iter_typed_dicts(self) -> Iterator[TypedDict]:
        for mod in self.modules.values():
            yield from mod.typed_dicts.values()

    def iter_fields(self) -> Iterator[Field]:
        for td in self.iter_typed_dicts():
            yield from td.fields

    def iter_field_types(self) -> Iterator[TypeExpr]:
        for td in self.iter_typed_dicts():
            for fld in td.fields:
                yield fld.type_expr

    # TODO @dangotbanned: Port over some EDA bits from notebook
    def describe(self) -> pl.DataFrame:
        """Gather some facts about this representation.

        ## Notes
        - How many models?
        - How many fields?
        - What inline types are there?
        - Schemas with overlapping fields
        """
        msg = f"TODO: {self.describe.__qualname__}()"
        raise NotImplementedError(msg)
