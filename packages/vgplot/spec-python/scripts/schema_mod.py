# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "msgspec>=0.21.1",
# ]
# ///
"""Transform `packages/vgplot/spec/dist/mosaic-schema.json` for use in python."""

from __future__ import annotations

from collections import deque
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Annotated as A, ClassVar, Final, Literal as L, Protocol

from tools import codemod, fs, serde
from tools.codegen import convert, typed_dict
from tools.codegen.docstrings import doc
from tools.models import mosaic as m
from tools.models.base import IdName

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator

    from tools.models.base import DefName

GENERATED_MODULE_NAME = "mosaic"
SCHEMA_IN = fs.SPEC / "dist/mosaic-schema.json"
SCHEMA_OUT = fs.SCHEMA / f"{GENERATED_MODULE_NAME}.json"

GENERATED_MODULE_MAIN = fs.MOSAIC_SPEC_GEN / f"{GENERATED_MODULE_NAME}.py"
TYPING_COMPAT = fs.MOSAIC_SPEC / "_typing_compat.py"

KEYS_REPLACE: Final = {"as": "bind", "from": "source", "for": "plot"}
"""Keys that collide with [`keyword.kwlist`][], but the values are required.

These keys only appear in `"properties"` and `"required"`, the challenge is finding those guys.
"""

SPEC: Final = "Spec"
"""Name of the `Spec` union and prefix for it's members"""

SPEC_HEAD: Final = "SpecHead"
"""Name of the base `TypedDict` for all `Spec` members.

Mixing this into the bases with the `Component` member is a limited form of an intersection type.
"""
SPEC_HEAD_NO_DATA: Final = "_SpecHead"


def _recursive_replace(schema: m.JsonSchema) -> m.JsonSchema:
    """Visit 4 fields at all levels of the schema, renaming matches for [`tools.codegen.convert.KEYS_REPLACE`][]."""
    replace = convert.KEYS_REPLACE.get
    recurse = _recursive_replace
    if properties := schema.properties:
        schema.properties = {replace(k, k): (recurse(v)) for k, v in properties.items()}
    if required := schema.required:
        schema.required = [replace(r, r) for r in required]
    if any_of := schema.any_of:
        schema.any_of = [recurse(a) for a in any_of]
    if (items := schema.items) and items is not True:
        if isinstance(items, m.JsonSchema):
            schema.items = recurse(items)
        else:
            schema.items = [recurse(i) for i in items]
    return schema


def _replace_annotation_with_ref(
    def_name: DefName, source: m.JsonSchema
) -> Callable[[m.JsonSchema], m.JsonSchema]:
    replacement = source.new_ref(def_name)
    matches = source.__eq__

    def recurse(target: m.JsonSchema, /) -> m.JsonSchema:
        if any_of := target.any_of:
            target.any_of = [recurse(a) for a in any_of]
        if (items := target.items) and items is not True:
            if isinstance(items, m.JsonSchema):
                target.items = recurse(items)
            else:
                target.items = [recurse(i) for i in items]
        if matches(target):
            return replacement
        return target

    return recurse


