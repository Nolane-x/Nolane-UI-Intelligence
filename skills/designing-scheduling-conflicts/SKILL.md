---
name: designing-scheduling-conflicts
description: Use when a proposed event or booking overlaps availability, constraints or another commitment and the interface must explain the exact conflict, affected participants/resources and safe alternatives rather than returning a generic scheduling error.
---

# Designing Scheduling Conflicts

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns detection-result presentation and recovery for scheduling conflicts. The scheduling engine is authoritative for conflict computation; this skill must not invent free/busy rules.

## Decision Boundary
Classify conflict source: participant busy/tentative/out-of-office, resource occupied, capacity exhausted, working-hours policy, travel/setup buffer, recurrence occurrence conflict, booking rule, permissions or stale availability. A generic “time unavailable” hides the recovery path.

Present exact overlap in a consistent timezone. Identify which participant/resource conflicts and whether the conflict is hard (cannot book) or advisory (can override with permission/rationale). Protect private calendars: a user may be allowed to know “busy” without seeing event title/details. Do not leak another person’s sensitive schedule in the name of explanation.

For multi-participant scheduling, summary counts such as `2 conflicts` should expand into enough actionable detail while avoiding overwhelming lists. Alternatives should be generated from the authoritative availability engine and preserve duration/resource requirements. Do not suggest a nearby time that violates a different hidden constraint.

Concurrent changes can create conflicts after a previously clean preview. Revalidate at commit and treat the result as stale availability. For recurring events, conflicts may affect only some occurrences; offer policies supported by product truth—choose another series time, skip/adjust exceptions, request override—without silently creating irregular series.

## Failure Topology
- Conflict dialog exposes another employee’s private appointment title.
- “2 attendees unavailable” gives no way to identify whether they are required participants.
- Suggested alternative solves participant overlap but the room is occupied.
- Soft working-hours warning is styled like a hard booking prohibition.
- Recurring series has three conflicts but UI says only “This time is unavailable.”
- Stale availability failure is blamed on malformed user input.

## Falsification and Recovery
Falsify with private free/busy, hard/soft constraints, participant/resource combinations, concurrent bookings, recurring partial conflicts, timezones and override permissions. Verify every suggested alternative against the same full constraint set.

Recover by exposing conflict type/scope without private leakage, distinguishing advisory vs blocking, recomputing alternatives with all constraints and revalidating immediately before commit.

## Output Contract
Return `scheduling-conflict-contract` with conflict taxonomy, affected entities/privacy level, overlap interval, hard/advisory semantics, recurrence scope, override authority, alternative-generation handoff, stale-availability behavior and full-constraint tests.