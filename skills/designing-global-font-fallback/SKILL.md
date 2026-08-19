---
name: designing-global-font-fallback
description: Use when the primary typeface lacks glyph coverage and fallback fonts must preserve language coverage, shaping, metrics, weight, and product hierarchy without tofu or disruptive font mixing.
---

# Designing Global Font Fallback

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns fallback-family architecture for multilingual UI. It is concerned with glyph availability, script shaping, metric compatibility, loading, and the visible transition between primary and fallback faces. It does not own typography hierarchy itself.

## Decision Boundary
Build fallback stacks from actual supported scripts and environments, not a single generic `sans-serif` promise. For each script, verify the selected fallback has required glyphs, joining/shaping behavior, punctuation, numerals, and weights. Where web fonts are used, decide whether script subsets are preloaded, lazily loaded, or delegated to high-quality system fonts. Loading strategy must not leave critical text blank or cause repeated layout shift when a new script appears.

Metrics matter because fallback can change line breaks, control heights, and table density. Calibrate size/line-height where a fallback's optical dimensions differ materially. Emoji and symbols need their own precedence rules so text presentation does not unexpectedly switch to colorful emoji or missing-glyph boxes. User-generated content may introduce scripts beyond the product's official locale set; provide a defensible system fallback rather than crashing the visual language.

## Failure Topology
- Unsupported characters render as tofu squares in names or addresses.
- Fallback font lacks the requested bold weight and synthesized weight becomes unreadable.
- Lazy script font loading shifts a dense interface after interaction begins.
- Emoji font precedence changes text-like symbols into colored pictographs with different meaning.
- Fallback glyph metrics clip inside fixed-height controls.
- A font stack covers common characters but misses locale-specific punctuation or combining marks.

## Falsification and Recovery
Generate coverage strings per supported script plus mixed-script names, symbols, numerals, combining marks, and uncommon but valid characters. Test cold/warm loading, offline/system-font fallback, all relevant weights, and constrained components. The design fails if meaning becomes missing glyphs or if fallback changes layout enough to hide controls or break hierarchy.

Recover by selecting script-capable families, adjusting precedence and metrics, preloading critical subsets, retaining robust system fallbacks, and testing font-file failure. Record licensing/performance constraints separately from semantic coverage so optimization does not silently remove language support.

## Output Contract
Return `global-font-fallback-contract` with script coverage matrix, family precedence, weight/glyph guarantees, subset/loading policy, metric adjustments, emoji/symbol rules, font-failure behavior, and coverage verification corpus.
