"""Data structures.

Re-exports [rpds.HashTrieMap] with fixed stubs as `FrozenMap` and `frozenmap`.

[rpds.HashTrieMap]: https://rpds.readthedocs.io/en/latest/api/#rpds.HashTrieMap
"""

from __future__ import annotations

import typing as t

if t.TYPE_CHECKING:
    from tools._rpds_stub import HashTrieMap as FrozenMap
else:
    from rpds import HashTrieMap as FrozenMap


__all__ = ("FrozenMap", "frozenmap")

frozenmap = FrozenMap
