---
name: designing-project-closure-and-archival
description: Own end-of-project closure, incomplete-work disposition, final evidence, ownership transfer, archival discoverability, retention, and controlled reopening.
---
# Designing Project Closure and Archival

## Decision ownership

Own the project lifecycle boundary between active execution and preserved historical record. Decide closure prerequisites, treatment of incomplete work, final milestone/outcome evidence, open risks/dependencies, ownership transfer, archive visibility, retention, read-only behavior, and reopening. Closure is not deletion and should not silently hide unresolved obligations.

## Inputs and evidence

Require project lifecycle policy, terminal work states, required completion evidence, unresolved item rules, financial/time records, external links, retention requirements, permissions, search/archive expectations, and reopen policy. Identify projects that can be cancelled or superseded rather than completed.

## Procedure

Offer distinct outcomes such as completed, cancelled, superseded, or abandoned when domain needs them. Before closure, summarize open work, unresolved blockers/risks, unfinished milestones, pending approvals, and ownership of follow-up. Require explicit disposition: move, cancel, convert to another project, or accept unresolved with rationale. Capture final outcome/retrospective links where appropriate. Archive should remove the project from active planning by default while preserving search, links, history, and audit evidence. Reopening must restore active status intentionally without rewriting the original closure event.

## Failure topology

Failures include archive acting like delete, unfinished work disappearing, closed projects still consuming active capacity, broken deep links, permissions changing so historical evidence becomes inaccessible, and reopen erasing original completion/cancellation context. Another failure is requiring every project to satisfy a heavyweight close checklist when the project type does not need it.

## Falsification

Reject if closure can hide unresolved critical work with no disposition; if archived projects vanish from search/history; if active portfolio totals still include archived work by default; if reopening overwrites the original close date/reason; if closure breaks references from dependent projects; or if users cannot distinguish completed from cancelled outcomes.

## Output contract

Return a `project-closure-and-archival-contract` with: terminal outcome taxonomy; closure prerequisites; unresolved-work disposition; final evidence; risk/dependency treatment; archive discoverability; active-summary exclusion; retention/access rules; deep-link preservation; reopen protocol; and historical closure event. Include one cancelled project with transferred follow-up work.

## Handoffs

Use status transitions for individual work, portfolio rollups for active/archive inclusion, risk register for unresolved risk handoff, and project templates only for future reuse—not as the archival representation of a completed project.