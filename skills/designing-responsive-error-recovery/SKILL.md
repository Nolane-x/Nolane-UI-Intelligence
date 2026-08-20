---
name: designing-responsive-error-recovery
description: Preserve error explanation, affected context, and recovery actions when responsive layouts collapse, reorder, or hide regions.
---

# Designing responsive error recovery

Errors become especially confusing when the control or content they refer to moves across responsive states. Use this skill when validation summaries, banners, inline errors, failed panels, or recovery commands must remain connected to their targets under reflow.

## Decision ownership

Own cross-state placement of error messages, visibility of affected controls, recovery-action priority, summary-to-target navigation, and preservation of error state during layout transitions. Decide what happens when the errored region would normally collapse or move into overflow.

## Inputs and evidence

Collect error types, target controls, current placement, responsive hiding rules, validation summaries, asynchronous retries, permissions, and recovery actions. Include long server messages and multiple simultaneous errors.

## Procedure

Give active error state priority over ordinary responsive collapse. If a hidden region contains the failing control, surface a visible indicator and a route to reveal it. Keep summaries linked to target fields or sections even after reordering. Ensure retry or corrective actions do not disappear into low-priority overflow.

Preserve errors across resize without duplicating announcements. If the presentation changes from inline to summary, manage assistive-technology announcements intentionally rather than remounting both versions.

## Failure topology

Responsive collapse can hide the only explanation for disabled progress. A validation summary may focus a field that is inside a closed drawer. Another failure is duplicate live-region announcements when desktop and mobile error components coexist invisibly.

Error banners can consume most of a short viewport and cover the control needed for recovery.

## Falsification

Trigger errors before and during resize. Navigate from summaries to targets at each state. Test hidden panels, overflowed actions, multiple errors, keyboard, screen reader, and virtual keyboard. Verify recovery actions remain available and announcements occur once with meaningful context.

## Output contract

Produce a `responsive-error-recovery-contract` containing error-priority rules, target visibility, summary navigation, action placement, announcement behavior, active-state exceptions to collapse, and resize tests with unresolved errors.

## Handoffs

Use `designing-field-validation-and-error-recovery` for field semantics, `designing-partial-failure-states` for distributed failures, `designing-responsive-priority-collapse` for active-state overrides, and `verifying-responsive-state-parity` for recovery equivalence.