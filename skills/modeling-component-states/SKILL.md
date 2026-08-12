---
name: modeling-component-states
description: Use when components or flows can change interaction, validation, async, permission, content, viewport, theme, locale, or accessibility state and those combinations can alter behavior or presentation.
---

# Modeling Component States

## Overview
A component is not its default screenshot. State modeling prevents beautiful static UI from collapsing under real data and interaction.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume component semantics and interaction contracts. Derive only applicable states; do not create a ceremonial matrix of states that cannot occur.

## State algebra
Consider dimensions independently:
- interaction: idle, hover when applicable, focus, pressed, selected, dragged
- availability: enabled, disabled, read-only, permission-denied
- validation: pristine, invalid, warning, valid
- async: idle, pending, queued, streaming, success, partial, failure, cancelled, stale
- content: normal, empty, long, truncated, unknown, skeleton/placeholder only when justified
- environment: narrow/wide viewport, pointer/touch/keyboard, light/dark/high-contrast, reduced motion
- locale: short, expanded, RTL, non-Latin typography

The matrix is the cross-product **only where dimensions interact materially**. Avoid combinatorial noise.

## State invariants
Record rules that must hold across states. Examples:
- label meaning does not change when disabled
- selection remains perceivable while focused
- pending action cannot be accidentally committed twice
- error message stays associated with the control it describes
- responsive transformation preserves the same semantic action
- theme changes do not make status depend on color alone

## Transition model
For critical components specify allowed transitions and triggers. A state that appears in the design but has no transition into or out of it is likely decorative rather than behavioral.

## Geometry stress
State changes often change size. Test error text, loading labels, translated content, selected icons, count growth, and validation help. Prevent layout jumps that move the action target under the pointer or hide the user’s context.

## Disabled-state challenge
Do not disable controls without explaining the unavailable condition when users need to know how to proceed. Sometimes a visible enabled action that returns an actionable permission/validation explanation is better than an unexplained disabled surface.

## Output: `component-state-matrix`
Return `component`, `dimensions`, `applicable_states`, `material_combinations`, `transitions`, `invariants`, `geometry_stress_cases`, `unreachable_states`, and `verification_requirements`.

## Completion rule
A component family cannot be considered specified when a material state is known to exist but its behavior, semantics, or visual treatment is omitted. Mark it `UNKNOWN` and keep the obligation open.
