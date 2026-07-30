from __future__ import annotations

import msgspec


class Struct(msgspec.Struct, omit_defaults=True, repr_omit_defaults=True):
    """`omit_defaults=True, repr_omit_defaults=True`."""
