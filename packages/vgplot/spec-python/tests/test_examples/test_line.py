from __future__ import annotations

from typing import Literal as L

import pytest

import mosaic_spec as ms


@pytest.fixture
def file() -> str:
    return "data/stocks.parquet"


@pytest.fixture
def mark() -> L["lineY"]:
    return "lineY"


@pytest.fixture
def where() -> str:
    return "Symbol = 'AAPL'"


def test_infer(file: str, where: str, mark: L["lineY"]) -> None:
    _spec: ms.Spec = {
        "data": {"aapl": {"type": "parquet", "file": file, "where": where}},
        "plot": [{"mark": mark, "data": {"source": "aapl"}, "x": "Date", "y": "Close"}],
        "width": 680,
        "height": 200,
    }


def test_typed_dict(file: str, where: str, mark: L["lineY"]) -> None:
    _spec = ms.SpecPlot(
        data={"aapl": ms.DataParquet(type="parquet", file=file, where=where)},
        plot=(ms.LineY(mark=mark, data={"source": "aapl"}, x="Date", y="Close"),),
        width=680,
        height=200,
    )


def test_invalid(file: str, where: str, mark: L["lineY"]) -> None:
    _spec: ms.SpecPlot = {  # pyright: ignore[reportAssignmentType]
        "data": {
            "aapl": {"type": "parquet", "file": file, "where": where},
            "plot": [{"mark": mark, "data": {"source": "aapl"}, "x": bytes(1), "y": "Close"}],
            "width": 680,
            "height": 200,
        }  # ty: ignore[invalid-argument-type]
    }
