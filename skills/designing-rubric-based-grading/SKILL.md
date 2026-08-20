---
name: designing-rubric-based-grading
description: Own criterion-based grading across rubric versions, performance levels, points, comments, evidence selection, moderation, incomplete criteria, recalculation, and feedback release.
---
# Designing Rubric-Based Grading

## Decision ownership

Own evaluator interaction with rubrics. Decide rubric version, criteria/levels, point or qualitative mapping, criterion comments, evidence anchors, total calculation, incomplete state, moderation/second marker, overrides, and feedback release. Generic tables/forms do not own scoring provenance or rubric evolution.

## Inputs and evidence

Require submission identity, rubric/version, criteria, performance levels/descriptors, points/weights, mandatory criteria, comments, moderation process, override permissions, release policy, and gradebook integration. Identify rubric edits after grading begins.

## Procedure

Keep submission and rubric/version fixed in the grading context. Each criterion selection shows descriptor and score impact; ungraded criteria remain visibly incomplete rather than defaulting to zero unless policy says so. Evidence/comment can be anchored to submission locations. Total updates transparently from criteria and flags overrides. If rubric changes after grading starts, version or migrate with explicit impact preview. Moderation views compare grader decisions without exposing consensus prematurely where independent marking is required. Releasing feedback is separate from merely saving a grade.

## Failure topology

Failures include blank criterion treated as zero, rubric edit silently recalculating historical grades, totals disagreeing with visible criterion scores, overrides with no rationale, grader comments detached from evidence, and feedback released accidentally on save. Another failure is color-coded performance levels without readable labels.

## Falsification

Reject if rubric version cannot be identified; if incomplete criteria look finalized; if grade total cannot explain its calculation; if rubric changes can alter submitted grades silently; if override lacks actor/rationale; if independent graders can see each other's choices contrary to policy; or if save/release states are conflated.

## Output contract

Return a `rubric-based-grading-contract` with: submission/rubric version; criteria/levels; points/weights; incomplete state; evidence/comments; total calculation; override; rubric-change policy; moderation; save/finalize/release states; and audit history. Include one post-start rubric revision case.

## Handoffs

Assignment submission provides artifact identity, gradebook receives finalized results, answer review displays released criterion feedback, and academic-integrity findings may be considered under separate authority.