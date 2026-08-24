from __future__ import annotations

import typing
from typing import Final, Self, final

from tools.ir.json_wrapper import nodes as jw
from tools.models import base

if typing.TYPE_CHECKING:
    from collections.abc import Iterator

    from tools.common import snake_case
    from tools.models.base import DefName, IdName

# NOTE: Use this instead of importing `Any`, since we have one defined here
type Incomplete = typing.Any


class MLIR(base.FrozenStruct, frozen=True, tag=True, tag_field="tag", kw_only=True):
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


@final
class Reference(MLIR, frozen=True, kw_only=True, cache_hash=True):
    """A reference to a symbol defined in the same file."""

    ref: DefName
    doc: str = ""

    def iter_refs(self) -> Iterator[Reference]:
        yield self


@final
class ExtReference(MLIR, frozen=True, kw_only=True, cache_hash=True):
    """A reference to a symbol defined externally."""

    ext: IdName
    ref: DefName
    doc: str = ""

    def iter_ext_refs(self) -> Iterator[ExtReference]:
        yield self


@final
class Any(MLIR, frozen=True, kw_only=True):
    doc: str = ""


@final
class Unknown(MLIR, frozen=True, kw_only=True):
    doc: str = ""


class PyBuiltin(MLIR, frozen=True, kw_only=True):
    doc: str = ""


@final
class PyStr(PyBuiltin, frozen=True): ...


@final
class PyInt(PyBuiltin, frozen=True): ...


@final
class PyFloat(PyBuiltin, frozen=True): ...


@final
class PyBool(PyBuiltin, frozen=True): ...


@final
class PyNone(PyBuiltin, frozen=True): ...


# TODO @dangotbanned: `None` should be `PyNone`
# TODO @dangotbanned: `LitBool` should be `PyTrue`, `PyFalse`
type _LiteralMember = jw.Lit | jw.LitBool | None


@final
class Literal(MLIR, frozen=True, kw_only=True):
    members: tuple[_LiteralMember, ...]
    doc: str = ""


@final
class EmptyTuple(MLIR, frozen=True, kw_only=True):
    doc: str = ""


class _HasChildren(MLIR, frozen=True, kw_only=True):
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


class _BaseType[T: MLIR](_HasChildren, frozen=True, kw_only=True):
    type: Final[T]
    doc: str = ""

    def iter_children(self) -> Iterator[MLIR]:
        yield self.type


@final
class Field[T: MLIR = MLIR](_BaseType[T], frozen=True):
    """An entry in a `*Dict` or `NamedTuple`."""

    name: snake_case
    """The name of the field."""
    required: bool = False


class _BaseSeq[T: MLIR](_BaseType[T], frozen=True): ...


class _BaseFields(_HasChildren, frozen=True, kw_only=True):
    fields: tuple[Field, ...]
    doc: str = ""

    def iter_children(self) -> Iterator[MLIR]:
        yield from self.fields


@final
class Sequence[T: MLIR](_BaseSeq[T], frozen=True):
    """A sequence where all elements are the same type."""


@final
class HomogeneousTuple[T: MLIR, N: int](_BaseSeq[T], frozen=True, kw_only=True):
    """A sequence where all elements are the same type and has a fixed-length.

    ## Notes
    Python's tuple is *heterogeneous*, but in `mosaic-schema.json` there are no cases of them
    """

    length: N


@final
class VariantHomogeneousTuple[T: MLIR, Ns: tuple[int, ...]](_BaseSeq[T], frozen=True, kw_only=True):
    """A sequence where all elements are the same type and has one of the lengths specified in `Ns`.

    ## Notes
    Represents `min: int, max: int`, which in Python means `tuple[T, T] | tuple[T, T, T] | ...`
    """

    lengths: Ns


@final
class NamedTuple(_BaseFields, frozen=True):
    """A tuple with `Annotated` field names."""


@final
class OpenDict(_BaseFields, frozen=True):
    """A `TypedDict` with the default configuration.

    `bases`, `total` will be in the next IR.
    """


@final
class ClosedDict(_BaseFields, frozen=True):
    """A `TypedDict` with `closed=True`."""


@final
class ExtraDict(_BaseFields, frozen=True):
    """A `TypedDict` with `extra_items`."""

    extra_items: MLIR

    def iter_children(self) -> Iterator[MLIR]:
        yield from super().iter_children()
        yield self.extra_items


@final
class Union(_HasChildren, frozen=True, kw_only=True):
    members: tuple[MLIR, ...]
    doc: str = ""

    def iter_children(self) -> Iterator[MLIR]:
        yield from self.members
