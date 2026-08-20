---
name: designing-milestone-tracking
description: Own discrete project checkpoints with target dates, acceptance evidence, dependency readiness, confidence, status, and completion criteria.
---
# Designing Milestone Tracking

## Decision ownership

Own milestone semantics as evidence-backed checkpoints, not decorative dates. Decide what constitutes a milestone, target versus actual date, readiness criteria, dependency status, confidence, completion evidence, and how missed or moved milestones retain history. Tasks and sprints may contribute to milestones but do not define them.

## Inputs and evidence

Require milestone types, date authority, acceptance criteria, contributing work, dependency relationships, responsible owner, reporting cadence, escalation rules, and whether milestones can be externally committed. Identify milestones where completion is a manual declaration versus derived from required deliverables.

## Procedure

Expose target date, owner, acceptance definition, and dependency readiness together so a date is not interpreted without evidence. Separate forecast movement from actual completion. When milestones are derived, show which required deliverables remain open; when manual, require a concise completion artifact or rationale where governance needs it. Moving a committed milestone should preserve old target, actor, reason, and affected downstream items. At project overview scale, prioritize upcoming, at-risk, blocked, missed, and recently completed milestones rather than showing every historical checkpoint equally.

## Failure topology

Failures include milestones marked complete because the date passed, changed target dates overwriting history, green milestones with unresolved required deliverables, duplicate milestones across roadmap/project views, and status based solely on manual color. Another failure is treating every task due date as a milestone, destroying signal.

## Falsification

Reject if completion can occur without meeting or explicitly waiving acceptance criteria; if moving a target erases the previous commitment; if a blocked dependency does not affect readiness; if the same milestone has divergent dates in project and roadmap surfaces; or if users cannot distinguish target, forecast, and actual dates.

## Output contract

Return a `milestone-tracking-contract` with: milestone taxonomy; target/forecast/actual dates; acceptance evidence; owner; contributing-work linkage; dependency readiness; risk state; reschedule provenance; completion/waiver protocol; and overview prioritization. Include one moved committed milestone and one derived incomplete milestone.

## Handoffs

Use roadmaps for long-horizon placement, dependency networks for prerequisite logic, project health for aggregate risk, and stakeholder communication when changes require external notice.