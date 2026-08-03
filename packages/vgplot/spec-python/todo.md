# Todo

Here's a big list of things to do/known issues

## General

- [x] Generate `TypedDict`s from the schema
- [x] Generate docstrings
- [x] Generate an `__all__`
  - [x] `_gen`
  - [x] `mosaic_spec`
- [x] Use `.py` for target output instead of `.pyi`
- [ ] Split up `mosaic.py` into multiple modules [^1]
  - **30k** LOC with docs
- [ ] Fix emitting 81 version of `Spec`
  - [x] Caused by a huge intersection type `Spec = SpecHead & Component` (see [explanation](https://github.com/dangotbanned/mosaic/blob/b3793004b483dbdfff0c6e390f9cc24fcbf897a7/packages/vgplot/spec-python/tools/models/source.py#L1-L55))
  - [x] Remove `Spec` from `mosaic.json`
    - Reduced `mosaic.py` **53k** -> **28k** LOC
  - [x] Fix `closed=True` on base class (~100 type errors)
  - [ ] Fix `data: PlotMarkData` Required/NotRequired conflict (~59 type errors)
- [ ] Define ~~`TypeAlias`~~`TypeAliasType`s in another module of instead of scattered between `TypedDict` defs
- [ ] Add some tests once the top-level namespace starts stabilizing
- [ ] `typing_extensions` compat (`closed=True` is required for runtime `TypedDict`s)
  - [x] Add `_typing_compat.py` to handle `"typing-extensions>=4.16 ; python_full_version < '3.15'"`
  - [ ] Use `_typing_compat.py` imports for codegen ([blocked by](https://github.com/koxudaxi/datamodel-code-generator/issues/3681))

[^1]: Huge files kill language servers. Having to disable pylance because it is too slow now

## Refactor

- [x] Use `msgspec` for models in `schema_mod`
  - [x] Input json schema
  - [x] Replace non-msgspec pipeline
- [x] Split up `scripts/`
  - [x] `tools/` (reusable)
  - [x] `scripts/` (Everything that does one job, on demand)

## `datamodel-code-generator` feature requests

Things that should be easiest to fix upstream in `datamodel-code-generator`

- [ ] [Support (`total=False`, `Required`) in `TypedDict` (#3680)](https://github.com/koxudaxi/datamodel-code-generator/issues/3680)
- [ ] [Support overriding default imports (#3681)](https://github.com/koxudaxi/datamodel-code-generator/issues/3681)
- [ ] [Support configuring `--use-type-alias` behavior (#3682)](https://github.com/koxudaxi/datamodel-code-generator/issues/3682)

## `mosaic-spec` feedback

Things that should be easiest to fix upstream in Mosaic

- [ ] Avoid anonymous literal/enums
- [ ] Generally, try to provide names for complex, repeated types
- [ ] Output multiple schemas -> fixes one big file issue
- [ ] Add `"x-*"` [extension fields](https://datamodel-code-generator.koxudaxi.dev/custom_template/#schema-extensions) into the schema which can be used here for templating
  - Which file did the symbol come from?
  - Inheritance?
- [ ] Follow some python-friendly rules when writing **docs** in TS
  - [ ] Avoid confusables
  - [ ] One line short description, ending with a period. Then go wild.
