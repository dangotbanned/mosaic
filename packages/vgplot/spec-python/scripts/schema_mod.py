# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "msgspec>=0.21.1",
# ]
# ///
"""Transform `packages/vgplot/spec/dist/mosaic-schema.json` for use in python."""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING, Annotated as A, ClassVar, Final, Literal as L, Protocol

from tools import codemod, fs, serde
from tools.codegen import typed_dict
from tools.codegen.docstrings import doc
from tools.models import mosaic as m

if TYPE_CHECKING:
    from collections.abc import Iterable

GENERATED_MODULE_NAME = "mosaic"
SCHEMA_IN = fs.SPEC / "dist/mosaic-schema.json"
SCHEMA_OUT = fs.SCHEMA / f"{GENERATED_MODULE_NAME}.json"

GENERATED_MODULE = fs.MOSAIC_SPEC / "_gen" / f"{GENERATED_MODULE_NAME}.py"
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
SPEC_HEAD_NO_DATA = f"_{SPEC_HEAD}"


def _recursive_replace(schema: m.JsonSchema) -> m.JsonSchema:
    """Visit 4 fields at all levels of the schema, renaming matches for [`KEYS_REPLACE`][]."""
    replace = KEYS_REPLACE.get
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


def _simplify_type_aliases(schema: m.InputSchema) -> None:
    # NOTE: Removes indirection, these are identical besides minor doc phrasing
    from copy import replace

    schema.insert(
        "Interval",
        replace(schema.pop("Interval"), ref="", any_of=schema.pop("LiteralTimeInterval").any_of),
    )
    schema.insert(
        "Curve", replace(schema.pop("CurveName"), description=schema.pop("Curve").description)
    )
    schema.insert(
        "StackOffset",
        replace(schema.pop("StackOffsetName"), description=schema.pop("StackOffset").description),
    )
    schema.insert("VectorShape", schema.pop("VectorShapeName"))


def generate_python_schema(source: str | Path, target: Path) -> tuple[m.InputSchema, str]:
    print(f"Reading json schema at: {Path(source).relative_to(fs.MONOREPO_ROOT).as_posix()}")
    schema = serde.read_json(source, m.InputSchema)
    spec_def = schema.pop("Spec")
    schema.ref = ""  # Removes `"$ref": "#/definitions/Spec"`
    schema.id = target.name

    schema.definitions = {k: _recursive_replace(v) for k, v in schema.iter_defs()}
    schema.flatten_component_union()

    _simplify_type_aliases(schema)

    CSSStylesSplit("CSSStyles", "css-styles.json").run(schema)
    ParamDefinitionSplit("ParamDefinition", "params.json").run(schema)
    InteractorsSplit("PlotInteractor", "interactors.json").run(schema)
    TransformSplit("Transform", "transform.json").run(schema)

    serde.write_json(target, schema)
    print(f"Generated python schema at: {fs.repo_relative_str(target)}")
    return schema, spec_def.description


class SchemaMod: ...


type Extracted[T] = A[T, L["Extracted"]]


class _CanSetRef(Protocol):
    """Any object with a mutable `ref` attribute."""

    ref: m.Ref


class SchemaSplit(SchemaMod):
    _SCHEMA_DIR: ClassVar[Path] = fs.SCHEMA

    def __init__(self, root_name: m.DefName, filename: str) -> None:
        self.root_name: m.DefName = root_name
        self.filename: str = filename

    @property
    def path(self) -> Path:
        return self._SCHEMA_DIR / self.filename

    def run(self, schema: m.InputSchema) -> None:
        """Split the definitions required for `root_name` from `schema` into `filename`."""
        self._update_refs(schema)
        extracted = self.extract(schema)
        serde.write_json(self.path, extracted)
        print(f"Generated {self.root_name!r} schema at: {fs.repo_relative_str(self.path)}")

    def _update_refs(self, schema: m.InputSchema) -> None:
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

    def _extract_definitions(self, schema: m.InputSchema) -> dict[m.DefName, m.JsonSchema]:
        """Return the contents of the `filename`'s `"definitions"`."""
        msg = f"'{self._extract_definitions.__qualname__}()' is not yet implemented"
        raise NotImplementedError(msg)

    def extract(self, schema: m.InputSchema) -> Extracted[m.InputSchema]:
        return schema.__replace__(id=self.filename, definitions=self._extract_definitions(schema))


class CSSStylesSplit(SchemaSplit):
    # NOTE: Has 500 fields
    def _referenced_by(self, schema: m.InputSchema) -> Iterable[Iterable[m.JsonSchema]]:
        for def_name in "Plot", "PlotAttributes":
            yield schema.get(def_name).properties["style"].iter_members()

    def _extract_definitions(self, schema: m.InputSchema) -> dict[m.DefName, m.JsonSchema]:
        return {self.root_name: schema.pop(self.root_name)}


