from __future__ import annotations

import operator
import typing
from typing import Final, Self, final

from tools import ds
from tools.common import copy_replace
from tools.models import base
from tools.models.base import Lit

if typing.TYPE_CHECKING:
    import collections.abc as cabc
    from collections.abc import Iterator

    from tools.ir.mlir.common import NameMap, RefMap
    from tools.models.base import DefName, IdName

# NOTE: Use this instead of importing `Any`, since we have one defined here
type Incomplete = typing.Any


class MLIR(base.FrozenHashableStruct):
    """Mid-level IR, representing something that's not quite JSON or Python."""

    doc: str

    def iter_children(self) -> Iterator[MLIR]:
        # `ast.iter_child_nodes`
        yield from ()

    def iter_descendants(self) -> Iterator[MLIR]:
        # `ast.walk`-ish
        yield self

    def iter_refs(self) -> Iterator[Reference]:
        """Yield all references owned by the current node.

        - If the node is a reference, it will yield itself.
        - References are not resolved.
        """
        yield from ()

    def iter_ext_refs(self) -> Iterator[ExtReference]:
        """Yield all external references owned by the current node."""
        yield from ()

    def with_doc(self, doc: str, /) -> Self:
        return copy_replace(self, doc=doc)

    def with_ext_refs(self, ref_map: RefMap, /) -> Self | MLIR:
        return self

    def find_replace(self, repl: cabc.Mapping[MLIR, MLIR], /) -> Self | MLIR:
        """Perform a deep substitution on the entire tree.

        ## Notes
        - If a parent node matches, it will not attempt to replace it's children
        - In other words, the largest match wins
        """
        return repl.get(self, self)

    def get_field(self, name: str, /) -> Field | None:
        """Return the field `name` if it exists."""
        return


@final
class Reference(MLIR):
    """A reference to a symbol defined in the same file.

    ## Differences from JSON Schema
    - `ref` stores the same name that is a key in `definitions`
    - A reference to an external symbol is **always** an `ExtReference`
    - External references have an additional **required** field, which identifies the external document

    ## Why?
    - Resolving a `Reference` becomes a simple lookup operation
    - Set operators can be used between a set of references and a `definitions` mapping
        - Repeatedly transforming documents (and creating new ones) can quickly produce many stale references
        - Checking for those cases are what this design is optimized for
    - Dependencies between documents are distinct from references that are self-contained
        - Same-document refs matter for python codegen *only* when they are used as a base class
            - The base must be defined before the child
        - External refs have the same constraint, but usage is primarily for typing-only imports
            - Circular imports are the main technical concern
    """

    ref: DefName
    doc: str = ""

    def iter_refs(self) -> Iterator[Reference]:
        yield self

    def to_ext_ref(self, ext: IdName, /) -> ExtReference:
        return ExtReference(ext=ext, ref=self.ref, doc=self.doc)

    def with_ext_refs(self, ref_map: RefMap, /) -> Reference | ExtReference:
        if ext := ref_map(self.ref):
            return self.to_ext_ref(ext)
        return self


def ref(name: DefName, /) -> Reference:
    return Reference(ref=name)


@final
class ExtReference(MLIR):
    """A reference to a symbol defined externally."""

    ext: IdName
    ref: DefName
    doc: str = ""

    def iter_ext_refs(self) -> Iterator[ExtReference]:
        yield self


@final
class Any(MLIR):
    doc: str = ""


@final
class Unknown(MLIR):
    doc: str = ""


class PyBuiltin(MLIR):
    doc: str = ""


@final
class PyStr(PyBuiltin): ...


@final
class PyInt(PyBuiltin): ...


@final
class PyFloat(PyBuiltin): ...


@final
class PyBool(PyBuiltin): ...


@final
class PyNone(PyBuiltin): ...


@final
class PyTrue(MLIR):
    doc: str = ""


@final
class PyFalse(MLIR):
    doc: str = ""


type LiteralMember = Lit | PyTrue | PyFalse | PyNone


