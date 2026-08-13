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

## V6 Platform-Native Reconciliation
Record a **native-convention delta** for every deliberate departure from platform expectations—navigation placement, context menus, keyboard shortcuts, window controls, back behavior, selection, share sheets, system dialogs, drag/drop, hover, or gestures. A delta needs a product benefit large enough to pay the learning and interoperability cost.

Audit **system-gesture collision** for edge swipes, browser zoom, scrolling, text selection, OS shortcuts, assistive gestures, and hardware controls. Custom gestures never get exclusive priority merely because they look distinctive. Define a **platform chrome contract** describing ownership of title bars, safe areas, status/navigation bars, browser history, window resizing, keyboard insets, and system overlays. Include explicit **safe-area behavior** for notches, fold/hinge regions, rounded corners, TV overscan where applicable, and on-screen keyboards.

Run a **fallback-parity test** when a platform capability is absent—hover, haptics, pointer precision, native share, biometric auth, GPU effects. The fallback must preserve the product action and essential feedback even if the presentation changes.

### Falsification
Perform the task using only standard platform expectations without tutorial knowledge. Then activate common OS/browser gestures and accessibility settings. If the product traps, overrides, or surprises without a strong reason, platform fit is falsified.

### Recovery
Prefer native behavior, add an alternate input/path, or isolate the unconventional interaction to a bounded expert mode. Do not teach users to fight the operating system.

## V7 Platform Authority Deference
When the target is a named platform, treat its current first-party human-interface guidance and native behavior as a high-authority input for platform convention, input ergonomics, typography/rendering, system motion, haptics, navigation and standard controls. NUI may synthesize across domains, but it must not overwrite platform-embodied craft with a generic cross-platform house style.

Deference is scoped. First-party platform guidance does not automatically own brand expression, product information architecture, domain workflows or web semantics outside the platform. Record where the platform is primary, where local product evidence is primary, and where a custom control earns deviation through a concrete need. Test custom interactions against device geometry and actual input modalities rather than desktop assumptions.

### Falsification
Render the same proposal on a different platform. If no interaction, geometry, typography or motion decisions need reconsideration, platform adaptation is superficial.

### Recovery
Restore native conventions for the failed dimension, document justified deviations, and rerun modality/platform critics on real target conditions.
