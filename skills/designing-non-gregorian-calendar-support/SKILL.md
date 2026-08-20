---
name: designing-non-gregorian-calendar-support
description: Use when users need calendar systems other than Gregorian and the product must preserve date semantics across display, picking, arithmetic, recurrence, storage, and cross-calendar communication.
---

# Designing Non Gregorian Calendar Support

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns calendar-system choice and behavior for dates represented in systems such as Buddhist, Islamic, Hebrew, Persian, Japanese eras, or other supported calendars. It does not merely translate month names. It ensures date selection and arithmetic follow the active calendar while internal interoperability remains explicit.

## Decision Boundary
Separate absolute instants, civil dates, and calendar representation. Decide whether the alternative calendar is a display preference, an input system, or the authoritative business calendar. A calendar picker must use correct month lengths, leap rules, eras, weekday alignment, and navigation for that system. Recurrence expressed as “every first day of month” can mean something different depending on the authoritative calendar.

Cross-calendar workflows need dual representation when participants or systems use different calendars. Do not force users to mentally convert consequential deadlines. Storage can use standardized temporal representations, but conversion must retain the original calendar intent where recurrence or legal documents depend on it.

## Failure Topology
- Only month labels change while grid arithmetic remains Gregorian.
- A recurrence created in an Islamic calendar drifts because backend repeats Gregorian month dates.
- Era/year input is accepted visually but stored without era context.
- A deadline is displayed in one calendar with no way for collaborators using another to confirm equivalence.
- Date picker assumes 12 months and fixed month-navigation logic.
- Conversion near calendar boundaries produces off-by-one dates because time zone is mixed into a date-only value.

## Falsification and Recovery
Test month/year navigation, leap rules, era boundaries, date-only entry, recurrence, min/max constraints, conversions, and dual-calendar display using authoritative calendar libraries/data. The design fails if the active calendar changes only decoration while arithmetic remains based on another system.

Recover by making calendar system part of the temporal contract, using authoritative calendar computations, preserving original recurrence semantics, and offering dual representation in cross-system contexts. Avoid hand-coded conversion tables.

## Output Contract
Return `calendar-system-contract` with supported systems, display/input authority, picker arithmetic, era/leap/month rules, recurrence semantics, storage/conversion boundary, dual-display policy, and calendar-specific verification cases.
