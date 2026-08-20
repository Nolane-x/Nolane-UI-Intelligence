---
name: verifying-responsive-state-parity
description: Verify that responsive representations preserve intended tasks, state, semantics, and recovery even when their visual structure differs substantially.
---

# Verifying responsive state parity

Responsive states are alternate realizations of one product, not separate designs that may drift unnoticed. Use this skill after structural responsive work to prove that users can still perform equivalent tasks and understand equivalent state.

## Decision ownership

Own the parity model, test matrix, acceptable divergences, state-transition checks, and evidence threshold for declaring responsive behavior complete. Decide which outcomes must be identical and which may legitimately differ because modality or platform changes.

## Inputs and evidence

Collect all responsive states, route/task inventory, visible and hidden commands, navigation destinations, form state, errors, selection, sort/filter state, scroll, focus, permissions, loading states, and accessibility semantics. Include intermediate widths and dynamic transitions, not only snapshots.

## Procedure

Build a capability matrix across states. Verify each priority task has a reachable path, each active state remains discoverable, and each recovery action exists. Compare semantics rather than pixels: a command may move into overflow, but its label, enabled state, consequence, and shortcut should remain coherent.

Test transitions with live state. Resize while editing, dragging, loading, viewing an error, or navigating a nested hierarchy. Record intentional divergences with rationale instead of treating them as test exclusions.

Include keyboard and assistive-technology parity alongside pointer/touch behavior.

## Failure topology

Snapshot tests can show visually correct layouts while mobile silently lacks actions. Separate desktop/mobile component trees can drift in validation, analytics, or accessibility. Another failure is state parity without transition parity: each endpoint works, but resizing between them loses focus or data.

A parity checklist can also become too literal and reject sensible modality-specific adaptations.

## Falsification

Run the same task scripts across all composition states and compare outcomes. Force rare states such as partial failure, permission denial, long localization, active filters, and unsaved forms. Resize during those states and verify continuity. Search DOM/accessibility trees for duplicate hidden implementations.

Any missing capability must be explicitly classified as intentional or defect.

## Output contract

Produce a `responsive-state-parity-contract` containing state inventory, capability matrix, state/transition scenarios, accessibility and input coverage, intentional divergence ledger, failure evidence, and exact responsive cases verified before completion.

## Handoffs

Route discovered defects to the specific responsive specialist that owns them, use `engineering-responsive-composition` for systemic state-model problems, and use `designing-ui-regression-evidence` when parity becomes part of ongoing release gates.