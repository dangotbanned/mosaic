# Generated: `mosaic_spec._gen.data`
from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Literal as L

from mosaic_spec._typing_compat import Required, TypeAliasType, TypedDict

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
    type: Required[L["csv"]]
    """The data source type. One of:
- `"table"`: Define a new table based on a SQL query.
- `"csv"`: Load a comma-separated values (CSV) file.
- `"json"`: Load JavaScript Object Notation (json) data.
- `"parquet"`: Load a Parquet file.
- `"spatial"`: Load a spatial data file format via `ST_Read`."""
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: Sequence[str] | str
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
    where: Sequence[str] | str
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
    type: Required[L["json"]]
    """The data source type. One of:
- `"table"`: Define a new table based on a SQL query.
- `"csv"`: Load a comma-separated values (CSV) file.
- `"json"`: Load JavaScript Object Notation (json) data.
- `"parquet"`: Load a Parquet file.
- `"spatial"`: Load a spatial data file format via `ST_Read`."""
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: Sequence[str] | str
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
    type: L["json"]
    """The data source type. One of:
- `"table"`: Define a new table based on a SQL query.
- `"csv"`: Load a comma-separated values (CSV) file.
- `"json"`: Load JavaScript Object Notation (json) data.
- `"parquet"`: Load a Parquet file.
- `"spatial"`: Load a spatial data file format via `ST_Read`."""
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: Sequence[str] | str
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
    type: Required[L["parquet"]]
    """The data source type. One of:
- `"table"`: Define a new table based on a SQL query.
- `"csv"`: Load a comma-separated values (CSV) file.
- `"json"`: Load JavaScript Object Notation (json) data.
- `"parquet"`: Load a Parquet file.
- `"spatial"`: Load a spatial data file format via `ST_Read`."""
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: Sequence[str] | str
    """A filter (WHERE clause) to apply upon load. Only rows that pass the filter are included."""


DataQuery = TypeAliasType("DataQuery", str)
"""A SQL query defining a new temporary database table."""


class DataSpatial(TypedDict, total=False, closed=True):
    """A data definition that loads a supported spatial data file format."""

    file: Required[str]
    """The file path for the spatial dataset to load. See the [DuckDB spatial documentation][1] for more information on supported file types.

[1]: https://duckdb.org/docs/extensions/spatial.html#st_read--read-spatial-data-from-files"""
    layer: str
    """The named layer to load from the file. For example, in a TopoJSON file the layer is the named object to extract. For Excel spreadsheet files, the layer is the name of the worksheet to extract."""
    replace: bool
    """Flag (default `true`) to replace an existing table of the same name. If `false`, creating a new table with an existing name raises an error."""
    select: Sequence[str]
    """A list of column names to extract upon load. Any other columns are omitted."""
    temp: bool
    """Flag (default `true`) to generate a temporary view or table."""
    type: Required[L["spatial"]]
    """The data source type. One of:
- `"table"`: Define a new table based on a SQL query.
- `"csv"`: Load a comma-separated values (CSV) file.
- `"json"`: Load JavaScript Object Notation (json) data.
- `"parquet"`: Load a Parquet file.
- `"spatial"`: Load a spatial data file format via `ST_Read`."""
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: Sequence[str] | str
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
    type: Required[L["table"]]
    """The data source type. One of:
- `"table"`: Define a new table based on a SQL query.
- `"csv"`: Load a comma-separated values (CSV) file.
- `"json"`: Load JavaScript Object Notation (json) data.
- `"parquet"`: Load a Parquet file.
- `"spatial"`: Load a spatial data file format via `ST_Read`."""
    view: bool
    """Flag (default `false`) to generate a view instead of a table."""
    where: Sequence[str] | str
    """A filter (WHERE clause) to apply upon load. Only rows that pass the filter are included."""


DataDefinition = TypeAliasType(
    "DataDefinition",
    DataArray
    | DataCSV
    | DataFile
    | DataJSON
    | DataJSONObjects
    | DataParquet
    | DataQuery
    | DataSpatial
    | DataTable,
)
Data = TypeAliasType("Data", Mapping[str, DataDefinition])
"""Top-level dataset definitions."""


__all__ = (
    "Data",
    "DataArray",
    "DataCSV",
    "DataDefinition",
    "DataFile",
    "DataJSON",
    "DataJSONObjects",
    "DataParquet",
    "DataQuery",
    "DataSpatial",
    "DataTable",
)
