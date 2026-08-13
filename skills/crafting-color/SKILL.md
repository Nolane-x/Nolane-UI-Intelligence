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

## V6 Color System Engineering
Work in a **perceptual color space** for palette relationships where tooling permits (for example OKLCH/OKLab), while verifying final sRGB/P3 output. Numeric HSL steps are not perceptually uniform. Define semantic roles first—canvas, surface, elevated surface, content tiers, accent, focus, success, warning, danger, selection, data categories—and then tune appearances.

Check **gamut clipping** and browser/device fallbacks for saturated colors. A wide-gamut accent that clips differently across devices can change hierarchy or semantic distinction. Maintain tested fallbacks rather than assuming modern color syntax is enough.

Audit **simultaneous contrast**: the same token can appear lighter/darker or more/less saturated depending on surrounding fields. Test text/icons against actual local background, gradients, translucent overlays, images and selected/focused states rather than a token table.

Build a **semantic tone ladder** for each role: default, subtle, hover, active, selected, disabled, inverse, high-contrast and dark-theme contexts as needed. Color must not be the sole carrier of state; pair with shape, text, icon, position or pattern according to importance.

Treat **dark-mode inversion** as re-composition, not `L -> 100-L`. Dark fields change perceived contrast, glow, shadow, saturation and surface separation. Re-evaluate elevation, quiet regions, imagery, data colors, focus visibility and text weight in each theme.

For data visualization, separate categorical/diverging/sequential palettes and prove encoding semantics. For brand color, distinguish recognition from overuse: a strong brand hue often gains power when concentrated.

### Falsification
Inspect grayscale, common color-vision deficiencies where relevant, high-contrast mode, low-quality display and ambient-light extremes. Swap background tone while keeping tokens; if hierarchy changes unpredictably, token relationships are under-specified.

### Recovery
When contrast compliance forces visually harsh output, adjust surrounding tone, weight, size or surface relationship rather than simply maxing text to white/black. When an expressive palette compromises data semantics, reserve it for framing and use truthful encoding colors for the data.
