# Todo

- [x] Experiment with docs config
  - [x] **Fixed** `ParamRef` being "deduplicated" to `DataQuery`
- [ ] Try to split up output into modules
  - **14k**/**53k** LOC with/out docs
  - Huge files kill language servers
- [x] Generate an `__all__`
  - [x] `_gen`
  - [x] `mosaic_spec`
- [ ] Fix `Spec1` - `Spec81`
  - [x] Caused by a huge intersection type `Spec = SpecHead & Component`
  - [ ] Replace with manual inheritance?
- [ ] Open an issue about preference for `total=False` instead of 90237393x `NotRequired`
  - When most are `NotRequired`, the important bit is which one's are `Required`
- [x] Using `.py` for target output
  - Needed to use stubs when functional syntax prevented forward refs
  - Will need to add `typing_extensions` dependency
- [ ] Ordering of `TypeAlias`s
  - Possibly move to another file, instead of sctattered between `TypedDict` defs
- [ ] Add some tests once the top-level namespace starts stabilizing

## `mosaic-spec` feedback

Things that should be easiest to fix upstream

- [ ] Avoid anonymous literal/enums
- [ ] Generally, try to provide names for complex, repeated types
- [ ] Output multiple schemas -> fixes one big file issue
- [ ] Add `"x-*"` [extension fields](https://datamodel-code-generator.koxudaxi.dev/custom_template/#schema-extensions) into the schema which can be used here for templating
  - Which file did the symbol come from?
  - Inheritance?
- [ ] Follow some python-friendly rules when writing **docs** in TS
