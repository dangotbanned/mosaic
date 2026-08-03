from __future__ import annotations

from collections.abc import Callable
from functools import partial
from types import FunctionType
from typing import TYPE_CHECKING, Any, Protocol, overload

if TYPE_CHECKING:

    class Deferred(Protocol):
        def __call__[R](self, f: Callable[..., R], /) -> TypeDispatch[R]: ...


__all__ = ["type_dispatch"]


class TypeDispatch[R]:
    __slots__ = ("_decorated_name", "_registry", "_upper_bound")

    def __init__(self, function: Callable[..., R], /, upper_bound: type[Any]) -> None:
        if not isinstance(function, FunctionType):
            msg = (
                f"Expected unreachable, but got a true error for: "
                f"https://docs.astral.sh/ty/reference/typing-faq/#why-does-ty-say-callable-has-no-attribute-__name__\n\n"
                f"Caused by {function!r}"
            )
            raise TypeError(msg)
        self._decorated_name: str = function.__name__
        self._upper_bound: type[Any] = upper_bound
        self._registry: dict[type[Any], Callable[..., R]] = {upper_bound: function}

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

    def __call__(self, arg: type[Any], *args: Any, **kwds: Any) -> R:
        """Dispatch on the first argument, passing through all arguments."""
        return self.dispatch(arg)(arg, *args, **kwds)


@overload
def type_dispatch[R](function: Callable[..., R], /) -> TypeDispatch[R]: ...
@overload
def type_dispatch(*, upper_bound: type[Any] = type) -> Deferred: ...
def type_dispatch[R](
    function: Callable[..., R] | None = None, /, *, upper_bound: type[Any] = type
) -> TypeDispatch[R] | Deferred:
    """Transform a function into a single-dispatch generic function.

    - A variant of, a variant of [@functools.singledispatch][1]
    - Almost identical to [@just_dispatch][2]

    The difference is from both is that the first argument is **already a type**.
    (Like `msgspec`'s [dec_hook][3])

    [1]: https://docs.python.org/3/library/functools.html#functools.singledispatch
    [2]: https://github.com/narwhals-dev/narwhals/pull/3410
    [3]: https://msgspec.dev/extending#mapping-to-from-native-types
    """
    if function is not None:
        return TypeDispatch(function, upper_bound)
    return partial(TypeDispatch[Any], upper_bound=upper_bound)
