from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING, Any, Literal as L, TypeIs, assert_never, final

import msgspec

from tools.common import POUND_DEFS
from tools.ir.json_wrapper.nodes import JsonWrapper, Reference, _from_schema
from tools.models import base

if TYPE_CHECKING:
    from collections.abc import Iterator

    from tools.models.config import JsonWrapperToMLIR
    from tools.models.mosaic import InputSchema


@final
class Root(base.Root[JsonWrapper], kw_only=True):
    """Top-level context for `mosaic-schema.json`."""

    id: base.IdName = msgspec.field(name="$id", default=base.IdName(""))
    ref: str = msgspec.field(name="$ref", default="")
    schema: str = msgspec.field(name="$schema")

    @classmethod
    def from_input_schema(cls, source: InputSchema) -> Root:
        return Root(
            id=source.id,
            definitions={k: _from_schema(v) for k, v in source.definitions.items()},
            ref=source.ref,
            schema=source.schema,
        )

    def iter_refs(self) -> Iterator[Reference]:
        """Yield all references within the entire schema."""
        for schema in self.definitions.values():
            yield from schema.iter_refs()

    def ref_unwrap(self, config: JsonWrapperToMLIR) -> None:
        """Rewrite top-level references.

        ## Notes
        - Used for 4 reference/(union/literal) pairs:
            - Curve/CurveName
            - Interval/LiteralTimeInterval
            - StackOffset/StackOffsetName
            - VectorShape/VectorShapeName
        - Want to remove the nesting, pick 1 description (they often have 2), update everywhere they are ref'd
        """
        cfg = config.ref_unwrap
        default = config.ref_unwrap_default
        modified = {}
        to_replace = {}
        for outer_name, outer in self.iter_defs(is_ref):
            inner_name = outer.def_name
            inner = self[inner_name]
            policy = cfg.get(outer_name, default)
            if policy.name == "outer":
                final_name = outer_name
            else:
                final_name = _unwrap_pick(policy.name, outer_name, inner_name)

            outer_desc = outer.description
            if policy.description == "outer":
                inner.description = outer_desc
            else:
                inner.description = _unwrap_pick(policy.description, outer_desc, inner.description)
            modified[final_name] = inner
            to_replace[(outer_name, inner_name)] = final_name

        if not to_replace:
            return
        for old in set(chain.from_iterable(to_replace)):
            self.definitions.pop(old)
        self.definitions.update(modified)

        defs = POUND_DEFS
        repl_table: dict[str, str] = {}
        for (key1, key2), new_name in to_replace.items():
            repl_table[f"{defs}{key1}"] = repl_table[f"{defs}{key2}"] = f"{defs}{new_name}"
        replacement_fn = repl_table.get
        for ref in self.iter_refs():
            if match := replacement_fn(ref.ref):
                ref.ref = match


def _unwrap_pick(policy: L["inner", "longest", "shortest"], outer: str, inner: str) -> str:
    match policy:
        case "inner":
            return inner
        case "longest":
            return max(outer, inner)
        case "shortest":
            return min(outer, inner)
        case _:
            assert_never(policy)


def is_ref(obj: Any) -> TypeIs[Reference]:
    return isinstance(obj, Reference)
