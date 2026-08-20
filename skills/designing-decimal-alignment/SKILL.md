---
name: designing-decimal-alignment
description: Align decimal quantities so magnitude can be compared accurately across rows despite signs, currencies, varying precision, missing values, and localization.
---

# Designing decimal alignment

Right-aligning numbers is not always enough when values have different precision. Use this skill for financial statements, measurements, scientific data, pricing, or analytical tables where readers compare decimal magnitude.

## Decision ownership

Own alignment anchor, precision display, sign and currency placement, missing-value representation, and locale-aware decimal separator behavior. Decide whether values align on decimal separator, unit boundary, or least significant digit.

## Inputs and evidence

Collect value ranges, precision rules, currencies/units, negatives, accounting notation, percentages, scientific notation, locale separators, nulls, and editable states. Understand whether displayed precision is fixed by domain rules or varies with data quality.

## Procedure

Choose an alignment method that preserves magnitude scanning. For fixed precision, right alignment with tabular numerals may suffice. For mixed precision, align decimal separators or reserve integer/fraction regions explicitly. Keep units visually distinct without breaking the numeric column.

Handle negatives and accounting parentheses consistently. Reserve space for signs where needed so positive and negative values remain comparable. Localize separators without assuming `.` is the decimal anchor.

For editable grids, keep caret behavior and selection intuitive; visual alignment should not require awkward text manipulation.

## Failure topology

Mixed precision can make right-aligned values appear comparable while decimal positions differ. Currency symbols of different width distort columns. Another failure is substituting em dashes for nulls without deciding whether they align as numeric absence or textual annotation.

CSS tricks based on splitting strings can harm accessibility or copy/paste.

## Falsification

Test large/small values, negatives, zero, null, multiple currencies, locales, and scientific notation. Copy values from the UI and verify semantic text remains intact. Compare columns with tabular figures enabled and disabled.

If alignment requires altering the spoken or copied number structure, choose a safer rendering method.

## Output contract

Produce a `decimal-alignment-contract` defining alignment anchor, precision policy, sign/currency/unit treatment, locale behavior, null representation, editing/copy semantics, and representative value matrices.

## Handoffs

Use `designing-tabular-numerals` for fixed glyph width, `designing-numeric-comparison-typography` for emphasis and hierarchy, monetary-input skills for editable values, and data-table skills for column sizing.