from collections.abc import Mapping, Sequence

from msgspec import field

from tools.config.actions import Action
from tools.config.ref_unwrap import ReferenceUnwrap
from tools.models.base import DefName, FrozenStruct


class ToMLIR(FrozenStruct, frozen=True, forbid_unknown_fields=True):
    """Configure converting from json schema.

    Represents the first conversion stage.
    """

    ref_unwrap: Mapping[DefName, ReferenceUnwrap] = field(default_factory=dict)
    """Mapping from the outer ("$ref"-defining) definition name to a policy table."""

    actions: Sequence[Action] = field(default_factory=list[Action])

    @property
    def ref_unwrap_default(self) -> ReferenceUnwrap:
        return ReferenceUnwrap()