@dataclass
class Artifacts:
    mosaic: m.InputSchema
    marks: m.InputSchema
    spec_description: str

    def iter_components(self) -> Iterator[tuple[DefName, str, L["_SpecHead", "SpecHead"], Path]]:
        paths = GENERATED_MODULE_MAIN, fs.MOSAIC_SPEC_GEN / "marks.py"
        all_defs = self.mosaic.definitions, self.marks.definitions
        for path, defs in zip(paths, all_defs, strict=False):
            for name, schema in defs.items():
                if (
                    (template := schema.x_template)
                    and isinstance(template, m.ExtraTemplate)
                    and name != "PlotAttributes"
                ):
                    base_open_name = template.base
                    base_spec = (
                        SPEC_HEAD_NO_DATA
                        if (template.root in {_MARK_DATA, _MARK_DATA_OPTIONAL})
                        else SPEC_HEAD
                    )
                    yield name, base_open_name, base_spec, path

    def generate_spec_module(self, target: Path) -> None:
        fields_excluding_data = (
            typed_dict.Field("config", "Config", "Configuration options."),
            typed_dict.Field("meta", "Meta", "Specification metadata."),
            typed_dict.Field("params", "Params", "Param and Selection definitions."),
            typed_dict.Field(
                "plot_defaults",
                "PlotAttributes",
                "A default set of attributes to apply to all plot components.",
            ),
        )
        field_data = typed_dict.Field("data", "Data", "Dataset definitions.")
        module = deque(typed_dict.iter_lines(SPEC_HEAD_NO_DATA, fields_excluding_data))
        module.extend(typed_dict.iter_lines(SPEC_HEAD, (field_data,), bases=(SPEC_HEAD_NO_DATA,)))
        import_from = codemod.fragments.import_from
        module.extendleft(
            (
                import_from(TYPING_COMPAT, ("TypedDict", "TypeAliasType")),
                import_from(
                    GENERATED_MODULE_MAIN, (fld.tp for fld in (*fields_excluding_data, field_data))
                ),
            )
        )
        import_statements = deque[str]()
        export_names = deque[str]()

        for name, base_open_name, base_spec, path in self.iter_components():
            module.extend(
                typed_dict.iter_lines(name, bases=(base_spec, base_open_name), closed=True)
            )
            export_names.append(name)
            import_statements.append(import_from(path, base_open_name))

        export_names_sort = sorted(export_names)
        module.extend(
            (
                f"{SPEC} = TypeAliasType({SPEC!r}, {'|'.join(export_names_sort)})",
                doc(self.spec_description),
            )
        )
        export_names_sort.append(SPEC)
        module.extendleft(import_statements)
        module.appendleft(codemod.fragments.FUTURE_ANNOTATIONS)
        module.append(f"\n__all__ = {tuple(export_names_sort)}\n")
        fs.write_lines(target, module, "Generated module")


def generate_python_schema(source: str | Path, target: Path) -> Artifacts:
    print(f"Reading json schema at: {Path(source).relative_to(fs.MONOREPO_ROOT).as_posix()}")
    schema = serde.read_json(source, m.InputSchema)
    spec_def = schema.pop("Spec")
    schema.ref = ""  # Removes `"$ref": "#/definitions/Spec"`
    schema.id = IdName(target.name)

    schema.definitions = {k: _recursive_replace(v) for k, v in schema.iter_defs()}
    ParamDefinitionSplit("ParamDefinition", "params.json").run(schema)
    PlotTypesSplit("typing.json").run(schema)
    spec_dedup = SpecDeduplicate("marks.json")
    spec_dedup.run(schema)

    CSSStylesSplit("CSSStyles", "css-styles.json").run(schema)
    InteractorsSplit("PlotInteractor", "interactors.json").run(schema)
    TransformSplit("Transform", "transform.json").run(schema)

    serde.write_json(target, schema, pretty=True)
    print(f"Generated python schema at: {fs.repo_relative_str(target)}")
    return Artifacts(schema, marks=spec_dedup.extracted, spec_description=spec_def.description)


class SchemaMod(Protocol):
    def run(self, schema: m.InputSchema) -> None: ...


type Extracted[T] = A[T, L["Extracted"]]


class _CanSetRef(Protocol):
    """Any object with a mutable `ref` attribute."""

    ref: m.Ref


class SchemaSplit(SchemaMod):
    _SCHEMA_DIR: ClassVar[Path] = fs.SCHEMA
    filename: str

    @property
    def path(self) -> Path:
        return self._SCHEMA_DIR / self.filename

    def run(self, schema: m.InputSchema) -> None:
        """Move definitions from `schema` into `filename`."""
        self.update_refs(schema)
        extracted = self.extract(schema)
        serde.write_json(self.path, extracted, pretty=True)
        print(f"Generated schema at: {fs.repo_relative_str(self.path)}")

    def update_refs(self, schema: m.InputSchema) -> None:
        """Redirect references that have moved to point to `filename`."""
        msg = f"'{self.update_refs.__qualname__}()' is not yet implemented"
        raise NotImplementedError(msg)

    def _extract_definitions(self, schema: m.InputSchema) -> dict[DefName, m.JsonSchema]:
        """Return the contents of the `filename`'s `"definitions"`."""
        msg = f"'{self._extract_definitions.__qualname__}()' is not yet implemented"
        raise NotImplementedError(msg)

    def extract(self, schema: m.InputSchema) -> Extracted[m.InputSchema]:
        return schema.__replace__(
            id=IdName(self.filename), definitions=self._extract_definitions(schema)
        )


