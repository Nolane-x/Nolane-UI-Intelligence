---
name: designing-learning-accommodation-controls
description: Use when this specialist's decision ownership is materially in scope. Own authorized learning and assessment accommodations such as extended time, alternate formats, attempts, deadlines, navigation rules, assistive access, and exemptions with privacy, scope, precedence, and provenance.
---
# Designing Learning Accommodation Controls

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own configuration and effective-value visibility for learner-specific or group accommodations. Decide accommodation type, scope, effective dates, course/activity override precedence, authorized roles, privacy, application to existing attempts, conflict resolution, and learner-visible confirmation. This owner does not determine eligibility or medical/disability basis; it minimizes exposure of reasons.

## Inputs and evidence

Require authorized accommodation record, learner/group identity, allowed adjustment types, base course/assessment settings, scope, effective dates, precedence rules, active attempts, instructor authority, audit, and privacy policy. Identify adjustments such as time multiplier, attempts, deadline, breaks, alternate format, no-backtracking exception, or content exemption.

## Procedure

Store the adjustment separately from sensitive rationale wherever possible. Show instructors the effective operational value and scope, not unnecessary diagnostic details. Precedence must be deterministic across institution/course/activity/individual layers. Before an assessment starts, verify effective timing/attempt/navigation accommodations; changes during an active attempt need explicit policy and audit. Learners should be able to confirm applied accommodations in appropriate terms without publicly exposing them. Expiration or course-copy operations should not silently drop adjustments.

## Failure topology

Failures include extended time configured but not applied, private accommodation reason visible to peers/unauthorized staff, two overrides combining unexpectedly, changes mid-exam resetting timer, copied course losing accommodations, and instructor unable to tell effective setting. Another failure is visually marking accommodated learners in gradebook in a stigmatizing way.

## Falsification

Reject if effective accommodation cannot be computed/explained; if sensitive rationale is exposed beyond need; if an active attempt can change timing without controlled policy; if precedence conflicts are unresolved; if course/version copy can silently discard accommodation; or if learner confirmation differs from actual effective assessment settings.

## Output contract

Return a `learning-accommodation-controls-contract` with: adjustment type/value; learner/group; scope; effective dates; precedence; base-versus-effective setting; authorized roles; privacy/minimal rationale; active-attempt policy; learner confirmation; copy/migration behavior; expiration; and audit provenance. Include one overlapping time-override scenario.

## Handoffs

Timed assessments consume effective time, quiz/navigation owners consume attempt/navigation adjustments, curriculum/progress consume exemptions, and privacy/accessibility owners govern disclosure and interface equivalence.