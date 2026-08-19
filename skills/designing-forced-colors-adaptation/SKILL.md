---
name: designing-forced-colors-adaptation
description: Use when system-enforced color palettes or high-contrast modes can replace authored colors and the interface must preserve controls, boundaries, focus, selection, and state meaning.
---

# Designing Forced Colors Adaptation

## Parent Contract
**Required parent:** `designing-low-vision-and-high-contrast`.

This faculty owns behavior when the platform overrides authored colors. It distinguishes visual brand styling from state cues that must survive replacement by system colors. It does not prescribe a dark theme or ordinary contrast palette; forced-colors mode is an authority change in which many CSS colors cease to be under product control.

## Decision Boundary
Audit every state whose meaning depends on fill, border, shadow, gradient, or background image. Determine how focus, selection, pressed state, disabled state, links, inputs, icons, and data markers remain distinguishable when those authored colors are mapped to system values. Prefer semantic system participation over globally opting out of forced adjustment. Selective preservation is justified only when an essential visual asset would otherwise become uninterpretable and an accessible equivalent still exists.

Transparent borders and box shadows often disappear as meaningful separators; controls may need real borders or outlines in forced palettes. SVG icons should inherit usable current color where appropriate rather than bake brand colors into every path. Do not rely on a white page assumption when system canvas and text colors can invert.

## Failure Topology
- Selected and unselected items become identical because selection was encoded only with a background fill.
- Focus rings disappear after their authored color maps to the same system color as the surface.
- An icon retains a hard-coded dark fill on a dark system canvas.
- `forced-color-adjust: none` is applied to broad containers, defeating user color preferences.
- Charts collapse into indistinguishable series because all meaning was color-only.
- Input boundaries were shadow-only and vanish, making fields impossible to locate.

## Falsification and Recovery
Run the product in actual forced-colors/high-contrast environments and inspect interactive states, not just static screenshots. Navigate keyboard focus, selection, validation, disabled controls, menus, charts, and overlays. The design fails when system color replacement removes action boundaries or semantic distinctions even if text remains technically visible.

Recover by adding non-color geometry, system-color-compatible borders/outlines, current-color icons, state markers, and narrowly scoped opt-outs only where required. Re-test hover/focus/selected combinations because forced palettes expose collisions hidden in ordinary themes.

## Output Contract
Return `forced-colors-contract` with affected component/state inventory, system-color adaptation rules, non-color fallback cues, icon/SVG policy, permitted opt-outs, chart/data adaptations, and platform high-contrast verification cases.
