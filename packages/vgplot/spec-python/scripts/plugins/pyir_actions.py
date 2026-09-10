"""(Non-integrated) extensions run after generating the `PyIR`/`Module` representation."""

from __future__ import annotations

import dataclasses
import typing as t
from itertools import chain

from tools.codegen.convert import py_identifier_snake
from tools.common import PyIdentifier, PyIdentifierSnake, ensure_type
from tools.ir import pyir
from tools.ir.pyir import Ref, TypedExtRef, definition as pyir_d, dsl, expr as pyir_e
from tools.ir.pyir.definition import ClosedDict, OpenDict

if t.TYPE_CHECKING:
    from collections.abc import Collection, Iterable, Iterator

    from tools.app import App

type SpecTarget = tuple[PyIdentifier, TypedExtRef[OpenDict]]


def massage_components(app: App) -> None:
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
    module_marks = app.module("mosaic_spec._gen.marks")
    marks_rels = _MarksRelations.from_module(module_marks)
    module_marks.update_defs(marks_rels.iter_defs())

    spec_targets = _non_mark_components(app)
    spec_targets = chain(spec_targets, marks_rels.iter_spec_targets())
    _build_spec_module(app, spec_targets)


def _non_mark_components(app: App) -> Iterable[SpecTarget]:
    """Handle the rest of `Component`, that is not covered by `PlotMark`.

    The awkward part is to represent this hierarchy:

    Defined in `_gen.mosaic.py`:

    ```py
    # fmt: off
    class _PlotAttributesOpen(TypedDict, total=False): ...
    class _PlotOpen(_PlotAttributesOpen, total=False): ...

    class PlotAttributes(_PlotAttributesOpen, total=False, closed=True): ...
    class Plot(_PlotOpen, total=False, closed=True): ...
    ```

    Defined in `spec.py`:

    ```py
    class SpecHead(TypedDict, total=False):
        config: Config
        meta: Meta
        params: Params
        plot_defaults: PlotAttributes
        data: Data


    class Plot(SpecHead, _PlotOpen, closed=True): ...
    ```
    """
    pkg_gen = app.package("mosaic_spec._gen")
    module_plot = pkg_gen.module("plot")

    component = ensure_type(app.module("mosaic_spec._gen.mosaic")["Component"], pyir_d.TypeAlias)
    union = ensure_type(component.expr, pyir_e.Union)
    found: dict[tuple[PyIdentifierSnake, PyIdentifier], ClosedDict] = {}
    for m in union.members:
        if isinstance(m, pyir.ExtRef):
            if m.ref != "PlotMark":
                found[m.ext, m.ref] = ensure_type(pkg_gen.module(m.ext)[m.ref], ClosedDict)
        else:
            # NOTE: I don't have any cases like this here, but it would complicate things if I did
            raise NotImplementedError(type(m))

    plot_name = py_identifier_snake("plot")
    plot = found.pop((plot_name, PyIdentifier("Plot")))
    plot_attrs = module_plot.get_typed("PlotAttributes", ClosedDict)

    plot_attrs_base = plot_attrs.to_open()
    plot_attrs = plot_attrs_base.with_child_closed(plot_attrs.name)

    plot_base = plot_attrs_base.with_child_open(
        OpenDict.format_name(plot.name), doc=plot.doc, fields={plot_name: plot.fields["plot"]}
    )
    plot = plot_base.with_child_closed(plot.name)
    module_plot.update_defs((plot_attrs_base, plot_attrs, plot_base, plot))

    spec_targets: dict[PyIdentifier, TypedExtRef[OpenDict]] = {
        plot.name: TypedExtRef(ext=plot_name, ref=plot_base.name, type=plot_base.__class__)
    }

    for (module_name, name), v in found.items():
        v_base = v.to_open()
        v_closed = v_base.with_child_closed(name)
        spec_targets[name] = TypedExtRef(
            ext=py_identifier_snake(module_name), ref=v_base.name, type=v_base.__class__
        )
        pkg_gen.module(module_name).update_defs((v_base, v_closed))
    return spec_targets.items()


