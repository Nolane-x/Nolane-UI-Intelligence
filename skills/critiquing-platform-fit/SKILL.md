---
name: critiquing-platform-fit
description: Use when an independent reviewer must evaluate whether a UI preserves product semantics while respecting the interaction, navigation, input, system, and accessibility conventions of its target platform.
---

# Critiquing Platform Fit

## Overview
Review platform adaptation by user cost. Pixel similarity across platforms is not inherently good; arbitrary custom behavior is not inherently innovative.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

`may_modify: false`. Use the platform delta, authoritative platform guidance, product invariants, and inspectable implementation.

## Review questions
- Does back/navigation behavior match user expectations and preserve product state?
- Are system/native patterns replaced with custom controls without a real benefit?
- Do pointer, keyboard, touch, context-menu, gesture, and window conventions behave appropriately?
- Are safe areas, dynamic type/text scaling, system themes, focus, and accessibility APIs respected where relevant?
- Does a cross-platform component preserve semantic meaning even when presentation differs?
- Are platform-specific actions (share, file, permissions, selection, menu) integrated coherently?

## Convention severity
A deviation is a finding only when it creates learning cost, task failure, accessibility loss, destructive ambiguity, or maintenance inconsistency relative to the product benefit. “Not native-looking” alone is not sufficient.

## Cross-platform translation
When a source design comes from another platform, judge whether the implementation preserved the thesis and information hierarchy while translating platform behavior. Do not demand foreign platform chrome for visual fidelity unless the contract explicitly requires a literal simulation.

## Output
Return typed findings with target platform, convention/source, observed behavior, user cost, product benefit if any, and repair direction. Separate `platform-defect` from `intentional-cross-platform-brand-choice`.
