from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Generic, Literal as L, final

from mosaic_spec._typing_compat import TypeAliasType, TypedDict, TypeVar, Unpack

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from mosaic_spec._gen.inputs import Options as Option
    from tests.apis.params import Param, Selection


# NOTE: Will reuse the options on the Param-side (e.g. `menu(bind=param, ...)` -> `param.menu(...)`)
class _BaseOptions(TypedDict, total=False):
    bind: Selection | Param
    """The output selection."""
    filter_by: Selection | Param
    """A selection to filter the database table indicated by the `source` field."""


class _NonTableOptions(_BaseOptions, total=False):
    field: str
    """The database column name to use within generated selection clause predicates.

    Defaults to the `column` field.
    """

    label: str
    """A text label for this input."""

    source: str
    """The name of a database table to use as a data source for this widget.

    Used in conjunction with the `column` property."""


class SearchOptions(_NonTableOptions, total=False, closed=True):
    """A text search input widget."""

    bind: Selection | Param
    """The output selection.

    A selection clause is added for the current text search query.
    """

    column: str
    """The name of a database column from which to pull valid search results.

    The unique column values are used as search autocomplete values. Used in conjunction with the `source` field.
    """

    type: L["contains", "prefix", "regexp", "suffix"]
    """The type of text search query to perform.

    One of:
    - `"contains"` (default): the query string may appear anywhere in the text
    - `"prefix"`: the query string must appear at the start of the text
    - `"suffix"`: the query string must appear at the end of the text
    - `"regexp"`: the query string is a regular expression the text must match
    """


class SliderOptions(_NonTableOptions, total=False, closed=True):
    """A slider input widget."""

    bind: Selection | Param
    """The output selection.

    A selection clause is added for the currently selected slider option.
    """

    column: str
    """The name of a database column whose values determine the slider range.

    Used in conjunction with the `source` field.
    The minimum and maximum values of the column determine the slider range.
    """

    max: float
    """The maximum slider value."""

    min: float
    """The minimum slider value."""

    select: L["interval", "point"]
    """The type of selection clause predicate to generate if the **as** option is a Selection.

    If `'point'` (the default), the selection predicate is an equality check for the slider value.
    If `'interval'`, the predicate checks an interval from the minimum to the current slider value.
    """

    step: float
    """The slider step, the amount to increment between consecutive values."""

    value: float
    """The initial slider value."""

    width: float
    """The width of the slider in screen pixels."""


class TableOptions(_BaseOptions, total=False, closed=True):
    """A table grid widget."""

    align: Mapping[str, L["center", "justify", "left", "right"]]
    """An object of per-column alignment values.

    Column names should be object keys, which map to alignment values.
    Valid alignment values are: `"left"`, `"right"`, `"center"`, and `"justify"`.
    By default, numbers are right-aligned and other values are left-aligned.
    """

    bind: Selection | Param
    """The output selection.

    A selection clause is added for each currently selected table row.
    """

    columns: Sequence[str]
    """A list of column names to include in the table grid.

    If unspecified, all table columns are included.
    """

    height: float
    """The height of the table widget, in pixels."""

    max_width: float
    """The maximum width of the table widget, in pixels."""

    row_batch: float
    """The number of rows load in a new batch upon table scroll."""

    width: Mapping[str, float] | float
    """If a number, sets the total width of the table widget, in pixels.

    If an object, provides per-column pixel width values.
    Column names should be object keys, mapped to numeric width values.
    """


class MenuOptions(_NonTableOptions, total=False, closed=True):
    """A menu input widget."""

    bind: Selection | Param
    """The output selection.

    A selection clause is added for the currently selected menu option.
    """

    column: str
    """The name of a database column from which to pull menu options.

    The unique column values are used as menu options.
    Used in conjunction with the `source` property.
    """

    list_match: L["all", "any"]
    """Required if the database column is an list, this property determines how to match the selected menu option against the list values."""

    options: Sequence[Any | Option]
    """An array of menu options, as literal values or option objects.

    Option objects have a `value` property and an optional `label` property.
    If no label is provided, the string-coerced value is used.
    """

    value: Any
    """The initial selected menu value."""


_O = TypeVar("_O", bound=_BaseOptions)


class _Input(Generic[_O]):
    """Base input widget."""

    __slots__ = ("options",)
    options: _O
    _INPUT: ClassVar[L["menu", "search", "slider", "table"]]


_SO = TypeVar("_SO", bound=_NonTableOptions)


class _NonTable(_Input[_SO], Generic[_SO]):
    __slots__ = ()


@final
class Menu(_NonTable[MenuOptions]):
    __slots__ = ()
    _INPUT = "menu"

    def __init__(self, **options: Unpack[MenuOptions]) -> None:
        self.options = options


@final
class Search(_NonTable[SearchOptions]):
    __slots__ = ()
    _INPUT = "search"

    def __init__(self, **options: Unpack[SearchOptions]) -> None:
        self.options = options


@final
class Slider(_NonTable[SliderOptions]):
    __slots__ = ()
    _INPUT = "slider"

    def __init__(self, **options: Unpack[SliderOptions]) -> None:
        self.options = options


@final
class Table(_Input[TableOptions]):
    __slots__ = ("source",)
    _INPUT = "table"

    source: Param | str
    """The name of a database table to use as a data source for this widget."""

    def __init__(self, source: Param | str, **options: Unpack[TableOptions]) -> None:
        self.source = source
        self.options = options


InputWidget = TypeAliasType("InputWidget", Menu | Search | Slider | Table)
"""Standalone data-driven components such as input menus, text search boxes, and sortable, load-on-scroll data tables.

Input widgets integrate with Mosaic Params and Selections, and can either be used in a standalone fashion or draw values from a backing data table.
"""
