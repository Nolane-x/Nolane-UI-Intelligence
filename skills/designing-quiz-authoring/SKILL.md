---
name: designing-quiz-authoring
description: Use when this specialist's decision ownership is materially in scope. Own construction of quizzes and question banks across item types, answer keys, scoring, randomization, pools, feedback, attempts, timing, release rules, and pre-publication validation.
---
# Designing Quiz Authoring

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own instructor/editor creation of structured assessments. Decide quiz identity/version, question/item model, answer keys/rubrics, points, pools/randomization, ordering, attempts, timing, feedback release, availability, accommodations hooks, and validation before publish. Generic form builders do not own scoring/randomization/evaluation semantics.

## Inputs and evidence

Require supported question types, scoring rules, partial credit, answer variants, item-bank identity, randomization/pools, attempts, time limits, feedback policy, availability, accessibility, grading integration, and version behavior after learners begin. Identify question edits that would invalidate existing attempts.

## Procedure

Separate draft quiz definition from learner attempt instances. Each question has stable identity and version plus scoring/answer evidence. Random pools should preview possible count/composition and prevent impossible selection constraints. Point totals and partial-credit rules update transparently. Feedback settings specify when learners see correctness, answers, explanations, or score. Pre-publish validation finds missing answers, zero/duplicate points, inaccessible media, contradictory pool rules, and timing/attempt gaps. Once attempts exist, material edits should version or explicitly handle existing attempts rather than rewriting history.

## Failure topology

Failures include missing correct answer, random pool requesting more items than available, points totals silently changing, feedback releasing answers before all attempts, question edit altering already-submitted scores, and preview not matching learner experience. Another failure is inaccessible question media with no text alternative or accommodation route.

## Falsification

Reject if a publishable quiz contains unresolved scoring-invalid items; if randomization constraints cannot be satisfied; if feedback timing is ambiguous; if material edits can mutate historical attempts silently; if point totals differ between authoring and gradebook; or if learner preview cannot reproduce timing/navigation constraints.

## Output contract

Return a `quiz-authoring-contract` with: quiz/version; question identities/types; scoring/partial credit; points; pools/randomization; order; attempts; timing; feedback release; availability; accommodation hooks; validation findings; learner preview; and edit-after-attempt policy. Include one impossible pool and one post-attempt edit case.

## Handoffs

Quiz taking consumes the published definition, timed assessment handles active clock behavior, gradebook consumes results, rubric grading applies to open responses, and accessibility/media owners validate question content.