---
name: designing-theme-inheritance
description: Define theme inheritance and override precedence so derived themes can reuse shared decisions without accidental leakage or override ambiguity.
---

# Designing theme inheritance

Theme inheritance is a contract about authority, not a shortcut for copying fewer values. Use this skill when a base theme, brand theme, product theme, accessibility theme, or platform theme must extend another theme while preserving a predictable resolution path.

## Decision ownership

Own which theme layers may inherit from which, what kinds of decisions may be overridden, how precedence is computed, and where inheritance must stop. Decide whether an override expresses a true local semantic difference or is merely compensating for a weak upstream token model.

This skill does not choose palette values. It governs the cascade that decides which declared value wins and why.

## Inputs and evidence

Collect the full theme graph, token resolution traces, override files, runtime theme selectors, product-specific patches, and historical incidents where one theme unintentionally affected another. Inspect both declared and resolved values across representative components; source files alone can hide implicit defaults injected by tooling.

Record every inheritance edge with its rationale. Pay special attention to diamonds, multiple parents, late-loading overrides, and themes that override large portions of their parent.

## Procedure

Model inheritance as a directed acyclic authority graph. Prefer a single semantic baseline plus sparse, purpose-specific overrides. If multiple inheritance is unavoidable, define deterministic conflict rules by semantic authority rather than file order. Separate inheritance from composition: a high-contrast layer may compose with a brand theme, while a regional brand derivative may truly inherit brand decisions.

Specify override admissibility by layer. A product theme may replace product semantics but should not silently redefine foundational primitive meaning if downstream themes assume that primitive is stable. Require tooling to expose the origin path of every resolved token.

For deep chains, evaluate whether each level contributes an independently governed decision. Flatten decorative layers that only forward values.

## Failure topology

The dangerous failure is invisible coupling: a parent change appears local but alters descendants whose overrides were incomplete. Diamond inheritance can make precedence dependent on load order. Another failure is override saturation, where a child replaces most of its parent and still claims inheritance, making reviewers underestimate independence.

A theme hierarchy can also become semantically inverted when an accessibility layer inherits from a brand layer and is later overridden by brand-specific values, defeating the accessibility intent.

## Falsification

Change one upstream semantic token and enumerate all descendant resolutions. Unexpected descendants indicate hidden coupling. Shuffle declaration order and verify outputs stay stable. Remove a parent edge from a heavily overridden theme; if almost nothing changes, the inheritance claim may be misleading. Test supported combinations such as brand × dark × contrast and confirm the same authority rules explain every winning value.

Ask a maintainer to trace one resolved token to its origin without reading build implementation. If that is impractical, the inheritance model is too opaque.

## Output contract

Produce a `theme-inheritance-contract` containing the inheritance graph, allowed parent-child relations, override authority rules, precedence algorithm, composition-vs-inheritance decisions, cycle prevention, origin diagnostics, sparse-override expectations, and representative resolution traces across supported theme combinations.

## Handoffs

Use `designing-token-mode-architecture` for orthogonal contextual dimensions, `designing-semantic-token-aliasing` for reference chains inside a theme, `designing-multi-brand-theming` for brand separation, and `designing-design-system-versioning` when inheritance changes require compatibility boundaries.