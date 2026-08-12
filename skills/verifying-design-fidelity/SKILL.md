---
name: verifying-design-fidelity
description: Use when a coded UI must faithfully reproduce an accepted screenshot, mockup, Figma frame, prototype, visual concept, design system, or other authoritative visual target.
---

# Verifying Design Fidelity

## Overview
Fidelity is a comparison problem. Do not infer visual match from source code, memory, or the fact that the implementation uses the same tokens.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

Require an authoritative target, the current rendered artifact, fidelity level from the UI contract, and available capture/measurement capabilities.

## Freeze the target
Record target identity/revision and which axes are authoritative:
- visible content/copy
- geometry/layout
- typography
- color/surfaces
- imagery/icons
- density/spacing
- component states
- interactions
- responsive views

Do not “fix” mismatch by editing/reinterpreting the target unless the user/design authority explicitly changes it.

## Compare by region and dimension
Partition the surface into stable regions (shell, primary header, navigation, table, inspector, form, etc.). For each compare:
- geometry: position, size, alignment, proportions
- typography: family, size, weight, line height, wrap, tracking
- color: background/surface/text/border/accent/status
- spacing: padding/gaps/gutters/rhythm
- shape: radius, border, shadow, stroke
- assets: crop, focal point, icon metaphor/style
- content: exact visible strings/data where authoritative
- state: selected/focus/hover/loading/error as relevant
- interaction: behavior and transition when target specifies it

## Capture discipline
Bind screenshot evidence to viewport/container size, device scale when relevant, route, state, theme, locale, target, and implementation revision. One desktop screenshot cannot prove mobile fidelity.

## Measurement vs judgment
Use deterministic pixel/geometry/token comparison for what tools can measure. Use independent visual review for composition, optical alignment, crop, hierarchy, and perceptual mismatch that raw pixel diff may overstate/understate.

Pixel diff alone can fail due to font rasterization or animation; screenshot “looks close” can miss systematic spacing/color drift. Use both when fidelity is strict.

## Tolerance
Tolerance comes from the contract. `faithful` allows only implementation/platform constraints that do not change the accepted visual/interaction thesis. `directional` permits larger deltas but must still preserve the declared design system and hierarchy.

## Iteration
Prioritize mismatches by perceptual impact:
1. macro geometry/container
2. typography and major spacing
3. color/surfaces
4. component anatomy/states
5. icons/assets
6. micro optical polish

Do not polish shadows while the layout is proportionally wrong.

## Output: `fidelity-ledger`
Return `target_ref`, `render_ref`, `capture_context`, `regions[] {region, dimension, target_observation, render_observation, delta, severity, evidence, repair}`, `unmeasured_axes`, and `fidelity_decision`.

## Hard stop
If no target render can be inspected, do not claim visual fidelity. Source-level reasoning may prepare implementation but the obligation remains `UNKNOWN/BLOCKED`.
