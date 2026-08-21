---
name: engineering-font-subsetting-and-glyph-coverage
description: Use when font files are subset by script, Unicode range, locale, feature, or product surface and loading savings must not create missing glyphs, broken fallback chains, or inconsistent typographic behavior.
---

# Engineering Font Subsetting and Glyph Coverage

## Performance With a Coverage Boundary
Font subsetting reduces transfer cost by removing glyphs and tables, but every removed code point creates a potential runtime branch into another face. This skill owns how subsets are partitioned, declared, requested, and verified against the actual character repertoire a product promises to support.

## Parent Contract
**Required parent:** `crafting-typography`.

The parent establishes typographic roles and supported product language intent. This specialist turns that promise into concrete glyph/package coverage without deciding broader localization policy.

## Coverage Model
Build a repertoire from supported scripts, locale content, names, user-generated text, symbols, currency, mathematical notation, punctuation, emoji interaction, and product-specific glyph needs. Separate static authored content from unbounded user content. Map each repertoire slice to a font face/subset and define what fallback is acceptable for uncovered characters.

Unicode-range declarations are routing rules, not proof that the binary contains the declared glyphs. Likewise, a glyph can exist but lack required shaping or OpenType data. Coverage verification must inspect actual font resources and rendering.

## Subset Decisions
Partition when savings are material and request patterns justify separate resources. Avoid tiny slices that cause connection/request overhead or visible mixed-face runs. Preserve tables/features needed for shaping, kerning, variable axes, and script behavior. Version subset generation so cache identity tracks content changes.

## Evidence
Evidence includes code-point inventories, font-table inspection, representative multilingual strings, mixed-script runs, currency/symbol fixtures, missing-glyph probes, network waterfalls, and offline/cached behavior. Test a string spanning two subsets because boundary rendering can expose mismatched metrics.

## Failure Modes
Failure includes tofu boxes for rare but valid names, punctuation taken from an unintended fallback, a currency symbol missing from a “Latin” subset, shaping tables removed from complex scripts, ranges that trigger both large files, and build pipelines whose subset contents drift without cache/version updates.

## Falsification
Falsification samples the edge of every declared range, introduces rare supported characters, tests mixed-script and combining sequences, and blocks secondary subsets. If supported content produces missing glyphs or an undeclared face while coverage evidence claims completeness, the contract is falsified.

## Recovery
Recovery restores missing repertoire, merges over-fragmented subsets, reintroduces required shaping tables, or explicitly delegates unsupported characters to a tested fallback. Do not hide coverage defects with generic system-font fallback when visual/metric continuity is a product requirement.

## Output
Output: `font-subsetting-and-glyph-coverage-contract` with repertoire, subset boundaries, binary coverage evidence, fallback mapping, feature-table requirements, and network tradeoffs.

## Handoff
Handoff simultaneous-face baseline issues to mixed-font baseline alignment and fallback geometry to fallback-metric engineering.

## Sibling Boundary and delete-the-skill
Fallback metrics assume a fallback is intentionally selected; this skill decides whether and when missing repertoire forces that selection. Removing it leaves subset-performance decisions without a glyph-coverage authority, satisfying the delete-the-skill test.