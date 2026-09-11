# Generated: `mosaic_spec._gen.inputs`
from __future__ import annotations

from collections.abc import Mapping
from collections.abc import Sequence
from mosaic_spec._gen.params import ParamRef
from mosaic_spec._typing_compat import Required
from mosaic_spec._typing_compat import TypedDict
from typing import Any
from typing import Literal as L

class Options(TypedDict,total=False,closed=True):
    label: str
    value: Required[Any]
class _SearchOpen(TypedDict,total=False):
    """A search input component."""
    bind: ParamRef
    '''The output selection. A selection clause is added for the current text search query.'''
    column: str
    '''The name of a database column from which to pull valid search results. The unique column values are used as search autocomplete values. Used in conjunction with the `from` property.'''
    field: str
    '''The database column name to use within generated selection clause predicates. Defaults to the `column` property.'''
    filter_by: ParamRef
    '''A selection to filter the database table indicated by the `from` property.'''
    input: Required[L['search']]
    '''A text search input widget.'''
    label: str
    '''A text label for this input.'''
    source: str
    '''The name of a database table to use as an autocomplete data source for this widget. Used in conjunction with the `column` property.'''
    type: L['contains','prefix','regexp','suffix']
    '''The type of text search query to perform. One of:
- `"contains"` (default): the query string may appear anywhere in the text
- `"prefix"`: the query string must appear at the start of the text
- `"suffix"`: the query string must appear at the end of the text
- `"regexp"`: the query string is a regular expression the text must match'''
class _SliderOpen(TypedDict,total=False):
    """A slider input component."""
    bind: ParamRef
    '''The output selection. A selection clause is added for the currently selected slider option.'''
    column: str
    '''The name of a database column whose values determine the slider range. Used in conjunction with the `from` property. The minimum and maximum values of the column determine the slider range.'''
    field: str
    '''The database column name to use within generated selection clause predicates. Defaults to the `column` property.'''
    filter_by: ParamRef
    '''A selection to filter the database table indicated by the `from` property.'''
    input: Required[L['slider']]
    '''A slider input widget.'''
    label: str
    '''A text label for this input.'''
    max: float
    '''The maximum slider value.'''
    min: float
    '''The minimum slider value.'''
    select: L['interval','point']
    '''The type of selection clause predicate to generate if the **as** option is a Selection. If `'point'` (the default), the selection predicate is an equality check for the slider value. If `'interval'`, the predicate checks an interval from the minimum to the current slider value.'''
    source: str
    '''The name of a database table to use as a data source for this widget. Used in conjunction with the `column` property. The minimum and maximum values of the column determine the slider range.'''
    step: float
    '''The slider step, the amount to increment between consecutive values.'''
    value: float
    '''The initial slider value.'''
    width: float
    '''The width of the slider in screen pixels.'''
class _TableOpen(TypedDict,total=False):
    """A table grid view component."""
    align: Mapping[str, L['center','justify','left','right']]
    '''An object of per-column alignment values. Column names should be object keys, which map to alignment values. Valid alignment values are: `"left"`, `"right"`, `"center"`, and `"justify"`. By default, numbers are right-aligned and other values are left-aligned.'''
    bind: ParamRef
    '''The output selection. A selection clause is added for each currently selected table row.'''
    columns: Sequence[str]
    '''A list of column names to include in the table grid. If unspecified, all table columns are included.'''
    filter_by: ParamRef
    '''A selection to filter the database table indicated by the `from` property.'''
    height: float
    '''The height of the table widget, in pixels.'''
    input: Required[L['table']]
    '''A table grid widget.'''
    max_width: float
    '''The maximum width of the table widget, in pixels.'''
    row_batch: float
    '''The number of rows load in a new batch upon table scroll.'''
    source: Required[ParamRef | str]
    '''The name of a database table to use as a data source for this widget.'''
    width: Mapping[str, float] | float
    '''If a number, sets the total width of the table widget, in pixels. If an object, provides per-column pixel width values. Column names should be object keys, mapped to numeric width values.'''
class _MenuOpen(TypedDict,total=False):
    """A menu input component."""
    bind: ParamRef
    '''The output selection. A selection clause is added for the currently selected menu option.'''
    column: str
    '''The name of a database column from which to pull menu options. The unique column values are used as menu options. Used in conjunction with the `from` property.'''
    field: str
    '''The database column name to use within generated selection clause predicates. Defaults to the `column` property.'''
    filter_by: ParamRef
    '''A selection to filter the database table indicated by the `from` property.'''
    input: Required[L['menu']]
    '''A menu input widget.'''
    label: str
    '''A text label for this input.'''
    list_match: L['all','any']
    '''Required if the database column is an list, this property determines how to match the selected menu option against the list values.'''
    options: Sequence[Any | Options]
    '''An array of menu options, as literal values or option objects. Option objects have a `value` property and an optional `label` property. If no label is provided, the string-coerced value is used.'''
    source: str
    '''The name of a database table to use as a data source for this widget. Used in conjunction with the `column` property.'''
    value: Any
    '''The initial selected menu value.'''
class Search(_SearchOpen,total=False,closed=True):...
class Slider(_SliderOpen,total=False,closed=True):...
class Table(_TableOpen,total=False,closed=True):...
class Menu(_MenuOpen,total=False,closed=True):...


__all__ = ("Menu","Options","Search","Slider","Table",)
