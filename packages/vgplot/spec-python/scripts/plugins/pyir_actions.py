"""(Non-integrated) extensions run after generating the `PyIR`/`Module` representation."""

from __future__ import annotations

import dataclasses
import typing as t

from tools.codegen.convert import py_identifier_snake
from tools.common import prepend
from tools.ir.pyir import dsl
from tools.ir.pyir.definition import ClosedDict, supertype

if t.TYPE_CHECKING:
    from collections.abc import Collection, Iterator

    from tools.app import App
    from tools.ir import pyir
    from tools.ir.pyir.definition import OpenDict


def shrink_marks_build_spec(app: App) -> None:
    """Derive a hierarchy for `marks.py` and reuse it to construct the intersections for `spec.py`.

    These operations have had the most impactful reduction in generated code.

    ## Spec

    Removing the (schema generated) version of `Spec` also removed **25,000 LOC**
    ([2bc61fd69c179bcde83b410741baf4b021027e85][1]).
    It was replaced with **500 LOC** ([mosaic_spec/spec.py][2])

    [1]: https://github.com/dangotbanned/mosaic/commit/2bc61fd69c179bcde83b410741baf4b021027e85
    [2]: https://github.com/dangotbanned/mosaic/blob/fa2e49460ceb1bf5a94513a456bcc21fac5f4327/packages/vgplot/spec-python/src/mosaic_spec/spec.py

    ## Marks

    Synthesizing [MarkOptions][3] and using it as base class for all marks removed **16,000 LOC**
    ([d0f225cddfb173da0aea024ad6d03ce4a5041f51][4]).

    [3]: https://github.com/uwdata/mosaic/blob/5f393469e0d1fba8c46e727b4b9f7bbab565ca94/packages/vgplot/spec/src/spec/marks/Marks.ts#L223-L613
    [4]: https://github.com/dangotbanned/mosaic/commit/d0f225cddfb173da0aea024ad6d03ce4a5041f51
    """
    module_marks = app.module("marks")
    marks_rels = _MarksRelations.from_module(module_marks)
    module_marks.update_defs(marks_rels.iter_defs())
    app.update_modules(_build_spec_module(app, marks_rels))


def _build_spec_module(app: App, rels: _MarksRelations) -> pyir.Module:
    module_mosaic = app.module("mosaic")
    td_spec_head = dsl.dict(
        "SpecHead",
        dsl.field("config", module_mosaic.import_ref("Config"), "Configuration options."),
        dsl.field("meta", module_mosaic.import_ref("Meta"), "Specification metadata."),
        dsl.field(
            "params", app.module("params").import_ref("Params"), "Param and Selection definitions."
        ),
        dsl.field(
            "plot_defaults",
            app.module("plot").import_ref("PlotAttributes"),
            "A default set of attributes to apply to all plot components.",
        ),
        dsl.field("data", app.module("data").import_ref("Data"), "Dataset definitions."),
    )
    td_spec_head_ref = td_spec_head.to_typed_ref()
    spec_defns = (
        dsl.dict(closed.name, closed=True, bases=(td_spec_head_ref, open.to_typed_ref()))
        for open, closed in rels.marks
    )
    return app.module("mosaic_spec").child("spec", prepend(td_spec_head, spec_defns))


@dataclasses.dataclass
class _MarksRelations:
    """Stores shared components between `marks` and `spec`.

    This is about keeping (Parent, Child) class pairs together.
    """

    mark_options: OpenDict
    """Base class common to all marks."""
    marks: tuple[tuple[OpenDict, ClosedDict], ...]
    """(Parent, Child) class pairs."""

    @classmethod
    def from_module(
        cls, module: pyir.Module, *, fmt_parent_name: str = "_{name}Open"
    ) -> _MarksRelations:
        """Generate a hierarchy from definitions with `mark` field in `module`.

        For `n` definitions, this operation returns `(n * 2) + 1` definitions.

        Using `Graticule` as an example:

        ```py
        # `(...) + 1`
        class MarkOptions(TypedDict, total=False):
            # 39 fields common to every mark
            ...


        # `(... * 2) + ...`
        class _GraticuleOpen(MarkOptions, total=False):
            '''The graticule mark.'''

            mark: Required[Literal["graticule"]]
            '''A geo mark whose *data* is ...'''


        # `(n * ...) + ...`
        class Graticule(_GraticuleOpen, total=False, closed=True): ...
        ```
        """
        mark_defns = tuple(
            defn
            for defn in module.def_values()
            if isinstance(defn, ClosedDict) and defn.has_field("mark")
        )
        return _MarksRelations._from_marks(mark_defns, fmt_parent_name)

    def iter_defs(self) -> Iterator[OpenDict | ClosedDict]:
        yield self.mark_options
        for open_closed in self.marks:
            yield from open_closed

    @classmethod
    def _from_marks(
        cls, definitions: Collection[ClosedDict], fmt_parent_name: str
    ) -> _MarksRelations:
        options = supertype(
            definitions,
            name="MarkOptions",
            doc="Shared options for all marks.",
            # NOTE: This is a bug in the TS source:
            #   `SpecHead.data?: Data | (Data & PlotMarkData)`
            # The runtime code doesn't expect the rhs, so here we will exclude it from
            # where `Spec` derives - and leave it in for the `PlotMark` classes
            exclude={"mark", "data"},
        )
        return _MarksRelations(
            options, tuple(cls._generate_pairs(definitions, options, fmt_parent_name))
        )

    @staticmethod
    def _generate_pairs(
        definitions: Collection[ClosedDict], options: OpenDict, fmt_parent_name: str
    ) -> Iterator[tuple[OpenDict, ClosedDict]]:
        data = py_identifier_snake("data")
        for mark in definitions:
            name = mark.name
            parent = mark.with_parent(options, fmt_parent_name.format(name=name))
            child_fields = {data: f} if (f := mark.fields.get(data)) else ()
            yield parent, parent.with_child_closed(name, fields=child_fields)
