---
name: governing-component-variant-taxonomies
description: Use when a component accumulates size, emphasis, intent, density, layout, platform, or stylistic options and the system must decide which differences deserve first-class variants instead of tokens or composition.
---

# Governing Component Variant Taxonomies

## Why Variant Taxonomy Matters
Every new boolean or variant value multiplies the public state surface. This skill owns the decision about which axes are legitimate component variants, which are semantic state, which belong in tokens, and which should be achieved through composition. It prevents “variant” from becoming a storage bin for every design difference.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent defines component boundaries and API philosophy. This specialist decides the classification and governance of variation axes within those boundaries.

## Classification Test
For a proposed axis ask: does it change semantic purpose, interaction behavior, layout responsibility, emphasis hierarchy, platform convention, or only raw styling? Is the variation reusable across product contexts? Does it create incompatible combinations with existing axes? Can a token express it without changing component contract? Can composition express it without hidden coupling?

A first-class variant must have a stable semantic reason and bounded values. Avoid booleans whose negative meaning is unclear; prefer an explicit axis when values are mutually exclusive.

## Combination Budget
Map meaningful cross-axis interactions, not every mathematical product. Declare forbidden or nonsensical combinations and choose which axis has authority when two affect the same property. A variant matrix is evidence for API coherence, not a command to render every cell.

## Evidence
Evidence includes consumer use cases, API examples, combination review, rendered representative states, implementation complexity, and migration analysis for removing redundant variants. Demonstrate that each accepted value communicates a distinction users or integrators can reason about.

## Failure Modes
Failure includes `compact` and `small` overlapping, semantic danger encoded only as a color variant, platform names used as style presets, booleans that interact unpredictably, and variant values that exist for one page-specific exception. Another failure is moving runtime state such as `loading` into purely visual variants.

## Falsification
Falsification removes a proposed variant and tries tokenization or composition; if no material semantic/behavioral decision is lost, the variant was unnecessary. Conversely, combine boundary values and verify the API predicts the result. Ambiguous precedence falsifies the taxonomy.

## Recovery
Recovery consolidates overlapping axes, migrates visual-only differences to tokens, promotes true state to the state contract, and creates composition primitives for structural differences. Provide a compatibility path for consumers when public variants are retired.

## Output
Output: `component-variant-taxonomies-contract`, documenting accepted axes, semantics, values, forbidden combinations, ownership, and rejected alternatives.

## Handoff
Handoff runtime transition semantics to component-state governance and semantic part stability to anatomy governance.

## Sibling Boundary and delete-the-skill
State contracts can be correct while the public variant API is still incoherent. The delete-the-skill test passes because no sibling owns the classification boundary between variant, token, state, and composition.