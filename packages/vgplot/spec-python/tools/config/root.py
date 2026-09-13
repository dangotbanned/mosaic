from collections.abc import Sequence
from pathlib import Path
from typing import final

from msgspec import field

from tools.config.to_mlir import ToMLIR
from tools.config.to_pyir import ToPyIR
from tools.models.base import FrozenStruct, IdName


class Source(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """A schema source for conversion."""

    path: Path
    """A relative path to the schema, resolved against the location of `mosaic-spec.toml`."""
    id: IdName
    """A unique identifier for the loaded result.

    In the final representation, `id` is used for the name of a python module.
    """


# TODO @dangotbanned: really should use less verbose names
class Convert(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Configure translation/codegen."""

    to_mlir: ToMLIR = field(default_factory=ToMLIR)
    to_pyir: ToPyIR = field(default_factory=ToPyIR)


@final
class MosaicSpecToml(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Top-level config."""

    sources: Sequence[Source] = field(default_factory=list[Source])
    """Schemas to convert."""
    convert: Convert = field(default_factory=Convert)
