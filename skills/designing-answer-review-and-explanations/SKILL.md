---
name: designing-answer-review-and-explanations
description: Own post-attempt review of learner responses, correctness, scoring, explanations, feedback, rubric evidence, answer release timing, and navigation without leaking protected assessment content prematurely.
---
# Designing Answer Review and Explanations

## Decision ownership

Own what a learner can inspect after an attempt is evaluated or submitted. Decide response versus correct answer display, score/partial credit, explanation, instructor feedback, rubric criteria, attempt comparison, release timing, question navigation, and protected-item restrictions. This owner does not author the assessment or regrade it.

## Inputs and evidence

Require attempt responses, evaluated results, answer key, explanations, rubric/feedback, release policy, item-security restrictions, attempt count, regrade status, and accessibility. Identify cases where correct answers must remain hidden until a cohort window closes.

## Procedure

Bind review to a specific attempt and assessment version. Show learner response first, then correctness/score and correct/reference answer only when release policy permits. Explanations should distinguish conceptual reasoning from merely repeating the answer. For partial credit, show criterion or scoring basis. Instructor feedback remains attributable and versioned. If a regrade changes score, show current result plus regrade event rather than silently altering history. Allow navigation among reviewed questions while respecting items withheld for security; explain withholding without implying technical error.

## Failure topology

Failures include answers leaked before release, review showing a different randomized item/version, score changing with no regrade history, partial credit unexplained, withheld answers appearing as blank failures, and multiple attempts merged so learner cannot see which response earned which result. Another failure is feedback markup inaccessible to screen readers.

## Falsification

Reject if review cannot identify attempt/version; if protected correct answers can be revealed early; if score changes have no provenance; if partial credit has no basis where one exists; if multiple attempts are conflated; or if hidden/withheld content looks like missing data.

## Output contract

Return an `answer-review-and-explanations-contract` with: attempt/version identity; response; correctness/score; answer-release policy; explanation; rubric/criterion evidence; instructor feedback; regrade history; withheld-item representation; attempt comparison; navigation; and accessible equivalents. Include one delayed-answer-release case.

## Handoffs

Quiz authoring supplies keys/explanations, grading/rubrics supply evaluation, gradebook consumes final scores, and academic integrity may restrict disclosure under policy.