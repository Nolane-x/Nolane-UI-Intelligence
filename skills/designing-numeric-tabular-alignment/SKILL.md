---
name: designing-numeric-tabular-alignment
description: Use when changing numeric values must remain visually comparable across rows, columns, counters, timers, or dashboards and digit width, sign, grouping, and update stability need typographic control.
---

# Designing Numeric Tabular Alignment

## Comparison Through Stable Rhythm
When users scan changing numbers, proportional digit widths can make columns and counters jitter even if their containers are fixed. This skill owns typographic treatment that preserves digit rhythm and positional comparability for general numeric data without imposing financial/accounting conventions.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent chooses font roles. This specialist governs numeric glyph features and alignment when comparison or update stability is the task.

## Numeric Model
Record whether values are integers, decimals, percentages, durations, ranks, counts, or measurements; whether sign and grouping are present; and whether magnitude changes frequently. Decide when tabular numerals are required, where columns align, and whether units belong inside or outside the alignment field.

Tabular digits solve equal advance width, not decimal structure by themselves. Preserve locale formatting and semantic number representation; do not strip grouping or use monospaced text globally merely to make columns line up.

## Evidence
Evidence includes 0–9 specimen widths, values with different digit combinations and magnitudes, live updates, locale grouping, positive/negative signs, and fallback-font states. Measure column movement over time and compare scan behavior. Verify the intended OpenType numeric feature actually resolves in the runtime face.

## Failure Modes
Failure includes timers that visibly wobble each second, right-aligned columns whose internal digit widths impede comparison, fallback fonts lacking the requested feature, units causing changing column width, and numeric styling that accidentally makes text labels monospaced too. Another failure is using visual spacing characters that corrupt copy/paste or screen-reader output.

## Falsification
Falsification cycles every digit through the same position, updates magnitude boundaries such as 99→100, switches locale/grouping, and blocks the primary font. If aligned columns move materially or the runtime falls back to proportional digits without an accepted degradation, the contract fails.

## Recovery
Recovery enables verified tabular figures, separates units from the comparison field, chooses right/center alignment based on task, and provides a compatible fallback. Avoid fixed character boxes that break kerning, selection, or accessibility unless the content is genuinely segmented.

## Output
Output: `numeric-tabular-alignment-contract` with numeric classes, font-feature requirements, alignment rules, unit/sign treatment, fallback behavior, and update-stability evidence.

## Handoff
Handoff currency/accounting-specific decimal and sign structures to financial-type alignment and overall font choice to the parent.

## Sibling Boundary and delete-the-skill
Financial alignment owns accounting semantics; this skill applies to generic dynamic numbers such as metrics and timers. Removing it leaves digit-width and update-jitter decisions without a specialist owner.