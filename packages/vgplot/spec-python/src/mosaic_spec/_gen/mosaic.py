# NOTE: DO NOT EDIT.
# Regenerate with: pnpm generate

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any, Literal, Union

from mosaic_spec._gen.marks import PlotMark
from mosaic_spec._gen.params import ParamDefinition
from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict

if TYPE_CHECKING:
    from mosaic_spec._gen.css_styles import CSSStyles
    from mosaic_spec._gen.interactors import PlotInteractor
    from mosaic_spec._gen.typing import ColorScheme, Interval
    from mosaic_spec.typing import ParamRef

ColorScaleType = TypeAliasType(
    "ColorScaleType",
    Literal[
        "linear",
        "pow",
        "sqrt",
        "log",
        "symlog",
        "utc",
        "time",
        "point",
        "band",
        "ordinal",
        "sequential",
        "cyclical",
        "diverging",
        "diverging-log",
        "diverging-pow",
        "diverging-sqrt",
        "diverging-symlog",
        "categorical",
        "threshold",
        "quantile",
        "quantize",
        "identity",
    ],
)
"""The supported scale types for *color* encodings.

For quantitative data, one of:

- *linear* (default) - linear transform (translate and scale)
- *pow* - power (exponential) transform
- *sqrt* - square-root transform; *pow* with *exponent* = 0.5
- *log* - logarithmic transform
- *symlog* - bi-symmetric logarithmic transform per Webber et al.

For temporal data, one of:

- *utc* (default, recommended) - UTC time
- *time* - local time

For ordinal data, one of:

- *ordinal* - from discrete inputs to discrete outputs

For color, one of:

- *categorical* - equivalent to *ordinal*; defaults to *observable10*
- *sequential* - equivalent to *linear*; defaults to *turbo*
- *cyclical* - equivalent to *linear*; defaults to *rainbow*
- *threshold* - encodes using discrete thresholds; defaults to *rdylbu*
- *quantile* - encodes using quantile thresholds; defaults to *rdylbu*
- *quantize* - uniformly quantizes a continuous domain; defaults to *rdylbu*
- *diverging* - *linear*, but with a pivot; defaults to *rdbu*
- *diverging-log* - *log*, but with a pivot; defaults to *rdbu*
- *diverging-pow* - *pow*, but with a pivot; defaults to *rdbu*
- *diverging-sqrt* - *sqrt*, but with a pivot; defaults to *rdbu*
- *diverging-symlog* - *symlog*, but with a pivot; defaults to *rdbu*

Other scale types:

- *identity* - do not transform values when encoding"""


class Config(TypedDict, total=False):
    """Configuration options."""

    extensions: str | Sequence[str]


ContinuousScaleType = TypeAliasType(
    "ContinuousScaleType",
    Literal["linear", "pow", "sqrt", "log", "symlog", "utc", "time", "identity"],
)
"""The supported scale types for continuous encoding channels.

For quantitative data, one of:

- *linear* (default) - linear transform (translate and scale)
- *pow* - power (exponential) transform
- *sqrt* - square-root transform; *pow* with *exponent* = 0.5
- *log* - logarithmic transform
- *symlog* - bi-symmetric logarithmic transform per Webber et al.

For temporal data, one of:

- *utc* (default, recommended) - UTC time
- *time* - local time

Other scale types:

- *identity* - do not transform values when encoding"""


DataArray = TypeAliasType("DataArray", Sequence[Mapping[str, Any]])
"""An inline array of data objects to treat as JSON data."""


class DataCSV(TypedDict, total=False, closed=True):
    """A data definition that loads a csv file."""

    delimiter: str
    """The column delimiter string. If not specified, DuckDB will try to infer the delimiter automatically."""
    file: Required[str]
    """The file path for the dataset to load."""
    replace: bool
    """Flag (default `true`) to replace an existing table of the same name. If `false`, creating a new table with an existing name raises an error."""
    sample_size: float
    """The sample size, in table rows, to consult for type inference. Set to `-1` to process all rows in the dataset."""
    select: Sequence[str]
    """A list of column names to extract upon load. Any other columns are omitted."""
    temp: bool
    """Flag (default `true`) to generate a temporary view or table."""
    type: Required[Literal["csv"]]
    """
    The data source type. One of:
    - `"table"`: Define a new table based on a SQL query.
    - `"csv"`: Load a comma-separated values (CSV) file.
    - `"json"`: Load JavaScript Object Notation (json) data.
    - `"parquet"`: Load a Parquet file.
    - `"spatial"`: Load a spatial data file format via `ST_Read`.
    """
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: str | Sequence[str]
    """A filter (WHERE clause) to apply upon load. Only rows that pass the filter are included."""


class DataFile(TypedDict, total=False, closed=True):
    """A data definition that loads an external data file."""

    file: Required[str]
    """The data file to load. If no type option is provided, the file suffix must be one of `.csv`, `.json`, or `.parquet`."""
    replace: bool
    """Flag (default `true`) to replace an existing table of the same name. If `false`, creating a new table with an existing name raises an error."""
    select: Sequence[str]
    """A list of column names to extract upon load. Any other columns are omitted."""
    temp: bool
    """Flag (default `true`) to generate a temporary view or table."""
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: str | Sequence[str]
    """A filter (WHERE clause) to apply upon load. Only rows that pass the filter are included."""


class DataJSON(TypedDict, total=False, closed=True):
    file: Required[str]
    """The file path for the dataset to load."""
    replace: bool
    """Flag (default `true`) to replace an existing table of the same name. If `false`, creating a new table with an existing name raises an error."""
    select: Sequence[str]
    """A list of column names to extract upon load. Any other columns are omitted."""
    temp: bool
    """Flag (default `true`) to generate a temporary view or table."""
    type: Required[Literal["json"]]
    """
    The data source type. One of:
    - `"table"`: Define a new table based on a SQL query.
    - `"csv"`: Load a comma-separated values (CSV) file.
    - `"json"`: Load JavaScript Object Notation (json) data.
    - `"parquet"`: Load a Parquet file.
    - `"spatial"`: Load a spatial data file format via `ST_Read`.
    """
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: str | Sequence[str]
    """A filter (WHERE clause) to apply upon load. Only rows that pass the filter are included."""


class DataJSONObjects(TypedDict, total=False, closed=True):
    data: Required[Sequence[Mapping[str, Any]]]
    """An array of inline objects in JSON-style format."""
    replace: bool
    """Flag (default `true`) to replace an existing table of the same name. If `false`, creating a new table with an existing name raises an error."""
    select: Sequence[str]
    """A list of column names to extract upon load. Any other columns are omitted."""
    temp: bool
    """Flag (default `true`) to generate a temporary view or table."""
    type: Literal["json"]
    """
    The data source type. One of:
    - `"table"`: Define a new table based on a SQL query.
    - `"csv"`: Load a comma-separated values (CSV) file.
    - `"json"`: Load JavaScript Object Notation (json) data.
    - `"parquet"`: Load a Parquet file.
    - `"spatial"`: Load a spatial data file format via `ST_Read`.
    """
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: str | Sequence[str]
    """A filter (WHERE clause) to apply upon load. Only rows that pass the filter are included."""


