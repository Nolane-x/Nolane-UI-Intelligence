---
name: crafting-depth-and-surfaces
description: Use when borders, elevation, shadows, translucency, blur, layers, panels, cards, or material treatment need to communicate hierarchy, interaction, or brand without over-framing the interface.
---

# Crafting Depth and Surfaces

## Overview
Depth is a model of layering and containment, not a bag of shadows. Every surface boundary should communicate something.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use composition, hierarchy, component semantics, theme, and platform conventions.

## Define the layer model
Name the product’s actual layers, for example:
- canvas/background
- primary working surface
- bounded object/panel
- raised interactive overlay
- modal/system interruption
- transient tooltip/menu

Do not create 5 elevation tiers because a design system template has 5 values. Create only tiers with semantic meaning.

## Boundary choice
Choose among whitespace, tonal surface, border, shadow, inset, translucency, or overlap based on:
- containment strength needed
- separation from background
- interaction/layering expectation
- scroll ownership
- theme contrast
- brand/material direction

Using border + shadow + tinted background + radius simultaneously often overstates hierarchy.

## Cards
A card is valid when it represents a bounded object/group, repeated selectable unit, media object, or meaningful container. It is not the default wrapper for every paragraph or metric.

For data comparison, card boundaries may reduce alignment; a table/list can be more truthful.

## Elevation
Elevation should correspond to overlap or interaction priority. Hover elevation must not imply clickability on a non-interactive surface. Selected state should not rely only on stronger shadow if selection semantics need a clearer cue.

## Translucency/glass
Use when the layered context behind the surface is part of the experience and readability remains robust. Blur/transparency that merely signals “futuristic” is decorative cost. Define fallback for reduced transparency/high contrast/platform constraints when relevant.

## Shadows
Specify purpose: edge separation, floating layer, focus, ambient material, or brand. Keep light direction/softness consistent. Dark themes may need subtle borders/tonal separation more than large black shadows.

## Output: `surface-contract`
Return `layer_model`, `surface_tokens`, `boundary_rules`, `elevation_rules`, `card_criteria`, `overlay_rules`, `transparency_policy`, `theme_behavior`, and `anti_nesting_limits`.

## Anti-nesting check
If a surface contains another surface with equal visual strength, ask which one owns the semantic boundary. Flatten until the hierarchy is legible unless nested ownership is real (for example window → panel → selected object).

## V5 Global Material Quality Gate
Local border correctness can still create global border soup. Inspect **boundary density**, edge density, surface entropy, boundary repetition, **material variety**, and **quiet region** ratio across the rendered surface. If the whole product is divided by the same hairline/pane mechanism, flatten, open space, or introduce semantically different containment/material behavior even when no individual border violates a local rule. Do not replace card soup with pane soup.

## V6 Surface and Depth Material System
Define a **material hierarchy**: base field, embedded region, raised interactive layer, transient overlay, modal boundary, tooltip/popover and any domain-specific canvas/material. Each level needs a semantic reason; elevation is not a reward for being a card.

Maintain **light-model consistency** when shadows/highlights imply physical depth. Direction, softness, spread and ambient lift should relate across the system unless a deliberate luminous/material effect breaks physical metaphor. Random shadow recipes make the product feel assembled.

Assign **occlusion ownership**. Every overlay declares what it may cover, how focus/input is constrained, whether underlying content remains contextually visible, and how dismissal/restoration works. Visual depth and interaction depth must agree.

Track a **boundary-density budget** across the whole viewport: borders, separators, outlines, surface color changes, shadows and padding all create boundaries. Replacing cards with bordered panes can preserve the same “box soup” at a different radius. Use grouping/negative space and content alignment where possible.

Treat translucency as a material with information risk. A **transparency failure** occurs when background variability reduces text/control legibility, when blur is expensive, when stacked transparent layers muddy hierarchy, or when glass becomes generic style rather than semantic depth.

### Falsification
Remove all shadows while preserving surface colors/borders; then remove borders while preserving spacing. Which boundaries are actually necessary for comprehension and interaction? Test bright/dark backgrounds behind translucent layers and low-power devices for blur/rendering cost.

### Recovery
If depth semantics are unclear, simplify to fewer material levels. If the product needs richness, deepen texture, lighting, media and large-scale material contrast at meaningful regions rather than surrounding every component with another container.
