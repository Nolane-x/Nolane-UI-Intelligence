---
name: designing-variant-prop-taxonomies
description: Model component variants as orthogonal semantic dimensions so prop combinations remain meaningful, testable, and stable as components evolve.
---

# Designing variant prop taxonomies

Variants should encode meaningful alternatives, not every visual difference observed in screenshots. Use this skill when a component exposes size, emphasis, intent, appearance, density, placement, or other finite prop dimensions and combinations are becoming difficult to reason about.

## Decision ownership

Own variant dimensions, value names, orthogonality, dependency and exclusion rules, defaults, and promotion criteria. Decide whether a visual difference is a variant, a state, a responsive adaptation, a theme decision, or a separate component.

## Inputs and evidence

Collect current prop combinations, design variants, usage frequency, invalid combinations, style branches, product wrappers, accessibility differences, and historical additions. Identify dimensions that are correlated in practice even if modeled independently.

Map each variant value to user or product intent rather than appearance alone.

## Procedure

Define one semantic axis at a time. Keep axes orthogonal when consumers may legitimately combine them; merge values when combinations are nonsensical. Use names such as `intent=critical` or `emphasis=strong` when they express meaning better than `red` or `filled`.

Separate interaction state from variants: disabled, pressed, selected, and loading usually arise from runtime state. Separate responsive adaptations unless consumers explicitly choose them. Document invalid combinations and enforce them in types or runtime validation where feasible.

Review defaults as part of the contract; changing a default can be more breaking than adding a new value.

## Failure topology

Variant explosion produces combinatorial styling and untested corners. Boolean props often represent hidden axes and permit contradictions. Another failure is appearance naming that prevents themes from changing visuals without making prop names false.

A variant dimension can also mask a component split when two values have different semantics, keyboard behavior, or structure.

## Falsification

Generate the meaningful combination matrix and inspect empty or contradictory regions. Build examples across themes and responsive contexts; semantic names should remain true when visuals differ. Remove a rarely used value and determine whether its use case can be composed or expressed through another axis.

If adding one new value requires branches across unrelated dimensions, the taxonomy is coupled.

## Output contract

Produce a `variant-prop-taxonomies-contract` defining axes, values, semantic intent, defaults, orthogonality, dependencies, invalid combinations, state/theme/responsive boundaries, testing matrix, and criteria for adding, merging, or splitting variants.

## Handoffs

Use `designing-component-api-governance` for public API shape, `designing-composition-boundaries` when a variant is structurally distinct, `designing-component-token-scopes` for styling ownership, and `designing-design-system-versioning` when changing established defaults or values.