class DataParquet(TypedDict, total=False, closed=True):
    """A data definition that loads a parquet file."""

    file: Required[str]
    """The file path for the dataset to load."""
    replace: bool
    """Flag (default `true`) to replace an existing table of the same name. If `false`, creating a new table with an existing name raises an error."""
    select: Sequence[str]
    """A list of column names to extract upon load. Any other columns are omitted."""
    temp: bool
    """Flag (default `true`) to generate a temporary view or table."""
    type: Required[Literal["parquet"]]
    """
    The data source type. One of:
    - `"table"`: Define a new table based on a SQL query.
    - `"csv"`: Load a comma-separated values (CSV) file.
    - `"json"`: Load JavaScript Object Notation (json) data.
    - `"parquet"`: Load a Parquet file.
    - `"spatial"`: Load a spatial data file format via `ST_Read`.
    """
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: str | Sequence[str]
    """A filter (WHERE clause) to apply upon load. Only rows that pass the filter are included."""


DataQuery = TypeAliasType("DataQuery", str)
"""A SQL query defining a new temporary database table."""


class DataSpatial(TypedDict, total=False, closed=True):
    """A data definition that loads a supported spatial data file format."""

    file: Required[str]
    """
    The file path for the spatial dataset to load. See the [DuckDB spatial documentation][1] for more information on supported file types.

    [1]: https://duckdb.org/docs/extensions/spatial.html#st_read--read-spatial-data-from-files
    """
    layer: str
    """The named layer to load from the file. For example, in a TopoJSON file the layer is the named object to extract. For Excel spreadsheet files, the layer is the name of the worksheet to extract."""
    replace: bool
    """Flag (default `true`) to replace an existing table of the same name. If `false`, creating a new table with an existing name raises an error."""
    select: Sequence[str]
    """A list of column names to extract upon load. Any other columns are omitted."""
    temp: bool
    """Flag (default `true`) to generate a temporary view or table."""
    type: Required[Literal["spatial"]]
    """
    The data source type. One of:
    - `"table"`: Define a new table based on a SQL query.
    - `"csv"`: Load a comma-separated values (CSV) file.
    - `"json"`: Load JavaScript Object Notation (json) data.
    - `"parquet"`: Load a Parquet file.
    - `"spatial"`: Load a spatial data file format via `ST_Read`.
    """
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: str | Sequence[str]
    """A filter (WHERE clause) to apply upon load. Only rows that pass the filter are included."""


class DataTable(TypedDict, total=False, closed=True):
    """A data definition that queries an existing table."""

    query: Required[str]
    """A SQL query string for the desired table data."""
    replace: bool
    """Flag (default `true`) to replace an existing table of the same name. If `false`, creating a new table with an existing name raises an error."""
    select: Sequence[str]
    """A list of column names to extract upon load. Any other columns are omitted."""
    temp: bool
    """Flag (default `true`) to generate a temporary view or table."""
    type: Required[Literal["table"]]
    """
    The data source type. One of:
    - `"table"`: Define a new table based on a SQL query.
    - `"csv"`: Load a comma-separated values (CSV) file.
    - `"json"`: Load JavaScript Object Notation (json) data.
    - `"parquet"`: Load a Parquet file.
    - `"spatial"`: Load a spatial data file format via `ST_Read`.
    """
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: str | Sequence[str]
    """A filter (WHERE clause) to apply upon load. Only rows that pass the filter are included."""


DiscreteScaleType = TypeAliasType("DiscreteScaleType", Literal["ordinal", "identity"])
"""The supported scale types for discrete encoding channels. One of:

- *ordinal* - from discrete inputs to discrete outputs
- *identity* - do not transform values when encoding"""


Fixed = TypeAliasType("Fixed", Literal["Fixed"])
"""A symbol indicating a fixed scale domain. A fixed domain is initially determined from data as usual, but subsequently "fixed" so that it does not change over subsequent interactive filtering, ensring stable comparisons."""


class _HSpaceOpen(TypedDict, total=False):
    """An hspace component."""

    hspace: Required[float | str]
    """Horizontal space to place between components. Number values indicate screen pixels. String values may use CSS units (em, pt, px, etc)."""


class HSpace(_HSpaceOpen, total=False, closed=True): ...


Interpolate = TypeAliasType("Interpolate", Literal["number", "rgb", "hsl", "hcl", "lab"])
r"""How to interpolate range (output) values for continuous scales; one of:

- *number* - linear numeric interpolation
- *rgb* - red, green, blue (sRGB)
- *hsl* - hue, saturation, lightness (HSL; cylindrical sRGB)
- *hcl* - hue, chroma, perceptual lightness (CIELCh_ab; cylindrical CIELAB)
- *lab* - perceptual lightness and opponent colors (L\*a\*b\*, CIELAB)"""


LabelArrow = TypeAliasType(
    "LabelArrow", Literal["auto", "up", "right", "down", "left", "none", True, False] | None
)


class Options(TypedDict, total=False, closed=True):
    label: str
    value: Required[Any]


class Meta(TypedDict, total=False):
    """Specification metadata."""

    credit: str
    """Credits or other acknowledgements."""
    description: str
    """A description of the specification content."""
    title: str
    """The specification title."""


class Margins(TypedDict, total=False, closed=True):
    """A shorthand object notation for setting multiple margin values. The object keys are margin names (top, right, etc)."""

    bottom: float | ParamRef
    left: float | ParamRef
    right: float | ParamRef
    top: float | ParamRef


class PlotLegend(TypedDict, total=False, closed=True):
    """A legend defined as an entry within a plot."""

    bind: ParamRef
    """The output selection. If specified, the legend is interactive, using a `toggle` interaction for discrete legends or an `intervalX` interaction for continuous legends."""
    columns: float
    """The number of columns to use to layout a discrete legend."""
    field: str
    """The data field over which to generate output selection clauses. If unspecified, a matching field is retrieved from existing plot marks."""
    height: float
    """The height of a continuous legend, in pixels."""
    label: str
    """The legend label."""
    legend: Required[Literal["color", "opacity", "symbol"]]
    """A legend of the given type. The valid types are `"color"`, `"opacity"`, and `"symbol"`."""
    margin_bottom: float
    """The bottom margin of the legend component, in pixels."""
    margin_left: float
    """The left margin of the legend component, in pixels."""
    margin_right: float
    """The right margin of the legend component, in pixels."""
    margin_top: float
    """The top margin of the legend component, in pixels."""
    tick_size: float
    """The size of legend ticks in a continuous legend, in pixels."""
    width: float
    """The width of a continuous legend, in pixels."""


PositionScaleType = TypeAliasType(
    "PositionScaleType",
    Literal[
        "linear",
        "pow",
        "sqrt",
        "log",
        "symlog",
        "utc",
        "time",
        "point",
        "band",
        "threshold",
        "quantile",
        "quantize",
        "identity",
    ],
)
"""The supported scale types for *x* and *y* position encodings.

For quantitative data, one of:

- *linear* (default) - linear transform (translate and scale)
- *pow* - power (exponential) transform
- *sqrt* - square-root transform; *pow* with *exponent* = 0.5
- *log* - logarithmic transform
- *symlog* - bi-symmetric logarithmic transform per Webber et al.

For temporal data, one of:

- *utc* (default, recommended) - UTC time
- *time* - local time

For ordinal data, one of:

- *point* (for position only) - divide a continuous range into discrete points
- *band* (for position only) - divide a continuous range into discrete points

Other scale types:

- *identity* - do not transform values when encoding"""


