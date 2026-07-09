from __future__ import annotations

from typing import Any


class todo:
    """A descriptor that raises a `NotImplementedError` on attribute access.

    Ported from [narwhals](https://github.com/narwhals-dev/narwhals/blob/c57e72c801b5817dc9d20262029fc6c6143c31b2/src/narwhals/_plan/common.py#L321-L338)
    """

    __slots__ = ("__name__", "_name_owner", "_reason")

    def __init__(self, reason: str = "", /) -> None:
        self._reason: str = reason

    def __set_name__(self, owner: type[Any], name: str) -> None:
        self._name_owner: str = owner.__name__
        self.__name__: str = name

    def __get__(self, instance: object | None, owner: type[Any] | None, /) -> Any:
        if instance is None:
            return self
        msg = f"TODO: `{self._name_owner}.{self.__name__}`"
        if why := self._reason:
            msg = f"{msg}\n    {why}"
        raise NotImplementedError(msg)
