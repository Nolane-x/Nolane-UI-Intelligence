---
name: critiquing-localization
description: Use when UI ships across languages, scripts, locales, RTL contexts, regional formats, plural/grammar systems, cultures, names, addresses, currencies, dates, or translated content that can change geometry and interaction meaning.
---

# Critiquing Localization

## Overview
Independently test whether the interface survives real language and locale change without truncating actions, reversing semantic icons incorrectly, corrupting formats, or assuming English grammar and name/address structure.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

**May modify:** false. Consume locale stress plan, content contract, responsive/component system, formatting/data model, and actual localized builds where available. Pseudo-localization helps but cannot prove linguistic/cultural correctness.

## Decision Model
Review **expansion**, **direction**, **format**, **grammar**, **data model**, and **cultural meaning**. Expansion: long labels, buttons, navigation, tables, error text, and dynamic data must wrap/reflow without hiding critical actions. Direction: RTL mirrors spatial layout where appropriate, but not all symbols — media timelines, numbers, brand marks, maps, and directional meaning need context-specific handling. Format: date/time/calendar, number/decimal/grouping, currency, measurement, address, phone, collation, and timezone must use locale-aware rules.

Grammar affects component architecture. Concatenating translated fragments breaks word order, gender, case, plural, and inflection. Messages should be complete translatable units with structured variables. Data models should not force Western first/last-name, state/ZIP, or fixed address assumptions.

Check icon/metaphor and color only where culture changes comprehension; avoid stereotype-driven localization. Voice/AI UI adds pronunciation, script mixing, input method, and generated-language quality. Ensure locale fallback is explicit and does not mix untranslated technical strings into critical flows silently.

## Evidence
Use representative locale builds, pseudo-localization, RTL, CLDR-backed formatting tests, native-speaker/translator review for critical content, long names/addresses, plural cases, timezone boundaries, search/sort/collation, screen reader pronunciation where relevant, and screenshots/runtime interaction. Record untranslated/fallback behavior.

## Output Contract
Return a `finding-set` with `may_modify:false`, `artifact_revision`, `locales_tested[]`, `findings[] {finding_id, severity, locale, localization_class, evidence, user_impact, falsifier, recommended_repair, required_reverification}`, `truncation_overflow[]`, `rtl_defects[]`, `format_errors[]`, `grammar_fragmentation[]`, and `release_recommendation`.

## Failure Traps
- Translating strings only, with no layout/runtime test.
- Mirroring every icon in RTL automatically.
- Dollar sign used as universal currency context.
- Month/day ambiguity in high-stakes date fields.
- Concatenated translated fragments.
- “First name / Last name” required for all identities.
- Pseudo-localization treated as linguistic validation.

Localization passes when the task remains semantically and interactively correct, not merely when all strings have translations.