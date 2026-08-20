---
name: designing-density-token-systems
description: Model density as coordinated interaction and spatial decisions rather than a global scale factor that shrinks interfaces indiscriminately.
---

# Designing density token systems

Density changes how much work fits in a surface, but it also changes targeting, scanning, rhythm, and error risk. Use this skill when compact, comfortable, touch, expert, or data-dense modes must coexist in one design system.

## Decision ownership

Own which spatial and control metrics participate in density, how density levels are named, which dimensions are invariant for accessibility, and whether density is global, regional, or component-scoped. Decide when a compact variant is a true mode versus a distinct component configuration.

Do not own responsive breakpoint behavior or arbitrary spacing tokens outside the density relationship.

## Inputs and evidence

Collect component dimensions, padding, row heights, target sizes, typography metrics, pointer/touch usage, expert-user workflows, error rates, viewport constraints, and current compact overrides. Inspect components where reducing height changes affordance, not merely appearance: checkboxes, drag handles, tree rows, data grids, and toolbars are especially sensitive.

Separate visual whitespace from hit-area geometry; they may need different density policies.

## Procedure

Define density levels as coordinated bundles with explicit intent. Establish invariant minimum hit targets and focus visibility before reducing visual spacing. Decide which tokens scale discretely and which remain fixed. For text-bearing controls, ensure line height and internal padding still accommodate localization and zoom.

Prefer semantic density tokens such as control block padding or row rhythm over multiplying every spacing primitive. Allow components to opt out when their interaction model cannot safely compact. Document whether density can change at runtime and whether nested regions may use different levels.

Test dense layouts with keyboard, pointer, touch, zoom, and large content. A useful dense mode improves information throughput without turning neighboring controls into ambiguous targets.

## Failure topology

Global scaling often creates tiny hit areas, clipped labels, weakened focus rings, and inconsistent icon alignment. A second failure is pseudo-density: only whitespace shrinks while information architecture remains unchanged, so the interface becomes cramped without improving throughput. Mixed-density regions can also create rhythm discontinuities and unpredictable component heights.

If compact mode requires dozens of one-off CSS overrides, density is not modeled as a system.

## Falsification

Measure target sizes, row scan efficiency, label clipping, and interaction error rates across levels. Toggle density at runtime and inspect every compound component for geometry jumps or stale measurements. Compare keyboard traversal and touch use; if dense mode is only viable for one modality, that constraint must be explicit.

Add a new component and attempt to implement all supported density levels using existing tokens. Needing ad hoc numeric values falsifies coverage.

## Output contract

Produce a `density-token-systems-contract` defining density levels, participating token categories, invariants, hit-area policy, opt-out rules, regional mixing constraints, runtime switching behavior, and verification cases for representative components across input modalities, zoom, and localization.

## Handoffs

Use `designing-token-mode-architecture` for global mode composition, `designing-component-token-scopes` for component-local geometry, `designing-touch-targets` for target safety, and `designing-responsive-density-shifts` when available space triggers density changes.