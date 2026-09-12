# Intersection

The TypeScript definition of [Spec] does not translate well through JSON schema to `TypedDict`.
This doc is to *show* the problem, as explaining it is tricky.

## What are `Spec` and `Component`?

Here's a visual to illustrate the complexity

```ts
export type PlotMark = Area | ... | Density | DensityX | DensityY;
//                     ----       ^           --------   --------
//                     |        Union         |          |
//                     Interface              |          |
//                                            Interface(s) intersected with a
//                                            union of 4x anonymous interfaces

export type Component = HConcat | ... | Legend | PlotMark;
//                     --------       ^          --------
//                     |            Union        |
//                     Interface                 Union (65 members)

export type Spec = SpecHead & Component;
//                 -------- ^ ---------|
//                 |   Intersection    |
//                 |                   Union (11 members)
//                 Interface
```

## How does that fit into python?

A **limited form** of [Intersection Types] *are* representable using either `TypedDict` or
`Protocol`.

```py
class SpecHead(TypedDict): ...
class HConcat(TypedDict): ...
class Area(TypedDict): ...

class SpecHConcat(SpecHead, HConcat): ...
class SpecArea(SpecHead, Area): ...

type Spec = SpecHConcat | ... | SpecArea
```

Sadly, this doesn't cover intersecting with a union.

## The fix?

- Find all the deeply-nested union members (80-90ish)
  - Includes defining names for those that are anonymous in the schema
- Mix each one with `SpecHead` to create a new TypedDict
- Union each of those to define `Spec`

[Spec]: https://github.com/uwdata/mosaic/blob/e3cb141cfae4a0692990a924c03772956af89f78/packages/vgplot/spec/src/spec/Spec.ts#L34-L70
[Intersection Types]: https://www.typescriptlang.org/docs/handbook/2/objects.html#intersection-types
