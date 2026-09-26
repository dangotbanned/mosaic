from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final, Generic, Literal as L, final, overload

import mosaic_spec as ms
from mosaic_spec._gen.data import _DataOptions
from mosaic_spec._typing_compat import TypeAliasType, TypeVar

if TYPE_CHECKING:
    from collections.abc import Mapping

    from mosaic_spec._typing_compat import Self, Unpack
    from tests.apis.marks import MarksNs
    from tests.apis.params import Param, ParamDef
    from tests.apis.protocols import DataDefs, ParamDefs

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

    @property
    def _source(self) -> str:
        return self.name

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

    def source(
        self, filter_by: ParamDef | None = None, *, optimize: L[False] | None = None
    ) -> DataSource:
        """Create an input data specification for a plot mark.

        Args:
            filter_by: A selection that filters the mark data.
            optimize: A flag to enable any mark-specific query optimizations.
                If `false`, optimizations are disabled to aid testing and debugging.

        Examples:
            >>> from tests.apis.params import p
            >>> file = "data/flights-200k.parquet"
            >>> Data.from_parquet(file, "flights").source(p.brush.cross())
            Source({'source': 'flights', 'filter_by': '$brush'})

            >>> Data.from_parquet(file).source(optimize=False)
            Source({'source': 'flights-200k', 'optimize': False})
        """
        return DataSource(self, filter_by, optimize=optimize)

    @overload
    def filter(self, filter_by: ParamDef, /) -> Source: ...
    @overload
    def filter(self, where: ms.DataQuery, /) -> Data: ...
    def filter(self, by: ParamDef | ms.DataQuery, /) -> Data | Source:
        """Filter the data source.

        Bind a selection parameter that filters the mark data:

        >>> from tests.apis.params import p
        >>> Data.from_parquet("data/athletes.parquet").filter(p.category.intersect())
        Source({'source': 'athletes', 'filter_by': '$category'})

        Apply a `WHERE` clause to the data upon load.
        Only rows that pass the filter are included:

        >>> Data.from_parquet("data/stocks.parquet").filter(query("Symbol = 'AAPL'"))
        Data(name='stocks', options={'file': 'data/stocks.parquet', 'type': 'parquet', 'where': "Symbol = 'AAPL'"})
        """
        if isinstance(by, str):
            options = deepcopy(self.options)
            options["where"] = by
            return Data(self.name, options)
        return DataSource(self, by)

    def no_optimizations(self) -> Source:
        return DataSource(self, optimize=False)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, options={self.options!r})"


S = TypeVar("S", Data, "Param")
V = TypeVar("V", str, ms.ParamRef)


class _Source(Generic[S, V]):
    __slots__ = ("_filter_by", "_optimize", "_source")

    def __init__(
        self, source: S, filter_by: ParamDef | None = None, *, optimize: L[False] | None = None
    ) -> None:
        self._source: S = source
        self._filter_by: ParamDef | None = filter_by
        self._optimize: L[False] | None = optimize

    def _source_value(self, data: DataDefs, params: ParamDefs) -> V:
        raise NotImplementedError

    def to_dict(self, data: DataDefs, params: ParamDefs) -> ms.PlotFrom:
        result: ms.PlotFrom = {"source": self._source_value(data, params)}
        if filter_by := self._filter_by:
            result["filter_by"] = filter_by.ref(params)
        if self._optimize is False:
            result["optimize"] = False
        return result


@final
class DataSource(_Source[Data, str]):
    __slots__ = ()

    def _source_value(self, data: DataDefs, params: ParamDefs) -> str:
        source_name = self._source.name
        if source_name not in data:
            data[source_name] = self._source.options
        return source_name

    def __repr__(self) -> str:
        result: ms.PlotFrom = {"source": self._source.name}
        if filter_by := self._filter_by:
            result["filter_by"] = filter_by.__repr__()
        if self._optimize is False:
            result["optimize"] = False
        return f"Source({result})"

    @property
    def mark(self) -> MarksNs:
        from tests.apis.marks import MarksNs

        return MarksNs(self)


@final
class ParamSource(_Source["Param", ms.ParamRef]):
    __slots__ = ()

    def _source_value(self, data: DataDefs, params: ParamDefs) -> ms.ParamRef:
        # needs to traverse the param every time, since it may include others we can't see yet
        return self._source.ref(params)

    def __repr__(self) -> str:
        result: ms.PlotFrom = {"source": self._source.__repr__()}
        if filter_by := self._filter_by:
            result["filter_by"] = filter_by.__repr__()
        if self._optimize is False:
            result["optimize"] = False
        return f"Source({result})"

    @property
    def mark(self) -> MarksNs:
        from tests.apis.marks import MarksNs

        return MarksNs(self)


Source = TypeAliasType("Source", DataSource | ParamSource)
"""An input data specification for a plot mark."""
