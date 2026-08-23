"""Mid-level IR, representing something that's not quite JSON or Python.

- Not a full transition to python yet
    - But nodes are not allowed to keep a `schema` field
    - Anything useful must have been peeled off
- Missing things like
    - TypeVar/parameters
    - Type qualifiers
    - Type alias
    - Special forms (well some of them at least)
    - Generics
- Not 100% sure what to call this yet.
"""

from __future__ import annotations

import dataclasses

# ruff: file-ignore[builtin-argument-shadowing]
import functools
import typing
from collections import defaultdict, deque
from collections.abc import Iterator, Mapping
from typing import Final, NewType, Self, final

from tools.codegen.convert import pascal_to_snake_case
from tools.models import base, json_wrapper as jw
from tools.models.base import DefName

if typing.TYPE_CHECKING:
    from tools.common import snake_case

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

    ext: str
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


_JSON_PY_INST: Final[Mapping[jw.Scalar, PyBuiltin]] = {
    "boolean": PyBool(),
    "integer": PyInt(),
    "number": PyFloat(),
    "string": PyStr(),
    "null": PyNone(),
}
_JSON_PY_TYPE: Final[Mapping[jw.Scalar, type[PyBuiltin]]] = {
    "boolean": PyBool,
    "integer": PyInt,
    "number": PyFloat,
    "string": PyStr,
    "null": PyNone,
}


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

    @classmethod
    def from_json(
        cls,
        owner: DefName,
        name: jw.camelCase,
        type: jw.JsonWrapper,
        ctx: ConversionCtx,
        *,
        required: bool,
    ) -> Field:
        out_name = pascal_to_snake_case(name)
        out_type = _I_KNOW_WHAT_IM_DOING(type, owner, ctx)
        doc = out_type.doc
        out_type = out_type.with_doc("")
        ctx.add(out_type, owner)
        result = Field(name=out_name, type=out_type, required=required, doc=doc)
        ctx.add(result, owner)
        return result


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


Idx = NewType("Idx", int)


@dataclasses.dataclass
class ConversionCtx:
    """A history of what happened during `JsonWrapper` to `MLIR` conversion.

    ## Notes
    - Everything is traced, and serves as a descriptive tool to start with
    - Need to build things differently to take advantage of this
        - Making aliases for common types and replacing the duplication with references
        - Identifying when to synthesize base classes and or intersections
    """

    seen: defaultdict[type[MLIR], list[MLIR]] = dataclasses.field(
        default_factory=lambda: defaultdict(list)
    )
    """Per-MLIR-type to instances, ordered by creation time.

    Can answer questions like:
    - How frequently does each `type[MLIR]` appear?
    - What does each instance look like?
    - Do we have runs of similar/duplicated instances?
    """

    positions: defaultdict[DefName, deque[tuple[type[MLIR], Idx]]] = dataclasses.field(
        default_factory=lambda: defaultdict(deque)
    )
    """Per-top-level definition to keys into `seen`.

    Can answer questions like:
    - What does each definition produce?
    - Do we have more patterns in `seen` that are repeated across definitions?
    """

    def add(self, result: MLIR, owner: DefName, /) -> None:
        seen_key = type(result)
        seen_list = self.seen[seen_key]
        seen_list.append(result)
        idx = Idx(seen_list.__len__() - 1)
        self.positions[owner].append((seen_key, idx))

    def get_instances_of[M: MLIR](self, tp: type[M], /) -> list[M]:
        return typing.cast("list[M]", self.seen[tp])

    def get_instances_owned(self, owner: DefName, /) -> Iterator[MLIR]:
        seen_get = self.seen.__getitem__
        for tp, idx in self.positions[owner]:
            yield seen_get(tp)[idx]


