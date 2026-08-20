---
name: designing-tabular-numerals
description: Use tabular numeral features where changing numeric width would disrupt comparison, alignment, timers, counters, or dense financial and analytical interfaces.
---

# Designing tabular numerals

Numbers that change width as values update can create visual jitter and weaken column scanning. Use this skill for tables, dashboards, timers, balances, scores, counters, and any aligned numeric presentation.

## Decision ownership

Own when fixed-width numeral glyphs are required, which font features or fallback fonts provide them, and where proportional numerals remain preferable for prose. Decide how tabular numerals interact with currency, signs, decimals, units, and variable fonts.

## Inputs and evidence

Collect numeric surfaces, live-updating values, supported fonts, OpenType feature availability, fallback behavior, locales, currencies, percent signs, grouping separators, and comparison tasks. Inspect whether columns are aligned by CSS but still visually wobble because glyph widths vary.

## Procedure

Enable tabular figures for numeric columns and rapidly changing values where stable width supports scanning. Keep proportional figures in ordinary prose unless alignment is useful. Verify the chosen font actually supports `tnum`; some fallbacks silently ignore the feature.

Coordinate with decimal alignment and sign/currency placement. Test locale-specific separators and non-Latin numeral systems. In variable fonts, confirm feature behavior across weight and width axes.

## Failure topology

Applying tabular figures globally can make prose numbers feel mechanically spaced. Unsupported font features create false confidence. Another failure is aligning digits while currency symbols or parentheses still vary enough to cause column jitter.

Live counters may reserve insufficient width for digit-count changes even with tabular glyphs.

## Falsification

Animate representative values through all digits and sign states and measure horizontal movement. Switch fonts and locales. Compare numeric columns at several weights. Test values that grow from three to four digits; figure features cannot solve changing character count.

## Output contract

Produce a `tabular-numerals-contract` defining eligible surfaces, font-feature settings, fallback policy, locale and sign handling, width reservation, and visual stability tests for changing values.

## Handoffs

Use `designing-decimal-alignment` for decimal columns, `designing-numeric-comparison-typography` for broader numeric hierarchy, `designing-font-loading-fallback-behavior` for font substitution, and data-table skills for column layout.