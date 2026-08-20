---
name: designing-learning-progress-tracking
description: Use when this specialist's decision ownership is materially in scope. Own derivation and display of learner progress from requirements, activities, attempts, mastery, exemptions, and time without collapsing educational evidence into one misleading percentage.
---
# Designing Learning Progress Tracking

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own progress state across a course or program. Decide denominator/requirements, activity completion, partial state, assessed mastery, optional content, exemptions, transfer credit, overdue/stalled state, and progress history. This owner distinguishes progress toward completion from performance and from time spent.

## Inputs and evidence

Require curriculum/course requirements, activity completion rules, attempts/submissions, grade/mastery thresholds, optional items, exemptions, transfer credit, dates, and synchronization across devices. Identify activities with asynchronous grading where completion and score arrive at different times.

## Procedure

Expose how progress is calculated. Use requirement-based counts or weighted structures only when defined, and allow drill-down from aggregate to unsatisfied requirements. Keep completion progress separate from mastery/grade and from engagement/time metrics. Optional activities do not reduce completion unless selected into a requirement group. Pending grading should produce a pending state rather than false incomplete or complete. Exemptions/transfer satisfy requirements with their own provenance. Stalled/overdue cues need an evidence-based rule and should not shame learners.

## Failure topology

Failures include arbitrary percent complete, optional lessons inflating denominator, high grade shown as completed curriculum despite missing requirements, pending grading treated as failure, transfer credit hidden, and progress regressing because catalog content was added mid-course without migration rule. Another failure is public leaderboards exposing educational performance without consent.

## Falsification

Reject if a percentage cannot explain its numerator/denominator; if completion and performance are visually conflated; if optional content changes required progress unexpectedly; if pending evaluation looks failed; if transfer/exemption has no provenance; if curriculum updates can reduce earned completion silently; or if sensitive progress is exposed beyond authorized roles.

## Output contract

Return a `learning-progress-tracking-contract` with: requirement basis; completed/in-progress/pending/mastered distinctions; optional/exempt/transfer handling; aggregate derivation; drill-down; curriculum-update behavior; stalled/overdue rule; history; and privacy scope. Include one pending-grade and one curriculum-change case.

## Handoffs

Curriculum pathways define requirements, lesson/assessment/submission owners produce evidence, gradebook provides graded outcomes, and credentials consume completion state without redefining it.