@final
class DefInfo(base.Struct):
    """The mutable thing stored next to each top-level def.

    ## Notes
    - Definition
        - Each definition is a graph of immutable nodes
        - A definition is stored in a mutable structure (dict)
        - That dict provides the name and is stored in a mutable struct (Root)
    - All of this can be respected with changes triggering a replacement of the definition with a new one
    - Making sense of that means storing details about references
        - To allow moving node `A` to file x, we need to check for references **to** and **from** `A`
        - This can be computed for the full `definitions` dict on creation
        - Then subsequent changes are incremental
    """

    refs: set[Reference]
    ext_refs: set[ExtReference]

    @classmethod
    def from_def(cls, defn: MLIR, /) -> DefInfo:
        return DefInfo(refs=set(defn.iter_refs()), ext_refs=set(defn.iter_ext_refs()))

    def has_references(self) -> bool:
        return bool(self.refs or self.ext_refs)


@final
class Root(base.Root[MLIR], kw_only=True):
    def_infos: dict[str, DefInfo]

    def pop(self, name: DefName, /) -> MLIR:
        result = super().pop(name)
        del self.def_infos[name]
        return result

    def replace(self, name: DefName, defn: MLIR, /) -> None:
        """Replace an existing definition with an updated version.

        *Unconditionally* recomputes reference information based on the new version.
        """
        self.def_infos[name] = DefInfo.from_def(defn)
        self.definitions[name] = defn

    def replace_naive(self, name: DefName, defn: MLIR, /) -> None:
        """Replace an existing definition with an updated version.

        *Naive* as we assume that because the definition didn't start with references, it never will.
        """
        current_info = self.def_infos[name]
        if current_info.has_references():
            self.def_infos[name] = DefInfo.from_def(defn)
        self.definitions[name] = defn

    @classmethod
    def from_json_wrapper(cls, source: jw.Root, /) -> tuple[Root, ConversionCtx]:
        source.ref_unwrap()
        ctx = ConversionCtx()
        definitions: dict[DefName, MLIR] = {}
        def_infos: dict[str, DefInfo] = {}
        for name, schema in source.definitions.items():
            defn = definitions[name] = from_json(schema, name, ctx)
            def_infos[name] = DefInfo.from_def(defn)
        root = Root(id=source.id, definitions=definitions, def_infos=def_infos)
        return root, ctx


def from_json(obj: jw.JsonWrapper, owner: DefName, ctx: ConversionCtx, /) -> MLIR:
    """Convert a `JsonWrapper` to a `MLIR`.

    Args:
        obj: The object to convert.
        owner: The definition that we originated from.
            Used for error messages.
        ctx: Mutable state that records the conversion process.
    """
    result = _from_json_dispatch(obj, owner, ctx)
    ctx.add(result, owner)
    return result


@functools.singledispatch
def _from_json_dispatch(obj: jw.JsonWrapper, owner: DefName, ctx: ConversionCtx, /) -> MLIR:
    """Impl for `from_json`.

    Use this for registration only.
    """
    msg = f"Converting {obj.__class__.__name__!r} is not yet implemented, in {owner!r}\n\n{obj!r}"
    raise NotImplementedError(msg)


_I_KNOW_WHAT_IM_DOING: Final = _from_json_dispatch
"""A marker for rewrites inside of `from_json`.

The caller is responsible for recording the result in `ctx`, which allows things like:

- Replacing parts of the result
- De-duplicating members of a union
- Skipping things entirely
"""


@_from_json_dispatch.register(jw.EmptySequence)
def _(obj: jw.EmptySequence, _owner: DefName, _ctx: ConversionCtx, /) -> EmptyTuple:
    return EmptyTuple(doc=obj.description)


@_from_json_dispatch.register(jw.Unknown)
def _(obj: jw.Unknown, _owner: DefName, _ctx: ConversionCtx, /) -> Unknown:
    return Unknown(doc=obj.description)


_POUND_DEFS = "#/definitions/"


@_from_json_dispatch.register(jw.Reference)
def _(obj: jw.Reference, _owner: DefName, _ctx: ConversionCtx, /) -> Reference | ExtReference:
    ref = obj.ref
    if ref.startswith(_POUND_DEFS):
        return Reference(ref=ref.removeprefix(_POUND_DEFS), doc=obj.description)
    ext, ref = ref.split(_POUND_DEFS)
    return ExtReference(ref=ref, ext=ext, doc=obj.description)


@_from_json_dispatch.register(jw.Const)
@_from_json_dispatch.register(jw.Enum)
def _(obj: jw.Const | jw.Enum, _owner: DefName, _ctx: ConversionCtx, /) -> Literal:
    return Literal(members=tuple(obj.iter_values()), doc=obj.description)


