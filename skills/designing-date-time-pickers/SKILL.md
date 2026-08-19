---
name: designing-date-time-pickers
description: Use when users choose dates or times and the interface must reconcile direct text entry, calendar/clock selection, locale, calendar system, timezone, constraints, ranges and accessible keyboard operation.
---

# Designing Date and Time Pickers

## Parent Contract
**Required parent:** `engineering-rich-interactive-components`.

This faculty owns picker interaction for date/time values. Timezone-aware scheduling and recurrence are separate specialist concerns.

## Decision Model
Define the underlying value before designing the calendar: date-only, local time-only, local date-time, instant in time, date range, month/year or recurring rule. A birthday is not a timestamp; a meeting instant is not just “10:00”. UI labels and serialization must reflect that distinction.

Offer text entry when users may know the value faster than navigating a calendar, especially for distant dates. Parsing must follow locale and avoid ambiguous formats; examples/placeholders are not substitutes for labels. Calendar navigation should expose month/year movement efficiently rather than forcing dozens of next-month presses.

Constraints—minimum/maximum, unavailable days, business hours, excluded intervals—must be perceivable before selection where possible. Disabled dates need reasons when the constraint is nonobvious. For ranges, distinguish start, end, provisional hover/focus range and invalid reverse/minimum-stay rules.

Keyboard and screen-reader operation need a coherent grid or platform-native model. Focused date, selected date and today are separate states. Do not encode all three with the same circle/color.

## Failure Topology
- Locale `03/04/2026` is accepted without clarifying whether it means March 4 or April 3.
- Selecting “10:00” silently binds to device timezone when the domain expects venue timezone.
- Calendar opens on current month for a birth date 40 years ago with no year navigation.
- Disabled dates have no explanation.
- Today, focus and selected state look identical.
- Date range preview suggests invalid nights that later fail at submit.

## Falsification and Recovery
Test multiple locales, keyboard-only, screen reader, date-only vs instant, leap day, DST boundary inputs, far-past/future year, invalid ranges, unavailable dates and manual typing. The contract fails if users can choose a display value whose underlying temporal type is ambiguous.

Recover by clarifying value type, adding direct input/efficient year navigation, surfacing constraints earlier and delegating timezone conversion to scheduling logic rather than implicit device assumptions.

## Output Contract
Return `date-time-picker-contract` with temporal value type, input/picker modes, locale/calendar rules, constraints, range state, focus/selection/today visuals, keyboard/AT model, parsing/validation and temporal edge tests.