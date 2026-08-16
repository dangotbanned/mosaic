"""Convenience wrapper around [`msgspec.json`][]."""

from __future__ import annotations

import functools
from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal as L

import msgspec

if TYPE_CHECKING:
    from collections.abc import Buffer, Callable, Mapping

    from typing_extensions import TypeForm

    from tools.fs import IntoPath

__all__ = ("convert_json", "deserialize_json", "read_json", "serialize_json", "write_json")


def serialize_json(obj: Any, /, *, order: L["deterministic", "sorted"] | None = None) -> bytes:
    """Serialize an object as JSON."""
    return _encoder_json(order).encode(obj)


def deserialize_json[T](buf: Buffer | str, tp: type[T], /) -> T:
    """Deserialize an object from JSON into `T`."""
    return _decoder_json(tp).decode(buf)


def deserialize_yaml[T](buf: Buffer | str, tp: type[T] | TypeForm[T], /) -> T:
    """Deserialize an object from YAML into `T`."""
    # NOTE: msgspec overloads "forget" to use `Buffer` after the first one
    # pyrefly: ignore[no-matching-overload]
    return msgspec.yaml.decode(buf, type=tp, dec_hook=_decoder_hook)  # ty: ignore[no-matching-overload] # pyright: ignore[reportCallIssue,reportArgumentType]


def convert_json[T](obj: msgspec.Struct | Mapping[str, Any], into: type[T], /) -> T:
    """Convert a struct-like object through `msgspec`.

    This is like a field filter with struct-level configuration on strict-ness.

    ## Notes
    There might be a way to configure [msgspec.convert] for this.

    [msgspec.convert]: https://msgspec.dev/api#msgspec.convert
    """
    return deserialize_json(serialize_json(obj), into)


def read_json[T](path: IntoPath, tp: type[T], /) -> T:
    """Deserialize a JSON file into `T`."""
    with Path(path).open(encoding="utf8") as fd:
        return deserialize_json(fd.read(), tp)


def write_json(path: IntoPath, obj: Any, *, pretty: bool = False) -> None:
    """Serialize an object to a JSON file."""
    bstring = serialize_json(obj, order="sorted")
    bstring = msgspec.json.format(bstring) if pretty else bstring
    _write_bytes_as_str(path, bstring)


def write_toml(path: IntoPath, obj: Any) -> None:
    """Serialize an object to a TOML file."""
    _write_bytes_as_str(path, msgspec.toml.encode(obj, order="sorted"))


def read_yaml[T](path: IntoPath, tp: type[T] | TypeForm[T], /) -> T:
    """Deserialize a YAML file into `T`."""
    with Path(path).open(encoding="utf8") as fd:
        return deserialize_yaml(fd.read(), tp)


def read_yaml_untyped(path: IntoPath) -> Any:
    """Like `read_yaml`, but avoids `pyright` and `ty` disagreement on how the gradual version should work.

    Prefer [`read_yaml`][] if possible.
    """
    return read_yaml(path, Any)


def _write_bytes_as_str(path: IntoPath, b_string: bytes, /) -> None:
    path = Path(path)
    path.touch()
    with path.open("w", encoding="utf8", newline="\n") as fd:
        fd.write(b_string.decode())


@functools.cache
def _decoder_json[T](tp: type[T], /) -> msgspec.json.Decoder[T]:
    return msgspec.json.Decoder(tp, dec_hook=_decoder_hook)


@functools.cache
def _encoder_json(order: L["deterministic", "sorted"] | None = None, /) -> msgspec.json.Encoder:
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


# TODO @dangotbanned: This one is a real bug, see fix in:
# https://github.com/dangotbanned/mosaic/commit/bd9094f49de844f1862a6c635dfba3dffe85f3c5
@_decoder_hook.register(deque)  # pyrefly: ignore[bad-singledispatch-register]
def _use_constructor[T, R](cb: Callable[[T], R], obj: T, /) -> R:
    return cb(obj)


_encoder_hook.register(deque, list)
