---
name: designing-locale-aware-sorting
description: Use when human-facing lists of names, titles, labels, or strings must be ordered according to locale collation rather than raw Unicode or ASCII code-point order.
---

# Designing Locale Aware Sorting

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns collation semantics for user-facing text sorting. It does not own generic table sorting controls. It decides which locale, sensitivity, numeric treatment, punctuation behavior, and normalization rules produce an order users recognize as linguistically coherent.

## Decision Boundary
Identify the data type and audience before choosing a collation locale. A multilingual global directory may need a product-defined ordering strategy distinct from each viewer's shell locale; a personal contact list may reasonably follow the viewer locale. Decide how accents, case, punctuation, articles, and embedded numbers affect order. “File 2” versus “File 10” may require numeric collation even though the values are strings.

Do not use transliteration as a hidden sort key unless product semantics justify it and users can understand the result. Stable sorting is important when equal-collation strings differ in hidden details. Server and client must use compatible collation or pagination will appear to reshuffle as more data loads.

## Failure Topology
- Names are sorted by Unicode code point and accented letters appear in surprising blocks.
- Client-side locale sorting is applied only to the current page of server-paginated data.
- Case sensitivity differs between initial load and interactive re-sort.
- Numeric-looking labels order as 1, 10, 2.
- Hidden transliterations determine position while visible strings give no clue why.
- Changing UI language unexpectedly reorders an audit list whose authoritative order should remain stable.

## Falsification and Recovery
Build data sets with accents, composed/decomposed forms, case variants, punctuation, numbers, multiple scripts, and equal-collation values. Compare ordering across supported locales, pagination, server/client execution, and locale changes. The design fails when users see unstable order or when identical filters produce different sequences depending on where sorting ran.

Recover by choosing explicit collation authority, using locale-aware collation libraries consistently, defining sensitivity/numeric options, normalizing safely, and adding deterministic tie-breakers. Keep machine identifiers out of human collation unless the task is explicitly technical.

## Output Contract
Return `locale-sorting-contract` with collation authority, locale selection, sensitivity/numeric/punctuation options, normalization/tie-break rules, server-client consistency, pagination behavior, and multilingual sorting fixtures.
