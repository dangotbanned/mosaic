from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Self

import msgspec


class Struct(msgspec.Struct, omit_defaults=True, repr_omit_defaults=True):
    """`omit_defaults=True, repr_omit_defaults=True`."""

    if TYPE_CHECKING:
        # NOTE: All are defined at runtime and documented
        # Some aren't in the typing but all are missing for `ty`
        __slots__ = ()
        __struct_defaults__: ClassVar[tuple[Any, ...]]
        __struct_encode_fields__: ClassVar[tuple[str, ...]]

        def __copy__(self) -> Self: ...


class FrozenStruct(msgspec.Struct, frozen=True, omit_defaults=True, repr_omit_defaults=True):
    """`frozen=True, omit_defaults=True, repr_omit_defaults=True`."""

    # NOTE: > "Frozen dataclass cannot inherit from non-frozen dataclass"
    if TYPE_CHECKING:
        __slots__ = ()
        __struct_defaults__: ClassVar[tuple[Any, ...]]
        __struct_encode_fields__: ClassVar[tuple[str, ...]]

        def __copy__(self) -> Self: ...
