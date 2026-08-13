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

## V6 Component API Evolution Protocol
Before changing a shared component, build a **compatibility matrix** across existing props/slots/events, semantic states, keyboard/accessibility behavior, tokens, responsive modes, and supported frameworks/platforms. Distinguish source compatibility, runtime behavior compatibility, and visual compatibility; they can break independently.

Construct a **consumer impact graph** from the component to high-traffic and high-risk consumers, wrappers, variants, documentation examples, visual tests, and downstream design-system packages. A low-use prop may still be critical if it encodes destructive confirmation or accessibility behavior. Make an explicit **semantic-version decision** based on observable consumer breakage, not implementation diff size.

Assess **codemod feasibility** for mechanical migrations: renamed props, variant mapping, import changes, token aliases, anatomy shifts. Codemods cannot repair changed product semantics; those require human/agent review. Define a **deprecation exit test** with telemetry/search evidence, migration docs, deadline, fallback behavior, and proof that supported consumers no longer rely on the old contract before removal.

### Falsification
Run representative old consumers against the proposed API and intentionally exercise uncommon states. If the change appears source-compatible but changes focus, labeling, state timing, or visual hierarchy, the “non-breaking” claim is falsified.

### Recovery
Add an adapter/compatibility layer, split the new semantic concept into a separate component, or postpone removal. Never keep ambiguous dual behavior forever merely to avoid a major version.
