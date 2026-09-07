from __future__ import annotations

import enum
import operator
import typing as t
from collections.abc import Collection
from itertools import chain
from typing import Literal as L, Self

from tools import ds
from tools.codegen.convert import py_identifier
from tools.codegen.docstrings import doc
from tools.common import PyIdentifier, PyIdentifierSnake, copy_replace
from tools.ir.pyir import special as sf
from tools.ir.pyir.base import (
    INDENT,
    Definition,
    Expr,
    IterExprs,
    Lines,
    RefRepl,
    RuntimeScope,
    TypedExtRef,
    TypedRef,
    join_comma,
)
from tools.ir.pyir.field import Field

if t.TYPE_CHECKING:
    import collections.abc as cabc
    from collections.abc import Iterable, Iterator

    from tools.ir.pyir.type_param import TypeVar

type OneOrIterable[T] = T | t.Iterable[T]
type _IntoMap[K, V] = cabc.Mapping[K, V] | Iterable[tuple[K, V]]
type IntoFields = _IntoMap[PyIdentifierSnake, Field]

_E = t.TypeVar("_E", bound=Expr, default=Expr, covariant=True)


@t.final
class TypeAlias(Definition, t.Generic[_E]):  # ruff: ignore[non-pep695-generic-class]
    """A representation of a TypeAliasType."""

    expr: t.Final[RuntimeScope[_E]]
    type_params: RuntimeScope[tuple[TypeVar, ...]] = ()

    _ALIAS: t.ClassVar[L["TypeAliasType", "TypeAlias"]] = "TypeAliasType"

    def iter_lines(self) -> Lines:
        params = f", {self.expr}"
        if type_params := self.type_params:
            params = f", type_params = {join_comma(tp.as_ref() for tp in type_params)}"
        yield f"{self.name} = {self._ALIAS}({self.name!r}{params})"
        if self.doc:
            yield doc(self.doc)

    def iter_exprs(self) -> IterExprs:
        yield from self.expr.iter_exprs()
        for param in self.type_params:
            yield from param.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> Self | TypeAlias:
        current = self.expr
        expr_changed = self.expr.with_refs(repl)
        if not self.type_params:
            if current == expr_changed:
                return self
            return copy_replace(self, expr=expr_changed)
        changes: dict[str, t.Any] = {"expr": expr_changed} if current != expr_changed else {}
        params_changed = tuple(p.with_refs(repl) for p in self.type_params)
        if params_changed != self.type_params:
            changes["type_params"] = params_changed
        if not changes:
            return self
        return copy_replace(self, **changes)


@t.final
class NewTypeStr(Definition):
    """A representation of a NewType, where the runtime type is unconditionally `str`.

    `str` is the only use-case I have for `NewType`, so this'll do for now.
    """

    def iter_lines(self) -> Lines:
        yield f"{self.name} = NewType({self.name!r}, str)"
        if self.doc:
            yield doc(self.doc)

    def iter_exprs(self) -> IterExprs:
        yield from ()


# TODO @dangotbanned: Fix the field order being broken from the first `FrozenMap`
@t.final
class NamedTuple(Definition):
    """A representation of a `typing.NamedTuple`."""

    # requires `typing.NamedTuple` import
    fields: tuple[Field[Expr], ...]

    def iter_lines(self) -> Lines:
        yield f"class {self.name}(NamedTuple):"
        if self.doc:
            yield f'{INDENT}"""{self.doc}"""'
        for line in chain.from_iterable(fld.iter_lines() for fld in self.fields):
            yield f"{INDENT}{line}"

    def iter_exprs(self) -> IterExprs:
        for f in self.fields:
            yield from f.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> NamedTuple:
        changed = tuple(f.with_refs(repl) for f in self.fields)
        if self.fields == changed:
            return self
        return self.__replace__(fields=changed)


type BaseTD = sf.TypedDict | sf.Generic | TypedRef[OpenDict] | TypedExtRef[OpenDict]
"""Any type that is valid to use in the bases of a `TypedDict`.

Where one or more of these symbols appear as below:

```py
class TD(<BaseTD>, ...):...
```

## Important
This definition is *intentionally narrower* than what [the spec defines][1],
and is aimed to be an easier to understand subset.

In short:

1. By default, the `TypedDict` special-form will be the only type that is present.
2. Synthesizing a generic will add `Generic[T, ...]`.
3. Synthesizing a base class will add `<name of new base>`.

`OpenDict` and `Generic` can only be generated explicitly,
whereas `{Closed,Extra}Dict` are created during conversion of JSON Schema.

[1]: https://typing.python.org/en/latest/spec/typeddict.html#inheritance
"""

_get_key = operator.itemgetter(0)


