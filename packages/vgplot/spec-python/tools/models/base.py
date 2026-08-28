from collections.abc import Callable, Collection, Iterator
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Final,
    NewType,
    Self,
    TypeIs,
    dataclass_transform,
    overload,
)

import msgspec

type DefName = str
"""The name that keys the schema in `{"definitions": {<here>: ...}}`."""

IdName = NewType("IdName", str)
"""The unique name for a `Root`."""

if TYPE_CHECKING:
    # https://github.com/python/typeshed/pull/12309
    from _collections_abc import dict_items, dict_keys


class Struct(msgspec.Struct, omit_defaults=True, repr_omit_defaults=True):
    """`omit_defaults=True, repr_omit_defaults=True`."""

    if TYPE_CHECKING:
        # NOTE: All are defined at runtime and documented
        # Some aren't in the typing but all are missing for `ty`
        __slots__ = ()
        __struct_defaults__: ClassVar[tuple[Any, ...]]
        __struct_encode_fields__: ClassVar[tuple[str, ...]]

        def __copy__(self) -> Self: ...


# TODO @dangotbanned: Switch to using a variation of `FrozenHashableMeta` as a metaclass
# The diff right now will be huge and pointless
class FrozenStruct(msgspec.Struct, frozen=True, omit_defaults=True, repr_omit_defaults=True):
    """`frozen=True, omit_defaults=True, repr_omit_defaults=True`."""

    # NOTE: > "Frozen dataclass cannot inherit from non-frozen dataclass"
    if TYPE_CHECKING:
        __slots__ = ()
        __struct_defaults__: ClassVar[tuple[Any, ...]]
        __struct_encode_fields__: ClassVar[tuple[str, ...]]

        def __copy__(self) -> Self: ...


_KWDS_FROZEN_CACHE_HASH: Final = {
    "cache_hash": True,
    "frozen": True,
    "kw_only": True,
    "tag": True,
    "tag_field": "tag",
    "omit_defaults": True,
    "repr_omit_defaults": True,
}


@dataclass_transform(field_specifiers=(msgspec.field,), frozen_default=True, kw_only_default=True)
class FrozenHashableMeta(msgspec.StructMeta):
    """Custom `msgspec.Struct` metaclass.

    Similar to writing this definition:

    ```py
    import msgspec


    class SomeClass(
        msgspec.Struct,
        cache_hash=True,
        frozen=True,
        kw_only=True,
        tag=True,
        tag_field="tag",
        omit_defaults=True,
        repr_omit_defaults=True,
    ): ...
    ```

    But all keyword arguments will be inherited in subclasses.

    ## See Also
    https://msgspec.dev/api#msgspec.StructMeta
    """

    def __new__[FHM: FrozenHashableMeta](  # ruff: ignore[custom-type-var-for-self]
        mcls: type[FHM],
        name: str,
        bases: tuple[type, ...],
        namespace: dict[str, Any],
        **struct_config: Any,
    ) -> FHM:
        for k, v in _KWDS_FROZEN_CACHE_HASH.items():
            struct_config.setdefault(k, v)
        return super().__new__(mcls, name, bases, namespace, **struct_config)


# TODO @dangotbanned: Make a minimal repro for `pyrefly` getting this wrong
# NOTE: This base class is required for `pyrefly`
# Other type checkers understand the metaclass on it's own
@dataclass_transform(field_specifiers=(msgspec.field,), frozen_default=True, kw_only_default=True)
class FrozenHashableStruct(
    msgspec.Struct, omit_defaults=True, repr_omit_defaults=True, metaclass=FrozenHashableMeta
):
    if TYPE_CHECKING:
        __slots__ = ()
        __struct_defaults__: ClassVar[tuple[Any, ...]]
        __struct_encode_fields__: ClassVar[tuple[str, ...]]

        def __copy__(self) -> Self: ...


type Predicate = Callable[[Any], bool]
"""A function that returns a boolean."""

type Guard[T] = Callable[[Any], TypeIs[T]]
"""A predicate that provides type narrowing."""

type Entry[T] = tuple[DefName, T]
"""An named definition."""


class Root[D](Struct, kw_only=True):
    """A top-level context for managing definitions.

    Provides some common tools that any conversion stage can use for ergonomics.
    """

    id: IdName = IdName("")
    definitions: dict[DefName, D]

    def __repr__(self) -> str:
        # NOTE: Fallback used to keep bound method reprs small
        tp = self.__class__
        module_name = tp.__module__.removeprefix("tools.models.")
        return f"{module_name}.{tp.__name__}{self._describe(names=False)}"

    def _describe(self, *, length: bool = True, names: bool = True) -> str:
        header = f"<id: {self.id}, defs: {len(self.definitions)}>" if length else f"<id: {self.id}>"
        if not names:
            return header
        return f"{header}\n    {list(self.definitions)!r}"

    @overload
    def iter_defs[R](self, predicate: Guard[R], /) -> Iterator[Entry[R]]: ...
    @overload
    def iter_defs(self, predicate: Predicate | None = None, /) -> Iterator[Entry[D]]: ...
    def iter_defs[R](
        self, predicate: Guard[R] | Predicate | None = None, /
    ) -> Iterator[Entry[R | D]]:
        """Iterate over the definitions in this context.

        Args:
            predicate: Optionally, yield defs that satisfy `predicate(D)`.

                For improved type inference, write this as a function that returns
                [`TypeIs[R]`](https://typing.python.org/en/latest/spec/narrowing.html#typeis).
        """
        entries = self.definitions.items()
        if predicate is None:
            yield from entries
            return
        yield from ((name, defn) for name, defn in entries if predicate(defn))

    def __getitem__(self, name: DefName, /) -> D:
        """Get definition `name`."""
        return self.definitions.__getitem__(name)

    def get_typed[R](self, name: DefName, tp: type[R], /) -> R:
        """Get definition `name`, raising if it is not of type `tp`."""
        defn = self[name]
        if not isinstance(defn, tp):
            msg = f"Expected {name!r} to be of type {tp.__name__!r}, got:\n{defn!r}"
            raise TypeError(msg)
        return defn

    def pop(self, name: DefName, /) -> D:
        """Remove definition `name` and return it.

        If `name` is not found, raise a KeyError.
        """
        return self.definitions.pop(name)

    def def_names(self) -> dict_keys[DefName, D]:
        return self.definitions.keys()

    def def_items(self) -> dict_items[DefName, D]:
        return self.definitions.items()

    def iter_defs_by_name(self, names: Collection[DefName], /) -> Iterator[Entry[D]]:
        defs = self.definitions
        if (len_names := len(names)) == 1:
            for name in names:
                yield name, defs[name]
            return
        elif (len_names / len(defs)) < 0.1:
            get = defs.__getitem__
            for name in names:
                yield name, get(name)
            return
        for name, node in defs.items():
            if name in names:
                yield name, node
