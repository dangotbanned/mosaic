"""Convenience wrapper around [`msgspec.json`][]."""

from __future__ import annotations

import functools
from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal as L

import msgspec

if TYPE_CHECKING:
    from collections.abc import Buffer, Callable, Mapping

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
    return msgspec.json.Decoder(tp, dec_hook=_decoder_hook)


@functools.cache
def _encoder(order: L["deterministic", "sorted"] | None = None, /) -> msgspec.json.Encoder:
    return msgspec.json.Encoder(order=order, enc_hook=_encoder_hook)


@functools.singledispatch
def _encoder_hook(obj: Any, /) -> Any:
    tp = type(obj)
    msg = f"Objects of type '{tp.__module__}.{tp.__name__}' cannot be serialized by msgspec, got: {obj!r}"
    raise NotImplementedError(msg)


@functools.singledispatch
def _decoder_hook(tp: type[Any], obj: Any, /) -> Any:
    tp = type(obj)
    msg = f"Objects of type '{tp.__module__}.{tp.__name__}' cannot be deserialized by msgspec, got: {obj!r}"
    raise NotImplementedError(msg)


@_decoder_hook.register(deque)
def _use_constructor[T, R](cb: Callable[[T], R], obj: T, /) -> R:
    return cb(obj)


_encoder_hook.register(deque, list)
