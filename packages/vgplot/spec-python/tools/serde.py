"""Convenience wrapper around [`msgspec.json`][]."""

from __future__ import annotations

import functools
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal as L

import msgspec

if TYPE_CHECKING:
    from collections.abc import Buffer, Mapping

__all__ = ("convert", "deserialize", "read_json", "serialize", "write_json")


def serialize(obj: Any, /, *, order: L["deterministic", "sorted"] | None = None) -> bytes:
    return _encoder(order).encode(obj)


def deserialize[T](buf: Buffer | str, tp: type[T], /) -> T:
    return _decoder(tp).decode(buf)


def convert[T](obj: msgspec.Struct | Mapping[str, Any], into: type[T], /) -> T:
    return deserialize(serialize(obj), into)


def read_json[T](path: str | Path, tp: type[T], /) -> T:
    with Path(path).open(encoding="utf8") as fd:
        return deserialize(fd.read(), tp)


def write_json(path: str | Path, obj: Any) -> None:
    json_str = serialize(obj, order="sorted").decode()
    path = Path(path)
    path.touch()
    with path.open("w", encoding="utf8", newline="\n") as fd:
        fd.write(json_str)


@functools.cache
def _decoder[T](tp: type[T], /) -> msgspec.json.Decoder[T]:
    return msgspec.json.Decoder(tp)


@functools.cache
def _encoder(order: L["deterministic", "sorted"] | None = None, /) -> msgspec.json.Encoder:
    return msgspec.json.Encoder(order=order)