ProjectionName = TypeAliasType(
    "ProjectionName",
    Literal[
        "albers-usa",
        "albers",
        "azimuthal-equal-area",
        "azimuthal-equidistant",
        "conic-conformal",
        "conic-equal-area",
        "conic-equidistant",
        "equal-earth",
        "equirectangular",
        "gnomonic",
        "identity",
        "reflect-y",
        "mercator",
        "orthographic",
        "stereographic",
        "transverse-mercator",
    ],
)
"""The built-in projection implementations; one of:

- *albers-usa* - a U.S.-centric composite projection with insets for Alaska and Hawaii
- *albers* - a U.S.-centric *conic-equal-area* projection
- *azimuthal-equal-area* - the azimuthal equal-area projection
- *azimuthal-equidistant* - the azimuthal equidistant projection
- *conic-conformal* - the conic conformal projection
- *conic-equal-area* - the conic equal-area projection
- *conic-equidistant* - the conic equidistant projection
- *equal-earth* - the Equal Earth projection Šavrič et al., 2018
- *equirectangular* - the equirectangular (plate carrée) projection
- *gnomonic* - the gnomonic projection
- *identity* - the identity projection
- *reflect-y* - the identity projection, but flipping *y*
- *mercator* - the spherical Mercator projection
- *orthographic* - the orthographic projection
- *stereographic* - the stereographic projection
- *transverse-mercator* - the transverse spherical Mercator projection"""


class _SearchOpen(TypedDict, total=False):
    """A search input component."""

    bind: ParamRef
    """The output selection. A selection clause is added for the current text search query."""
    column: str
    """The name of a database column from which to pull valid search results. The unique column values are used as search autocomplete values. Used in conjunction with the `from` property."""
    field: str
    """The database column name to use within generated selection clause predicates. Defaults to the `column` property."""
    filter_by: ParamRef
    """A selection to filter the database table indicated by the `from` property."""
    input: Required[Literal["search"]]
    """A text search input widget."""
    label: str
    """A text label for this input."""
    source: str
    """The name of a database table to use as an autocomplete data source for this widget. Used in conjunction with the `column` property."""
    type: Literal["contains", "prefix", "suffix", "regexp"]
    """
    The type of text search query to perform. One of:
    - `"contains"` (default): the query string may appear anywhere in the text
    - `"prefix"`: the query string must appear at the start of the text
    - `"suffix"`: the query string must appear at the end of the text
    - `"regexp"`: the query string is a regular expression the text must match
    """


class Search(_SearchOpen, total=False, closed=True): ...


class _SliderOpen(TypedDict, total=False):
    """A slider input component."""

    bind: ParamRef
    """The output selection. A selection clause is added for the currently selected slider option."""
    column: str
    """The name of a database column whose values determine the slider range. Used in conjunction with the `from` property. The minimum and maximum values of the column determine the slider range."""
    field: str
    """The database column name to use within generated selection clause predicates. Defaults to the `column` property."""
    filter_by: ParamRef
    """A selection to filter the database table indicated by the `from` property."""
    input: Required[Literal["slider"]]
    """A slider input widget."""
    label: str
    """A text label for this input."""
    max: float
    """The maximum slider value."""
    min: float
    """The minimum slider value."""
    select: Literal["point", "interval"]
    """The type of selection clause predicate to generate if the **as** option is a Selection. If `'point'` (the default), the selection predicate is an equality check for the slider value. If `'interval'`, the predicate checks an interval from the minimum to the current slider value."""
    source: str
    """The name of a database table to use as a data source for this widget. Used in conjunction with the `column` property. The minimum and maximum values of the column determine the slider range."""
    step: float
    """The slider step, the amount to increment between consecutive values."""
    value: float
    """The initial slider value."""
    width: float
    """The width of the slider in screen pixels."""


class Slider(_SliderOpen, total=False, closed=True): ...


class _TableOpen(TypedDict, total=False):
    """A table grid view component."""

    align: Mapping[str, Literal["left", "right", "center", "justify"]]
    """An object of per-column alignment values. Column names should be object keys, which map to alignment values. Valid alignment values are: `"left"`, `"right"`, `"center"`, and `"justify"`. By default, numbers are right-aligned and other values are left-aligned."""
    bind: ParamRef
    """The output selection. A selection clause is added for each currently selected table row."""
    columns: Sequence[str]
    """A list of column names to include in the table grid. If unspecified, all table columns are included."""
    filter_by: ParamRef
    """A selection to filter the database table indicated by the `from` property."""
    height: float
    """The height of the table widget, in pixels."""
    input: Required[Literal["table"]]
    """A table grid widget."""
    max_width: float
    """The maximum width of the table widget, in pixels."""
    row_batch: float
    """The number of rows load in a new batch upon table scroll."""
    source: Required[str | ParamRef]
    """The name of a database table to use as a data source for this widget."""
    width: float | Mapping[str, float]
    """If a number, sets the total width of the table widget, in pixels. If an object, provides per-column pixel width values. Column names should be object keys, mapped to numeric width values."""


class Table(_TableOpen, total=False, closed=True): ...


class _VSpaceOpen(TypedDict, total=False):
    """A vspace component."""

    vspace: Required[float | str]
    """Vertical space to place between components. Number values indicate screen pixels. String values may use CSS units (em, pt, px, etc)."""


class VSpace(_VSpaceOpen, total=False, closed=True): ...


DataDefinition = TypeAliasType(
    "DataDefinition",
    DataQuery
    | DataArray
    | DataFile
    | DataTable
    | DataParquet
    | DataCSV
    | DataSpatial
    | DataJSON
    | DataJSONObjects,
)


class _LegendOpen(TypedDict, total=False):
    """A legend defined as a top-level spec component."""

    bind: ParamRef
    """The output selection. If specified, the legend is interactive, using a `toggle` interaction for discrete legends or an `intervalX` interaction for continuous legends."""
    columns: float
    """The number of columns to use to layout a discrete legend."""
    field: str
    """The data field over which to generate output selection clauses. If unspecified, a matching field is retrieved from existing plot marks."""
    height: float
    """The height of a continuous legend, in pixels."""
    label: str
    """The legend label."""
    legend: Required[Literal["color", "opacity", "symbol"]]
    """A legend of the given type. The valid types are `"color"`, `"opacity"`, and `"symbol"`."""
    margin_bottom: float
    """The bottom margin of the legend component, in pixels."""
    margin_left: float
    """The left margin of the legend component, in pixels."""
    margin_right: float
    """The right margin of the legend component, in pixels."""
    margin_top: float
    """The top margin of the legend component, in pixels."""
    plot: Required[str]
    """The name of the plot this legend applies to. A plot must include a `name` attribute to be referenced."""
    tick_size: float
    """The size of legend ticks in a continuous legend, in pixels."""
    width: float
    """The width of a continuous legend, in pixels."""


class Legend(_LegendOpen, total=False, closed=True): ...


class _MenuOpen(TypedDict, total=False):
    """A menu input component."""

    bind: ParamRef
    """The output selection. A selection clause is added for the currently selected menu option."""
    column: str
    """The name of a database column from which to pull menu options. The unique column values are used as menu options. Used in conjunction with the `from` property."""
    field: str
    """The database column name to use within generated selection clause predicates. Defaults to the `column` property."""
    filter_by: ParamRef
    """A selection to filter the database table indicated by the `from` property."""
    input: Required[Literal["menu"]]
    """A menu input widget."""
    label: str
    """A text label for this input."""
    list_match: Literal["any", "all"]
    """Required if the database column is an list, this property determines how to match the selected menu option against the list values."""
    options: Sequence[Any | Options]
    """An array of menu options, as literal values or option objects. Option objects have a `value` property and an optional `label` property. If no label is provided, the string-coerced value is used."""
    source: str
    """The name of a database table to use as a data source for this widget. Used in conjunction with the `column` property."""
    value: Any
    """The initial selected menu value."""


