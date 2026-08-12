---
name: evolving-component-apis
description: Use when a shared UI component changes props, variants, semantics, keyboard behavior, DOM/accessibility contract, visual states, tokens, composition model, or migration path across multiple consumers.
---

# Evolving Component APIs

## Overview
A component API is a behavioral contract, not just prop names. Evolve semantics, interaction, accessibility, and theming with explicit compatibility and migration so local products do not silently break or fork.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require current API/behavior, consumer inventory, semantic role, variants/states, accessibility contract, token dependencies, target change, version policy, and migration capability. Coordinate with design-system governance for shared releases.

## Decision Model
Classify change impact: additive compatible, behavior-changing compatible with opt-in, deprecating, or breaking. A visual default can be behavior-breaking if it alters hierarchy, target size, contrast, focus, or layout. A prop rename can be minor mechanically but breaking operationally across hundreds of consumers.

Keep semantic APIs small. Prefer intent props (`tone="danger"`, `status="error"`) over raw styling switches that let consumers construct invalid combinations. Prevent variant explosion by composing primitives or slot patterns when the semantic combinations are truly independent.

For interaction components, document state machine and accessibility behavior as part of API: focus entry/return, keyboard keys, selection semantics, disabled/read-only, async/loading, validation, and announcements. Changes to any of these require behavioral tests and release notes even if screenshots look identical.

Plan migration: codemod where mechanical, compatibility layer where behavior can transition, warnings with removal version, examples of old/new intent, and detection of unsupported combinations. Do not keep deprecated behavior forever without cost review.

## Evidence
Run consumer tests, visual/semantic snapshots, keyboard/a11y behavior, theme/localization, API type tests, migration dry-runs, and usage analysis. Review real consumer edge cases before removing escape hatches. Validate that new API eliminates a problem rather than only becoming more elegant internally.

## Output Contract
Return a `component-migration-contract` with `change_class`, `old_contract`, `new_contract`, `semantic_invariants[]`, `behavioral_deltas[]`, `affected_consumers`, `compatibility_strategy`, `deprecation_timeline`, `migration_steps[]`, `automatable_changes[]`, `manual_review_cases[]`, and `release_tests[]`.

## Failure Traps
- Calling a focus/keyboard change “visual only.”
- Dozens of boolean props that permit impossible combinations.
- Minor release silently changing default spacing enough to break layouts.
- Deprecation with no replacement path or removal date.
- Codemod changing syntax but not semantic intent.
- Keeping legacy prop forever because migration was never measured.
- New API optimized for library authors rather than consumer tasks.

Component evolution is successful when product teams can upgrade without relearning hidden semantics.