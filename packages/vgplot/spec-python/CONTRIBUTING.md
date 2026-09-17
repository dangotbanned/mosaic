# Contributing

The entire `mosaic_spec` API is currently generated. All the fun stuff
happens *outside of* [`src/mosaic_spec`] which can be thought of as the finished cake.

Try baking it with:

```sh
cd packages/vgplot/spec-python
pnpm generate
```

## How it works

### Source

Life for us starts at [`mosaic-schema.json`], which [Mosaic Spec (TypeScript)] takes care of
producing it for us.  
The important part to know is that [`mosaic-schema.json`] encodes [`Spec.ts`] that
lives next door.

### Dataflow

This design is shaped by an understanding that we wish to migrate from using [`mosaic-schema.json`]
as source [in the future]. Therefore, types flow through a series of [Intermediate representations]
(**IR**) before we generate any code:

| What                   | Kind       | Description                                                                                                                                                                                                          | Owner                      |
| ---------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [`Spec.ts`]            | Source     | Where the *original* [root type] comes from.                                                                                                                                                                         | [Mosaic Spec (TypeScript)] |
| [`mosaic-schema.json`] | Source     | *Our* source, which  is generated via [`run schema`].                                                                                                                                                                | [Mosaic Spec (TypeScript)] |
| [`JsonWrapper`]        | **IR** (1) | JSON Schema with annotations. This is the first and **only** stage that has access to the schema.                                                                                                                    | Python                     |
| [`MLIR`] [^2]          | **IR** (2) | A step towards python. <br> Can represent types that python cannot[^3].<br>`MLIR` supports declarative transformation [actions] that let us reshape things to work better in python.                                 | Python                     |
| [`PyIR`]               | **IR** (3) | A subset of the [python type system] which understands concepts like [`TypedDict`] (with [multiple inheritance]) and [`TypeAliasType`].<br>Beyond types, this stage also understands [`Module`(s) and `Package`(s)]. | Python                     |
| [`src/mosaic_spec`]    | Target     | Where our codegen lands.                                                                                                                                                                                             | Python                     |

[^2]: ML -> Mid-level, as it is between the other two

[^3]: Such as TypeScript's [anonymous object types], which would require acceptance of
    [PEP 764 - Inline typed dictionaries].

## Project layout

Most activity takes place in [`/scripts/`] and [`/tools/`], where *ideally* a script is
mostly an arrangement of tools.

| What                 | Description                                                                    |
| -------------------- | ------------------------------------------------------------------------------ |
| [`/scripts/`]        | Code that is run by [`generate`] and other [pnpm scripts].                     |
| [`/tests/`]          | The test suites.                                                               |
| [`/tools/`]          | Building blocks for [`/scripts/`], e.g. [`/tools/app.py`] and  [`/tools/ir/`]. |
| [`mosaic-spec.toml`] | Configuration for [`/tools/app.py`].                                           |
| [Roadmap]            | Ideas for what's next.                                                         |

## Tests

The primary output of `mosaic_spec` are the generated `TypedDict` and `TypeAliasType`s.

These guys have very little runtime behavior, so tests are focused on how this typing is understood
by multiple type checkers, which can be checked via:

```sh
cd packages/vgplot/spec-python
pnpm typecheck
```

To run using a single type checker, use one of:

```sh
pnpm typecheck:ty
pnpm typecheck:pyright
pnpm typecheck:pyrefly
```

> [!NOTE]
> `typecheck` is the final step of [`generate`]

The tests defined under [`/tests/test_examples`] are [also generated], which can be re-run via:

```sh
pnpm generate:examples
```

Runtime tests are still a work-in-progress (see [Test PEPs]), but can be run via:

```sh
pnpm test
```

[`src/mosaic_spec`]: ./src/mosaic_spec/__init__.py
[Mosaic Spec (TypeScript)]: ../spec/README.md
[`mosaic-schema.json`]: ../spec/dist/mosaic-schema.json
[`Spec.ts`]: ../spec/src/spec/Spec.ts
[`run schema`]: ../spec/package.json
[Intermediate representations]: https://en.wikipedia.org/wiki/Intermediate_representation
[in the future]: https://github.com/uwdata/mosaic/issues/1154#issuecomment-5308118344
[root type]: https://json-schema.org/understanding-json-schema/structuring#id
[`JsonWrapper`]: ./tools/ir/json_wrapper/__init__.py
[`MLIR`]: ./tools/ir/mlir/__init__.py
[`PyIR`]: ./tools/ir/pyir/__init__.py
[anonymous object types]: https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#object-types
[PEP 764 - Inline typed dictionaries]: https://peps.python.org/pep-0764/
[actions]: ./mosaic-spec.toml
[`Module`(s) and `Package`(s)]: ./tools/ir/pyir/module.py
[`/scripts/`]: ./scripts/__init__.py
[`/tools/`]: ./tools/__init__.py
[`/tests/`]: ./tests/__init__.py
[Roadmap]: ./docs/roadmap.md
[`/tools/app.py`]: ./tools/app.py
[`/tools/ir/`]: ./tools/ir/__init__.py
[`mosaic-spec.toml`]: ./mosaic-spec.toml
[`generate`]: #contributing
[pnpm scripts]: ./package.json
[`/tests/test_examples`]: ./tests/test_examples/__init__.py
[also generated]: ./scripts/prepare_examples.py
[Test PEPs]: ./docs/roadmap.md#test-peps
[python type system]: https://typing.python.org/en/latest/spec/index.html
[`TypedDict`]: https://typing.python.org/en/latest/spec/typeddict.html
[multiple inheritance]: https://typing.python.org/en/latest/spec/typeddict.html#multiple-inheritance
[`TypeAliasType`]: https://docs.python.org/3/library/typing.html#typing.TypeAliasType
