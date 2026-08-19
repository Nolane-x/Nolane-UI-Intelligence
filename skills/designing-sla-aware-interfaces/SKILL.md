---
name: designing-sla-aware-interfaces
description: Use when contractual or operational response/resolution targets affect work prioritization and the interface must represent clocks, pauses, business calendars, breach risk and responsibility without reducing SLA to a red countdown.
---

# Designing SLA-Aware Interfaces

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns user-facing service-level timing semantics. It does not define the contract, business calendar or legal meaning of an SLA; those are external policy authorities.

## Decision Boundary
An SLA timer is derived from a **policy clock**, not simply `deadline - current device time`. Capture target type (first response, next response, resolution, restore service), start event, business calendar/timezone, pause conditions, exemptions, priority/service tier and responsible party. The UI should identify which clock is shown when several coexist.

Prefer human-actionable timing over panic visuals. “47 min remaining to first response” may be useful; “breaches at 16:30 Europe/London” adds exact context; “paused awaiting customer since 14:10” explains why a clock stopped. Do not render a ticking seconds countdown for a multi-day target unless seconds change decisions.

Risk states should derive from policy/forecast rather than arbitrary color thresholds. Due soon, at risk and breached can have distinct semantics. Red must not be the only cue. Sorting by SLA should distinguish actual deadline from predicted breach risk.

Pausing and resuming require provenance. If an operator changes case state to one that pauses the clock, communicate that consequence before or immediately after the action. A stale browser must not continue showing a local countdown after server policy recalculates the target.

## Failure Topology
- Device timezone makes a target look one hour earlier/later than policy timezone.
- Countdown reaches zero locally although the SLA was paused server-side.
- “At risk” is defined as under 1 hour for every service tier with no policy basis.
- Dashboard shows one SLA badge while case actually has response and resolution targets.
- Changing status pauses the clock without user realizing it.
- Reopened case reuses the old deadline although policy starts a new target.

## Falsification and Recovery
Falsify across DST, business-hours boundaries, pause/resume, priority change, reopen, policy recalculation, offline/stale client and multiple simultaneous targets. Compare UI timing to authoritative server-calculated SLA records.

Recover by displaying policy-derived timestamps/states, separating multiple target types, marking stale calculations, exposing pause/resume reasons and avoiding local-only timer authority.

## Output Contract
Return `sla-aware-interface-contract` with target types, authoritative clock inputs, business-time/timezone, pause/resume rules, risk/breach semantics, responsibility, stale/recalculation handling, presentation cadence and temporal parity tests.