@_from_json_dispatch.register(jw.Primitive)
def _(obj: jw.Primitive, _owner: DefName, _ctx: ConversionCtx, /) -> PyBuiltin:
    if doc := obj.description:
        return _JSON_PY_TYPE[obj.type](doc=doc)
    return _JSON_PY_INST[obj.type]


@_from_json_dispatch.register(jw.PrimitiveUnion)
def _(obj: jw.PrimitiveUnion, _owner: DefName, _ctx: ConversionCtx, /) -> Union:
    return Union(members=tuple(_JSON_PY_INST[t] for t in obj.types), doc=obj.description)


@_from_json_dispatch.register(jw.Sequence)
def _(
    obj: jw.Sequence, owner: DefName, ctx: ConversionCtx, /
) -> Sequence[MLIR] | HomogeneousTuple[MLIR, int] | VariantHomogeneousTuple[MLIR, tuple[int, ...]]:
    doc = obj.description
    type = from_json(obj.items, owner, ctx)
    match (obj.min, obj.max):
        case (0, None):
            result = Sequence(type=type, doc=doc)
        case (minimum, maximum) if minimum == maximum:
            result = HomogeneousTuple(type=type, length=minimum, doc=doc)
        case (minimum, int() as maximum):
            # NOTE: `Lag.lag` should be min 1, max 3 and datamodel-code-generator gets that wrong
            result = VariantHomogeneousTuple(
                type=type, lengths=tuple(range(minimum, maximum + 1)), doc=doc
            )
        case _:
            # NOTE: could be representable in python as `tuple[T, Min, *tuple[T, ...]]`
            # We don't have any cases like it yet though
            msg = f"Didn't expect to see ({(obj.min, obj.max)!r}) in {owner!r}\n\n{obj!r}"
            raise NotImplementedError(msg)
    return result


@_from_json_dispatch.register(jw.NamedSequence)
def _(obj: jw.NamedSequence, owner: DefName, ctx: ConversionCtx, /) -> NamedTuple:
    fields = tuple(
        Field.from_json(owner, f_name, f_type, ctx, required=True)
        for f_name, f_type in obj.fields.items()
    )
    return NamedTuple(fields=fields, doc=obj.description)


# TODO @dangotbanned: Report pyrefly bug for `None` case (failed to narrow after trying the cheap cases)
@_from_json_dispatch.register(jw.Object)
def _(obj: jw.Object, owner: DefName, ctx: ConversionCtx, /) -> OpenDict | ClosedDict | ExtraDict:
    # Having `required` paired with each field removes a surface to sync
    is_required = frozenset(obj.required).__contains__
    fields = tuple(
        Field.from_json(owner, f_name, f_type, ctx, required=is_required(f_name))
        for f_name, f_type in obj.fields.items()
    )
    doc = obj.description
    match obj.closed, obj.extra_items:
        case (None, None):
            result = OpenDict(fields=fields, doc=doc)
        case ("closed", None):
            result = ClosedDict(fields=fields, doc=doc)
        case (None, extra):
            result = ExtraDict(fields=fields, extra_items=from_json(extra, owner, ctx), doc=doc)  # pyrefly: ignore[bad-argument-type]
        case _:
            msg = f"Cannot combine closed={obj.closed!r} and extra_items={obj.extra_items!r} in {owner!r}\n\n{obj!r}"
            raise TypeError(msg)
    return result


@_from_json_dispatch.register(jw.Union)
def _(obj: jw.Union, owner: DefName, ctx: ConversionCtx, /) -> Union:
    merge_literals = set()
    members = set[MLIR]()
    for member in obj.members:
        converted = _I_KNOW_WHAT_IM_DOING(member, owner, ctx)
        if (not converted.doc) and isinstance(converted, Literal):
            merge_literals.update(converted.members)
        else:
            members.add(converted)
    if merge_literals:
        members.add(Literal(members=tuple(merge_literals)))
    members_final = tuple(members)
    for member in members_final:
        ctx.add(member, owner)
    return Union(members=members_final, doc=obj.description)