@final
class Literal(MLIR):
    members: tuple[LiteralMember, ...]
    doc: str = ""


@final
class EmptyTuple(MLIR):
    doc: str = ""


class _HasChildren(MLIR):
    def iter_descendants(self) -> Iterator[MLIR]:
        # `ast.walk`-ish
        yield self
        for child in self.iter_children():
            yield from child.iter_descendants()

    def iter_refs(self) -> Iterator[Reference]:
        for child in self.iter_children():
            yield from child.iter_refs()

    def iter_ext_refs(self) -> Iterator[ExtReference]:
        for child in self.iter_children():
            yield from child.iter_ext_refs()


class _BaseType[T: MLIR](_HasChildren):
    type: Final[T]
    doc: str = ""

    def iter_children(self) -> Iterator[MLIR]:
        yield self.type

    def with_ext_refs(self, ref_map: RefMap, /) -> Self:
        current = self.type
        maybe_changed = self.type.with_ext_refs(ref_map)
        if current == maybe_changed:
            return self
        return copy_replace(self, type=maybe_changed)

    def find_replace(self, repl: cabc.Mapping[MLIR, MLIR], /) -> Self | MLIR:
        if replaced := repl.get(self):
            return replaced
        current = self.type
        maybe_changed = current.find_replace(repl)
        if maybe_changed is current:
            return self
        return copy_replace(self, type=maybe_changed)


@final
class Field[T: MLIR = MLIR](_BaseType[T]):
    """An entry in a `*Dict` or `NamedTuple`."""

    required: bool = False

    def with_type[M: MLIR = MLIR](self, type: M, /) -> Field[M]:  # ruff: ignore[builtin-argument-shadowing]
        return copy_replace(self, type=type)


@final
class Mapping[T: MLIR = MLIR](_BaseType[T]):
    """Special-case of `ExtraDict`, with only `extra_items`."""


class _BaseSeq[T: MLIR](_BaseType[T]): ...


_get_name = operator.itemgetter(0)


class _BaseFields(_HasChildren):
    fields: Final[ds.FrozenMap[str, Field]]
    doc: str = ""

    def iter_children(self) -> Iterator[MLIR]:
        yield from self.fields.values()

    def iter_fields_names(self) -> Iterator[str]:
        yield from self.fields

    def iter_fields_types(self) -> Iterator[Field]:
        yield from self.fields.values()

    def iter_fields_items(self) -> Iterator[tuple[str, Field]]:
        yield from self.fields.items()

    def with_ext_refs(self, ref_map: RefMap, /) -> Self:
        changes = {}
        for name, field in self.fields.items():
            field_out = field.with_ext_refs(ref_map)
            if field_out is not field:
                changes[name] = field_out
        if not changes:
            return self
        return copy_replace(self, fields=self.fields.update(changes))

    def find_replace(self, repl: cabc.Mapping[MLIR, MLIR], /) -> Self | MLIR:
        if replaced := repl.get(self):
            return replaced
        changes = {
            name: out
            for name, field in self.fields.items()
            if (out := field.find_replace(repl)) is not field
        }
        if not changes:
            return self
        return copy_replace(self, fields=self.fields.update(changes))

    def rename_fields(self, overrides: NameMap, /) -> Self:
        # TODO @dangotbanned: Redo the param type
        # this is optimized for the tuple version
        new_names = {
            idx: changed for idx, name in enumerate(self.fields) if (changed := overrides(name))
        }
        if not new_names:
            return self
        fields = ds.frozenmap(
            (new_names.get(idx, name), field)
            for idx, (name, field) in enumerate(self.fields.items())
        )
        return copy_replace(self, fields=fields)

    def merge_fields(self, updates: cabc.Mapping[str, Field]) -> Self:
        return copy_replace(self, fields=self.fields.update(updates))

    def get_field(self, name: str, /) -> Field | None:
        return self.fields.get(name)

    def __rich_repr__(self) -> Iterator[tuple[str, typing.Any]]:
        # NOTE: Resolving 2 problems
        # 1. `rich` renders `rpds.HashTrieMap` as a single line.
        #    This doesn't mix well with 40-500 fields
        # 2. `rpds.HashTrieMap` appears to be either unordered,
        #    or it is defined but seeded by something that I can't control
        # Being unordered is okay, just need to sort things later
        yield "fields", dict(sorted(self.iter_fields_items(), key=_get_name))
        yield "doc", self.doc


