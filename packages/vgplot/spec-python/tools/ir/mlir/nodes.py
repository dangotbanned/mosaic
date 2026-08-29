from __future__ import annotations

import copy
import typing
from typing import Final, Self, final

from tools.models import base
from tools.models.base import Lit

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from tools.ir.mlir.common import RefMap
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
        # NOTE: One day someone will resolve https://discuss.python.org/t/make-replace-stop-interfering-with-variance-inference/96092
        return self.__replace__(doc=doc)  # ty: ignore[invalid-return-type] # pyrefly: ignore[bad-return]

    def with_ext_refs(self, ref_map: RefMap, /) -> Self | MLIR:
        return self


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


@final
class ExtReference(MLIR):
    """A reference to a symbol defined externally."""

    ext: IdName
    ref: DefName
    doc: str = ""

    def iter_ext_refs(self) -> Iterator[ExtReference]:
        yield self

    def to_ref(self) -> Reference:
        return Reference(ref=self.ref, doc=self.doc)


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
        # NOTE: https://discuss.python.org/t/make-replace-stop-interfering-with-variance-inference/96092
        return copy.replace(self, type=maybe_changed)  # pyrefly: ignore[bad-argument-type]


@final
class Field[T: MLIR = MLIR](_BaseType[T]):
    """An entry in a `*Dict` or `NamedTuple`."""

    name: str
    """The name of the field."""
    required: bool = False


class _BaseSeq[T: MLIR](_BaseType[T]): ...


class _BaseFields(_HasChildren):
    fields: tuple[Field, ...]
    doc: str = ""

    def iter_children(self) -> Iterator[MLIR]:
        yield from self.fields

    def with_ext_refs(self, ref_map: RefMap, /) -> Self:
        new_fields = tuple(fld.with_ext_refs(ref_map) for fld in self.fields)
        if self.fields == new_fields:
            return self
        # NOTE: https://discuss.python.org/t/make-replace-stop-interfering-with-variance-inference/96092
        return copy.replace(self, fields=new_fields)  # pyrefly: ignore[bad-argument-type]


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
