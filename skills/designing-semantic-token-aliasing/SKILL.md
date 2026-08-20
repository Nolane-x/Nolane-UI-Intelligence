---
name: designing-semantic-token-aliasing
description: Define semantic token reference chains so meaning can evolve independently from raw values without creating opaque alias mazes.
---

# Designing semantic token aliasing

Semantic aliases are useful only when each indirection adds a stable layer of meaning. Use this skill when tokens need to reference other tokens across primitives, semantic roles, components, brands, or platforms and the system must remain understandable under change.

## Decision ownership

Own when aliasing is justified, what a reference may point to, how many semantic boundaries a chain may cross, and how cycles or accidental coupling are prevented. Decide whether an alias represents equivalence, inheritance, fallback, or a theme-specific mapping; those relationships must not be conflated.

This skill does not own the taxonomy itself or the build-tool syntax. It owns semantic reference integrity.

## Inputs and evidence

Collect the token graph, resolved values for all supported themes and modes, component call sites, override layers, and historical changes. Identify aliases created solely to preserve old names, aliases shared by unrelated roles, and chains whose terminal primitive changes unexpectedly when a middle layer is edited.

For every important alias, capture the reason the source and target are related. A graph with edges but no rationale is impossible to review safely.

## Procedure

Classify each reference edge. A semantic-to-primitive edge binds a role to a value family; a component-to-semantic edge binds a local need to a reusable role; a brand or mode mapping changes resolution under a declared context. Keep these directions consistent so consumers can reason from intent toward value.

Minimize indirection that adds no meaning. If several aliases simply forward the same value, determine which concepts have independent change authority. Remove pass-through aliases that exist only because previous tooling encouraged them.

Define cycle detection, missing-reference behavior, fallback semantics, and diagnostics for resolution. Require tooling to expose both declared and resolved values so designers and engineers can inspect why a token became a particular value.

## Failure topology

Alias chains become dangerous when semantic ownership is hidden behind many hops, when two roles are coupled because they currently resolve to the same primitive, or when a platform override changes a low-level token and unexpectedly repaints unrelated components. A compatibility alias can also become permanent and mislead new consumers into choosing a deprecated concept.

Another failure is direction inversion: primitive names alias semantic names, making the foundation depend on product intent and creating cycles during theme expansion.

## Falsification

Perturb a terminal primitive and inspect the resolved blast radius. If unrelated semantic roles change, the aliases encode false equivalence. Remove an intermediate alias; if no decision boundary disappears, that layer may be decorative. Resolve every supported mode and verify that no reference is missing, cyclic, or silently falling back to a context-inappropriate default.

Ask maintainers to explain the meaning added by each hop in a long chain. An unexplained hop is evidence against keeping it.

## Output contract

Produce a `semantic-token-aliasing-contract` with allowed edge types, direction rules, maximum reviewable indirection, cycle and missing-reference behavior, compatibility-alias policy, diagnostic requirements, and inspected reference chains showing declared intent and resolved values across modes.

## Handoffs

Use `designing-token-taxonomies` for layer definitions, `designing-token-mode-architecture` for contextual resolution dimensions, `designing-theme-inheritance` for theme override precedence, and `designing-token-deprecation-migrations` when an alias exists primarily to bridge an old contract.