"""Convenience wrapper around [`msgspec.json`][]."""

from __future__ import annotations

import functools
from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING, Any, Final, Literal as L

import msgspec

if TYPE_CHECKING:
    from collections.abc import Buffer, Callable, Mapping

    from typing_extensions import TypeForm

    from tools.fs import IntoPath

__all__ = ("convert_json", "deserialize_json", "read_json", "serialize_json", "write_json")

type _SerializableNative = Any
"""A type natively supported by `msgspec`."""

type _Extension = Any
"""A type that requires conversion for use with `msgspec`."""

type _IntoExtension = Callable[[type[_Extension], _SerializableNative], _Extension]
"""A [converter] from native msgspec -> extension.

[converter]: https://msgspec.dev/extending#mapping-to-from-native-types
"""

_SORT_TO_ORDER: Final[Mapping[bool, L["sorted"] | None]] = {True: "sorted", False: None}


def serialize_json(obj: Any, /, *, sort: bool = False) -> bytes:
    """Serialize an object as JSON."""
    return _encoder_json(_SORT_TO_ORDER[sort]).encode(obj)


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


def write_json(path: IntoPath, obj: Any, *, pretty: bool = False, sort: bool = True) -> None:
    """Serialize an object to a JSON file."""
    bstring = serialize_json(obj, sort=sort)
    bstring = msgspec.json.format(bstring) if pretty else bstring
    _write_bytes_as_str(path, bstring)


def write_toml(path: IntoPath, obj: Any, *, sort: bool = True) -> None:
    """Serialize an object to a TOML file."""
    _write_bytes_as_str(path, msgspec.toml.encode(obj, order=_SORT_TO_ORDER[sort]))


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
def _encoder_hook(obj: _Extension, /) -> _SerializableNative:
    tp = type(obj)
    msg = f"Objects of type '{tp.__module__}.{tp.__name__}' cannot be serialized by msgspec, got: {obj!r}"
    raise NotImplementedError(msg)


def _decoder_hook(field_type_expr: type[_Extension], obj: _SerializableNative, /) -> _Extension:
    # NOTE: `@functools.singledispatch` cannot be used here,
    # as `tp: type[Any]` gets converted to `type[type[Any]]`
    if converter := _DECODER_DISPATCH.get(field_type_expr):
        return converter(field_type_expr, obj)
    field_type_expr = type(obj)
    msg = f"Objects of type '{field_type_expr.__module__}.{field_type_expr.__name__}' cannot be deserialized by msgspec, got: {obj!r}"
    raise NotImplementedError(msg)


def _use_constructor[T, R](cb: Callable[[T], R], obj: T, /) -> R:
    return cb(obj)


_encoder_hook.register(deque, list)
_DECODER_DISPATCH: Mapping[type[_Extension], _IntoExtension] = {deque: _use_constructor}
