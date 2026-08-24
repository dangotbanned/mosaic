from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING, ClassVar, Protocol, Self, assert_never

from tools.ir.mlir.root import Root
from tools.ir.mlir.scopes import Matcher
from tools.models import config as cfg

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from tools.models.base import IdName

type RootsMut = deque[Root]


__all__ = ("Action", "from_config")


class Action(Protocol):
    """A mutating operation over a stack of [`tools.ir.mlir.Root`][].

    An `Action` can produce new `Root`s, update those that exist or remove them entirely.

    These traits define the shape of `run`, which requires the output of each `Action` to be collected before starting another.
    """

    def run(self, roots: RootsMut, /) -> Iterator[Root]: ...
    @property
    def kind(self) -> cfg.ActionKind: ...


class _Base[C: cfg._BaseAction]:
    __slots__ = ("matcher",)
    matcher: Matcher
    _kind: ClassVar[cfg.ActionKind]

    @property
    def kind(self) -> cfg.ActionKind:
        return self._kind

    @classmethod
    def from_config(cls, config: C) -> Self:
        self = cls.__new__(cls)
        self.matcher = Matcher.from_scopes(config.scope)
        return self

    def run(self, roots: RootsMut) -> Iterator[Root]:
        msg = f"{type(self).__name__}.{self.run.__name__}() is not yet implemented"
        raise NotImplementedError(msg)


class NewTree(_Base[cfg.NewTreeAction]):
    __slots__ = ("id_output",)
    id_output: IdName
    _kind = "new-tree"

    @classmethod
    def from_config(cls, config: cfg.NewTreeAction) -> Self:
        self = super().from_config(config)
        self.id_output = config.id
        return self


class Remove(_Base[cfg.RemoveAction]):
    _kind = "remove"

    def run(self, roots: RootsMut) -> Iterator[Root]:
        matcher = self.matcher
        for root in roots:
            if matcher.id.matches(root.id):
                if matcher.over == "definitions":
                    for def_name in tuple(name for name, _ in matcher.matching_definitions(root)):
                        root.pop(def_name)
                    yield root
                else:
                    msg = f"Using (action={self._kind!r}, over={matcher.over!r}) is not yet implemented."
                    raise NotImplementedError(msg)
            else:
                yield root


def from_config(configs: Sequence[cfg.Action], /) -> Iterator[tuple[int, Action]]:
    for idx, config in enumerate(configs):
        match config:
            case cfg.RemoveAction():
                item = Remove.from_config(config)
            case cfg.NewTreeAction():
                item = NewTree.from_config(config)
            case cfg.AsRefAction():
                msg = f"TODO @dangotbanned: action='as-ref', got: {config!r}"
                raise NotImplementedError(msg)
            case _:
                assert_never(config)

        yield idx, item
