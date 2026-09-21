from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Final, final

import mosaic_spec as ms
from mosaic_spec._gen.data import _DataOptions
from mosaic_spec._typing_compat import TypeAliasType

if TYPE_CHECKING:
    from collections.abc import Mapping

    from mosaic_spec._typing_compat import Self, Unpack

__all__ = ("query",)

query: Final = ms.DataQuery

# target options, with required filled
DataOptions = TypeAliasType(
    "DataOptions",
    ms.DataCSV | ms.DataJSON | ms.DataParquet | ms.DataSpatial | ms.DataTable | ms.DataJSONObjects,
)


# common options that can be unpacked safely
class Options(_DataOptions, closed=True): ...


class CSVOptions(_DataOptions, closed=True):
    delimiter: str
    """The column delimiter string.

    If not specified, DuckDB will try to infer the delimiter automatically.
    """
    sample_size: float
    """The sample size, in table rows, to consult for type inference.

    Set to `-1` to process all rows in the dataset.
    """


class SpatialOptions(_DataOptions, closed=True):
    layer: str
    """The named layer to load from the file.

    For example, in a TopoJSON file the layer is the named object to extract.
    For Excel spreadsheet files, the layer is the name of the worksheet to extract.
    """


def _into_file_name(file: str | Path, name: str, /) -> tuple[str, str]:
    """Normalize file path and reuse the file name if we don't have one to name the dataset."""
    path = Path(file)
    return path.as_posix(), name or path.stem


@final
class Data:
    """A named dataset definition.

    >>> Data.from_parquet("data/berlin-covid.parquet")
    Data(name='berlin-covid', options={'file': 'data/berlin-covid.parquet', 'type': 'parquet'})
    """

    __slots__ = ("name", "options")

    def __init__(self, name: str, options: DataOptions) -> None:
        self.name: str = name
        self.options: DataOptions = options

    @classmethod
    def from_csv(cls, file: str | Path, /, name: str = "", **kwds: Unpack[CSVOptions]) -> Self:
        file, name = _into_file_name(file, name)
        return cls(name, ms.DataCSV(file=file, type="csv", **kwds))

    @classmethod
    def from_json(cls, file: str | Path, /, name: str = "", **kwds: Unpack[Options]) -> Self:
        file, name = _into_file_name(file, name)
        return cls(name, ms.DataJSON(file=file, type="json", **kwds))

    @classmethod
    def from_parquet(cls, file: str | Path, /, name: str = "", **kwds: Unpack[Options]) -> Self:
        file, name = _into_file_name(file, name)
        return cls(name, ms.DataParquet(file=file, type="parquet", **kwds))

    @classmethod
    def from_spatial(
        cls, file: str | Path, /, name: str = "", **kwds: Unpack[SpatialOptions]
    ) -> Self:
        file, name = _into_file_name(file, name)
        return cls(name, ms.DataSpatial(file=file, type="spatial", **kwds))

    @classmethod
    def from_sql(cls, query: str, /, name: str, **kwds: Unpack[Options]) -> Self:
        return cls(name, ms.DataTable(query=query, type="table", **kwds))

    @classmethod
    def from_rows(cls, name: str, *rows: Mapping[str, Any]) -> Self:
        return cls(name, ms.DataJSONObjects(data=rows, type="json"))

    @classmethod
    def from_columns(cls, name: str, /, **named_columns: list[Any] | tuple[Any, ...]) -> Self:
        column_names = named_columns.keys()
        rows = (dict(zip(column_names, row, strict=False)) for row in named_columns.values())
        return cls.from_rows(name, *rows)

    def source(self, filter_by: ms.ParamRef | None = None, *, optimize: bool = True) -> Source:
        """Create an input data specification for a plot mark.

        Args:
            filter_by: A selection that filters the mark data.
            optimize: A flag to enable any mark-specific query optimizations.
                If `false`, optimizations are disabled to aid testing and debugging.

        Examples:
            >>> file = "data/flights-200k.parquet"
            >>> Data.from_parquet(file, "flights").source(ms.ParamRef("$brush"))
            Source({'source': 'flights', 'filter_by': '$brush'})

            >>> Data.from_parquet(file).source(optimize=False)
            Source({'source': 'flights-200k', 'optimize': False})
        """
        result: ms.PlotFrom = {"source": self.name}
        if (not filter_by) and optimize:
            return Source(result)
        if filter_by:
            result["filter_by"] = filter_by
        if not optimize:
            result["optimize"] = optimize
        return Source(result)

    def to_dict(self) -> ms.Data:
        return {self.name: self.options}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, options={self.options!r})"


@final
class Source:
    """An input data specification for a plot mark."""

    __slots__ = ("options",)

    def __init__(self, options: ms.PlotFrom) -> None:
        self.options: ms.PlotFrom = options

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.options!r})"
