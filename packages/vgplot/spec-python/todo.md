# Todo

[datamodel-code-generator issue]: https://github.com/koxudaxi/datamodel-code-generator/issues/new?template=feature_request.md

- [x] Experiment with docs config
  - [x] **Fixed** `ParamRef` being "deduplicated" to `DataQuery`
- [ ] Try to split up output into modules (*huge files kill language servers*)
  - **14k** LOC without docs
  - ~~**53k**~~ **28k** LOC with docs
    - After removing `Spec`
- [x] Generate an `__all__`
  - [x] `_gen`
  - [x] `mosaic_spec`
- [ ] Fix `Spec1` - `Spec81`
  - [x] Caused by a huge intersection type `Spec = SpecHead & Component`
  - [x] Remove `Spec` from `mosaic.json`
  - [ ] Add a manual version of `Spec`
- [ ] Open a [datamodel-code-generator issue] about preference for `total=False` instead of 90237393x `NotRequired`
  - When most are `NotRequired`, the important bit is which one's are `Required`
- [x] Using `.py` for target output
  - Needed to use stubs when functional syntax prevented forward refs
  - Will need to add `typing_extensions` dependency
- [ ] Ordering of `TypeAlias`s
  - Possibly move to another file, instead of sctattered between `TypedDict` defs
- [ ] Add some tests once the top-level namespace starts stabilizing
- [ ] `typing_extensions` compat (`closed=True` is required for runtime `TypedDict`s)
  - [x] Add `_typing_compat.py` to handle `"typing-extensions>=4.16 ; python_full_version < '3.15'"`
  - [ ] Use `_typing_compat.py` imports for codegen

## `mosaic-spec` feedback

Things that should be easiest to fix upstream

- [ ] Avoid anonymous literal/enums
- [ ] Generally, try to provide names for complex, repeated types
- [ ] Output multiple schemas -> fixes one big file issue
- [ ] Add `"x-*"` [extension fields](https://datamodel-code-generator.koxudaxi.dev/custom_template/#schema-extensions) into the schema which can be used here for templating
  - Which file did the symbol come from?
  - Inheritance?
- [ ] Follow some python-friendly rules when writing **docs** in TS
