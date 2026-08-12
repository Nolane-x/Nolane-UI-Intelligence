---
name: adapting-platform-conventions
description: Use when the same product must behave appropriately across web, iOS, Android, desktop, touch, keyboard, or other platform conventions without losing shared product semantics.
---

# Adapting Platform Conventions

## Overview
Keep product semantics consistent while adapting interaction and presentation to platform expectations. “Universal” must not mean “web UI pasted everywhere.”

## Parent Contract
**Required parent:** `routing-ui-work`.

Use authoritative platform guidance at a higher authority level than community heuristics. Record the exact guidance source when it drives a consequential rule.

## Separate product invariant from platform expression
Examples:
- invariant: user can navigate back without losing draft state
- web expression: route/history/back behavior
- iOS expression: navigation stack/back gesture/button
- Android expression: system back behavior and predictive conventions where applicable

Do not force visual parity when native behavior materially improves comprehension or accessibility.

## Platform dimensions
For each target consider:
- navigation model/back semantics
- menu/context action conventions
- pointer vs touch vs keyboard
- focus model
- window/viewport/safe-area behavior
- system typography and dynamic text
- system colors/high-contrast themes
- alerts/sheets/dialogs/popovers
- drag/drop and context menus
- share/file/permission surfaces
- platform accessibility APIs

## Shared vs adapted tokens
Brand color, semantic intent, and core spacing relationships can be shared while fonts, target sizes, safe areas, elevations, system controls, and motion may adapt. Record the delta rather than branching the whole design system.

## Convention override
Breaking a convention requires a measurable benefit and an alternate learnability/accessibility plan. A custom control that is merely prettier than the native pattern is not enough.

## Cross-platform fidelity
When reproducing a design reference created for one platform, do not copy platform-specific chrome blindly onto another. Preserve the design thesis and product information while translating expected behavior.

## Output: `platform-delta`
Return `product_invariants`, `targets`, `shared_rules`, `platform_overrides`, `native_components`, `custom_exceptions`, `input_models`, `accessibility_deltas`, and `verification_requirements`.

## Common failures
- Hover-dependent mobile controls.
- Desktop shortcut hints shown on touch-only devices.
- Web modal patterns copied into native sheets without back/gesture behavior.
- Identical pixel spacing across platforms when typography/metrics differ.
