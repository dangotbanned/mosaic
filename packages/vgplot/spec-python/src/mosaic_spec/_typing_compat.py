"""Compatibility for `"typing-extensions>=4.16 ; python_full_version < '3.15'"`."""

from __future__ import annotations

import sys

if sys.version_info >= (3, 15):
    from builtins import sentinel
    from collections.abc import Buffer
    from io import Reader, Writer
    from typing import (
        LiteralString,
        Never,
        NotRequired,
        ParamSpec,
        Protocol,
        ReadOnly,
        Required,
        Self,
        TypeAliasType,
        TypedDict,
        TypeForm,
        TypeIs,
        TypeVar,
        TypeVarTuple,
        Unpack,
        assert_never,
        assert_type,
        dataclass_transform,
        get_protocol_members,
        override,
        reveal_type,
    )
    from warnings import deprecated
else:
    from typing_extensions import (
        Buffer,
        LiteralString,
        Never,
        NotRequired,
        ParamSpec,
        Protocol,
        Reader,
        ReadOnly,
        Required,
        Self,
        TypeAliasType,
        TypedDict,
        TypeForm,
        TypeIs,
        TypeVar,
        TypeVarTuple,
        Unpack,
        Writer,
        assert_never,
        assert_type,
        dataclass_transform,
        deprecated,
        get_protocol_members,
        override,
        reveal_type,
        sentinel,
    )

__all__ = (
    "Buffer",
    "LiteralString",
    "Never",
    "NotRequired",
    "ParamSpec",
    "Protocol",
    "ReadOnly",
    "Reader",
    "Required",
    "Self",
    "TypeAliasType",
    "TypeForm",
    "TypeIs",
    "TypeVar",
    "TypeVarTuple",
    "TypedDict",
    "Unpack",
    "Writer",
    "assert_never",
    "assert_type",
    "dataclass_transform",
    "deprecated",
    "get_protocol_members",
    "override",
    "reveal_type",
    "sentinel",
)
