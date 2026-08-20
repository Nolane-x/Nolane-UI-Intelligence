---
name: designing-assessment-question-navigation
description: Use when this specialist's decision ownership is materially in scope. Own navigation across assessment questions, sections, passages, flags, answered state, locked sequencing, review screens, and large-item maps while respecting timing and exam policy.
---
# Designing Assessment Question Navigation

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own movement and orientation inside an assessment attempt. Decide one-at-a-time versus paged presentation, item map, section boundaries, forward/back restrictions, passage-linked groups, answered/unanswered/flagged state, review mode, and how navigation behaves near submission. Generic lesson navigation cannot override exam policy.

## Inputs and evidence

Require question count/order, randomization, sections, passage/stimulus grouping, navigation restrictions, ability to revisit, flagging, timing, accessibility, mobile display, and submission policy. Identify adaptive assessments where future items do not yet exist.

## Procedure

Keep current question/section position and total recoverable. For large assessments, provide an item navigator that encodes answered/unanswered/flagged/current without revealing correctness. Respect locked sections or no-backtracking rules and explain consequences before leaving when the transition becomes irreversible. Stimulus/passage context should remain available across linked questions. Review mode summarizes incomplete/flagged items and navigation availability. Adaptive tests must not imply a fixed total or unavailable future questions. Keyboard/screen-reader paths need equivalent navigation and status labels.

## Failure topology

Failures include question numbers changing after resume, item map colors with no labels, irreversible section exit without warning, passage disappearing while answering linked questions, flagged state lost, adaptive future items shown as locked errors, and review allowing navigation that policy forbids. Another failure is a sticky navigator covering question content on small screens.

## Falsification

Reject if current/total state is misleading; if navigation policy cannot be understood before an irreversible transition; if answered/flagged states rely only on color; if passage context cannot be recovered; if randomization changes item identity on resume; or if keyboard/screen-reader users cannot reach and interpret the question map.

## Output contract

Return an `assessment-question-navigation-contract` with: presentation mode; current/total semantics; sections; item-map states; passage grouping; forward/back restrictions; irreversible-transition warning; flagging; review behavior; adaptive-test handling; resume stability; and accessible navigation. Include one no-backtracking section boundary.

## Handoffs

Quiz/timed assessment provide attempt/clock state, answer review applies after submission, and generic navigation components provide structural mechanics.