class _Dict(Definition):
    fields: t.Final[ds.FrozenMap[PyIdentifierSnake, Field]]
    bases: RuntimeScope[tuple[BaseTD, ...]] = (sf.TYPED_DICT,)
    total: bool = False

    def keywords(self) -> Iterator[str]:
        """Keyword arguments, as defined [here](https://typing.python.org/en/latest/spec/typeddict.html#class-based-syntax)."""
        if not self.total:
            yield "total=False"

    def has_field(self, name: str, /) -> bool:
        """Check for the existence of a single field by name."""
        return self.fields.__contains__(name)

    def iter_fields_types(self) -> Iterator[Field]:
        yield from self.fields.values()

    def iter_lines(self) -> Lines:
        inheritance_list = join_comma(
            chain((base.as_base() for base in self.bases), self.keywords())
        )
        yield f"class {self.name}({inheritance_list}):"
        if self.doc:
            yield f'{INDENT}"""{self.doc}"""'
        for line in chain.from_iterable(
            f.iter_lines() for _, f in sorted(self.fields.items(), key=_get_key)
        ):
            yield f"{INDENT}{line}"

    def iter_exprs(self) -> IterExprs:
        for f in self.iter_fields_types():
            yield from f.iter_exprs()
        for base in self.bases:
            yield from base.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> Self:
        changes: dict[str, t.Any] = {}
        if fields_changed := {
            name: out
            for name, field in self.fields.items()
            if (out := field.with_refs(repl)) is not field
        }:
            changes["fields"] = self.fields.update(fields_changed)
        if self.bases != (sf.TYPED_DICT,):
            bases_changed = tuple(b.with_refs(repl) for b in self.bases)
            if self.bases != bases_changed:
                changes["bases"] = bases_changed
        if not changes:
            return self
        return copy_replace(self, **changes)


class Source(enum.Enum):
    PARENT = enum.auto()
    SELF = enum.auto()


@t.final
class OpenDict(_Dict):
    _FORMAT: t.ClassVar[str] = "_{name}Open"

    def with_child_closed(
        self, name: PyIdentifier, *, doc: L[Source.SELF] | str = "", fields: IntoFields = ()
    ) -> ClosedDict:
        """Return a new typed dict that inherits from `self`, preventing further subclassing."""
        return ClosedDict(
            name=name,
            fields=ds.frozenmap(fields),  # pyright: ignore[reportArgumentType]
            bases=(self.to_typed_ref(),),  # pyright: ignore[reportArgumentType]
            total=self.total,
            doc=self.doc if doc is Source.SELF else doc,
        )

    def with_child_open(
        self, name: PyIdentifier, *, doc: L[Source.SELF] | str = "", fields: IntoFields = ()
    ) -> OpenDict:
        """Return a new typed dict that inherits from `self`."""
        return OpenDict(
            name=name,
            fields=ds.frozenmap(fields),  # pyright: ignore[reportArgumentType]
            bases=(self.to_typed_ref(),),  # pyright: ignore[reportArgumentType]
            total=self.total,
            doc=self.doc if doc is Source.SELF else doc,
        )

    @classmethod
    def format_name(cls, original_name: PyIdentifier, /) -> PyIdentifier:
        return py_identifier(cls._FORMAT.format(name=original_name))


@t.final
class ClosedDict(_Dict):
    def keywords(self) -> Iterator[str]:
        yield from super().keywords()
        yield "closed=True"

    def with_parent(
        self, parent: OpenDict, name: PyIdentifier | str, *, doc: Source | str = Source.SELF
    ) -> OpenDict:
        """Return a new typed dict that inherits from `parent`.

        Field names which are shared with `parent` will be dropped in the result.
        """
        for base in parent.bases:
            if isinstance(base, sf.Generic):
                msg = f"TODO: Support inheriting from a generic parent:\n{parent!r}"
                raise NotImplementedError(msg)

        bases = (parent.to_typed_ref(),)
        match doc:
            case Source.PARENT:
                doc = parent.doc
            case Source.SELF:
                doc = self.doc
            case str():
                ...
            case _:
                t.assert_never(doc)

        parent_field_names = frozenset(parent.fields)
        fields = ds.frozenmap((k, v) for k, v in self.fields.items() if k not in parent_field_names)
        return OpenDict(
            name=py_identifier(name), fields=fields, bases=bases, total=self.total, doc=doc
        )

    def to_open(self) -> OpenDict:
        """Return a new typed dict that will be a parent for this one."""
        return OpenDict(
            name=OpenDict.format_name(self.name),
            fields=self.fields,
            bases=self.bases,
            total=self.total,
            doc=self.doc,
        )


@t.final
class ExtraDict(_Dict):
    extra_items: RuntimeScope[Expr]

    def keywords(self) -> Iterator[str]:
        yield from super().keywords()
        yield from self.extra_items.iter_lines()

    def iter_exprs(self) -> IterExprs:
        yield from super().iter_exprs()
        yield from self.extra_items.iter_exprs()

    def with_refs(self, repl: RefRepl, /) -> ExtraDict:
        out = super().with_refs(repl)
        extra_items = self.extra_items.with_refs(repl)
        if self.extra_items == extra_items:
            return out
        return out.__replace__(extra_items=extra_items)


def supertype(
    definitions: Iterable[ClosedDict],
    name: PyIdentifier | str,
    *,
    doc: str = "",
    bases: RuntimeScope[tuple[BaseTD, ...]] = (sf.TYPED_DICT,),
    exclude: OneOrIterable[str] = frozenset(),
) -> OpenDict:
    """Approximate a base class that all members of `definitions` can inherit from.

    ## Notes
    - This operation only makes sense if the common fields are non-generic
    - `exclude` should be used for discriminator/generic fields to preserve in children
        - For `MarkOptions`-derived, each `mark` field has unique documentation to preserve
    """
    it = iter(definitions)
    fields = next(it).fields
    first = frozenset(fields)
    common = set(first.difference(exclude if not isinstance(exclude, str) else (exclude,)))
    common.intersection_update(*(defn.fields for defn in it))
    if not common:
        msg = "`definitions` have 0 common fields"
        if isinstance(definitions, Collection):
            msg += f", got:\n{definitions!r}"
        raise TypeError(msg)
    fields = ds.frozenmap((k, v) for k, v in fields.items() if k in common)
    return OpenDict(name=py_identifier(name), fields=fields, bases=bases, doc=doc)
