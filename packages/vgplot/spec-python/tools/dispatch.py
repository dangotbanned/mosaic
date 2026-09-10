from __future__ import annotations

import contextlib
import copy
import types
from collections.abc import Callable, Iterator
from functools import partial
from types import FunctionType
from typing import TYPE_CHECKING, Any, Protocol, final, overload

if TYPE_CHECKING:

    class Deferred(Protocol):
        def __call__[R](self, f: Callable[..., R], /) -> JustDispatch[R]: ...


__all__ = ["just_dispatch"]

type _Registry[R] = dict[type[Any], Callable[..., R]]

_URL = "https://docs.astral.sh/ty/reference/typing-faq/#why-does-ty-say-callable-has-no-attribute-__name__"


class _Base[R]:
    __slots__ = ("_decorated_name", "_registry", "_upper_bound")

    def __init__(self, function: Callable[..., R], /, upper_bound: type[Any]) -> None:
        if not isinstance(function, FunctionType):
            msg = (
                f"Expected unreachable, but got a true error for: {_URL}\n\nCaused by {function!r}"
            )
            raise TypeError(msg)
        self._decorated_name: str = function.__name__
        self._upper_bound: type[Any] = upper_bound
        self._registry: _Registry[R] = {upper_bound: function}

    @property
    def registry(self) -> types.MappingProxyType[type[Any], Callable[..., R]]:
        return types.MappingProxyType(self._registry)

    def dispatch(self, tp: type[Any], /) -> Callable[..., R]:
        """Get the implementation for a given type."""
        if f := self._registry.get(tp):
            return f
        if issubclass(tp, self._upper_bound):
            f = self._registry[tp] = self._registry[self._upper_bound]
            return f
        msg = f"{self._decorated_name!r} does not support {tp.__name__!r}"
        raise TypeError(msg)

    def register[Fn: Callable[..., Any]](
        self, tp: type[Any], *tps: type[Any]
    ) -> Callable[[Fn], Fn]:
        """Register types to dispatch via the decorated function."""

        def decorate(f: Fn, /) -> Fn:
            self._registry.update((tp_, f) for tp_ in (tp, *tps))
            return f

        return decorate

    @contextlib.contextmanager
    def context(
        self, change_the_world: Callable[[_Registry[R]], _Registry[R]], /
    ) -> Iterator[None]:
        """Context manager to temporarily change the dispatch algorithm.

        The original state will be restored on exit.
        """
        reg = self._registry
        temp = copy.deepcopy(reg)

        self._registry = change_the_world(reg)
        try:
            yield
        finally:
            self._registry = temp
            del temp, reg


@final
class JustDispatch[R](_Base[R]):
    __slots__ = ()

    def __call__(self, arg: object, *args: Any, **kwds: Any) -> R:
        """Dispatch on the type of the first argument, passing through all arguments."""
        return self.dispatch(arg.__class__)(arg, *args, **kwds)


@overload
def just_dispatch[R](function: Callable[..., R], /) -> JustDispatch[R]: ...
@overload
def just_dispatch(*, upper_bound: type[Any] = object) -> Deferred: ...
def just_dispatch[R](
    function: Callable[..., R] | None = None, /, *, upper_bound: type[Any] = object
) -> JustDispatch[R] | Deferred:
    """Transform a function into a single-dispatch generic function.

    - A variant of, a variant of [@functools.singledispatch][1]
    - Almost identical to [@just_dispatch][2]

    [1]: https://docs.python.org/3/library/functools.html#functools.singledispatch
    [2]: https://github.com/narwhals-dev/narwhals/pull/3410
    """
    if function is not None:
        return JustDispatch(function, upper_bound)
    return partial(JustDispatch[Any], upper_bound=upper_bound)
