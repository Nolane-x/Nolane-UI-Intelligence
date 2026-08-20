---
name: designing-quiz-taking
description: Own learner quiz attempts across start, answer state, save, navigation, submit, retries, connectivity, feedback release, and distinction between recorded versus unsaved responses.
---
# Designing Quiz Taking

## Decision ownership

Own the active attempt experience for ordinary quizzes. Decide start/resume, question presentation, answer selection/input, save state, navigation, unanswered flags, submit review, confirmation, network recovery, attempt completion, and feedback release. Timed/high-stakes clock behavior is delegated when applicable.

## Inputs and evidence

Require published quiz/version, question order/randomization, attempt limits, answer types, autosave, connectivity model, submit policy, navigation freedom, feedback release, accessibility, and device/session constraints. Identify questions where media or external tools load asynchronously.

## Procedure

Bind the learner to one stable attempt and quiz version. Every response should show saved/saving/failed state when persistence is asynchronous. Navigation preserves answers and indicates answered/unanswered/flagged without revealing correctness unless policy allows. Before final submit, summarize unanswered or incomplete items and consequences. Submission must be idempotent and produce a receipt/attempt state. Connectivity loss should keep local responses where safe, show uncertainty, and reconcile before final submission. Resuming an attempt restores question order and existing answers.

## Failure topology

Failures include answers appearing selected but not saved, accidental double submission, back navigation losing input, random order changing on resume, feedback shown before permitted, offline responses overwritten by stale server state, and submit proceeding while saves are pending. Another failure is a "completed" screen with no evidence the server accepted the attempt.

## Falsification

Reject if recorded versus local-unsaved answer cannot be distinguished; if resume can reshuffle question identity; if final submit can race pending saves; if duplicate submit creates two attempts; if network reconciliation can silently discard a newer response; or if attempt receipt/status is absent.

## Output contract

Return a `quiz-taking-contract` with: attempt/version identity; start/resume; question/order stability; response states; autosave/connectivity; navigation flags; submit review; idempotent submission; receipt; retry/attempt limit; feedback-release gating; and accessibility behavior. Include one offline-reconcile scenario.

## Handoffs

Timed assessments add clock/deadline authority, question navigation specializes large/high-stakes navigation, answer review handles post-submit explanations, and quiz authoring defines the immutable attempt inputs.