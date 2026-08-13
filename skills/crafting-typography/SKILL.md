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

## V6 Typographic Engineering and Art Direction
Typography decisions start from reading behavior and glyph geometry. Make an **optical-size decision** for display and text roles: if a variable font exposes `opsz`, determine whether automatic or explicit optical sizing improves stroke contrast, spacing and detail at the rendered sizes. Do not assume one master behaves equally from 10px UI text to 96px display type.

Compare **x-height and width** against the target density, not only font-size. High x-height can increase small-size presence but alter texture; narrow families can save horizontal space while harming word shape or multilingual readability. Inspect cap height, ascenders/descenders, punctuation, ambiguous glyphs, numeral styles, tabular widths and math/code symbols where relevant.

Build a **script stress matrix** covering all material scripts/locales and stress cases: long Latin labels, RTL, CJK, Thai/complex shaping, Indic, mixed-script technical strings, localized numerals and fallback glyphs. Record family coverage, fallback family, metric mismatch and whether expressive roles survive script changes.

Treat **line-box geometry** as layout infrastructure. Specify line-height by role; inspect baseline alignment between icons/text, inline code, superscripts/subscripts, mixed fonts, multi-line controls and text zoom. For reading surfaces include measure, paragraph spacing, rag, hyphenation and orphan/widow behavior when platform support permits.

Plan font delivery and a **font-loading failure** state: preload/subset strategy, variable versus static files, fallback metrics, `font-display`, late swap risk and offline behavior. A beautiful type system that collapses or shifts during load is not finished.

Use hierarchy channels deliberately—family, weight, width, size, case, tracking, color and spacing. Avoid using all channels at once. Data typography requires tabular numerals where comparison matters, stable decimal/unit alignment, signed/estimated/stale-value treatment and sufficient differentiation between `0/O`, `1/l/I` where domain risk warrants it.

### Falsification
Render the most difficult content with the actual resolved fonts, target scripts, 200% text scaling and narrowest supported width. Remove color and inspect whether type hierarchy still carries structure. If the expressive family disappears in a key script and the product identity collapses, the pairing is not globally valid.

### Recovery
When density fails, first improve width, hierarchy, grouping and information policy before shrinking text. When font loading/coverage is unreliable, prefer a stronger available family or narrow expressive use to roles that can be safely substituted. Typography never gets to hide required information behind truncation without a full-content path.

## V7 Rendered Type Proof
Typography decisions are incomplete until the intended face survives actual loading, fallback, content length, viewport and script conditions. Add a rendered-type evidence row for each material role: intended family/axis/weight, resolved family, loading state, fallback path, observed line breaks, density effect, and any change to hierarchy or brand character.

For high-ambition work, type must do more than avoid illegibility. Identify what role carries personality, which roles remain quiet, how width/weight/optical size alter composition, and how the hierarchy survives when display text wraps. Treat upstream typography systems as concrete evidence only within their scope; a platform type convention may outrank an aesthetic preference, while a reference font pairing is merely exploratory until local language coverage and rendering are proven.

### Falsification
Force the first fallback, narrow the viewport, and replace copy with a longer localized string. If hierarchy or signature collapses, the type system was designed as a screenshot.

### Recovery
Adjust role scale, metrics, fallback stack, width/measure, or font selection and capture fresh resolved-font evidence.