class RootSplit(SchemaSplit):
    """Generate a new schema, starting at a single root type."""

    def __init__(self, root_name: DefName, filename: str) -> None:
        self.root_name: DefName = root_name
        self.filename: str = filename

    def update_refs(self, schema: m.InputSchema) -> None:
        """Redirect references to `root_name` to point to `filename`."""
        root_name, filename = self.root_name, self.filename
        ref_original = f"#/definitions/{root_name}"
        for location in self._referenced_by(schema):
            search = (item for item in location if (_ref := item.ref) == ref_original)
            if found := next(search, None):
                found.ref = f"{filename}{ref_original}"
            else:
                msg = (
                    f"Expected to find a ref to {root_name!r} in `iterable`.\n"
                    f"Failed to update '{filename}{ref_original}'"
                )
                raise NotImplementedError(msg)

    def _referenced_by(self, schema: m.InputSchema) -> Iterable[Iterable[_CanSetRef]]:
        """Yield search spaces, where each contains a single reference to the new root."""
        msg = f"'{self._referenced_by.__qualname__}()' is not yet implemented"
        raise NotImplementedError(msg)


class CSSStylesSplit(RootSplit):
    # NOTE: Has 500 fields
    def _referenced_by(self, schema: m.InputSchema) -> Iterable[Iterable[m.JsonSchema]]:
        for def_name in ("PlotAttributes",):
            yield schema[def_name].properties["style"].iter_members()

    def _extract_definitions(self, schema: m.InputSchema) -> dict[DefName, m.JsonSchema]:
        return {self.root_name: schema.pop(self.root_name)}


class InteractorsSplit(RootSplit):
    def _referenced_by(self, schema: m.InputSchema) -> Iterable[Iterable[m.JsonSchema]]:
        it = schema["Plot"].properties["plot"].items_schema().iter_members()
        yield from (it,)

    def _extract_definitions(self, schema: m.InputSchema) -> dict[DefName, m.JsonSchema]:
        root = schema.pop(self.root_name)
        definitions = {self.root_name: root}
        for member_ref in root.iter_members():
            member_name = member_ref.def_name
            definitions[member_name] = schema.pop(member_name)
        definitions["BrushStyles"] = schema.pop("BrushStyles")
        return definitions


class ParamDefinitionSplit(RootSplit):
    def run(self, schema: m.InputSchema) -> None:
        extracted = self.extract(schema)
        obj = schema["Params"].additional_properties
        if isinstance(obj, bool):
            raise NotImplementedError
        obj.ref = f"{self.filename}{obj.ref}"
        schema.map_refs({"ParamRef": self.filename})
        serde.write_json(self.path, extracted, pretty=True)
        print(f"Generated schema at: {fs.repo_relative_str(self.path)}")

    def _extract_definitions(self, schema: m.InputSchema) -> dict[DefName, m.JsonSchema]:
        root = schema.pop(self.root_name)
        return {
            self.root_name: root,
            "ParamRef": schema.pop("ParamRef"),
            "ParamLiteral": schema.pop("ParamLiteral"),
        } | {name: schema.pop(name) for ref in root.iter_members() if (name := ref.def_name)}


