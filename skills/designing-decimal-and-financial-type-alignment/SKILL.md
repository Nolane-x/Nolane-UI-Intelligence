---
name: designing-decimal-and-financial-type-alignment
description: Use when monetary or accounting values require consistent decimal, sign, currency, magnitude, parenthesis, and missing-value alignment so financial comparison remains truthful across locales and states.
---

# Designing Decimal and Financial Type Alignment

## Financial Columns Encode Structure
A financial table communicates more than magnitude. Currency symbols, decimal places, negatives, parentheses, zero conventions, missing values, and units all affect interpretation. This skill owns the visual alignment contract that makes those structures comparable without falsifying locale or accounting meaning.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent establishes font roles. This specialist governs monetary/accounting alignment, building on but not replacing generic numeric tabular behavior.

## Value Anatomy
Represent displayed values as semantic parts: sign/accounting marker, currency or unit, integer magnitude, decimal separator, fraction, suffix/scale, and exceptional state such as unavailable or estimated. Decide which parts share alignment guides. A column may align decimals while currency symbols occupy a reserved lane; parentheses for negatives must not shift the numeric core unpredictably.

Preserve locale conventions. Decimal and grouping separators can swap roles; currency may prefix or suffix. Do not force an English accounting pattern into all locales solely for visual neatness.

## Evidence
Evidence includes positive, negative, zero, very large/small, missing, estimated, and rounded values across supported locales; fallback font states; and copy/accessibility output. Compare decimal guides and sign lanes visually while checking canonical numeric values remain machine/readably distinct from formatting.

## Failure Modes
Failure includes negatives whose parentheses shift decimals, currency symbols consuming variable width and hiding comparison, em dashes that look like negative signs for missing values, mixed decimal precision without a declared rounding policy, locale formatting overridden to keep columns visually identical, and accounting alignment achieved with inserted spaces that corrupt copying.

## Falsification
Falsification changes locale, sign, magnitude, precision, and exceptional state while holding the column contract constant. If values that are materially different become visually ambiguous, decimals no longer align where comparison requires it, or copy/speech semantics diverge from the canonical number, the contract fails.

## Recovery
Recovery separates semantic parts into alignment lanes or uses formatting APIs plus layout rather than hand-inserted whitespace. Reserve sign/currency space where needed, clarify missing-value notation, and accept locale-specific geometry when that is the truthful representation.

## Output and Handoff
Output: `decimal-and-financial-type-alignment-contract` with value anatomy, locale rules, decimal/sign/currency alignment, exceptional-state notation, and comparison evidence. Handoff generic digit-width behavior to numeric-tabular alignment and financial business semantics to domain specialists.

## Sibling Boundary and delete-the-skill
Generic tabular numerals cannot decide accounting parentheses, currency lanes, missing-value notation, or locale-specific decimal guides. Removing this skill leaves those financially material presentation decisions unowned.