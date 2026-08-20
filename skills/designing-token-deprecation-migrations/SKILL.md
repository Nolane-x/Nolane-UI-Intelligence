---
name: designing-token-deprecation-migrations
description: Retire or rename design tokens with detectable migration paths, compatibility windows, and semantic correction rather than indefinite aliases.
---

# Designing token deprecation migrations

Token changes propagate through code, design files, themes, documentation, and third-party consumers. Use this skill when a token is obsolete, misnamed, semantically wrong, or being replaced by a new ontology.

## Decision ownership

Own the deprecation lifecycle: replacement mapping, compatibility behavior, detection, migration sequencing, support window, and removal criteria. Decide whether old and new tokens can safely alias during transition or whether coexistence would hide a semantic mismatch.

This skill does not decide the new taxonomy itself; it makes the transition evidence-driven.

## Inputs and evidence

Gather token definitions, repository-wide usage, generated platform artifacts, design-tool references, external package consumers, documentation examples, and resolved-value differences between old and proposed replacements. Identify dynamic lookups that static search may miss and consumers pinned to older package versions.

For renamed semantics, document whether the old token ever represented multiple intents; one-to-one replacement may be false.

## Procedure

Classify migration as pure rename, semantic split, semantic merge, value-policy change, or removal. Provide codemods only where mapping is mechanically safe. For ambiguous uses, require human classification rather than guessing. Emit deprecation diagnostics at build or lint time and make replacement guidance actionable.

Define compatibility aliases with an expiration condition. Ensure aliases do not allow new usage to proliferate; deprecated names should be blocked in new code where feasible. Track adoption by remaining call sites, packages, and design-file references.

Coordinate removal with versioning so consumers know when aliases disappear.

## Failure topology

Indefinite aliases make the old ontology immortal. Automated search-and-replace can silently map one overloaded token to the wrong new role. Another failure is migration telemetry that counts source references but misses generated assets, runtime string keys, or design-tool usage.

Removing a token immediately may force synchronized upgrades across products that cannot coordinate release timing.

## Falsification

Run the migration detector across all known consumer surfaces and seed representative ambiguous cases. Verify it refuses unsafe auto-mapping. Test old and new versions during the compatibility window and after planned removal. Search for new deprecated usage after the deprecation announcement; if it can still enter unnoticed, the control is incomplete.

Sample resolved UI before and after migration to catch semantic changes that static typing cannot detect.

## Output contract

Produce a `token-deprecation-migrations-contract` describing change class, old-to-new mapping, ambiguous cases, diagnostic and codemod behavior, compatibility alias policy, version boundary, migration telemetry, support window, removal gate, rollback strategy, and evidence that visual semantics are preserved or intentionally changed.

## Handoffs

Use `designing-token-taxonomies` to define replacement ownership, `designing-semantic-token-aliasing` for temporary reference chains, `designing-design-system-versioning` for release boundaries, and `designing-design-system-adoption-migrations` for product-level rollout.