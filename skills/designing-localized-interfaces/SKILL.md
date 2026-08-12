---
name: designing-localized-interfaces
description: Use when a UI may support multiple languages, scripts, regions, writing directions, date-number formats, or content expansion that can change geometry or meaning.
---

# Designing Localized Interfaces

## Overview
Localization is a layout and interaction constraint, not a translation step at the end.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use target locales if known. If international support is required but locales are unknown, design against stress classes instead of assuming English geometry.

## Text expansion
Expect labels, headings, buttons, validation, and help text to grow. Prefer flexible containers, wrapping, and content-aware height. Fixed-width controls that only fit English are defects unless the product explicitly constrains language.

## Writing direction
RTL adaptation includes:
- layout flow and start/end alignment
- navigation direction where semantically appropriate
- directional icons/chevrons
- progress/sequence direction
- mixed-direction content such as URLs, code, numbers, phone values
- gesture expectations

Do not mirror icons whose meaning is independent of direction (for example many brand marks or media controls) without checking semantics.

Use logical start/end concepts rather than hard-coded left/right in the design contract when direction can vary.

## Script and typography
Verify font coverage, x-height/legibility equivalents, line metrics, shaping, diacritics, and fallback behavior. An expressive Latin display face may need a script-compatible alternative that preserves tone rather than forcing missing glyphs/fallback chaos.

## Locale-sensitive data
Design for different:
- date/time order and time zones
- decimal/group separators
- currency placement/precision
- measurement units
- address/name conventions
- pluralization and grammatical gender where copy generation matters

Do not bake formatted strings into component logic.

## Content order
Translation can change sentence structure and label/action ordering. Components should expose semantic slots rather than concatenate pieces into a visual sentence.

## Truncation
If truncation is necessary, preserve access to the full value and do not truncate the differentiating suffix/prefix users rely on (e.g., environment names, file paths) without domain-aware rules.

## Locale stress plan
At minimum include:
- compact Latin
- expanded Latin
- RTL
- non-Latin script with different metrics
- mixed bidi technical content when relevant
- long numeric/date/currency formats

## Output: `locale-stress-plan`
Return `target_locales`, `expansion_rules`, `direction_rules`, `icon_mirroring`, `typography_fallbacks`, `data_formatting`, `component_risks`, `stress_cases`, and `verification_matrix`.

## Common failures
- RTL implemented as `text-align:right` only.
- Icon + label order wrong after mirroring.
- Fixed-height buttons clip translated copy.
- Screenshot/generated-image text impossible to localize.
