---
name: designing-plural-sensitive-copy
description: Use when counts appear in interface messages and language-specific plural categories require grammatical variants beyond an English singular-versus-plural branch.
---

# Designing Plural-Sensitive Copy

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns the runtime contract between numeric quantities and localized message variants. It does not translate copy itself. It prevents concatenated fragments and binary plural logic from producing ungrammatical or misleading messages in languages with zero, one, two, few, many, or other categories.

## Decision Boundary
Treat the whole sentence or message as the translation unit. Pass structured values into locale-aware message formatting rather than assembling `count + noun + suffix`. Decide whether exact-zero wording is product semantics (“No messages”) or simply a plural category. Ordinal forms such as “1st/2nd” use different rules from cardinal counts and need separate messages.

Counts can be exact, rounded, compact, ranges, or hidden for privacy. The grammatical choice must use the same value semantics displayed to the user. A visible “1K items” should not be paired with grammar computed from an inaccessible raw value in a way that creates inconsistency. Dynamic count updates should not trigger excessive announcements merely because the grammatical string changes.

## Failure Topology
- Code handles only `count == 1` versus everything else.
- A noun is translated separately and concatenated after a number, preventing correct inflection or word order.
- Zero is hard-coded as English “No” inside otherwise localized text.
- Ordinal suffixes are copied across locales.
- Compact rounded numbers use a plural form based on a different hidden quantity.
- One message key contains embedded HTML fragments that translators cannot reorder safely.

## Falsification and Recovery
Test zero, one, two, small/few, large/many, decimals, negative values where valid, ranges, and ordinals across languages with materially different plural systems. Inspect full rendered sentences and screen-reader output. The design fails if grammar depends on English word order or if translators cannot express the whole message naturally.

Recover by using locale-aware plural/select message formats, passing typed values, separating cardinal/ordinal/range cases, and eliminating string concatenation. Add unit tests for representative plural categories without pretending those tests replace native-language review.

## Output Contract
Return `plural-sensitive-copy-contract` with message units, value semantics, cardinal/ordinal handling, zero policy, range/compact-number interaction, translator-reorder requirements, and plural-category verification matrix.
