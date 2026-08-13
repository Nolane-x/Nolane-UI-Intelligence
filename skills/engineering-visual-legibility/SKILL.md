---
name: engineering-visual-legibility
description: Use when typography, density, expert-tool pressure, or responsive rendering can push text and glyphs below a protected legibility floor.
---

# Engineering Visual Legibility

## Parent Contract
**Required parent:** `crafting-typography`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own executable legibility evidence from rendered/computed styles and resolved font behavior. Do not choose the typographic personality; crafting-typography owns that.

## Product Truth
Expert user does not imply tiny text. Source CSS intent is weaker evidence than the browser's resolved result. A nominal font family that falls back on another machine is not a proven typeface decision.

## Decision Model
Apply a microtext budget: below 11px requires a semantic reason; below 10px cannot carry required information; below 9px is decorative/auxiliary only. Escalate compound risk when small text also has low contrast, uppercase transformation, or tracking. Audit computed styles rather than regex counts when browser evidence exists. For fonts capture intended family, actual resolved family, loading state, fallback visual delta, numeric metrics where critical, x-height/width considerations, glyph coverage, and CLS/layout-shift risk. Optimize expert density as a Pareto problem: information throughput, scanability, aesthetic hierarchy, and emotional power subject to a protected legibility floor.

## Evidence
Return representative computed samples across important roles/breakpoints plus resolved-font evidence. Required information under 10px is a blocking finding regardless of how technically sophisticated it looks.

## Output Contract: `visual-legibility-evidence`
Return the canonical `visual-legibility-evidence` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
Using px grep as the only audit; expert⇒small; accepting 8px because it fits more data; low contrast + uppercase + tracking compounding; declaring a font choice from CSS stack only; fixing microtext by globally enlarging everything without rebalancing hierarchy.

## V6 Rendered Legibility Engineering
Legibility is a rendered-system property. Record a **reading-distance context** for each surface: handheld near-field, desktop working distance, ten-foot TV, vehicle glance, wearable, spatial/XR or high-density control room. The same CSS size does not imply the same perceptual adequacy.

Capture computed typography and a **resolved-font delta**: intended family/weight/style/axis versus actual rendered font; fallback metrics; x-height, width and numeral changes; layout shift; missing glyph/script substitution. A nominal 12px label rendered in a different fallback face may become materially harder to scan even when source CSS is unchanged.

Model **compound legibility risk**. Small size, low luminance contrast, thin weight, uppercase, tracking, translucency, motion, blur, dense background, narrow line-height and compression amplify one another. Do not test each factor independently and declare PASS. Record the stack and escalate when several weak signals coincide.

Run a **zoom-reflow probe** at relevant browser/platform text scaling, not only viewport resizing. Inspect clipping, lost controls, overlap, fixed-height containers, truncation policy, visual-order/DOM-order divergence and whether data relationships survive reflow. Perform an **occlusion audit** for sticky bars, floating actions, popovers, tooltips, virtual keyboards, safe areas and system UI.

Measure scanning roles: primary task text, controls, metadata, data values, annotations and decoration must have intentional legibility tiers. The v5 microtext floor remains a guardrail, not a target. Dense expert UI earns density through alignment, grouping, predictable rhythms and information compression—not through making everything tiny.

### Falsification
Swap the intended typeface for the actual fallback and capture the rendered surface; if hierarchy or density changes materially, the type contract is unresolved. Test grayscale/low-quality display, long locale strings, large text and high-contrast mode. A design that is only legible on the designer's calibrated monitor is falsified.

### Recovery
If visual ambition depends on illegible micro-detail, relocate expression into scale, material, imagery, motion or composition. If zoom/reflow destroys the information model, return to layout architecture rather than patching font sizes. If the resolved-font delta is large, repair loading/subsetting/fallback metrics before aesthetic critique continues.
