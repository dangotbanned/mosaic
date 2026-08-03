"""Convenience wrapper around [`msgspec.json`][].

## Extensions
### Full support
- [`collections.deque`][]

### Limited support
- [`pathlib.Path`][] (must be related to `spec-python/src`)
"""

from __future__ import annotations

import functools
from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal as L

import msgspec

from tools import fs
from tools._dispatch import type_dispatch

if TYPE_CHECKING:
    from collections.abc import Buffer, Callable, Mapping

__all__ = ("convert", "deserialize", "read_json", "serialize", "write_json")


def serialize(obj: Any, /, *, order: L["deterministic", "sorted"] | None = None) -> bytes:
    """Serialize an object as JSON."""
    return _encoder(order).encode(obj)


def deserialize[T](buf: Buffer | str, tp: type[T], /) -> T:
    """Deserialize an object from JSON into `T`"""
    return _decoder(tp).decode(buf)


def convert[T](obj: msgspec.Struct | Mapping[str, Any], into: type[T], /) -> T:
    """Convert a struct-like object through `msgspec`.

    This is like a field filter with struct-level configuration on strict-ness.

    ## Notes
    There might be a way to configure [msgspec.convert] for this.

    [msgspec.convert]: https://msgspec.dev/api#msgspec.convert
    """
    return deserialize(serialize(obj), into)


def read_json[T](path: str | Path, tp: type[T], /) -> T:
    """Deserialize a JSON file into `T`."""
    with Path(path).open(encoding="utf8") as fd:
        return deserialize(fd.read(), tp)


def write_json(path: str | Path, obj: Any) -> None:
    """Serialize an object to a JSON file."""
    _write_bytes_as_str(path, serialize(obj, order="sorted"))


def write_toml(path: str | Path, obj: Any) -> None:
    """Serialize an object to a TOML file."""
    _write_bytes_as_str(path, msgspec.toml.encode(obj, order="sorted"))


def _write_bytes_as_str(path: str | Path, b_string: bytes, /) -> None:
    path = Path(path)
    path.touch()
    with path.open("w", encoding="utf8", newline="\n") as fd:
        fd.write(b_string.decode())


@functools.cache
def _decoder[T](tp: type[T], /) -> msgspec.json.Decoder[T]:
    return msgspec.json.Decoder(tp, dec_hook=_decoder_hook)


@functools.cache
def _encoder(order: L["deterministic", "sorted"] | None = None, /) -> msgspec.json.Encoder:
    return msgspec.json.Encoder(order=order, enc_hook=_encoder_hook)


def _serialize_error(obj: Any) -> NotImplementedError:
    tp = type(obj)
    msg = f"Objects of type '{tp.__module__}.{tp.__name__}' cannot be serialized by msgspec, got: {obj!r}"
    return NotImplementedError(msg)


def _deserialize_error(tp: type[Any], obj: Any, /) -> NotImplementedError:
    tp = type(obj)
    msg = f"Objects of type '{tp.__module__}.{tp.__name__}' cannot be deserialized by msgspec, got: {obj!r}"
    return NotImplementedError(msg)


@functools.singledispatch
def _encoder_hook(obj: Any, /) -> Any:
    raise _serialize_error(obj)


@type_dispatch
def _decoder_hook(tp: type[Any], obj: Any, /) -> Any:
    raise _deserialize_error(tp, obj)


@_decoder_hook.register(deque)
def _use_constructor[T, R](cb: Callable[[T], R], obj: T, /) -> R:
    return cb(obj)


_encoder_hook.register(deque, list)


@_decoder_hook.register(Path)
def _deserialize_src_path(tp: type[Path], obj: object, /) -> Path:
    if isinstance(obj, str) and (absolute_path := fs.SRC / obj).exists():
        return absolute_path
    raise _deserialize_error(tp, obj)


@_encoder_hook.register(Path)
def _serialize_src_path(obj: Path, /) -> str:
    try:
        relative_path = obj.relative_to(fs.SRC)
    except ValueError:
        raise _serialize_error(obj) from None
    return relative_path.as_posix()