class InteractorsSplit(SchemaSplit):
    def _referenced_by(self, schema: m.InputSchema) -> Iterable[Iterable[m.JsonSchema]]:
        it = schema.get("Plot").properties["plot"].items_schema().iter_members()
        yield from (it,)

    def _extract_definitions(self, schema: m.InputSchema) -> dict[m.DefName, m.JsonSchema]:
        root = schema.pop(self.root_name)
        definitions = {self.root_name: root}
        for member_ref in root.iter_members():
            member_name = member_ref.def_name
            definitions[member_name] = schema.pop(member_name)
        definitions["BrushStyles"] = schema.pop("BrushStyles")
        definitions["ParamRef"] = schema.get("ParamRef")
        return definitions


class ParamDefinitionSplit(SchemaSplit):
    def _referenced_by(self, schema: m.InputSchema) -> Iterable[Iterable[_CanSetRef]]:
        obj = schema.get("Params").additional_properties
        if isinstance(obj, bool):
            raise NotImplementedError
        yield from ((obj,),)

    def _extract_definitions(self, schema: m.InputSchema) -> dict[m.DefName, m.JsonSchema]:
        root = schema.pop(self.root_name)
        return {
            self.root_name: root,
            # HACK @dangotbanned: Would need to go multiple levels deep via `ParamValue` to reach these.
            # codegen will report if any other refs are missing in the future
            "ParamRef": schema.get("ParamRef"),
            "ParamLiteral": schema.pop("ParamLiteral"),
        } | {name: schema.pop(name) for ref in root.iter_members() if (name := ref.def_name)}


class TransformSplit(SchemaSplit):
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
        it = schema.get("ChannelValue").iter_members()
        yield from (it,)

    def _extract_definitions(self, schema: m.InputSchema) -> dict[m.DefName, m.JsonSchema]:
        root = schema.pop(self.root_name)
        definitions = {self.root_name: root}

        for kind in root.iter_members():
            kind_name = kind.def_name
            for member_ref in schema.get(kind_name).iter_members():
                member_name = member_ref.def_name
                definitions[member_name] = schema.pop(member_name)

            definitions[kind_name] = schema.pop(kind_name)

        only_transform = "BinInterval", "FrameValue", "TransformField"
        for def_name in only_transform:
            definitions[def_name] = schema.pop(def_name)

        interval_tf = schema.pop("IntervalTransform")
        for member_ref in interval_tf.iter_members():
            member_name = member_ref.def_name
            definitions[member_name] = schema.pop(member_name)
        definitions["IntervalTransform"] = interval_tf
        # HACK @dangotbanned: `ParamRef` is not generated in `transform.py`.
        # - `dcg` tries to do some very complicated things to "solve" circular imports,
        #   and this + the linked override disables that.
        # - Ideally, it would ignore circular **typing only** imports or use forward refs in runtime aliases
        # - https://github.com/dangotbanned/mosaic/blob/7004de2a9f4d9f5ea8cd2c11a827b6d0ee2ab437/packages/vgplot/spec-python/pyproject.toml#L79-L80
        definitions["ParamRef"] = schema.get("ParamRef")
        return definitions


def generate_spec_module(
    components: dict[str, m.JsonSchema], spec_doc: str, target: str | Path
) -> None:
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
            import_from(GENERATED_MODULE, (fld.tp for fld in (*fields_excluding_data, field_data))),
        )
    )

    import_names = deque[str]()
    export_names = deque[str]()

    for original_name, component in components.items():
        base_open_name = component.x_base_open
        import_names.append(base_open_name)
        name = f"{SPEC}{original_name}"
        base_spec = SPEC_HEAD_NO_DATA if "data" in component.properties else SPEC_HEAD
        module.extend(typed_dict.iter_lines(name, bases=(base_spec, base_open_name), closed=True))
        export_names.append(name)

    module.extend((f"{SPEC} = TypeAliasType({SPEC!r}, {'|'.join(export_names)})", doc(spec_doc)))
    export_names.append(SPEC)
    module.appendleft(import_from(GENERATED_MODULE, import_names))
    module.appendleft(codemod.fragments.FUTURE_ANNOTATIONS)
    module.append(f"\n__all__ = {tuple(export_names)}\n")
    fs.write_lines(target, module, "Generated module")


def main() -> None:
    # mosaic -> msgspec -> json -> datamodel-codegen -> back here for more
    schema, spec_doc = generate_python_schema(SCHEMA_IN, SCHEMA_OUT)
    components = {name: s for name, s in schema.definitions.items() if s.x_base_open}
    fs.run("uv", "run", "datamodel-codegen", "--profile=spec")
    print(f"Generated module at: {fs.repo_relative_str(GENERATED_MODULE)}")
    generate_spec_module(components, spec_doc, fs.MOSAIC_SPEC_INTERSECTION)


if __name__ == "__main__":
    main()
