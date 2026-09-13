import collections.abc as cabc
import typing as t
from collections.abc import Callable
from operator import attrgetter
from typing import Annotated as A, Literal as L

import msgspec
from msgspec import field

from tools.config.typing import OPEN_DICT_BASE_PATTERN
from tools.models.base import FrozenStruct


class AliasesTyping(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    Literal: L["Literal", "L", "Lit"] = "Literal"
    Annotated: L["Annotated", "A", "An", "Ann"] = "Annotated"
    TypeAliasType: L["TypeAliasType", "TypeAlias"] = "TypeAliasType"


class AliasesCollectionsAbc(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    Sequence: L["Sequence", "Seq"] = "Sequence"


class AliasesCollections(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    abc: AliasesCollectionsAbc = field(default_factory=AliasesCollectionsAbc)


class Aliases(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    typing: AliasesTyping = field(default_factory=AliasesTyping)
    """These aliases also apply for `typing_extensions`."""
    collections: AliasesCollections = field(default_factory=AliasesCollections)

    def get_alias(self, module: L["typing", "collections.abc"], name: str) -> str:
        return getattr(self._GET_SECTION[module](self), name, name)

    _GET_SECTION: t.ClassVar[
        t.Final[cabc.Mapping[L["typing", "collections.abc"], Callable[[t.Any], t.Any]]]
    ] = {"typing": attrgetter("typing"), "collections.abc": attrgetter("collections.abc")}


class Naming(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    aliases: Aliases = field(default_factory=Aliases)
    """Import target aliases for standard library types."""

    format_base: t.Final[A[str, msgspec.Meta(pattern=OPEN_DICT_BASE_PATTERN)]] = "_{name}Open"
    """A format string that produces a name for synthesized `OpenDict` base classes.

    Defaults to:

    ```py
    >>> format_base = "_{name}Open"
    >>> format_base.format(name="Line")
    '_LineOpen'
    ```

    An override must contain the `"{name}"` placeholder, and produce a [valid python identifier][1]:

    ```py
    "{name}Base"
    "Base{name}"
    "_{name}"
    "{name}"
    ```

    [1]: https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords
    """


class Types(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    str: L["NewType", "TypeAliasType"] = "TypeAliasType"
    """How to represent direct aliases of `str`.

    By default, an alias of `str` is represented as:

    ```py
    MyCoolString = TypeAliasType("MyCoolString", str)
    ```

    This is problematic when it appears in a union with a literal, as `str` swallows it:

    ```py
    def in_a_pickle(arg: Literal["1", "2", "3"] | MyCoolString) -> None:
        reveal_type(arg)  #  Revealed type: `str`
    ```

    `"NewType"` resolves this issue, but [requires more of the caller](https://typing.python.org/en/latest/spec/aliases.html#newtype):

    ```py
    MyCoolString = NewType("MyCoolString", str)

    def all good(arg: Literal["1", "2", "3"] | MyCoolString) -> None:
        reveal_type(arg)  #  Revealed type: `Literal["1", "2", "3"] | MyCoolString`

    all_good(MyCoolString("bad"))

    all_good("bad")  # Argument to function `all_good` is incorrect
    #        ^^^^^ Expected `Literal["1", "2", "3"] | MyCoolString`, found `Literal["bad"]`
    ```
    """

    NamedTuple: L["Annotated", "NamedTuple"] = "Annotated"
    """How to represent tuples that have names for each position."""


class ToPyIR(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    name: Naming = field(default_factory=Naming)
    """Naming conventions for generated code."""
    type: Types = field(default_factory=Types)
    """Opinionated type configuration.

    These are edge cases where both options have trade-offs.
    """
