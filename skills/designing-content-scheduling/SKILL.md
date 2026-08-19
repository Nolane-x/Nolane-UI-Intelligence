---
name: designing-content-scheduling
description: Use when publication is deferred to a future time and the interface must coordinate timezone, revision binding, schedule authority, editing after scheduling, cancellation, missed execution, and destination-specific timing.
---

# Designing Content Scheduling

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns future publication timing. It is not generic calendar scheduling: a scheduled publication binds a content revision and destination to a future execution contract. It does not own recurrence or general appointment booking.

## Decision Boundary
Capture the intended wall-clock time, timezone, destination, and revision together. Never store/display a bare “9:00 AM” without timezone authority. If the author travels or changes account timezone later, decide whether the schedule preserves the originally chosen instant or the local wall-clock intent and make that behavior explicit.

Editing after scheduling creates revision ambiguity. Choose whether edits automatically update the scheduled revision, create an unscheduled draft while the scheduled version remains fixed, or require an explicit “Update scheduled version.” A status such as “Scheduled” should identify which revision will publish. If approval becomes invalid after edits, the schedule may need to block or return to review rather than publish stale/unapproved content.

Execution state must survive outages and delays. Distinguish scheduled, queued, publishing, published, missed, failed, cancelled, and rescheduled. If a scheduler runs late, do not backdate the visible publish time as if it executed on time. Destination rate limits or external outages may create partial schedule outcomes that need explicit recovery.

## Failure Topology
- Author selects 09:00 in Hanoi, account timezone later changes, and content publishes at an unintended instant.
- Content is edited after scheduling but UI never shows whether the scheduled job uses old or new revision.
- “Scheduled” remains green after required approval is revoked.
- Scheduler outage causes publication hours late while the timeline claims the planned time as actual publication time.
- Cancel button disappears during a queue window even though cancellation is still technically possible, or remains active after irreversible publish began.
- Multi-channel schedule reports success although one destination rejected the release.

## Falsification and Recovery
Falsify with DST transition, timezone change, revision edit after schedule, approval invalidation, service outage across scheduled time, cancellation just before execution, multi-channel partial failure, device offline when the job executes, and screen-reader review of date/time. The design fails if the scheduled artifact cannot be reconstructed as `{revision, destination, intended time, timezone, execution state}`.

Recover by binding schedule identity to content revision and timezone, exposing edit/schedule coupling, revalidating prerequisites before execution, recording planned versus actual times, defining cancellation boundaries, and representing destination outcomes independently.

## Output Contract
Return `content-scheduling-contract` with schedule identity, timezone/instant semantics, revision binding, post-schedule edit behavior, prerequisite revalidation, lifecycle states, planned-vs-actual timing, cancellation/reschedule rules, multi-destination outcomes, and falsification cases.