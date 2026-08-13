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

## Output: `finding-set`
Return typed findings with target platform, convention/source, observed behavior, user cost, product benefit if any, and repair direction. Separate `platform-defect` from `intentional-cross-platform-brand-choice`.

## V6 Platform Fit Critic
Search for a **platform-affordance mismatch**: controls that look native but behave differently, web metaphors transplanted into touch/TV/XR without adaptation, desktop hover dependencies on mobile, or mobile sheets used where windowed desktop expects persistent context. Keep a **convention-cost ledger** for each intentional deviation: user benefit, learning cost, compatibility cost, accessibility cost, and fallback.

Audit the **system-integration gap** around sharing, file pickers, notifications, permissions, back/history, window management, keyboard, clipboard, drag/drop, safe areas, install/update, and platform accessibility settings. Check **input-modality conflict** when one platform exposes several inputs; keyboard focus, touch target behavior, pointer hover, gamepad/remote navigation, voice, or gaze cannot contradict the same action.

Seek a **platform-native counterexample**: an authoritative first-party or mature native implementation of a comparable interaction. The goal is not to copy it, but to test whether the custom design pays its departure cost.

### Falsification
Give the UI to a platform-expert user without product-specific training and test system back, standard shortcuts/gestures, resizing, accessibility settings, and interruption. Repeated surprise falsifies “platform fit.”

### Recovery
Prefer native primitives or conventions where they solve the same product problem; where divergence is essential, expose clearer cues and fallback paths and document the reason as a bounded exception.
