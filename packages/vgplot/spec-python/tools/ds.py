"""Data structures."""

from __future__ import annotations

from typing import TYPE_CHECKING, overload

import rpds

if TYPE_CHECKING:
    import collections.abc as cabc


__all__ = ("FrozenMap", "frozenmap")

type FrozenMap[K, V] = rpds.HashTrieMap[K, V]
"""An immutable, persistent mapping."""


@overload
def frozenmap[K, V](
    iterable: cabc.Mapping[K, V] | cabc.Iterable[tuple[K, V]] = (), /
) -> FrozenMap[K, V]: ...
@overload
def frozenmap[V](**kwds: V) -> FrozenMap[str, V]: ...
@overload
def frozenmap[K, V](
    iterable: cabc.Mapping[K, V] | cabc.Iterable[tuple[K, V]], /, **kwds: V
) -> FrozenMap[K | str, V]: ...
def frozenmap[K, V](
    iterable: cabc.Mapping[K, V] | cabc.Iterable[tuple[K, V]] = (), /, **kwds: V
) -> FrozenMap[K, V]:
    """Create a new immutable mapping.

    ## Important
    Methods that *look like* mutation, return a new object with shared data.

    Args:
        iterable: Initial entries as a mapping or an iterable over entry pairs.
        **kwds: Keywords mapping keys to values.
            `**kwds` will override `iterable` **and** change the order of the new mapping.

    ## Notes
    Fixed typing, docs and aliasing around [rpds.HashTrieMap].

    *This is the documentation for* [`rpds::map::hash_trie_map`]

    A persistent map with structural sharing.
    This implementation uses a [hash array mapped trie].

    [rpds.HashTrieMap]: https://rpds.readthedocs.io/en/latest/api/#rpds.HashTrieMap
    [`rpds::map::hash_trie_map`]: https://docs.rs/rpds/latest/rpds/map/hash_trie_map/struct.HashTrieMap.html
    [hash array mapped trie]: https://en.wikipedia.org/wiki/Hash_array_mapped_trie
    """
    return rpds.HashTrieMap(iterable, **kwds)  # ty: ignore[invalid-argument-type] # pyrefly: ignore[bad-argument-type] # pyright: ignore[reportArgumentType]
