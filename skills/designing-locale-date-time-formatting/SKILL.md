---
name: designing-locale-date-time-formatting
description: Use when dates and times must be displayed in locale-appropriate order, wording, clock conventions, and relative forms without confusing calendar representation with time-zone conversion.
---

# Designing Locale Date Time Formatting

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns the human-readable representation of an already resolved temporal value in a selected locale. It is distinct from choosing a time zone or non-Gregorian calendar system. It decides field order, month names, 12/24-hour conventions, relative wording, precision, and ambiguity control.

## Decision Boundary
Start from the temporal semantic type: instant, local date, local time, duration, or interval. Do not format a date-only birthday as if it were an instant that can shift across zones. Choose short, medium, or explicit forms according to consequence. Numeric-only dates can be ambiguous across locales; high-stakes records may need named months or ISO-like supporting context.

Relative time such as “yesterday” or “in 3 hours” is useful only within a defined horizon and locale grammar. Pair it with an absolute value when future audit or coordination matters. Respect user clock preference where the platform/product exposes one. Seconds and milliseconds should appear only when the task needs that precision.

## Failure Topology
- `03/04/2026` is shown without locale context on a high-stakes transaction.
- A date-only value shifts one day because code converts it through UTC.
- The interface shows “tomorrow” near midnight while a collaborator in another zone sees a different absolute date.
- 12-hour formatting omits AM/PM.
- Relative time is persisted in screenshots/reports where it becomes misleading later.
- A machine timestamp is displayed verbatim instead of using locale formatting.

## Falsification and Recovery
Test date-only, time-only, instants, intervals, leap days, midnight/noon, short/long formats, relative thresholds, and 12/24-hour locales. Verify the same underlying value without changing time-zone configuration. The design fails if representation introduces ambiguity or changes the temporal type.

Recover by retaining typed temporal values, selecting explicit formats for consequential contexts, separating relative from absolute display, and avoiding instant conversion for local dates. Coordinate with the time-zone and calendar-system owners rather than hiding their decisions inside formatting code.

## Output Contract
Return `locale-date-time-format-contract` with temporal types, format styles by context, numeric-date ambiguity rules, clock convention, relative-time horizon, precision, absolute-support policy, and locale formatting verification cases.
