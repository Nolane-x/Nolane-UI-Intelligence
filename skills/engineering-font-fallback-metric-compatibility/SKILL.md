---
name: engineering-font-fallback-metric-compatibility
description: Use when fallback and final fonts need compatible advance widths, x-height, ascent, descent, and line metrics so font substitution does not materially reflow or shift the interface.
---

# Engineering Font Fallback Metric Compatibility

## Geometry Before Resemblance
A fallback face need not look identical to the final font, but its metrics must be close enough that the interface remains stable and readable. This skill owns metric compatibility: how fallback candidates are measured, normalized, and adjusted so substitution preserves line breaks, control size, and vertical rhythm within declared tolerances.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent owns typographic art direction. This specialist treats fallback as a runtime geometry problem and does not choose a face merely because it has a similar mood.

## Metric Contract
Inventory average and representative glyph advances, x-height, cap height, ascent, descent, line gap, weight mapping, and punctuation/numeric widths for the content actually used. Browser adjustment mechanisms may compensate size, ascent, descent, or line gap, but every adjustment must be evidenced against the final face. One global scale factor is rarely sufficient for both body prose and dense numeric UI.

Define tolerances by task. A paragraph may tolerate a small line-wrap shift; a tabular dashboard or two-line button may not. Preserve enough vertical metrics that focus rings, clipping, inline icons, and baseline relationships remain valid.

## Evidence Strategy
Use representative strings rather than alphabet-only samples: long localized labels, numbers, dates, punctuation, mixed case, and high-frequency product terms. Compare line breaks and bounding boxes under fallback and final fonts at several widths. Record actual resolved faces to avoid measuring a fallback that the target platform never selects.

## Failure Modes
Failure includes fallback text requiring an extra line that pushes actions below the fold, clipped diacritics from aggressive ascent overrides, icons misaligned because baseline metrics changed, numeric columns jittering after swap, and metric tuning based only on Latin samples while supported scripts choose a different fallback chain.

## Falsification
Falsification renders the same content with the final face blocked and enabled, sweeps widths near known wrapping boundaries, and checks height/line-count deltas. Introduce strings with ascenders, descenders, accents, numerals, and punctuation. If declared tolerances are exceeded or adjustments clip glyphs, compatibility is disproved.

## Recovery
Recovery selects a more suitable fallback per role or retunes explicit metric overrides from measured deltas. Do not squeeze a badly mismatched fallback until text becomes visually distorted. If no compatible local face exists for a script, accept controlled reflow and design sufficient layout resilience rather than claiming metric parity.

## Output
Output: `font-fallback-metric-compatibility-contract` with fallback chain, role-specific metrics, adjustment values, geometry tolerances, unsupported-script notes, and comparison fixtures.

## Handoff
Handoff font arrival timing to webfont-loading transition engineering, and glyph coverage/subset availability to font-subsetting engineering.

## Sibling Boundary
Loading transitions decide *when* substitution happens; this skill decides *how geometrically compatible* the states are. Mixed-font baseline alignment concerns simultaneous inline faces, not whole-role substitution.

## delete-the-skill test
Without this owner the system can load fonts correctly yet still incur preventable wrapping and layout shifts during fallback. That distinct runtime metric failure proves independent ownership.