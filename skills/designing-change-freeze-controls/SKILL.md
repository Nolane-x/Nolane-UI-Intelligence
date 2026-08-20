---
name: designing-change-freeze-controls
description: Use when this specialist's decision ownership is materially in scope. Own scheduled or policy-driven change freezes across environments/services, including scope, time zones, exception requests, emergency changes, visibility, and overlap with locks or maintenance.
---
# Designing Change Freeze Controls

## Parent Contract

**Required parent:** `designing-software-delivery-pipelines`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own broad policy windows that restrict classes of changes for a defined scope/time. Decide freeze scope, schedule/timezone, prohibited and allowed change types, exception workflow, emergency path, visibility, recurrence, and interaction with local deployment locks. This differs from a target lock because it represents organizational policy rather than one operational hold.

## Inputs and evidence

Require freeze policy, calendars, scope hierarchy, change categories, timezone, recurring holidays/events, exception approvers, emergency authority, affected pipelines, and notification rules. Identify teams operating across time zones where local date labels can be misleading.

## Procedure

Show upcoming and active freezes in planning and deployment contexts. Every freeze needs effective start/end with timezone, scope, affected action classes, owner/policy source, and exception process. Overlapping freezes should resolve to the strictest applicable policy while showing each source. Exception requests must bind to a specific change/artifact/scope and expire after use/window. Emergency change paths need stronger audit, not a hidden bypass. Recurring freeze schedules should preview future occurrences and handle calendar exceptions explicitly.

## Failure topology

Failures include surprise late-stage deployment denial, timezone ambiguity, one exception accidentally becoming a permanent exemption, overlapping freezes producing contradictory behavior, emergency bypass with no audit, and ended freezes continuing to block due stale cache. Another failure is users interpreting a freeze as proof that no change occurred despite emergency exceptions.

## Falsification

Reject if a user planning a deployment cannot see an applicable upcoming freeze; if effective time is ambiguous; if exception scope can exceed the approved artifact/change; if emergency bypass lacks authority/rationale; if overlapping policies cannot explain the final restriction; or if freeze history omits approved exceptions.

## Output contract

Return a `change-freeze-controls-contract` with: policy source; scope; prohibited/allowed changes; start/end/timezone; recurrence; overlap resolution; exception request/approval/scope; emergency path; planning/deployment visibility; notifications; and history. Include one cross-time-zone freeze boundary.

## Handoffs

Deployment locks represent local operational holds, release trains consume freeze calendars, target selection displays active restrictions, and approval workflows handle exceptions under this policy.