def _build_spec_module(app: App, targets: Iterable[SpecTarget]) -> None:
    mosaic_spec = app.package()
    pkg_gen = mosaic_spec.package("_gen")
    module_mosaic = pkg_gen.module("mosaic")
    td_spec_head = dsl.dict(
        "SpecHead",
        dsl.field("config", module_mosaic.import_ref("Config"), "Configuration options."),
        dsl.field("meta", module_mosaic.import_ref("Meta"), "Specification metadata."),
        dsl.field(
            "params",
            pkg_gen.module("params").import_ref("Params"),
            "Param and Selection definitions.",
        ),
        dsl.field(
            "plot_defaults",
            pkg_gen.module("plot").import_ref("PlotAttributes"),
            "A default set of attributes to apply to all plot components.",
        ),
        dsl.field("data", pkg_gen.module("data").import_ref("Data"), "Dataset definitions."),
    )
    td_spec_head_ref = td_spec_head.to_typed_ref()
    spec_defns = (
        dsl.dict(name, closed=True, bases=(td_spec_head_ref, base_ref))
        for name, base_ref in targets
    )
    module_spec = mosaic_spec.with_child("spec", spec_defns)
    alias_members = (defn.to_typed_ref() for defn in module_spec.def_values())
    spec_union = dsl.alias("Spec", *alias_members, doc="A declarative Mosaic specification.")
    module_spec.update_defs((spec_union, td_spec_head))


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
    def from_module(cls, module: pyir.Module) -> _MarksRelations:
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
        return _MarksRelations._from_marks(mark_defns)

    def iter_defs(self) -> Iterator[OpenDict | ClosedDict]:
        yield self.mark_options
        for open_closed in self.marks:
            yield from open_closed

    def iter_spec_targets(self) -> Iterator[SpecTarget]:
        ext = py_identifier_snake("marks")
        for open, closed in self.marks:
            yield closed.name, TypedExtRef(ext=ext, ref=open.name, type=open.__class__)

    @classmethod
    def _from_marks(cls, definitions: Collection[ClosedDict]) -> _MarksRelations:
        options = dsl.supertype(
            "MarkOptions",
            definitions,
            doc="Shared options for all marks.",
            # NOTE: This is a bug in the TS source:
            #   `SpecHead.data?: Data | (Data & PlotMarkData)`
            # The runtime code doesn't expect the rhs, so here we will exclude it from
            # where `Spec` derives - and leave it in for the `PlotMark` classes
            # NOTE: `opacity` has different docs for `GridOptions`
            # https://github.com/dangotbanned/mosaic/blob/510eeaf8bed2fdc97aa7dfa78a3475ea92c8e2a1/packages/vgplot/spec/src/spec/marks/Axis.ts#L131-L137
            exclude={"mark", "data", "opacity"},
        )
        return _MarksRelations(options, tuple(cls._generate_pairs(definitions, options)))

    @staticmethod
    def _generate_pairs(
        definitions: Collection[ClosedDict], options: OpenDict
    ) -> Iterator[tuple[OpenDict, ClosedDict]]:
        data = py_identifier_snake("data")
        fmt = OpenDict.format_name
        exclude = frozenset((*options.fields, data))
        for mark in definitions:
            name = mark.name
            parent = mark.with_parent_open(fmt(name), options, exclude=exclude)
            child_fields = {data: f} if (f := mark.get(data)) else ()
            yield parent, parent.with_child_closed(name, fields=child_fields)


def _synthesize_transform_hierarchy(app: App) -> None:
    module = app.module("mosaic_spec._gen.transform")
    window_transforms = tuple(
        module.get_typed(ensure_type(m, Ref).ref, ClosedDict)
        for m in ensure_type(
            ensure_type(module["WindowTransform"], pyir_d.TypeAlias).expr, pyir_e.Union
        ).members
    )
    window_options = dsl.supertype(
        "WindowOptions", window_transforms, doc="Window transform options."
    )
    distinct = dsl.field("distinct", pyir_e.BOOL)
    agg_options = window_options.with_child_open(
        "AggregateOptions", doc="Aggregate transform options.", fields={distinct.name: distinct}
    )

    aggregate_exclude = window_options.fields.keys() | agg_options.fields.keys()
    name = dsl.Source.SELF

    # NOTE: `AggregateOptions` children need to go first, as they iterate over the dictionary being updated
    module.update_defs(
        chain(
            (
                defn.with_parent_closed(name, agg_options, exclude=aggregate_exclude)
                for defn in module.def_values()
                if isinstance(defn, ClosedDict) and defn.has_field("distinct")
            ),
            (window_options, agg_options),
            (defn.with_parent_closed(name, window_options) for defn in window_transforms),
        )
    )


def run(app: App) -> None:
    """Run after typing all references."""
    massage_components(app)
    _synthesize_transform_hierarchy(app)
