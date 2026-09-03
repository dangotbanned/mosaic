from __future__ import annotations

import typing as t

from tools.common import ensure_type
from tools.ir import mlir
from tools.ir.mlir import MLIR, Definition, nodes
from tools.ir.mlir.nodes import ClosedDict, Union, ref

if t.TYPE_CHECKING:
    from collections.abc import Iterator

new_def: t.Final = Definition.from_mlir

FORMAT = "format"


@mlir.actions_plugin
def fix_tip(action: mlir.Plugin, roots: mlir.RootsMut) -> Iterator[mlir.Root]:
    # NOTE: Struggling to split this up.
    # It does something hyper-specfic and requires a lot of context while going very deep into a tree
    matcher = action.matcher
    for root in roots:
        if matcher.matches_root(root):
            # Updates to make at the end
            new_defs: dict[str, Definition[MLIR]] = {}
            # Cache for 60-80x of tip
            new_fields = {}
            for (def_name, defn), it_fields in matcher.matching_fields(root):
                for old_name, old_field in it_fields:
                    if new_fields.get(old_name):
                        continue
                    # We are in a field with a gigantic schema (yes that is 700 lines for 1 field, yes this is repeated for every mark)
                    # https://github.com/dangotbanned/mosaic/blob/823a51670664e40c4a141bed1bc97730f6102853/docs/public/schema/v0.31.0.json#L581-L1242
                    old_tip_type = ensure_type(old_field.type, Union, name="old_field.type")
                    tip_fields = _ensure_single_nested_member(old_tip_type).fields
                    format_field = tip_fields[FORMAT]
                    format_type, format_doc = format_field.type, format_field.doc
                    format_name = FORMAT.capitalize()
                    # Grab this guy, making a new definition named `Format`
                    # https://github.com/dangotbanned/mosaic/blob/823a51670664e40c4a141bed1bc97730f6102853/docs/public/schema/v0.31.0.json#L660-L1056
                    new_defs[format_name] = new_def(
                        ensure_type(format_type, ClosedDict, name="format_type").with_doc(
                            format_doc
                        )
                    )
                    # Now we need to walk back up, replacing everything in the reverse order of how we got here
                    tip_fields = tip_fields.update(
                        {FORMAT: format_field.with_type(ref(format_name))}
                    )

                    # NOTE: (Possibly unintentionally) `tip` is defined with `additional_properties=true`
                    # Don't want to support that, things are confusing enough already
                    new_def_name = old_name.capitalize()
                    new_defs[new_def_name] = new_def(
                        ClosedDict(fields=tip_fields, doc=old_field.doc)
                    )
                    new_fields[old_name] = old_field.with_type(
                        _replace_single_nested_member(old_tip_type, ref(new_def_name))
                    )

                new_defs[def_name] = new_def(defn.inner.merge_fields(new_fields))

            if new_defs:
                root.definitions.update(new_defs)
        yield root


def _ensure_single_nested_member(
    old_tip_type: Union,
) -> ClosedDict | nodes.ExtraDict | nodes.OpenDict:
    """Assert the shape of the union and pull out the anonymous object definition.

    Make sure that what we ignore still [starts here] and then [again here].

    [starts here]: https://github.com/dangotbanned/mosaic/blob/823a51670664e40c4a141bed1bc97730f6102853/docs/public/schema/v0.31.0.json#L582-L588
    [again here]: https://github.com/dangotbanned/mosaic/blob/823a51670664e40c4a141bed1bc97730f6102853/docs/public/schema/v0.31.0.json#L1237-L1239
    """
    path = "old_tip_type.members"
    it_members = (m for m in old_tip_type.members if nodes.is_dict(m))
    if (td_member := next(it_members, None)) is None:
        msg = f"Expected to find a nested dict in {path!r}, got: {old_tip_type.members!r}"
        raise NotImplementedError(msg)
    if more := next(it_members, None):
        msg = f"Expected to find a single nested dict in {path!r}, got:\n{td_member!r}\n\nand\n\n{more!r}"
        raise NotImplementedError(msg)
    return td_member


def _replace_single_nested_member(old_tip_type: Union, replacement: nodes.Reference) -> Union:
    new_members = tuple(replacement if nodes.is_dict(m) else m for m in old_tip_type.members)
    return old_tip_type.__replace__(members=new_members)
