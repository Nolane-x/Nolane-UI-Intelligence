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

## V6 Fidelity Evidence Model
Construct an **authoritative-target graph** before comparing implementation: design file, accepted rendered reference, token contract, content fixture, interaction/state specification, platform rule, and user-approved deviations each have different authority. A screenshot alone cannot override semantics or dynamic behavior.

Separate **semantic-versus-pixel invariant** classes. Pixel geometry, typography, spacing, color, and imagery can be compared visually; interaction state, responsive relationships, focus, accessibility, localization, data semantics, and motion require behavioral evidence. Verify **dynamic-state parity** across hover/focus/pressed/disabled/loading/error/empty/selected/expanded/permission and relevant motion states rather than comparing only the default screenshot.

Lock comparison conditions with a **font-and-viewport lock**: resolved font files/fallback state, viewport/container size, DPR/zoom, OS/browser rendering context, content fixture, theme, and animation clock. Run a **diff false-positive audit** for antialiasing, subpixel rendering, nondeterministic data, timestamps, caret/blink, GPU effects, and dynamic ads/assets before accepting image-diff noise as a defect.

### Falsification
Deliberately introduce one semantic regression with nearly identical pixels and one harmless pixel-level rendering variation. If the verifier flags only the latter, its fidelity model is falsified.

### Recovery
Use the appropriate evidence class for each invariant, normalize nondeterminism, and reopen implementation only on authoritative mismatches. Never chase screenshot pixels at the expense of correct behavior.

## V9 Design-to-Render Fidelity
Treat implementation as a translation chain: **design intent → semantic tokens → component constraints → platform/CSS expression → runtime render → visual regression evidence**. Every link can degrade quality. A correct mockup plus approximate CSS is not fidelity; a perfect token file plus components that ignore state/density is not fidelity; a clean default screenshot plus broken browser chrome or responsive states is not fidelity.

Audit token resolution at rendered scale: font family/fallback, optical size where relevant, font weight, line-height, tracking, spacing, radius, border opacity, elevation, status colors, density and motion. Look for “almost right everywhere” drift—e.g. one line-height too loose, borders too opaque, shadows too hard, every radius too large, or spacing tokens applied mechanically where optical correction is required. Repeated small deviations can change perceived quality more than one obvious local bug.

Inspect **default chrome** explicitly. Browser/OS controls are not defects merely because they are native; they are defects when their appearance or behavior is accidental and visually/semantically incompatible with the product. Audit scrollbar, select, file input, date/time/number/range controls, focus ring, text/object selection, caret, resize handles, drag ghost, validation UI, context menu, tooltip/popover, cursor and overscroll. Each receives an intentional strategy: native and appropriate, styled, adapted, overlay/reveal, or custom with equivalent semantics.

For the user's scrollbar class of defect, never adopt the simplistic rule “hide all scrollbars.” Verify scroll ownership, pointer/touch/keyboard/wheel operability, platform preferences, discoverability and contrast. A themed or reveal-on-interaction scrollbar may improve material coherence; a native scrollbar may be the correct platform expression; a hidden scrollbar without an equivalent visible/operable affordance can be worse than the original visual mismatch.

Bind responsive implementation to rendered evidence. Check real wrapping, min-content/max-content behavior, sticky/fixed regions, tables, panels, canvas/timeline regions, overlays, safe areas, software keyboard, localization and browser zoom. CSS breakpoints are implementation hypotheses; the final criterion is whether hierarchy and required capability semantics survive the rendered state.

Require **visual regression** evidence for material changes. Use deterministic screenshot comparison to locate geometry/style drift, then independent visual review to decide whether the delta is harmful. Preserve accepted deltas explicitly. Do not let a low pixel-diff percentage certify typography quality, motion, focus behavior or interaction correctness.

### V9 Falsification
Introduce one accidental browser-default control into a polished surface, one subtle systematic spacing/type drift, and one harmless antialiasing difference. If the fidelity process ignores the first two or blocks on only the harmless pixel noise, the implementation-quality model is wrong.

### V9 Recovery
Fix the earliest causal layer that owns the drift: token, component, CSS/platform expression or runtime state. Re-capture the same state and viewport, compare against the target/baseline, and retain both semantic runtime probes and screenshot evidence. Do not patch individual pages around a systemic token/component defect.

## V10 Runtime Fidelity Attribution
Two V10 hypotheses touch this owner and must remain distinct. `H-RENDER-FIDELITY` asks whether tracing intent through tokens/components/runtime catches implementation drift that design-file inspection misses. `H-RESIDUE-INTENTIONALITY` asks whether low-level browser/platform surfaces become deliberate without turning “native” into a defect category. In both cases, **artifact evidence is not efficacy evidence**.

For `H-RENDER-FIDELITY`, preserve an evidence chain for each material mismatch:

`accepted intent → token or component contract → computed/runtime state → rendered observation → consequence → repair owner → recaptured state`

The mutation `fidelity-design-file-only` removes runtime and visual-regression evidence. The `render-fidelity` ablation removes the V9/V10 fidelity plane. Full NUI should then detect more consequential font fallback, wrapping, state, overlay, theme, responsive and implementation-drift failures than those controls, without inflating harmless renderer noise into failures.

For `H-RESIDUE-INTENTIONALITY`, record each low-level surface with `semantic_role`, `platform_expectation`, `appearance`, `intentionality`, `treatment`, `operability_evidence`, and `render_ref`. The mutation `residue-default-accept` ignores this decision class. Full NUI should catch accidental default/legacy residue in authored products **and** preserve platform-native controls when native appearance is intentional, accessible and coherent. A benchmark that rewards customization count is invalid.

### V10 false-positive controls
Every empirical fidelity study should include at least one harmless rendering variation—antialiasing, platform font rasterization, subpixel position or another declared environment difference—and at least one semantically meaningful near-pixel-identical defect. This checks whether the verifier distinguishes perceptual/behavioral importance from raw image difference.

Responsive fidelity uses a related counterfactual: `responsive-shrink-only` should fail when structure and capability access need reauthoring, but a fixed-size or externally constrained surface should not be penalized for remaining structurally stable. The evaluator scores semantic continuity and rendered hierarchy, not breakpoint count.

### V10 claim boundary
A faithful implementation under full NUI proves facts about that implementation. To claim this skill **caused** better fidelity, run the same task/model/runtime/tool budget under baseline, full and targeted ablation/mutation; bind comparisons to exact renderer/environment evidence; retain failures/timeouts; and require targeted degradation with no hard accessibility/function regression. Repository validators, screenshot existence, or a low visual diff alone leave the efficacy state at `STRUCTURAL_ONLY`.