class Menu(_MenuOpen, total=False, closed=True): ...


Data = TypeAliasType("Data", Mapping[str, DataDefinition])
"""Top-level dataset definitions."""


Params = TypeAliasType("Params", Mapping[str, ParamDefinition])
"""Top-level Param and Selection definitions."""


class _PlotAttributesOpen(TypedDict, total=False):
    """Plot attributes."""

    align: float | ParamRef
    """
    How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

    - 0 - use the start of the range, putting unused space at the end
    - 0.5 (default) - use the middle, distributing unused space evenly
    - 1 use the end, putting unused space at the start

    For ordinal position scales only.
    """
    aria_description: str | None
    """
    The [aria-description attribute][1] on the SVG root.

    [1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-description
    """
    aria_label: str | None
    """
    The [aria-label attribute][1] on the SVG root.

    [1]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-label
    """
    aspect_ratio: float | bool | ParamRef | None
    """
    The desired aspect ratio of the *x* and *y* scales, affecting the default height. Given an aspect ratio of *dx* / *dy*, and assuming that the *x* and
    *y* scales represent equivalent units (say, degrees Celsius or meters), computes a default height such that *dx* pixels along *x* represents the same variation as *dy* pixels along *y*. Note: when faceting, set the *fx* and *fy* scales' **round** option to false for an exact aspect ratio.
    """
    axis: Literal["top", "right", "bottom", "left", "both"] | bool | ParamRef | None
    """
    The side of the frame on which to place the implicit axis: *top* or
    *bottom* for *x* or *fx*, or *left* or *right* for *y* or *fy*. The default depends on the scale:

    - *x* - *bottom*
    - *y* - *left*
    - *fx* - *top* if there is a *bottom* *x* axis, and otherwise *bottom*
    - *fy* - *right* if there is a *left* *y* axis, and otherwise *right*

    If *both*, an implicit axis will be rendered on both sides of the plot (*top* and *bottom* for *x* or *fx*, or *left* and *right* for *y* or
    *fy*). If null, the implicit axis is suppressed.

    For position axes only.
    """
    clip: Literal["frame", "sphere"] | bool | ParamRef | None
    """The default clip for all marks."""
    color_base: float | ParamRef
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* and *diverging-log* scales only."""
    color_clamp: bool | ParamRef
    """
    If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

    Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

    For continuous scales only.
    """
    color_constant: float | ParamRef
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* and *diverging-symlog* scales only."""
    color_domain: Sequence[Any] | Fixed | ParamRef
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order."""
    color_exponent: float | ParamRef
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* and *diverging-pow* scales only."""
    color_interpolate: Interpolate | ParamRef
    """How to interpolate color range values. For quantitative scales only. This attribute can be used to specify a color space for interpolating colors specified in the **colorRange**."""
    color_label: str | ParamRef | None
    """
    A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

    For axes and legends only.
    """
    color_n: float | ParamRef
    """For a *quantile* scale, the number of quantiles (creates *n* - 1 thresholds); for a *quantize* scale, the approximate number of thresholds; defaults to 5."""
    color_nice: bool | float | Interval | ParamRef
    """
    If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
    *minute*, *wednesday* or *month* to specify what constitutes a nice interval.

    For continuous scales only.
    """
    color_percent: bool | ParamRef
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    color_pivot: Any | ParamRef
    """
    For a diverging color scale, the input value (abstract value) that divides the domain into two parts; defaults to 0 for *diverging* scales, dividing the domain into negative and positive parts; defaults to 1 for
    *diverging-log* scales. By default, diverging scales are symmetric around the pivot; see the **symmetric** option.
    """
    color_range: Sequence[Any] | Fixed | ParamRef
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**. For other ordinal data, it is an array (or iterable) of output values in the same order as the **domain**."""
    color_reverse: bool | ParamRef
    """
    Whether to reverse the scale's encoding; equivalent to reversing either the
    **domain** or **range**.
    """
    color_scale: ColorScaleType | ParamRef | None
    """
    The *color* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled.

    For quantitative data (numbers), defaults to *linear*; for temporal data (dates), defaults to *utc*; for ordinal data (strings or booleans), defaults to *point* for position scales, *categorical* for color scales, and otherwise *ordinal*.
    """
    color_scheme: ColorScheme | ParamRef
    """If specified, shorthand for setting the **colorRange** or **colorInterpolate** option of a *color* scale."""
    color_symmetric: bool | ParamRef
    """
    For a diverging color scale, if true (the default), extend the domain to ensure that the lower part of the domain (below the **pivot**) is commensurate with the upper part of the domain (above the **pivot**).

    A symmetric diverging color scale may not use all of its output **range**; this reduces contrast but ensures that deviations both below and above the
    **pivot** are represented proportionally. Otherwise if false, the full output **range** will be used; this increases contrast but values on opposite sides of the **pivot** may not be meaningfully compared.
    """
    color_tick_format: str | ParamRef | None
    """
    How to format inputs (abstract values) for axis tick labels; one of:

    - a [d3-format][1] string for numeric scales
    - a [d3-time-format][2] string for temporal scales

    [1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format
    """
    color_zero: bool | ParamRef
    """
    Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

    For quantitative scales only.
    """
    facet_grid: bool | str | Interval | Sequence[Any] | ParamRef
    """Default axis grid for fx and fy scales; typically set to true to enable."""
    facet_label: str | ParamRef | None
    """Default axis label for fx and fy scales; typically set to null to disable."""
    facet_margin: float | ParamRef
    """Shorthand to set the same default for all four facet margins: marginTop, marginRight, marginBottom, and marginLeft."""
    facet_margin_bottom: float | ParamRef
    """The right facet margin; the (minimum) distance in pixels between the right edges of the inner and outer plot area."""
    facet_margin_left: float | ParamRef
    """The bottom facet margin; the (minimum) distance in pixels between the bottom edges of the inner and outer plot area."""
    facet_margin_right: float | ParamRef
    """The left facet margin; the (minimum) distance in pixels between the left edges of the inner and outer plot area."""
    facet_margin_top: float | ParamRef
    """The top facet margin; the (minimum) distance in pixels between the top edges of the inner and outer plot area."""
    fx_align: float | ParamRef
    """
    How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

    - 0 - use the start of the range, putting unused space at the end
    - 0.5 (default) - use the middle, distributing unused space evenly
    - 1 use the end, putting unused space at the start

    For ordinal position scales only.
    """
    fx_aria_description: str | ParamRef
    """A textual description for the axis in the accessibility tree."""
    fx_aria_label: str | ParamRef
    """A short label representing the axis in the accessibility tree."""
    fx_axis: Literal["top", "bottom", "both"] | bool | ParamRef | None
    """
    The side of the frame on which to place the implicit axis: *top* or
    *bottom* for *fx*. Defaults to *top* if there is a *bottom* *x* axis, and otherwise *bottom*.

    If *both*, an implicit axis will be rendered on both sides of the plot (*top* and *bottom* for *fx*). If null, the implicit axis is suppressed.
    """
    fx_domain: Sequence[Any] | Fixed | ParamRef
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order."""
    fx_font_variant: str | ParamRef
    """The font-variant attribute for axis ticks; defaults to *tabular-nums* for quantitative axes."""
    fx_grid: bool | str | Interval | Sequence[Any] | ParamRef
    """
    Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

    For axes only.
    """
    fx_inset: float | ParamRef
    """
    Shorthand to set the same default for all four insets: **insetTop**,
    **insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.
    """
    fx_inset_left: float | ParamRef
    """Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it)."""
    fx_inset_right: float | ParamRef
    """Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it)."""
    fx_label: str | ParamRef | None
    """
    A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

    For axes and legends only.
    """
    fx_label_anchor: Literal["top", "right", "bottom", "left", "center"] | ParamRef
    """
    Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
    *center*; for horizontal position scales (*x* and *fx*), may be *left*,
    *right*, or *center*. Defaults to *center* for ordinal scales (including
    *fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*.
    """
    fx_label_offset: float | ParamRef
    """The axis **label** position offset (in pixels); default depends on margins and orientation."""
    fx_line: bool | ParamRef
    """If true, draw a line along the axis; if false (default), do not."""
    fx_padding: float | ParamRef
    """
    For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

    For ordinal position scales only.
    """
    fx_padding_inner: float | ParamRef
    """For a *band* scale, how much of the range to reserve to separate adjacent bands."""
    fx_padding_outer: float | ParamRef
    """For a *band* scale, how much of the range to reserve to inset first and last bands."""
    fx_range: Sequence[Any] | Fixed | ParamRef
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and the plot's dimensions. For ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale."""
    fx_reverse: bool | ParamRef
    """
    Whether to reverse the scale's encoding; equivalent to reversing either the
    **domain** or **range**.
    """
    fx_round: bool | ParamRef
    """
    If true, round the output value to the nearest integer (pixel); useful for crisp edges when rendering.

    For position scales only.
    """
    fx_tick_format: str | ParamRef | None
    """
    How to format inputs (abstract values) for axis tick labels; one of:

    - a [d3-format][1] string for numeric scales
    - a [d3-time-format][2] string for temporal scales

    [1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format
    """
    fx_tick_padding: float | ParamRef
    """
    The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **fxTickSize** and
    **fxTickRotate**.
    """
    fx_tick_rotate: float | ParamRef
    """The rotation angle of axis tick labels in degrees clocksize; defaults to 0."""
    fx_tick_size: float | ParamRef
    """
    The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
    *opacity* *ramp* legends, and 0 for *fx* and *fy* axes.
    """
    fx_tick_spacing: float | ParamRef
    """The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*."""
    fx_ticks: float | Interval | Sequence[Any] | ParamRef
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""
    fy_align: float | ParamRef
    """
    How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

    - 0 - use the start of the range, putting unused space at the end
    - 0.5 (default) - use the middle, distributing unused space evenly
    - 1 use the end, putting unused space at the start

    For ordinal position scales only.
    """
    fy_aria_description: str | ParamRef
    """A textual description for the axis in the accessibility tree."""
    fy_aria_label: str | ParamRef
    """A short label representing the axis in the accessibility tree."""
    fy_axis: Literal["left", "right", "both"] | bool | ParamRef | None
    """
    The side of the frame on which to place the implicit axis: *left* or
    *right* for *fy*. Defaults to *left* for an *fy* scale.

    If *both*, an implicit axis will be rendered on both sides of the plot (*left* and *right* for *fy*). If null, the implicit axis is suppressed.
    """
    fy_domain: Sequence[Any] | Fixed | ParamRef
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order."""
    fy_font_variant: str | ParamRef
    """The font-variant attribute for axis ticks; defaults to *tabular-nums* for quantitative axes."""
    fy_grid: bool | str | Interval | Sequence[Any] | ParamRef
    """
    Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

    For axes only.
    """
    fy_inset: float | ParamRef
    """
    Shorthand to set the same default for all four insets: **insetTop**,
    **insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.
    """
    fy_inset_bottom: float | ParamRef
    """Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it)."""
    fy_inset_top: float | ParamRef
    """Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it)."""
    fy_label: str | ParamRef | None
    """
    A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

    For axes and legends only.
    """
    fy_label_anchor: Literal["top", "right", "bottom", "left", "center"] | ParamRef
    """
    Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
    *center*; for horizontal position scales (*x* and *fx*), may be *left*,
    *right*, or *center*. Defaults to *center* for ordinal scales (including
    *fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*.
    """
    fy_label_offset: float | ParamRef
    """The axis **label** position offset (in pixels); default depends on margins and orientation."""
    fy_line: bool | ParamRef
    """If true, draw a line along the axis; if false (default), do not."""
    fy_padding: float | ParamRef
    """
    For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

    For ordinal position scales only.
    """
    fy_padding_inner: float | ParamRef
    """For a *band* scale, how much of the range to reserve to separate adjacent bands."""
    fy_padding_outer: float | ParamRef
    """For a *band* scale, how much of the range to reserve to inset first and last bands."""
    fy_range: Sequence[Any] | Fixed | ParamRef
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and the plot's dimensions. For ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale."""
    fy_reverse: bool | ParamRef
    """
    Whether to reverse the scale's encoding; equivalent to reversing either the
    **domain** or **range**.
    """
    fy_round: bool | ParamRef
    """
    If true, round the output value to the nearest integer (pixel); useful for crisp edges when rendering.

    For position scales only.
    """
    fy_tick_format: str | ParamRef | None
    """
    How to format inputs (abstract values) for axis tick labels; one of:

    - a [d3-format][1] string for numeric scales
    - a [d3-time-format][2] string for temporal scales

    [1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format
    """
    fy_tick_padding: float | ParamRef
    """
    The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **fyTickSize** and
    **fyTickRotate**.
    """
    fy_tick_rotate: float | ParamRef
    """The rotation angle of axis tick labels in degrees clocksize; defaults to 0."""
    fy_tick_size: float | ParamRef
    """
    The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
    *opacity* *ramp* legends, and 0 for *fx* and *fy* axes.
    """
    fy_tick_spacing: float | ParamRef
    """The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*."""
    fy_ticks: float | Interval | Sequence[Any] | ParamRef
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""
    grid: bool | str | ParamRef
    """
    Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

    For axes only.
    """
    height: float | ParamRef
    """The outer height of the plot in pixels, including margins. The default depends on the plot's scales, and the plot's width if an aspectRatio is specified. For example, if the *y* scale is linear and there is no *fy* scale, it might be 396."""
    inset: float | ParamRef
    """
    Shorthand to set the same default for all four insets: **insetTop**,
    **insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.
    """
    length_base: float | ParamRef
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    length_clamp: Any
    """
    If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

    Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

    For continuous scales only.
    """
    length_constant: float | ParamRef
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    length_domain: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

    Linear scales have a default domain of [0, 1]. Log scales have a default domain of [1, 10] and cannot include zero. Radius scales have a default domain from 0 to the median first quartile of associated channels. Length have a default domain from 0 to the median median of associated channels. Opacity scales have a default domain from 0 to the maximum value of associated channels.
    """
    length_exponent: float | ParamRef
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    length_nice: bool | float | Interval | ParamRef
    """
    If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
    *minute*, *wednesday* or *month* to specify what constitutes a nice interval.

    For continuous scales only.
    """
    length_percent: bool | ParamRef
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    length_range: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For other ordinal data, such as for a *color* scale, it is an array (or iterable) of output values in the same order as the **domain**.

    Length scales have a default range of [0, 12].
    """
    length_scale: ContinuousScaleType | ParamRef | None
    """The *length* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled. The length scale defaults to *linear*, as this scale is intended for quantitative data."""
    length_zero: bool | ParamRef
    """
    Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

    For quantitative scales only.
    """
    margin: float | ParamRef
    """
    Shorthand to set the same default for all four margins: **marginTop**,
    **marginRight**, **marginBottom**, and **marginLeft**. Otherwise, the default margins depend on the maximum margins of the plot's marks. While most marks default to zero margins (because they are drawn inside the chart area), Plot's axis marks have non-zero default margins.
    """
    margin_bottom: float | ParamRef
    """The bottom margin; the distance in pixels between the bottom edges of the inner and outer plot area. Defaults to the maximum bottom margin of the plot's marks."""
    margin_left: float | ParamRef
    """The left margin; the distance in pixels between the left edges of the inner and outer plot area. Defaults to the maximum left margin of the plot's marks."""
    margin_right: float | ParamRef
    """The right margin; the distance in pixels between the right edges of the inner and outer plot area. Defaults to the maximum right margin of the plot's marks."""
    margin_top: float | ParamRef
    """The top margin; the distance in pixels between the top edges of the inner and outer plot area. Defaults to the maximum top margin of the plot's marks."""
    margins: Margins
    """A shorthand object notation for setting multiple margin values. The object keys are margin names (top, right, etc)."""
    name: str
    """A unique name for the plot. The name is used by standalone legend components to to lookup the plot and access scale mappings."""
    opacity_base: float | ParamRef
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    opacity_clamp: bool | ParamRef
    """
    If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

    Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

    For continuous scales only.
    """
    opacity_constant: float | ParamRef
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    opacity_domain: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

    Opacity scales have a default domain from 0 to the maximum value of associated channels.
    """
    opacity_exponent: float | ParamRef
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    opacity_label: str | ParamRef | None
    """
    A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

    For axes and legends only.
    """
    opacity_nice: bool | float | Interval | ParamRef
    """
    If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
    *minute*, *wednesday* or *month* to specify what constitutes a nice interval.

    For continuous scales only.
    """
    opacity_percent: bool | ParamRef
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    opacity_range: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's outputs (visual values).

    Opacity scales have a default range of [0, 1].
    """
    opacity_reverse: bool | ParamRef
    """
    Whether to reverse the scale's encoding; equivalent to reversing either the
    **domain** or **range**.
    """
    opacity_scale: ContinuousScaleType | ParamRef | None
    """The *opacity* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled. The opacity scale defaults to *linear*; this scales is intended for quantitative data."""
    opacity_tick_format: str | ParamRef | None
    """
    How to format inputs (abstract values) for axis tick labels; one of:

    - a [d3-format][1] string for numeric scales
    - a [d3-time-format][2] string for temporal scales

    [1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format
    """
    opacity_zero: bool | ParamRef
    """
    Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

    For quantitative scales only.
    """
    padding: float | ParamRef
    """
    For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

    For ordinal position scales only.
    """
    projection_clip: bool | float | Literal["frame"] | ParamRef | None
    """
    The projection's clipping method; one of:

    - *frame* or true (default) - clip to the plot's frame (including margins but not insets)
    - a number - clip to a circle of the given radius in degrees centered around the origin
    - null or false - do not clip

    Some projections (such as [*armadillo*][1] and [*berghaus*][2]) require spherical clipping: in that case set the marks' **clip** option to
    *sphere*.

    [1]: https://observablehq.com/@d3/armadillo [2]: https://observablehq.com/@d3/berghaus-star
    """
    projection_domain: Mapping[str, Any] | ParamRef
    """A GeoJSON object to fit to the plot's frame (minus insets); defaults to a Sphere for spherical projections (outline of the the whole globe)."""
    projection_inset: float | ParamRef
    """Shorthand to set the same default for all four projection insets. All insets typically default to zero, though not always. A positive inset reduces effective area, while a negative inset increases it."""
    projection_inset_bottom: float | ParamRef
    """Insets the bottom edge of the projection by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it)."""
    projection_inset_left: float | ParamRef
    """Insets the left edge of the projection by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it)."""
    projection_inset_right: float | ParamRef
    """Insets the right edge of the projection by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it)."""
    projection_inset_top: float | ParamRef
    """Insets the top edge of the projection by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it)."""
    projection_parallels: tuple[float | ParamRef, float | ParamRef] | ParamRef
    """
    The [standard parallels][1]. For conic projections only.

    [1]: https://d3js.org/d3-geo/conic#conic_parallels
    """
    projection_precision: float | ParamRef
    """
    The projection's [sampling threshold][1].

    [1]: https://d3js.org/d3-geo/projection#projection_precision
    """
    projection_rotate: tuple[float | ParamRef, float | ParamRef, float | ParamRef] | ParamRef
    """A rotation of the sphere before projection; defaults to [0, 0, 0]. Specified as Euler angles λ (yaw, or reference longitude), φ (pitch, or reference latitude), and optionally γ (roll), in degrees."""
    projection_type: ProjectionName | ParamRef | None
    """
    The desired projection; one of:

    - a named built-in projection such as *albers-usa*
    - null, for no projection

    Named projections are scaled and translated to fit the **domain** to the plot's frame (minus insets).
    """
    r_base: float | ParamRef
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    r_clamp: Any
    """
    If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

    Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

    For continuous scales only.
    """
    r_constant: float | ParamRef
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    r_domain: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

    Radius scales have a default domain from 0 to the median first quartile of associated channels.
    """
    r_exponent: float | ParamRef
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    r_label: str | ParamRef | None
    """A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value."""
    r_nice: bool | float | Interval | ParamRef
    """
    If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
    *minute*, *wednesday* or *month* to specify what constitutes a nice interval.

    For continuous scales only.
    """
    r_percent: bool | ParamRef
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    r_range: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For other ordinal data, such as for a *color* scale, it is an array (or iterable) of output values in the same order as the **domain**.

    Radius scales have a default range of [0, 3].
    """
    r_scale: ContinuousScaleType | ParamRef | None
    """The *r* (radius) scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled. The radius scale defaults to *sqrt*; this scale is intended for quantitative data."""
    r_zero: bool | ParamRef
    """
    Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

    For quantitative scales only.
    """
    style: str | CSSStyles | ParamRef | None
    """
    Custom styles to override Plot's defaults. Styles may be specified either as a string of inline styles (*e.g.*, `"color: red;"`, in the same fashion as assigning [*element*.style][1]) or an object of properties (*e.g.*, `{color: "red"}`, in the same fashion as assigning [*element*.style properties][2]). Note that unitless numbers ([quirky lengths][3]) such as `{padding: 20}` may not supported by some browsers; you should instead specify a string with units such as `{padding: "20px"}`. By default, the returned plot has a max-width of 100%, and the system-ui font. Plot's marks and axes default to [currentColor][4], meaning that they will inherit the surrounding content's color.

    [1]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style [2]: https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration [3]: https://www.w3.org/TR/css-values-4/#deprecated-quirky-length [4]: https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#currentcolor_keyword
    """
    symbol_domain: Sequence[Any] | Fixed | ParamRef
    """The extent of the scale's inputs (abstract values). By default inferred from channel values. As symbol scales are discrete, the domain is an array (or iterable) of values is the desired order, defaulting to natural ascending order."""
    symbol_range: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For other ordinal data, such as for a *color* scale, it is an array (or iterable) of output values in the same order as the **domain**.

    Symbol scales have a default range of categorical symbols; the choice of symbols depends on whether the associated dot mark is filled or stroked.
    """
    symbol_scale: DiscreteScaleType | ParamRef | None
    """The *symbol* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled. Defaults to an *ordinal* scale type."""
    width: float | ParamRef
    """
    The outer width of the plot in pixels, including margins. Defaults to 640. On Observable, this can be set to the built-in [width][1] for full-width responsive plots. Note: the default style has a max-width of 100%; the plot will automatically shrink to fit even when a fixed width is specified.

    [1]: https://github.com/observablehq/stdlib/blob/main/README.md#width
    """
    x_align: float | ParamRef
    """
    How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

    - 0 - use the start of the range, putting unused space at the end
    - 0.5 (default) - use the middle, distributing unused space evenly
    - 1 use the end, putting unused space at the start

    For ordinal position scales only.
    """
    x_aria_description: str | ParamRef
    """A textual description for the axis in the accessibility tree."""
    x_aria_label: str | ParamRef
    """A short label representing the axis in the accessibility tree."""
    x_axis: Literal["top", "bottom", "both"] | bool | ParamRef | None
    """
    The side of the frame on which to place the implicit axis: *top* or
    *bottom* for *x*. Defaults to *bottom* for an *x* scale.

    If *both*, an implicit axis will be rendered on both sides of the plot (*top* and *bottom* for *x*). If null, the implicit axis is suppressed.
    """
    x_base: float | ParamRef
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    x_clamp: bool | ParamRef
    """
    If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

    Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

    For continuous scales only.
    """
    x_constant: float | ParamRef
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    x_domain: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

    Linear scales have a default domain of [0, 1]. Log scales have a default domain of [1, 10] and cannot include zero. Radius scales have a default domain from 0 to the median first quartile of associated channels. Length have a default domain from 0 to the median median of associated channels. Opacity scales have a default domain from 0 to the maximum value of associated channels.
    """
    x_exponent: float | ParamRef
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    x_font_variant: str | ParamRef
    """The font-variant attribute for axis ticks; defaults to *tabular-nums* for quantitative axes."""
    x_grid: bool | str | Interval | Sequence[Any] | ParamRef
    """
    Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

    For axes only.
    """
    x_inset: float | ParamRef
    """
    Shorthand to set the same default for all four insets: **insetTop**,
    **insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.
    """
    x_inset_left: float | ParamRef
    """Insets the left edge by the specified number of pixels. A positive value insets towards the right edge (reducing effective area), while a negative value insets away from the right edge (increasing it)."""
    x_inset_right: float | ParamRef
    """Insets the right edge by the specified number of pixels. A positive value insets towards the left edge (reducing effective area), while a negative value insets away from the left edge (increasing it)."""
    x_label: str | ParamRef | None
    """
    A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

    For axes and legends only.
    """
    x_label_anchor: Literal["top", "right", "bottom", "left", "center"] | ParamRef
    """
    Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
    *center*; for horizontal position scales (*x* and *fx*), may be *left*,
    *right*, or *center*. Defaults to *center* for ordinal scales (including
    *fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*.
    """
    x_label_arrow: LabelArrow | ParamRef
    """Whether to apply a directional arrow such as → or ↑ to the x-axis scale label. If *auto* (the default), the presence of the arrow depends on whether the scale is ordinal."""
    x_label_offset: float | ParamRef
    """The axis **label** position offset (in pixels); default depends on margins and orientation."""
    x_line: bool | ParamRef
    """If true, draw a line along the axis; if false (default), do not."""
    x_nice: bool | float | Interval | ParamRef
    """
    If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
    *minute*, *wednesday* or *month* to specify what constitutes a nice interval.

    For continuous scales only.
    """
    x_padding: float | ParamRef
    """
    For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

    For ordinal position scales only.
    """
    x_padding_inner: float | ParamRef
    """For a *band* scale, how much of the range to reserve to separate adjacent bands."""
    x_padding_outer: float | ParamRef
    """For a *band* scale, how much of the range to reserve to inset first and last bands."""
    x_percent: bool | ParamRef
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    x_range: Sequence[Any] | Fixed | ParamRef
    """The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale."""
    x_reverse: bool | ParamRef
    """
    Whether to reverse the scale's encoding; equivalent to reversing either the
    **domain** or **range**.
    """
    x_round: bool | ParamRef
    """
    If true, round the output value to the nearest integer (pixel); useful for crisp edges when rendering.

    For position scales only.
    """
    x_scale: PositionScaleType | ParamRef | None
    """
    The *x* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled.

    For quantitative data (numbers), defaults to *linear*; for temporal data (dates), defaults to *utc*; for ordinal data (strings or booleans), defaults to *point* for position scales, *categorical* for color scales, and otherwise *ordinal*. However, the radius scale defaults to *sqrt*, and the length and opacity scales default to *linear*; these scales are intended for quantitative data. The plot's marks may also impose a scale type; for example, the barY mark requires that *x* is a *band* scale.
    """
    x_tick_format: str | ParamRef | None
    """
    How to format inputs (abstract values) for axis tick labels; one of:

    - a [d3-format][1] string for numeric scales
    - a [d3-time-format][2] string for temporal scales

    [1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format
    """
    x_tick_padding: float | ParamRef
    """
    The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **xTickSize** and
    **xTickRotate**.
    """
    x_tick_rotate: float | ParamRef
    """The rotation angle of axis tick labels in degrees clocksize; defaults to 0."""
    x_tick_size: float | ParamRef
    """
    The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
    *opacity* *ramp* legends, and 0 for *fx* and *fy* axes.
    """
    x_tick_spacing: float | ParamRef
    """The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*."""
    x_ticks: float | Interval | Sequence[Any] | ParamRef
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""
    x_zero: bool | ParamRef
    """
    Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

    For quantitative scales only.
    """
    xy_domain: Sequence[Any] | Fixed | ParamRef
    """Set the *x* and *y* scale domains."""
    y_align: float | ParamRef
    """
    How to distribute unused space in the **range** for *point* and *band* scales. A number in [0, 1], such as:

    - 0 - use the start of the range, putting unused space at the end
    - 0.5 (default) - use the middle, distributing unused space evenly
    - 1 use the end, putting unused space at the start

    For ordinal position scales only.
    """
    y_aria_description: str | ParamRef
    """A textual description for the axis in the accessibility tree."""
    y_aria_label: str | ParamRef
    """A short label representing the axis in the accessibility tree."""
    y_axis: Literal["left", "right", "both"] | bool | ParamRef | None
    """
    The side of the frame on which to place the implicit axis: *left* or
    *right* for *y*. Defaults to *left* for a *y* scale.

    If *both*, an implicit axis will be rendered on both sides of the plot (*left* and *right* for *y*). If null, the implicit axis is suppressed.
    """
    y_base: float | ParamRef
    """A log scale's base; defaults to 10. Does not affect the scale's encoding, but rather the default ticks. For *log* scales only."""
    y_clamp: bool | ParamRef
    """
    If true, values below the domain minimum are treated as the domain minimum, and values above the domain maximum are treated as the domain maximum.

    Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: clamped values may need an annotation to avoid misinterpretation. Clamping typically requires setting an explicit **domain** since if the domain is inferred, no values will be outside the domain.

    For continuous scales only.
    """
    y_constant: float | ParamRef
    """A symlog scale's constant, expressing the magnitude of the linear region around the origin; defaults to 1. For *symlog* scales only."""
    y_domain: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's inputs (abstract values). By default inferred from channel values. For continuous data (numbers and dates), it is typically [*min*, *max*]; it can be [*max*, *min*] to reverse the scale. For ordinal data (strings or booleans), it is an array (or iterable) of values is the desired order, defaulting to natural ascending order.

    Linear scales have a default domain of [0, 1]. Log scales have a default domain of [1, 10] and cannot include zero.
    """
    y_exponent: float | ParamRef
    """A power scale's exponent (*e.g.*, 0.5 for sqrt); defaults to 1 for a linear scale. For *pow* scales only."""
    y_font_variant: str | ParamRef
    """The font-variant attribute for axis ticks; defaults to *tabular-nums* for quantitative axes."""
    y_grid: bool | str | Interval | Sequence[Any] | ParamRef
    """
    Whether to show a grid aligned with the scale's ticks. If true, show a grid with the currentColor stroke; if a string, show a grid with the specified stroke color; if an approximate number of ticks, an interval, or an array of tick values, show corresponding grid lines. See also the grid mark.

    For axes only.
    """
    y_inset: float | ParamRef
    """
    Shorthand to set the same default for all four insets: **insetTop**,
    **insetRight**, **insetBottom**, and **insetLeft**. All insets typically default to zero, though not always (say when using bin transform). A positive inset reduces effective area, while a negative inset increases it.
    """
    y_inset_bottom: float | ParamRef
    """Insets the bottom edge by the specified number of pixels. A positive value insets towards the top edge (reducing effective area), while a negative value insets away from the top edge (increasing it)."""
    y_inset_top: float | ParamRef
    """Insets the top edge by the specified number of pixels. A positive value insets towards the bottom edge (reducing effective area), while a negative value insets away from the bottom edge (increasing it)."""
    y_label: str | ParamRef | None
    """
    A textual label to show on the axis or legend; if null, show no label. By default the scale label is inferred from channel definitions, possibly with an arrow (↑, →, ↓, or ←) to indicate the direction of increasing value.

    For axes and legends only.
    """
    y_label_anchor: Literal["top", "right", "bottom", "left", "center"] | ParamRef
    """
    Where to place the axis **label** relative to the plot's frame. For vertical position scales (*y* and *fy*), may be *top*, *bottom*, or
    *center*; for horizontal position scales (*x* and *fx*), may be *left*,
    *right*, or *center*. Defaults to *center* for ordinal scales (including
    *fx* and *fy*), and otherwise *top* for *y*, and *right* for *x*.
    """
    y_label_arrow: LabelArrow | ParamRef
    """Whether to apply a directional arrow such as → or ↑ to the x-axis scale label. If *auto* (the default), the presence of the arrow depends on whether the scale is ordinal."""
    y_label_offset: float | ParamRef
    """The axis **label** position offset (in pixels); default depends on margins and orientation."""
    y_line: bool | ParamRef
    """If true, draw a line along the axis; if false (default), do not."""
    y_nice: bool | float | Interval | ParamRef
    """
    If true, or a tick count or interval, extend the domain to nice round values. Defaults to 1, 2 or 5 times a power of 10 for *linear* scales, and nice time intervals for *utc* and *time* scales. Pass an interval such as
    *minute*, *wednesday* or *month* to specify what constitutes a nice interval.

    For continuous scales only.
    """
    y_padding: float | ParamRef
    """
    For *band* scales, how much of the **range** to reserve to separate adjacent bands; defaults to 0.1 (10%). For *point* scales, the amount of inset for the first and last value as a proportion of the bandwidth; defaults to 0.5 (50%).

    For ordinal position scales only.
    """
    y_padding_inner: float | ParamRef
    """For a *band* scale, how much of the range to reserve to separate adjacent bands."""
    y_padding_outer: float | ParamRef
    """For a *band* scale, how much of the range to reserve to inset first and last bands."""
    y_percent: bool | ParamRef
    """If true, shorthand for a transform suitable for percentages, mapping proportions in [0, 1] to [0, 100]."""
    y_range: Sequence[Any] | Fixed | ParamRef
    """
    The extent of the scale's outputs (visual values). By default inferred from the scale's **type** and **domain**, and for position scales, the plot's dimensions. For continuous data (numbers and dates), and for ordinal position scales (*point* and *band*), it is typically [*min*,
    *max*]; it can be [*max*, *min*] to reverse the scale.
    """
    y_reverse: bool | ParamRef
    """
    Whether to reverse the scale's encoding; equivalent to reversing either the
    **domain** or **range**. Note that by default, when the *y* scale is continuous, the *max* value points to the top of the screen, whereas ordinal values are ranked from top to bottom.
    """
    y_round: bool | ParamRef
    """
    If true, round the output value to the nearest integer (pixel); useful for crisp edges when rendering.

    For position scales only.
    """
    y_scale: PositionScaleType | ParamRef | None
    """
    The *y* scale type, affecting how the scale encodes abstract data, say by applying a mathematical transformation. If null, the scale is disabled.

    For quantitative data (numbers), defaults to *linear*; for temporal data (dates), defaults to *utc*; for ordinal data (strings or booleans), defaults to *point* for position scales,  The plot's marks may also impose a scale type; for example, the barY mark requires that *x* is a *band* scale.
    """
    y_tick_format: str | ParamRef | None
    """
    How to format inputs (abstract values) for axis tick labels; one of:

    - a [d3-format][1] string for numeric scales
    - a [d3-time-format][2] string for temporal scales

    [1]: https://d3js.org/d3-time [2]: https://d3js.org/d3-time-format
    """
    y_tick_padding: float | ParamRef
    """
    The distance between an axis tick mark and its associated text label (in pixels); often defaults to 3, but may be affected by **yTickSize** and
    **yTickRotate**.
    """
    y_tick_rotate: float | ParamRef
    """The rotation angle of axis tick labels in degrees clocksize; defaults to 0."""
    y_tick_size: float | ParamRef
    """
    The length of axis tick marks in pixels; negative values extend in the opposite direction. Defaults to 6 for *x* and *y* axes and *color* and
    *opacity* *ramp* legends, and 0 for *fx* and *fy* axes.
    """
    y_tick_spacing: float | ParamRef
    """The desired approximate spacing between adjacent axis ticks, affecting the default **ticks**; defaults to 80 pixels for *x* and *fx*, and 35 pixels for *y* and *fy*."""
    y_ticks: float | Interval | Sequence[Any] | ParamRef
    """The desired approximate number of axis ticks, or an explicit array of tick values, or an interval such as *day* or *month*."""
    y_zero: bool | ParamRef
    """
    Whether the **domain** must include zero. If the domain minimum is positive, it will be set to zero; otherwise if the domain maximum is negative, it will be set to zero.

    For quantitative scales only.
    """


class PlotAttributes(_PlotAttributesOpen, total=False, closed=True): ...


class _PlotOpen(_PlotAttributesOpen, total=False):
    """A plot component."""

    plot: Required[Sequence[PlotMark | PlotInteractor | PlotLegend]]
    """An array of plot marks, interactors, or legends. Marks are graphical elements that make up plot layers. Unless otherwise configured, interactors will use the nearest previous mark as a basis for which data fields to select."""


class Plot(_PlotOpen, total=False, closed=True): ...


Component = TypeAliasType(
    "Component",
    Union[
        "HConcat", "VConcat", HSpace, VSpace, Menu, Search, Slider, Table, Plot, PlotMark, Legend
    ],
)
"""A specification component such as a plot, input widget, or layout."""


class _HConcatOpen(TypedDict, total=False):
    """An hconcat component."""

    hconcat: Required[Sequence[Component]]
    """Horizontally concatenate components in a row layout."""


class HConcat(_HConcatOpen, total=False, closed=True): ...


class _VConcatOpen(TypedDict, total=False):
    """A vconcat component."""

    vconcat: Required[Sequence[Component]]
    """Vertically concatenate components in a column layout."""


class VConcat(_VConcatOpen, total=False, closed=True): ...
