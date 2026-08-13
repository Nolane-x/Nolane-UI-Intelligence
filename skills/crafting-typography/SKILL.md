---
name: crafting-typography
description: Use when typography materially affects hierarchy, brand character, reading, scanning, data density, control clarity, localization, or visual distinctiveness.
---

# Crafting Typography

## Overview
Typography is both interface infrastructure and visual voice. It must carry information hierarchy, remain legible under real content, and express the selected direction without turning every string into decoration.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use the aesthetic direction, hierarchy map, content types, density, platform, and localization constraints.

## Define roles before sizes
Typical roles include:
- display/hero
- page/screen title
- section heading
- body/reading
- UI control/label
- data/tabular
- caption/metadata
- code/technical

Not every project needs every role or separate family. Each role must have a purpose.

## Typeface selection
Choose typefaces by:
- character appropriate to product/brand
- readability at required sizes
- width/density behavior
- numeric and punctuation quality
- available weights/styles
- language/script coverage
- rendering/platform availability
- performance/licensing constraints

Do not choose a display face only because it is fashionable. For data-heavy products, numeral alignment, distinguishable glyphs, compact widths, and stable scanning may matter more than a dramatic personality.

## Pairing
Pair by complementary function, not random contrast. Define which family owns expressive voice and which owns sustained reading/control clarity. A utility face may be necessary for dense data or code, but avoid three-family complexity without a real role split.

## Scale and rhythm
Define a type scale with optical rather than purely mathematical relationships. For each role specify size, line height, weight, letter spacing, case, and max measure where relevant.

Large type needs tighter line height/tracking carefully; small UI text usually needs more generous line height and clear contrast. Avoid browser-default 16/14/12 scatter without a system.

## Hierarchy semantics
Size is one channel. Use weight, family, case, color, spacing, and position intentionally. Do not make secondary headings almost as loud as primary titles.

## Data typography
Use tabular numerals where comparison requires vertical alignment. Define decimal/unit treatment and prevent units from being visually confused with values. Negative, estimated, stale, or unavailable values need semantic treatment beyond typography alone.

## Content stress
Test:
- long headings wrapping to 2–4 lines
- narrow controls with translated labels
- all caps in languages/scripts where inappropriate
- very large numbers
- mixed code + prose
- bold accessibility settings
- zoom/reflow

Truncation is an information policy, not a styling trick; specify how full content remains accessible.

## Output: `typography-contract`
Return `families`, `roles`, `type_scale`, `metrics`, `numeric_rules`, `line_length`, `wrapping_truncation`, `script_coverage`, `responsive_type`, `fallbacks`, and `implementation_constraints`.

## Craft checks
- Does type alone reveal the main hierarchy?
- Does the chosen display character originate in the brief/product world?
- Are utility/control labels quieter than content without becoming illegible?
- Does dense information maintain alignment and scanability?

## V5 Computed Legibility and Resolved Typeface Evidence
Route rendered typography through `engineering-visual-legibility`. The microtext budget is explicit: below **11px** requires a semantic reason; below 10px cannot contain required information; below 9px is auxiliary/decorative only. Compound small + low-contrast + uppercase + tracking risk escalates. Prefer browser **computed** evidence over CSS grep. A typeface intention is not rendering proof: record intended family, actual **resolved font**, loading/fallback state, fallback visual delta, relevant numeric/glyph metrics and layout-shift risk.
