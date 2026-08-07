# Todo

Here's a big list of things to do/known issues

## General

- [x] Generate `TypedDict`s from the schema
- [x] Generate docstrings
- [x] Generate an `__all__`
  - [x] `_gen`
  - [x] `mosaic_spec`
- [x] Use `.py` for target output instead of `.pyi`
- [x] Fix emitting 81 version of `Spec`
  - [x] Caused by a huge intersection type `Spec = SpecHead & Component` (see [explanation](https://github.com/dangotbanned/mosaic/blob/b3793004b483dbdfff0c6e390f9cc24fcbf897a7/packages/vgplot/spec-python/tools/models/source.py#L1-L55))
  - [x] Remove `Spec` from `mosaic.json`
    - Reduced `mosaic.py` **53k** -> **28k** LOC
  - [x] Fix `closed=True` on base class (~100 type errors)
  - [x] Fix `data: PlotMarkData` Required/NotRequired conflict (~59 type errors)
- [ ] Define ~~`TypeAlias`~~`TypeAliasType`s in another module of instead of scattered between `TypedDict` defs
- [ ] Add some tests once the top-level namespace starts stabilizing
- [x] `typing_extensions` compat (`closed=True` is required for runtime `TypedDict`s)
  - [x] Add `_typing_compat.py` to handle `"typing-extensions>=4.16 ; python_full_version < '3.15'"`
  - [x] Use `_typing_compat.py` imports for codegen

## Splitting one big file

`mosaic.py` is too large (~**30k** LOC with docs) and this kills the performance of language servers.  

Pylance is non-functional as it isn't able to do the kind of incremental magic that `ty` can within a single file.
To mitigate this, here are some potential modules/subpackages to lighten the load:

- [x] `interactors.py`
- [ ] marks (**136 KB**)
  - [ ] `Marks.ts` (39 KB)
  - [ ] `Axis.ts` (13 KB)
  - [ ] 25 others (84 KB) total
- [ ] data (6 KB)
- [ ] inputs (7 KB)
- [ ] interval (2 KB)
- [x] `params.py`
- [ ] plot
  - [x] Share **215** fields between `Plot` & `PlotAttributes`
  - [ ] Move to another module (*maybe difficult*)
    - `PlotAttribute.ts` (**63 KB**)
- [x] `spec.py`
  - [x] Use the original class names and don't re-export to top-level, e.g.
    - `import mosaic_spec as ms; ms.spec.Plot(...)`
- [x] `transforms.py`
  - [x] split
  - [ ] cleanup
- [ ] typing (aliases)
  - [x] `ParamRef`
  - [ ] `PlotTypes.ts` (14 KB) and **isolated**
  - [ ] A large gain will come from naming duplicated inline types, e.g.
    - 60x of `str | float | bool | ParamRef`
    - 28x of `Literal["CURRENT ROW", "GROUP", "TIES", "NO OTHERS", "current row", "group", "ties", "no others"]`
    - **Many** `OneOrSeq[T]` cases ([altair/vegalite/v6/schema/_typing.py#L100-L114])
- [x] `css_styles.py`
  - Has **508** fields
  - Next 2 highest have **215** fields

[altair/vegalite/v6/schema/_typing.py#L100-L114]: https://github.com/vega/altair/blob/c217ba4b03386fe303b70c75551e96d4e2bc6f30/altair/vegalite/v6/schema/_typing.py#L100-L114

## `datamodel-code-generator` feature requests

Things that should be easiest to fix upstream in `datamodel-code-generator`

- [x] [Support (`total=False`, `Required`) in `TypedDict` (#3680)](https://github.com/koxudaxi/datamodel-code-generator/issues/3680)
- [x] [Support overriding default imports (#3681)](https://github.com/koxudaxi/datamodel-code-generator/issues/3681)
- [x] [Support configuring `--use-type-alias` behavior (#3682)](https://github.com/koxudaxi/datamodel-code-generator/issues/3682)

## `mosaic-spec` feedback

Things that should be easiest to fix upstream in Mosaic

- [ ] Avoid anonymous literal/enums
- [ ] Generally, try to provide names for complex, repeated types
- [ ] Output multiple schemas -> fixes one big file issue
- [ ] Add `"x-*"` [extension fields](https://datamodel-code-generator.koxudaxi.dev/custom_template/#schema-extensions) into the schema which can be used here for templating
  - Which file did the symbol come from?
  - Inheritance?
- [ ] Follow some python-friendly rules when writing **docs** in TS
  - [ ] Avoid confusables (c57e964e6016320bde07227a96cc2b4c047b33a8)
  - [ ] One line short description, ending with a period. Then go wild.

### Unflatten the spec

The current design favors large numbers of options available at a single level.
Groups of fields with prefixed names can be represented in another level (e.g. `opacity_*` -> `opacity.{*}`).

### Candidates

I expect we can shrink the size of the schema if these groups could be `"$ref"`s, since we can avoid duplicating so much

- `aria_*`
- `color_*`
- `facet_*`
- `font_*`
- `fx_*`
- `fy_*`
- `inset_*`
- `label_*`
- `length_*`
- `line_*`
- `margin_*`
- `marker_*`
- `opacity_*`
- `projection_*`
- `r_*`
- `stroke_*`
- `symbol_*`
- `text_*`
- `tick_*`
- `x_*`
- `y_*`

### Example

Here's what doing this for `fx_*` and `fy_*` on `PlotAttributes` could look like:

- (https://github.com/dangotbanned/mosaic/commit/38fd9cafc4e72785eae6edddde5b28bb959ddae2)

And here is the same thing in Observable Plot?

- (https://github.com/observablehq/plot/blob/356f579b1d947ee05a914420eddff0f29cee300a/src/plot.d.ts)
