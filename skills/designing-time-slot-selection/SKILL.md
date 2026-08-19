---
name: designing-time-slot-selection
description: Use when users choose one or more available intervals and the interface must distinguish availability, tentative selection, duration, constraints, timezone and stale availability under concurrent booking.
---

# Designing Time Slot Selection

## Parent Contract
**Required parent:** `designing-calendar-interfaces`.

This faculty owns choosing a bounded interval from an availability space. It does not compute availability or manage full resource booking lifecycle.

## Decision Model
Represent each candidate slot with authoritative start/end, display timezone, availability state, capacity where relevant and any constraints such as minimum lead time, duration increments or contiguous availability. A visual `10:00` label is not enough if the user, resource and venue may be in different zones.

Decide whether duration is fixed before selection, selected after a start time, or derived by dragging a range. If changing duration makes the current start invalid, explain and move users to valid alternatives instead of silently shifting time. Slots that are unavailable should either be omitted or shown disabled with meaningful reason when comparison matters; do not create a calendar full of unexplained grey boxes.

Selection is provisional until the booking engine reserves/commits it. Concurrency means a slot can become unavailable while visible. Revalidate at commit and present conflicts as freshness problems, not user validation errors. If temporary holds exist, surface hold expiration and do not imply a hold that the backend cannot guarantee.

For long lists of slots, group by date/time period and preserve scanability; avoid dozens of identically styled pills with no contextual hierarchy. Keyboard and screen-reader users need temporal ordering and clear selected/unavailable states.

## Failure Topology
- User selects 30 minutes, changes duration to 60, and UI keeps a start time whose second half is occupied.
- A slot looks selected/secured but no server-side hold exists and another user books it.
- Device timezone changes and previously selected text now maps to a different instant.
- Unavailable slots are hidden, making users think the business is closed rather than booked.
- Slot pills wrap out of chronological reading order on mobile.
- Commit conflict says “Invalid time” instead of explaining availability changed.

## Falsification and Recovery
Falsify with fixed/variable duration, concurrent booking, availability refresh, timezone change, DST, no slots, lead-time constraints, keyboard navigation and small viewport. Revalidate selected start/end against authoritative availability at commit.

Recover by storing temporal instants + display zone, making selection provisional, recalculating valid starts after duration changes and exposing stale/conflict state with nearby alternatives.

## Output Contract
Return `time-slot-selection-contract` with slot model, duration strategy, selection state, constraints/unavailable treatment, hold/commit semantics, concurrency refresh, timezone/DST, accessibility ordering and conflict tests.