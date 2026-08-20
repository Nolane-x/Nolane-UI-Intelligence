---
name: designing-practice-problem-workflows
description: Use when this specialist's decision ownership is materially in scope. Own low-stakes practice interactions across problem selection, attempt state, hints, feedback, solution reveal, retries, mastery evidence, and deliberate practice sequencing.
---
# Designing Practice Problem Workflows

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the learner experience for formative practice rather than scored high-stakes assessment. Decide attempt flow, answer submission, immediate/delayed feedback, hints, worked solutions, retry behavior, difficulty/adaptive sequencing, streak/mastery evidence, and whether practice counts toward progress. This owner must preserve a safe distinction between learning opportunity and evaluation.

## Inputs and evidence

Require problem types, solution/rubric, hint hierarchy, feedback policy, retry limits if any, adaptive selection rules, difficulty metadata, mastery model, progress credit, accessibility, and offline state. Identify problems with multi-step reasoning where final-answer correctness alone is insufficient.

## Procedure

Let learners commit an attempt before revealing correctness where retrieval practice matters. Feedback should identify the relevant error/strategy without automatically giving the full solution unless policy says so. Hints may be progressive and record use only if educationally relevant, not as punishment. Retries preserve previous attempts and can vary problem parameters. Worked solution reveal should clearly end or alter the practice opportunity. Adaptive next-problem choice should explain enough of its purpose without pretending algorithmic certainty. Practice progress and formal grades remain distinct.

## Failure topology

Failures include revealing answers on first focus, retries overwriting prior thinking, hints penalizing learners unexpectedly, practice scores appearing in formal grade surfaces, repetitive items encouraging memorization, and adaptive difficulty jumping with no recovery. Another failure is feedback saying only "incorrect" when the system has actionable diagnostic evidence.

## Falsification

Reject if practice can change formal grade without explicit policy; if previous attempts disappear; if solution reveal does not change future attempt semantics; if hint consequences are hidden; if adaptive selection can trap a learner at an inappropriate difficulty with no override; or if feedback exposes correct answers before the learner intentionally submits.

## Output contract

Return a `practice-problem-workflows-contract` with: problem selection; attempt lifecycle; answer commit; feedback timing/type; hint levels; solution reveal; retry/history; adaptive/difficulty logic; mastery/progress contribution; formal-grade separation; accessibility; and offline recovery. Include one multi-attempt hint-use scenario.

## Handoffs

Quiz taking owns scored assessment, spaced repetition may schedule practice, answer review explains evaluated attempts, and progress tracking consumes only policy-approved completion/mastery evidence.