@final
class Sequence[T: MLIR](_BaseSeq[T]):
    """A sequence where all elements are the same type."""


@final
class HomogeneousTuple[T: MLIR, N: int](_BaseSeq[T]):
    """A sequence where all elements are the same type and has a fixed-length.

    ## Notes
    Python's tuple is *heterogeneous*, but in `mosaic-schema.json` there are no cases of them
    """

    length: N


@final
class VariantHomogeneousTuple[T: MLIR, Ns: tuple[int, ...]](_BaseSeq[T]):
    """A sequence where all elements are the same type and has one of the lengths specified in `Ns`.

    ## Notes
    Represents `min: int, max: int`, which in Python means `tuple[T, T] | tuple[T, T, T] | ...`
    """

    lengths: Ns


@final
class NamedTuple(_BaseFields):
    """A tuple with `Annotated` field names."""


@final
class OpenDict(_BaseFields):
    """A `TypedDict` with the default configuration.

    `bases`, `total` will be in the next IR.
    """


@final
class ClosedDict(_BaseFields):
    """A `TypedDict` with `closed=True`."""


@final
class ExtraDict(_BaseFields):
    """A `TypedDict` with `extra_items`."""

    extra_items: MLIR

    def iter_children(self) -> Iterator[MLIR]:
        yield from super().iter_children()
        yield self.extra_items

    def with_ext_refs(self, ref_map: RefMap, /) -> ExtraDict:
        out = super().with_ext_refs(ref_map)
        extra_items = self.extra_items.with_ext_refs(ref_map)
        if self.extra_items == extra_items:
            return out
        return out.__replace__(extra_items=extra_items)

    def find_replace(self, repl: cabc.Mapping[MLIR, MLIR], /) -> Self | MLIR:
        out = super().find_replace(repl)
        extra_items = self.extra_items.find_replace(repl)
        if extra_items is self.extra_items:
            return out
        if not isinstance(out, ExtraDict):
            msg = (
                f"Cannot satisfy both replacements.\n\n"
                f"{self.__class__.__name__!r}\n-> {out.__class__.__name__!r}\n    {out!r}"
                f"{self.extra_items!r}\n-> {extra_items}"
            )
            raise TypeError(msg)
        return out.__replace__(extra_items=extra_items)

    def __rich_repr__(self) -> Iterator[tuple[str, typing.Any]]:
        yield "fields", dict(sorted(self.iter_fields_items(), key=_get_name))
        yield "extra_items", self.extra_items
        yield "doc", self.doc


@final
class Union(_HasChildren):
    members: tuple[MLIR, ...]
    doc: str = ""

    def iter_children(self) -> Iterator[MLIR]:
        yield from self.members

    def with_ext_refs(self, ref_map: RefMap, /) -> Union:
        new_members = tuple(member.with_ext_refs(ref_map) for member in self.members)
        if self.members == new_members:
            return self
        return self.__replace__(members=new_members)

    def find_replace(self, repl: cabc.Mapping[MLIR, MLIR], /) -> Self | MLIR:
        if replaced := repl.get(self):
            return replaced
        new_members = tuple(member.find_replace(repl) for member in self.members)
        if self.members == new_members:
            return self
        return self.__replace__(members=new_members)


_TPS_DICT: Final = (ClosedDict, ExtraDict, OpenDict)


def is_dict(obj: Incomplete) -> typing.TypeIs[ClosedDict | ExtraDict | OpenDict]:
    """Return True if `obj` is one of the `TypedDict`-based `MLIR` nodes."""
    return isinstance(obj, _TPS_DICT)