class PlotTypesSplit(RootSplit):
    """Aliases without a root or external dependencies.

    Tricky because they are referenced in lots of places
    """

    _DEF_NAMES = (
        "ColorScaleType",  # ref by `PlotAttributes.color_scale`
        "ColorScheme",  # ref by `PlotAttributes.color_scheme`
        "ContinuousScaleType",  # ref by `PlotAttributes.{length,opacity,r}_scale`
        "Curve",  # ref by `marks.Marks.{Curve,CurveAuto}Options.curve` (16x `_*Open` classes)
        #           replaces `CurveName`
        "DiscreteScaleType",  # ref by `PlotAttributes.symbol_scale`
        "Fixed",  # ref by `PlotAttributes` 20x fields
        "FrameAnchor",  # ref by `Tip.{anchor,frame_anchor,preferred_anchor}` + 23x `_*Open.frame_anchor`
        "Interpolate",  # ref by `PlotAttributes.color_interpolate`
        "Interval",  # ref 60x, lots of places
        #              replaces `LiteralTimeInterval`
        "PositionScaleType",  # ref by `PlotAttributes.{x,y}_scale`
        "ProjectionName",  # ref by `PlotAttributes.projection_type`
        "Reducer",  # ref by `{ChannelDomainValueSpec1,ChannelDomainSort}.reduce`
        "ReducerPercentile",  # ref by `Reducer` ^^^^
        "ScaleName",  # ref by `ChannelValueSpec1.scale`
        "SymbolType",  # ref by 9x `_*Open.symbol`
        "TimeIntervalName",  # ref by `Interval` (but this has a unique doc so keep it)
    )

    def __init__(self, filename: str) -> None:
        self.filename: str = filename

    def run(self, schema: m.InputSchema) -> None:
        pop = schema.pop
        definitions = {
            "Interval": pop("Interval").__replace__(
                ref="", any_of=pop("LiteralTimeInterval").any_of
            ),
            "TimeIntervalName": pop("TimeIntervalName"),
        }

        # NOTE: `& Record<never, never>` explodes into 51x `{'type': 'object'}`
        # https://github.com/dangotbanned/mosaic/blob/91ecaaf1db2716f89c309978a389d1dd822c36e3/packages/vgplot/spec/src/spec/PlotTypes.ts#L383-L384
        color_scheme = pop("ColorScheme")
        for s in tuple(color_scheme.any_of):
            if s.enum:
                definitions["ColorScheme"] = s.__replace__(description=color_scheme.description)
                break
        typing_schema = schema.__replace__(id=IdName(self.filename), definitions=definitions)
        schema.map_refs(dict.fromkeys(definitions, self.filename))
        serde.write_json(self.path, typing_schema, pretty=True)
        print(f"Generated schema at: {fs.repo_relative_str(self.path)}")


_WINDOW_TRANSFORM = "WindowTransform"
_WINDOW_OPTIONS = "WindowOptions"
_AGGREGATE_TRANSFORM = "AggregateTransform"
_AGGREGATE_OPTIONS = "AggregateOptions"
_ARG = "Arg"


