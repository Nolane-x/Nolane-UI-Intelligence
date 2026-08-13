---
name: crafting-color
description: Use when color must encode hierarchy, brand, state, theme, trust, accessibility, surfaces, or data without becoming decorative noise or the sole carrier of meaning.
---

# Crafting Color

## Overview
Color is a semantic system plus atmosphere. Build roles first, values second.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use aesthetic direction, hierarchy, accessibility constraints, theme requirements, data/status semantics, and platform context.

## Color role model
Define roles such as:
- canvas/background
- surface levels
- primary/secondary text
- subtle text
- borders/dividers
- interactive accent
- focus indicator
- selection
- destructive/danger
- warning
- success
- informational
- data series/categories
- decorative/brand accents

A single color may serve multiple roles only when the semantics remain unambiguous.

## Palette construction
Start from perceptual relationships: lightness hierarchy, chroma budget, warm/cool balance, contrast, and theme character. Prefer color spaces/tools that preserve perceptual reasoning when available (for example OKLCH) while validating actual rendered contrast in the target environment.

Do not blindly generate evenly spaced hue ramps; semantic colors need to work against their actual surfaces and states.

## Chroma budget
Highly saturated color attracts attention. Spend it on brand signature, primary action, live state, or meaningful data—not simultaneously everywhere. A calm product may use rich color only at decision points; an expressive product can use broader color but still needs hierarchy.

## State semantics
Never depend on color alone for status, error, selection, required fields, or interactive affordance when users need the distinction. Combine text, iconography, pattern, shape, position, or semantic markup as appropriate.

## Dark themes
Dark mode is not palette inversion. Define surface separation, text luminance, border visibility, focus, elevation, image treatment, and saturated-color behavior separately. Large luminous areas can dominate far more on dark backgrounds.

## Contrast
Contrast is a deterministic obligation where standards define it. Do not eyeball. Treat disabled/decorative exceptions carefully; avoid making important secondary information so muted that it becomes functionally unavailable.

## Data visualization
Reserve categorical/ordinal/sequential/diverging palettes according to data semantics. Ensure adjacent/important series remain distinguishable beyond hue where necessary. Status colors and chart-series colors should not collide semantically.

## Output: `color-contract`
Return `color_roles`, `palette`, `semantic_mappings`, `surface_model`, `theme_deltas`, `contrast_obligations`, `non_color_cues`, `data_palette_rules`, `chroma_budget`, and `forbidden_ambiguities`.

## Common failures
- Muted gray used for essential explanatory text.
- Red means both destructive action and ordinary chart series.
- Accent applied to every icon and heading.
- Dark theme uses black + neon by default regardless of product character.
- Gradient added because “AI product” rather than a compositional/brand reason.

## V5 Visual Energy Counterweight
A chroma ceiling is not an aesthetic objective. For high affective targets, route `directing-visual-energy` and ask whether **restraint** has collapsed expressive range. Inspect luminance range, **chroma mass**, focal color mass, depth contrast, material variation, and warm/cool tension where relevant. High visual energy does not mean “more saturated”; monochrome can pass if other perceptual mechanisms create sufficient tension, hierarchy and emotional force. The evidence must be relative to experiential intent.
