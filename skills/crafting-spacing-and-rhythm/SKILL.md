---
name: crafting-spacing-and-rhythm
description: Use when spacing, density, alignment rhythm, touch targets, content grouping, or repeated vertical and horizontal intervals materially affect clarity and craft.
---

# Crafting Spacing and Rhythm

## Overview
Spacing is relational grammar. A strong interface uses space to show belonging, hierarchy, pacing, and density—not as arbitrary breathing room.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use IA grouping, layout anchors, typography metrics, task frequency, density target, and platform/touch constraints.

## Establish a base system
Create a compact spacing scale with enough resolution for:
- icon/text gaps
- control internals
- sibling elements
- grouped blocks
- component padding
- section/zone separation

The scale does not need to be mathematically perfect, but repeated relationships should resolve to shared tokens unless content geometry requires an explicit exception.

## Relationship rule
Spacing **within a semantic group** should generally be smaller than spacing **between groups**. If separators/borders are doing all the grouping work, test whether the spacing hierarchy is insufficient.

## Optical correction
Pure numeric equality can look wrong due to glyph shapes, icons, uppercase labels, asymmetric media, or shadows. Allow optical exceptions but record them as component-level adjustments rather than silently corrupting global tokens.

## Density
Density is task-dependent:
- high-frequency expert tools prioritize scan distance and visible context
- reading/marketing surfaces can use larger pacing to establish narrative and focus
- touch contexts need adequate target and separation even if information remains dense

Do not confuse generous spacing with premium design. Excess space can hide relationships and increase navigation cost.

## Vertical rhythm
Align text baselines/line boxes and component intervals so the page has cadence. Long surfaces should alternate meaningful density without random section padding values.

## Edge/gutter behavior
Define stable gutters and safe areas. Components touching viewport edges need platform-aware treatment; centered content should not drift across pages because each section picked a different container width.

## Touch target vs visual size
A control can have a larger hit area than its visible icon. Do not inflate every icon visually just to meet target size; use appropriate interactive padding while preserving proximity between related controls.

## Output: `spacing-rhythm-contract`
Return `spacing_scale`, `relationship_rules`, `component_padding_rules`, `zone_spacing`, `density_target`, `gutter_model`, `touch_target_strategy`, `optical_exceptions`, and `rhythm_checks`.

## Stress checks
Compare sparse vs loaded data, one-line vs multi-line labels, translated text, 200% zoom, touch targets, and repeated rows. The system should remain coherent rather than accumulating one-off margin fixes.

## V5 Expert-Density Pareto Constraint
Expert software may prioritize visible context and short scan distance, but `expert` never implies “everything small”. Optimize information throughput, scanability, aesthetic hierarchy, and emotional power subject to a protected **legibility floor** owned by `engineering-visual-legibility`. Density must be allocated: primary action/information zones may compress while orientation, focal, and monumental/quiet regions preserve breathing room and perceptual rhythm.

## V6 Spacing, Density and Rhythm Mechanics
Define a **density ladder** by task frequency and content type rather than one global compact/comfortable switch. Reading, form entry, dense comparison, command surfaces, touch-first controls and immersive canvases can use different density bands while sharing a coherent spacing grammar.

Establish a **baseline rhythm** where typography and repeated rows benefit from it, but do not force every component to mathematical multiples when optical alignment requires correction. Track major vertical beats—page title to content, section cadence, list rows, table headers, form groups—and the relationships users scan repeatedly.

Apply **optical spacing correction** around asymmetric icons, uppercase labels, rounded shapes, large display type and mixed visual weights. Equal numeric padding can look unequal. Record intentional deviations rather than scattering unexplained literals.

A **touch-target exception** never means tiny hit areas because the visual glyph is small. Separate visual bounds from interactive target, preserve neighboring target separation, and test coarse pointer/mobile safe areas. Dense desktop modes may reduce visual padding but retain keyboard discoverability and minimum interactive precision.

Detect **rhythm discontinuity** where one imported library, empty state, modal or chart introduces a different spacing cadence. These discontinuities often reveal cross-source collage before color does.

### Falsification
Overlay alignment/baseline guides and then remove them: can users still perceive coherent grouping, or is the grid doing mathematical work without perceptual benefit? Stress long labels, error messages, translated text, zoom and dense real data. If rhythm survives only ideal demo content, it is not robust.

### Recovery
When screens feel cramped, identify whether the problem is local padding, information architecture or too many simultaneous controls; increasing every gap can destroy density without fixing comprehension. When screens feel empty, strengthen grouping/content hierarchy before filling space decoratively.
