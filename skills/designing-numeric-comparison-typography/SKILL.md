---
name: designing-numeric-comparison-typography
description: Structure numeric typography so magnitude, change, uncertainty, units, and exceptional values can be compared quickly without relying on color alone.
---

# Designing numeric comparison typography

Analytical and financial interfaces ask users to compare numbers, not merely read them. Use this skill when KPI cards, tables, reports, forecasts, scores, or measurements need typographic hierarchy optimized for quantitative scanning.

## Decision ownership

Own number-versus-label prominence, sign/change treatment, unit hierarchy, precision, alignment, exceptional-state emphasis, and relationship to trend indicators. Decide which information is primary in a comparison task.

## Inputs and evidence

Collect numeric tasks, value ranges, deltas, units, confidence/uncertainty, zeros, negatives, missing values, color semantics, localization, and screen-reader output. Observe whether users compare absolute values, changes, ranks, or thresholds.

## Procedure

Give the comparison variable clear typographic authority while keeping labels and units sufficiently visible. Use tabular figures and alignment where scanning benefits. Treat sign and delta consistently; do not rely solely on red/green to communicate direction.

Separate precision from importance. More decimal places should reflect meaningful measurement, not simply available data. De-emphasize units only if doing so cannot make values ambiguous.

For exceptional values, combine weight, symbol, wording, or structure with color.

## Failure topology

Huge KPI numerals can dominate without context, making users overlook units or date ranges. Inconsistent precision creates false differences. Tiny units can make `10 MB` and `10 GB` dangerously easy to confuse. Another failure is emphasizing percentage change while hiding the small absolute base.

## Falsification

Run scan tasks across dense tables and KPI groups. Convert to grayscale and verify positive/negative or warning distinctions remain. Test locale and unit changes, long values, missing data, and screen-reader output. Remove decorative trend graphics and see whether typography still communicates the necessary comparison.

## Output contract

Produce a `numeric-comparison-typography-contract` specifying number/label/unit hierarchy, alignment, figure style, precision, sign/delta treatment, color-independent cues, exceptional states, and tested comparison scenarios.

## Handoffs

Use `designing-tabular-numerals` and `designing-decimal-alignment` for alignment mechanics, data-visualization skills for graphical trend encoding, and `designing-legal-and-disclosure-typography` when numeric disclosures have regulated prominence.