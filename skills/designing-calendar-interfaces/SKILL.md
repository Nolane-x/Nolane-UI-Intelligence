---
name: designing-calendar-interfaces
description: Use when users browse and manipulate events over day, week, month or agenda views and the interface must preserve temporal position, overlap, all-day events, navigation, timezone and accessible nonvisual structure.
---

# Designing Calendar Interfaces

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns calendar-view interaction and temporal layout. Date/time input, timezone scheduling, recurrence and resource booking are specialist siblings.

## Decision Boundary
Start from the calendar’s task, not the familiar month grid. Scheduling density, shift planning, personal agenda and booking availability may require day/week, timeline, agenda, month or multi-resource views. Provide only views that preserve meaningful task capability rather than duplicating the same data in decorative formats.

Model visible temporal context explicitly: view type, anchor date, timezone, work-week/business-hour conventions and hidden/nonworking periods. “Today” is separate from selected date, focused time cell and event selection. Navigation to previous/next period should preserve view granularity and offer efficient jump-to-date/today routes.

Time-based event geometry must represent start/end and overlaps truthfully. Overlapping events need a deterministic lane/width algorithm that does not make shorter or later events inaccessible. Very short events require minimum hit/read size without visually claiming longer duration; use labels/details while retaining true temporal extent.

All-day/multi-day events belong to a distinct region and can span day boundaries. Month views need overflow handling such as `+3 more` with a reachable list; hiding excess events is not acceptable when they are operationally significant.

Drag to move/resize can accelerate editing but must have keyboard/form alternatives and clear timezone/recurrence consequences before commit. Calendar scrolling around DST must preserve labeled local times even when the day has 23 or 25 actual hours.

## Failure Topology
- Month view shows three events and silently hides the fourth with no overflow indicator.
- Two overlapping appointments occupy the same pixels and one cannot be selected.
- Minimum visual height makes a 5-minute event appear to last 30 minutes with no cue.
- “Today” highlight is indistinguishable from selected/focused date.
- DST day is rendered as 24 identical one-hour rows and time mapping becomes wrong.
- Keyboard users can reach toolbar controls but not events/time slots efficiently.

## Falsification and Recovery
Falsify with all-day, multi-day, short, overlapping, overnight and DST-boundary events; high event density; month overflow; keyboard/screen reader; timezone changes; and narrow viewport. Map every event rectangle back to authoritative start/end/timezone.

Recover by choosing task-appropriate views, separating temporal/state cues, using deterministic overlap/overflow, exposing exact times and providing agenda/list alternatives for dense or nonvisual access.

## Output Contract
Return `calendar-interface-contract` with view repertoire, temporal context, navigation, event layout/overlap, all-day/multi-day handling, overflow, move/resize handoffs, timezone/DST behavior, accessibility alternative and temporal-geometry tests.