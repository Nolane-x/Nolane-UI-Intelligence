---
name: designing-spaced-repetition-systems
description: Use when this specialist's decision ownership is materially in scope. Own review scheduling for memory practice, including item state, due queue, recall grading, interval updates, lapses, new/review balance, algorithm transparency, overload, and schedule recovery.
---
# Designing Spaced Repetition Systems

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own scheduling and interaction state for spaced retrieval practice. Decide item memory state, due time, new-versus-review queue, recall response/grading, interval update, lapse handling, daily limits, backlog recovery, suspension, algorithm/version visibility, and schedule provenance. This owner does not claim one scheduling algorithm is pedagogically optimal.

## Inputs and evidence

Require study items, introduction date, review history, response scale, scheduling algorithm/version/parameters, timezone/day boundary, new/review limits, lapse policy, suspended/buried state, and learner preferences. Identify sync/offline behavior and algorithm migration.

## Procedure

Show today's due/new workload and distinguish overdue backlog from newly scheduled items. During review, prompt retrieval before revealing answer. Recall grading labels should describe remembered difficulty rather than ambiguous numbers, and preview next interval where useful. Every review event updates a traceable schedule state. Suspension/bury/skip have distinct meanings. If backlog is large, offer bounded recovery settings rather than immediately scheduling thousands. Algorithm changes or parameter resets should preview effects and preserve prior history.

## Failure topology

Failures include answer visible before recall, due count changing inexplicably, timezone shift duplicating/skipping a day, "hard" versus "again" semantics unclear, backlog explosion, reset erasing history, and algorithm update rewriting intervals silently. Another failure is gamified streak pressure encouraging superficial review instead of recall quality.

## Falsification

Reject if a due item cannot explain last review/next scheduling basis at appropriate detail; if review history disappears after reschedule; if timezone/day-boundary changes cause duplicate events; if suspension and completion are conflated; if algorithm migration changes schedules without disclosure; or if overdue backlog has no manageable recovery path.

## Output contract

Return a `spaced-repetition-systems-contract` with: item memory state; review history; due/new queues; recall grading; interval update; lapse; daily limits; backlog policy; suspension/bury; timezone boundary; algorithm/version; migration/reset; and sync/offline behavior. Include one timezone change and one large-backlog scenario.

## Handoffs

Flashcards provide one study-item presentation, practice-problem workflows may feed scheduled items, progress tracking consumes practice cautiously, and learner accommodations may alter daily/interaction constraints.