# TODO @dangotbanned: [HIGH PRIORITY] Stop (manually) managing references
# - Map out where each definition needs to visit to find all `$ref`s
#   - Probably use a graph
#   - > This node depends on `{a, b, c}` and they can be found via ...
# - Wait until each job has "stolen" definitions to do any work
#   - Current: (update_refs -> extract -> write_json) * N
#   - Wanted : extract * N -> determine deps * N -> update_refs * N -> write_json * N
#       - Where each stage is handled in an outer context
#       - With visibility of dependencies in each file
class TransformSplit(RootSplit):
    """Remove `Transform` and it's members from the schema, to define them in another file.

    The definition is a union of unions of typed dicts:

    ```py
    type ColumnTransform = Column | ...
    type Transform = ColumnTransform | AggregateTransform | WindowTransform


    class Column(TypedDict):
        column: Any
    ```
    """

    def _referenced_by(self, schema: m.InputSchema) -> Iterable[Iterable[m.JsonSchema]]:
        # HACK @dangotbanned: Handling the reference update in `SpecDeduplicate`
        yield from ()

    def _extract_definitions(self, schema: m.InputSchema) -> dict[DefName, m.JsonSchema]:
        root = schema.pop(self.root_name)
        arg_def = m.JsonSchema(
            description="A transform argument.",
            any_of=[
                m.JsonSchema(type="string"),
                m.JsonSchema(type="number"),
                m.JsonSchema(type="boolean"),
                m.JsonSchema(ref="params.json#/definitions/ParamRef"),
            ],
        )
        definitions = {self.root_name: root, _ARG: arg_def}
        self._replace_arg = _replace_annotation_with_ref(_ARG, arg_def)

        # `ColumnTransform | AggregateTransform | WindowTransform`
        for name, member in schema.iter_members_defs(root):
            definitions[name] = schema.pop(name)
            if name == "ColumnTransform":
                for sub_member_ref in member.iter_members():
                    sub_member_name = sub_member_ref.def_name
                    sub_member_def = schema.pop(sub_member_name)
                    self._simplify_arg(sub_member_def)
                    definitions[sub_member_name] = sub_member_def

        # NOTE: needs structure
        definitions[_WINDOW_OPTIONS] = materialize_supertype(
            definitions[_WINDOW_TRANSFORM], schema, "Window transform options."
        )
        definitions[_AGGREGATE_OPTIONS] = m.JsonSchema(
            description="Aggregate transform options.",
            type="object",
            properties={"distinct": m.JsonSchema(type="boolean")},
            additional_properties=False,
            x_template=m.SingleTemplate(bases=_WINDOW_OPTIONS),
        )

        # NOTE: aggregate inherits everything from window, so it needs to go 2nd
        common = set[str]()
        for name_union, name_opts in zip(
            (_WINDOW_TRANSFORM, _AGGREGATE_TRANSFORM),
            (_WINDOW_OPTIONS, _AGGREGATE_OPTIONS),
            strict=False,
        ):
            common.update(definitions[name_opts].properties)
            for name, member in schema.iter_members_defs(definitions[name_union]):
                member.remove_properties(common)
                member.x_template = m.SingleTemplate(bases=name_opts, keywords="closed=True")
                self._simplify_arg(member)
                definitions[name] = schema.pop(name)

        only_transform = "BinInterval", "FrameValue", "TransformField"
        for def_name in only_transform:
            definitions[def_name] = schema.pop(def_name)

        interval_tf = schema.pop("IntervalTransform")
        for member_ref in interval_tf.iter_members():
            member_name = member_ref.def_name
            definitions[member_name] = schema.pop(member_name)
        definitions["IntervalTransform"] = interval_tf
        return definitions

    def _simplify_arg(self, member: m.JsonSchema) -> None:
        for prop_name in member.required:
            self._replace_arg(member.properties[prop_name])


def materialize_supertype(
    union: m.JsonSchema, schema: m.InputSchema, description: str
) -> m.JsonSchema:
    """Approximate a base class that all members of `union` can inherit from.

    ## Notes
    - `union` must be a union of refs, where each points to exactly 1 object type
    - This operation only makes sense if the common properties are non-generic
    """
    it = schema.iter_members_defs(union)
    _, first = next(it)
    owned_props = deepcopy(first.properties)
    common = set(owned_props)
    for _, member in it:
        common.intersection_update(member.properties)

    if not common:
        msg = f"The members of `union` have 0 common properties, got:\n{union!r}"
        raise TypeError(msg)
    return m.JsonSchema(
        description=description,
        type="object",
        properties={k: v for k, v in owned_props.items() if k in common},
        additional_properties=False,
        x_template=m.SingleTemplate(),
    )


_PLOT_ATTRS = "PlotAttributes"
_PLOT = "Plot"
_MARK_DATA = "MarkData"
_MARK_DATA_OPTIONAL = "MarkDataOptional"
_COMPONENT = "Component"
_PLOT_MARK = "PlotMark"
_MARK_OPTIONS = "MarkOptions"
_CHANNEL_VALUE = "ChannelValue"


