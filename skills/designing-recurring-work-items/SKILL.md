---
name: designing-recurring-work-items
description: Use when this specialist's decision ownership is materially in scope. Own recurring project work definitions, instance generation, schedule changes, skipped occurrences, completion independence, and future-versus-current edit scope.
---
# Designing Recurring Work Items

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own recurrence for work items. Decide whether recurrence creates distinct instances or reopens one item, generation timing, schedule rule, exceptions, skipped occurrences, edit-this/edit-future scope, ownership/field inheritance, and how history remains intelligible. Calendar recurrence mechanics are a reference, but project work has completion and backlog consequences that require distinct treatment.

## Inputs and evidence

Require recurrence patterns, time zones, generation lead time, assignment rules, fields copied to instances, dependency behavior, completion independence, exception needs, holidays/non-working days, and reporting expectations. Determine whether each occurrence must have a stable ID for audit and metrics.

## Procedure

Prefer distinct occurrence identities when completion, comments, evidence, or metrics matter. Show next generation date and rule in human-readable form. Editing an occurrence must clearly separate "this instance", "this and future", and "series" where supported. Skipping should create an explicit skipped record or exception rather than silently deleting evidence. If an overdue instance remains open when the next generates, show both and define whether backlog can accumulate. Changes to assignment/template fields should specify what propagates to future instances versus already-created work.

## Failure topology

Failures include one task repeatedly reopening and erasing prior completion, changing a series unexpectedly rewriting historical items, skipped work disappearing from reports, duplicate generation around time-zone changes, future items inheriting stale ownership, and recurring overdue items piling up with no policy. Another failure is applying meeting-style recurrence without project-specific instance identity.

## Falsification

Reject if a completed occurrence loses its comments/evidence when the next recurrence starts; if editing one instance can alter past instances without explicit scope; if DST/time-zone change can generate duplicates; if skipping an occurrence leaves no trace where compliance/history matters; if two open occurrences are impossible to distinguish; or if series changes have no effective-from point.

## Output contract

Return a `recurring-work-items-contract` containing: series identity; occurrence identity; recurrence rule; time-zone basis; generation timing; copied/inherited fields; edit-scope options; skip/exception semantics; overdue-overlap policy; series termination; and reporting/history behavior. Include one DST boundary and one edit-future scenario.

## Handoffs

Use generic recurring events for calendar rule parsing when appropriate, project templates for instance content, assignment for owner changes, and status transitions for each occurrence's independent lifecycle.