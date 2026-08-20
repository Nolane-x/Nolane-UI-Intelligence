---
name: designing-locale-number-formatting
description: Use when quantities, percentages, decimals, compact values, signs, or digit systems must follow locale conventions while preserving exact data meaning and machine operations.
---

# Designing Locale Number Formatting

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns presentation and parsing boundaries for locale-sensitive numeric values. It does not own monetary input specifically. It decides how separators, digits, signs, percentages, precision, compact notation, and copy/export behavior preserve meaning across locales.

## Decision Boundary
Separate internal numeric value from formatted display. Grouping and decimal separators vary, and some locales use non-Latin digit shapes. Percent formatting may scale stored values differently from how users perceive them. Define precision based on domain needs before localization; locale formatting chooses representation, not arbitrary rounding that changes the underlying decision.

For editable numeric fields, parsing must recognize the active locale while avoiding ambiguous mixed separators. Decide whether pasted values in another common format are rejected, normalized with confirmation, or accepted safely. Tables and charts should sort/filter using numeric values, never localized strings. Copy actions may need a human-readable form while machine export uses a locale-neutral representation.

## Failure Topology
- `1,234` is parsed as 1.234 in one locale and 1234 in another without feedback.
- Values are sorted lexicographically after localization.
- Percentage display multiplies an already-percent value again.
- Compact notation such as `1.2K` hides precision required for a financial or scientific decision.
- Non-Latin digits render but input validation accepts only ASCII digits.
- CSV export reuses localized decimal commas in a delimiter context that becomes ambiguous.

## Falsification and Recovery
Test positive/negative, zero, decimals, large grouped values, percentages, compact notation, non-Latin digits, copy/paste, sorting, filtering, and export across representative locales. The design fails if formatting changes numeric meaning or if visible and parsed values disagree.

Recover by maintaining typed numeric state, using locale-aware formatter/parser pairs, defining precision separately from locale, and separating human display from machine interchange. Add ambiguity handling for pasted values instead of guessing silently.

## Output Contract
Return `locale-number-format-contract` with numeric value model, formatter/parser behavior, separator/digit policy, precision/rounding ownership, percentage/compact rules, copy/export representation, and cross-locale numeric verification cases.
