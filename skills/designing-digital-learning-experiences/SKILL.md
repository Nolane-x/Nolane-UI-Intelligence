---
name: designing-digital-learning-experiences
description: Own the interaction architecture for digital learning systems where curriculum, learner state, practice, assessment, feedback, progress, credentials, instructor oversight, and accommodations must cohere.
---
# Designing Digital Learning Experiences

## Decision ownership

Own the top-level learning-state model. Decide how courses/modules/lessons, prerequisites, progress, practice, assessment, feedback, mastery, instructor actions, completion, and accommodations relate. This owner does not determine pedagogy or subject content; it ensures the interface distinguishes exposure from learning evidence and treats assessment/progress as state with provenance rather than decoration.

## Inputs and evidence

Require learner roles, course/curriculum structure, enrollment model, prerequisites, lesson/activity types, progress rules, mastery/completion criteria, assessment policies, attempts, grading, accommodations, cohort/instructor roles, credential rules, and privacy. Inspect incomplete, transferred, repeated, failed, and accommodated learners—not only a first-time linear happy path.

## Procedure

Define canonical learning entities and state transitions before page layout. Separate content viewed, activity attempted, activity completed, assessed performance, mastery, and credential completion; do not collapse them into one percentage. Preserve learner position and explain what is required next. Prerequisites and locked content need rationale plus the condition to unlock. Feedback and review should be tied to an attempt or submission. Instructor overrides, extensions, exemptions, and accommodations require scope/provenance and must not silently rewrite the learner's original evidence. Completion criteria should be inspectable and stable across catalog, course, gradebook, and credential surfaces.

## Failure topology

Failures include progress percentages with no denominator, watching a video counting as mastery, hidden prerequisites, retakes overwriting earlier evidence, instructor overrides with no history, accommodations exposed to peers, and course completion shown differently across surfaces. Another failure is a learner trapped by a broken prerequisite or unavailable activity with no recovery path.

## Falsification

Reject if users cannot distinguish completion from mastery; if a progress value cannot explain its contributing requirements; if failed/earlier attempts disappear after retry; if accommodations leak sensitive details beyond authorized roles; if prerequisite locks have no reason/unlock path; or if credential eligibility disagrees with the course's canonical completion state.

## Output contract

Return a `digital-learning-experiences-contract` containing: learning entity model; enrollment state; prerequisite/lock rules; viewed/attempted/completed/mastered distinctions; progress derivation; attempt/submission identity; feedback linkage; instructor override provenance; accommodation boundaries; completion/credential criteria; and blocked-state recovery. Include one retake and one exempted-requirement scenario.

## Handoffs

Delegate catalog, curriculum, lesson navigation, progress, practice, quiz authoring/taking, timed assessments, question navigation, review/explanation, grading, gradebook, submissions, integrity review, spaced repetition, flashcards, credentials, cohort analytics, and accommodations to dedicated owners. Generic content/forms/playback remain supporting mechanics.