# TODO @dangotbanned: Simplify `SpecDeduplicate._plot_mark`
class SpecDeduplicate(SchemaMod):
    """See `tools.models.mosaic` module doc for `Component` detail."""

    _SCHEMA_DIR: ClassVar[Path] = fs.SCHEMA
    extracted: m.InputSchema

    _MOVE_TO_MARKS = (
        "TipPointer",
        "SelectFilter",
        "ChannelDomainValueSpec",
        "ChannelDomainValue",
        "ChannelDomainSort",
        "ChannelName",
        "ChannelValueSpec",
        "ChannelValueIntervalSpec",
        "SortOrder",
        "ScaleName",  # (PlotTypes)
        "SQLExpression",
        "AggregateExpression",
        "ReducerPercentile",  # (PlotTypes)
        "Reducer",  # (PlotTypes)
        "FrameAnchor",  # (PlotTypes)
        "StackOrder",
        "StackOrderName",
        "MarkerName",
        "SymbolType",
        "GridInterpolate",
        "PlotFrom",
        "PlotDataInline",
        "PlotMarkData",
    )

    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.map_plot_mark = m.ref_mapper({_PLOT_MARK: self.filename})

    @property
    def path(self) -> Path:
        return self._SCHEMA_DIR / self.filename

    def run(self, schema: m.InputSchema) -> None:
        self.insert_base(_PLOT_ATTRS, schema.pop(_PLOT_ATTRS), schema)

        for name, member in schema.iter_members_defs(schema[_COMPONENT]):
            if not member.is_union():
                if name == _PLOT:
                    self._plot(member)
                else:
                    self.insert_base(name, member, schema)
            elif name == _PLOT_MARK:
                self.extracted = schema.__replace__(
                    id=IdName(self.filename), definitions=self._extract_marks(member, schema)
                )
                serde.write_json(self.path, self.extracted, pretty=True)
                print(f"Generated schema at: {fs.repo_relative_str(self.path)}")
            else:
                msg = f"Found unexpected union {name!r} in {_COMPONENT!r}, got:\n{member!r}"
                raise NotImplementedError(msg)

    def _plot(self, plot: m.JsonSchema) -> None:
        prop = plot.properties.pop("plot")
        prop.map_refs(self.map_plot_mark)
        # Plot extends PlotAttributes, adding a single `plot` required property
        plot.properties = {"plot": prop}
        plot.x_template = m.ExtraTemplate.from_open_root(_PLOT, _PLOT_ATTRS)

    def _extract_marks(
        self, plot_mark: m.JsonSchema, schema: m.InputSchema
    ) -> dict[DefName, m.JsonSchema]:
        definitions: dict[DefName, m.JsonSchema] = {}
        pop = schema.pop
        for name in self._MOVE_TO_MARKS:
            definitions[name] = pop(name)
        definitions[_CHANNEL_VALUE] = pop(_CHANNEL_VALUE)
        definitions[_CHANNEL_VALUE].map_refs(m.ref_mapper({"Transform": "transform.json"}))

        # NOTE: Removes indirection, these are identical besides minor doc phrasing
        pop("StackOffset")
        pop("VectorShape")
        definitions["StackOffset"] = pop("StackOffsetName")
        definitions["VectorShape"] = pop("VectorShapeName")
        definitions["Curve"] = pop("CurveName").__replace__(description=pop("Curve").description)

        owned_props = deepcopy(schema[plot_mark.any_of[0].def_name].properties)
        definitions["Tip"] = self._extract_tip_def(owned_props["tip"])

        mark_common = set(owned_props)
        previously_insert_base: list[tuple[DefName, m.JsonSchema]] = []
        """Need a another base class `MarkOptions`, but can't get that until visiting them all.
        Will hack around for now.
        """

        for member_1_name, member_1 in schema.iter_members_defs(plot_mark):
            if not member_1.is_union():
                mark_common.intersection_update(member_1.properties)
                previously_insert_base.append((member_1_name, member_1))

            else:
                # NOTE: Lift members of (`DensityX`, `DensityY`) into definitions.
                doc = member_1.description
                member_refs = []
                for idx, member_2 in enumerate(member_1.iter_members(), 1):
                    if member_2.is_ref():
                        msg = f"Expected only anonymous unions at this level, but found a reference member {member_2!r}"
                        raise NotImplementedError(msg)
                    member_name = f"{member_1_name}{idx}"
                    member_refs.append(m.JsonSchema.new_ref(member_name))
                    mark_common.intersection_update(member_2.properties)
                    previously_insert_base.append(
                        (member_name, member_2.__replace__(description=doc))
                    )
                member_1.any_of = member_refs
                definitions[member_1_name] = member_1
            pop(member_1_name)

        # TODO @dangotbanned: Make this generic when adding back
        # Too complicated for now, while there are multiple bases
        mark_common.discard("mark")
        definitions[_PLOT_MARK] = pop(_PLOT_MARK)

        definitions[_MARK_OPTIONS] = m.JsonSchema(
            description="Shared options for all marks.",
            type="object",
            properties={k: v for k, v in owned_props.items() if k in mark_common},
            additional_properties=False,
            x_template=m.SingleTemplate(),
        )
        definitions[_MARK_DATA_OPTIONAL] = m.JsonSchema(
            type="object",
            properties={
                "data": m.JsonSchema(
                    ref="#/definitions/PlotMarkData", description="The data source for the mark."
                )
            },
            additional_properties=False,
            x_template=m.SingleTemplate(bases=_MARK_OPTIONS),
        )
        definitions[_MARK_DATA] = definitions[_MARK_DATA_OPTIONAL].__replace__(required=["data"])

        common = tuple(mark_common)
        for name, member in previously_insert_base:
            member.remove_properties(common)
            definitions[name] = self._mark_with_base(name, member)

        for member in reversed(schema[_COMPONENT].any_of):
            # NOTE: Traversing a very large union to replace a single reference, needs early exit
            if member.ref.endswith(_PLOT_MARK):
                member.map_refs(self.map_plot_mark)
                break
        return definitions

    def _mark_with_base(self, name: str, mark: m.JsonSchema) -> m.JsonSchema:
        if "data" in mark.properties:
            if "data" in mark.required:
                required = list(mark.required)
                required.remove("data")
                mark.required = required
                root = _MARK_DATA
            else:
                root = _MARK_DATA_OPTIONAL
            del mark.properties["data"]
        else:
            root = _MARK_OPTIONS
        mark.x_template = m.ExtraTemplate.from_name(name, root)
        return mark

    def _extract_tip_def(self, tip_property: m.JsonSchema) -> m.JsonSchema:
        """Fix a mangled inline intersection, with an anonymous object, inside an inline union.

        https://github.com/dangotbanned/mosaic/blob/824e919b14f833578feed5c36edcd032d6fa6184/packages/vgplot/spec/src/spec/marks/Marks.ts#L428-L434
        """
        for idx, member in enumerate(tip_property.iter_members()):
            if member.type == "object":
                tip_def = deepcopy(member)
                tip_def.additional_properties = False
                tip_def.description = tip_property.description
                any_of = list(tip_property.any_of)
                any_of[idx] = m.JsonSchema.new_ref("Tip")
                tip_property.any_of = any_of
                return tip_def
        msg = f"Did not find inline `Tip` in: {tip_property!r}"
        raise NotImplementedError(msg)

    def insert_base(self, name: DefName, def_schema: m.JsonSchema, schema: m.InputSchema) -> None:
        """Mark `name` to generate an extra TypedDict that is [open](https://typing.python.org/en/latest/spec/typeddict.html#openness).

        The extra version becomes a shared base class for `name` and the version in `spec` (if a component).
        Each of those are then able to be [closed](https://typing.python.org/en/latest/spec/glossary.html#term-closed).
        """
        def_schema.x_template = m.ExtraTemplate.from_name(name, "TypedDict")
        schema.insert(name, def_schema)


def main() -> None:
    # mosaic -> msgspec -> json -> datamodel-codegen -> back here for more
    artifacts = generate_python_schema(SCHEMA_IN, SCHEMA_OUT)

    fs.run("uv", "run", "datamodel-codegen", "--profile=spec")
    module_names = (
        f"- {fs.repo_relative_str(fp)}"
        for fp in fs.MOSAIC_SPEC_GEN.iterdir()
        if fp.stem != "__init__" and fp.suffix == ".py"
    )
    print(f"Generated modules at:\n{'\n'.join(module_names)}")
    codemod.move.move_class_defs_to_top(
        fs.MOSAIC_SPEC_GEN / "marks.py", _MARK_OPTIONS, _MARK_DATA, _MARK_DATA_OPTIONAL
    )
    codemod.move.move_class_defs_to_top(fs.MOSAIC_SPEC_GEN / "transform.py", _WINDOW_OPTIONS)
    artifacts.generate_spec_module(fs.MOSAIC_SPEC_INTERSECTION)


if __name__ == "__main__":
    main()
