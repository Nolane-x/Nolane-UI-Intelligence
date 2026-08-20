---
name: designing-roadmap-timelines
description: Use when this specialist's decision ownership is materially in scope. Own multi-horizon roadmap views that communicate strategic sequencing, confidence, date precision, dependencies, and scope without presenting uncertain plans as fixed schedules.
---
# Designing Roadmap Timelines

## Parent Contract

**Required parent:** `designing-project-and-work-management`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the roadmap as a planning communication surface across months or quarters. Decide item granularity, time precision, confidence bands, grouping, dependency cues, now/next/later versus dated representation, zoom levels, and traceability from roadmap intent to underlying work. A roadmap is not a Gantt chart by default and must not fabricate exact dates from low-confidence strategy.

## Inputs and evidence

Require planning horizon, roadmap object types, date confidence, milestone relationships, dependency structure, audience, release cadence, portfolio grouping, update frequency, and whether commitments differ by audience. Determine which dates are contractual, forecast, target, or merely ordering hints.

## Procedure

Model time with precision proportional to evidence. Use ranges or quarter-level bands when exact dates are unjustified, and label confidence or commitment class where it matters. Preserve strategic grouping by outcome/product/theme while maintaining links to executable projects and milestones. Dependencies should show sequence pressure without turning every relationship into an unreadable line; allow focused dependency reveal. Zoom changes may alter detail but not silently change meaning. Historical shifts should be inspectable for important commitments. Sharing/export must retain date-confidence semantics rather than flattening everything into exact endpoints.

## Failure topology

Failures include false precision, timeline bars interpreted as committed delivery dates, roadmaps detached from actual project state, dependency spaghetti, overlapping labels that hide scope, and moving targets with no historical trace. Another failure is a roadmap that becomes a project plan at high zoom and loses its strategic outcome framing.

## Falsification

Reject if forecast and committed dates are visually indistinguishable; if a roadmap item cannot link to an owner/project/milestone; if zooming changes an approximate quarter into an exact day without evidence; if users cannot identify why an item moved; or if dependency visualization makes the roadmap less readable than a list for representative data.

## Output contract

Return a `roadmap-timelines-contract` containing: roadmap object taxonomy; time-precision levels; confidence/commitment encoding; grouping; zoom behavior; dependency reveal; underlying-work linkage; change history; audience variants; and export semantics. Include one uncertain long-range item and one fixed contractual milestone.

## Handoffs

Use milestone tracking for discrete commitments, project dependencies for executable blockers, portfolio rollups for cross-project aggregation, and generic calendar/time-series layout only as implementation support.