"""Data structures."""

from __future__ import annotations

import typing as t

import rpds

if t.TYPE_CHECKING:
    import collections.abc as cabc


__all__ = ("FrozenMap", "frozenmap")

type FrozenMap[K, V] = rpds.HashTrieMap[K, V]
"""An immutable, persistent mapping."""

type _IntoMapping[K, V] = cabc.Mapping[K, V] | cabc.Iterable[tuple[K, V]]
type _Unknown = t.Any


@t.overload
def frozenmap() -> FrozenMap[_Unknown, _Unknown]: ...
@t.overload
def frozenmap[V](iterable: _IntoMapping[str, V] = (), /, **kwds: V) -> FrozenMap[str, V]: ...
@t.overload
def frozenmap[K, V](iterable: _IntoMapping[K, V], /) -> FrozenMap[K, V]: ...
@t.overload
def frozenmap[K, V](iterable: _IntoMapping[K, V], /, **kwds: V) -> FrozenMap[K | str, V]: ...
def frozenmap[K, V](iterable: _IntoMapping[K, V] = (), /, **kwds: V) -> FrozenMap[K | str, V]:
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
