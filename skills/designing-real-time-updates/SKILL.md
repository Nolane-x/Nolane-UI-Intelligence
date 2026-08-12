---
name: designing-real-time-updates
description: Use when data, collaboration, monitoring, prices, logs, status, feeds, dashboards, or events change while the user is viewing or acting and live updates can move, replace, reorder, or invalidate visible state.
---

# Designing Real-Time Updates

## Overview
Live data must remain current without stealing the user’s locus of attention. Distinguish new data from changed data, preserve selection/reading position, and make temporal order and staleness understandable.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require update frequency, ordering guarantees, data criticality, user task, selection/edit behavior, collaboration, stale tolerance, and source timestamps. High-rate operational UI also needs density and cognitive-load analysis.

## Decision Model
Classify updates: append-only event, state replacement, value change, reorder/rank, deletion, conflict, or invalidation. Each class needs different UI. An append-only log can add below/above with unseen count; a monitored value may animate or highlight delta; reordering a table while the user clicks rows may be unacceptable.

Preserve interaction anchors. If the user scrolls, selects, edits, opens a menu, or expands a row, incoming data should not move the target unpredictably. Freeze/reconcile local regions, defer sort/reorder, or show “12 updates available” when applying immediately would disrupt the task.

Make time explicit when it matters: event time versus receive time, last updated, delayed feed, stale source, timezone. Do not use a green “live” dot when the stream silently stopped. On reconnect, explain whether gaps were replayed or data jumped to current state.

For high-rate updates, aggregate and prioritize. Flashing every cell change creates noise and motion risk. Highlight meaningful deltas with decay, and preserve a history/audit path for important transitions. User edits need conflict/lock/merge semantics rather than incoming data silently overwriting fields.

## Evidence
Test peak update rate, scrolling away from live tail, selection/menu/edit during reorder, reconnect/gap, delayed timestamps, deleted items, accessibility announcements, reduced motion, virtualization, and snapshot consistency. Measure missed/incorrect actions caused by movement, not just frame rate.

## Output Contract
Return a `realtime-contract` with `update_classes[]`, `ordering_model`, `attention_preservation`, `reorder_policy`, `unseen_update_model`, `timestamp_freshness`, `reconnect_gap_rules`, `change_highlight`, `aggregation`, `edit_conflict_policy`, and `realtime_tests[]`.

## Failure Traps
- Rows moving under the pointer as sort order changes.
- “Live” indicator with no heartbeat/staleness model.
- Every numeric change flashing continuously.
- Screen reader announcing every telemetry tick.
- User edit overwritten by remote update.
- Reconnect jumping state with no indication of missed interval.
- Autoscroll dragging users back to the newest item after they intentionally scrolled away.

Realtime UI should make change legible while keeping interaction stable.