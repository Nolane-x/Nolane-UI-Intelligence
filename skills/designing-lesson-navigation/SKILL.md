---
name: designing-lesson-navigation
description: Own within-course navigation across lessons, sections, activities, checkpoints, prerequisites, position memory, next/previous logic, sidebars, and return-to-context after deep links.
---
# Designing Lesson Navigation

## Decision ownership

Own how a learner moves through the internal structure of a course. Decide outline hierarchy, current position, next/previous behavior, gated activities, optional branches, progress markers, resume point, deep links, and relationship between content navigation and assessment boundaries. Generic navigation does not own pedagogical sequencing or completion state.

## Inputs and evidence

Require course outline, lesson/activity types, prerequisites/gates, optional items, estimated duration, progress state, resume policy, deep-link permissions, mobile/offline constraints, and accessibility. Identify courses that are nonlinear versus strictly sequenced.

## Procedure

Keep the course outline and current lesson location recoverable without permanently occupying excessive space. Next/previous follows curriculum sequence, not browser history, and must explain when an item is locked or optional. Resume should identify the last meaningful learner position while avoiding repeatedly returning to an already-completed transient item. Deep links reveal surrounding course context and prerequisite state. Progress indicators distinguish completed from current/available. For long lessons, local headings/bookmarks can coexist with course-level navigation without confusing the hierarchy.

## Failure topology

Failures include next skipping required activities, browser Back used as course sequencing, locked lessons with no reason, resume reopening an assessment mid-submission without state recovery, deep links making learners unaware of course context, and sidebar progress relying only on checkmarks that imply mastery. Another failure is mobile navigation hiding the course outline with no quick return.

## Falsification

Reject if next/previous sequence can contradict curriculum rules; if a locked lesson cannot state unlock condition; if resume loses an in-progress activity state; if a deep-linked lesson cannot reveal course/path location; if optional and required items are indistinguishable; or if keyboard/screen-reader navigation cannot recover current outline position.

## Output contract

Return a `lesson-navigation-contract` with: outline hierarchy; current-position cues; next/previous rules; required/optional/gated states; unlock explanation; resume policy; deep-link context; progress markers; local lesson navigation; mobile/accessible outline behavior; and in-progress recovery. Include one locked and one nonlinear branch scenario.

## Handoffs

Curriculum pathways own cross-course sequencing, progress tracking supplies state, quiz/assessment owners control in-progress test navigation, and generic navigation supplies structural components.