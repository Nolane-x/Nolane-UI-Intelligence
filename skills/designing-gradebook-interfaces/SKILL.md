---
name: designing-gradebook-interfaces
description: Own course gradebook state across learners, activities, weighting, missing/exempt/pending values, categories, overrides, calculated totals, release visibility, and audit-safe bulk operations.
---
# Designing Gradebook Interfaces

## Decision ownership

Own the authoritative instructor view of assessed outcomes across a cohort. Decide learner/activity matrix, grade states, weighting/categories, missing versus zero versus exempt versus pending, calculated total, manual override, release status, bulk edits/imports, and audit. This owner does not decide individual rubric evaluation but must preserve its provenance.

## Inputs and evidence

Require enrollment/cohort, graded activities, scoring scales, category weights, drop-lowest/extra-credit rules, exemptions, pending grading, missing/late policy, overrides, release visibility, accommodations/privacy, and import/export. Identify different grading schemes or sections.

## Procedure

Use explicit cell states, not blank cells with overloaded meaning. Distinguish unsubmitted, submitted-pending, graded, missing, zero, exempt, excused, overridden, and hidden/unreleased. Calculated totals must expose weighting/rules and handle pending/exempt values according to policy. Bulk paste/import previews learner/activity matching and rejected cells. Overrides preserve original calculated value and rationale. Release visibility should be inspectable per grade or column; instructors must not assume a saved grade is visible to learners. Large tables require frozen identifiers, keyboard editing, and safe virtualization.

## Failure topology

Failures include blank interpreted as zero, exempt work reducing grade, weights not summing but total shown anyway, imported rows matched to wrong learners, overrides erasing original scores, and hidden grades unexpectedly released. Another failure is sorting/filtering changing row order during bulk paste and assigning grades to wrong people.

## Falsification

Reject if any grade cell's state is ambiguous; if total cannot explain its calculation; if exempt/pending policy is hidden; if import matching cannot be previewed; if override lacks original value/rationale; if release state is unknowable; or if bulk editing can apply by screen row rather than stable learner/activity identity.

## Output contract

Return a `gradebook-interfaces-contract` with: learner/activity identity; grade-state vocabulary; scoring scale; category/weight rules; missing/exempt/pending treatment; total derivation; override provenance; release visibility; bulk import/edit mapping; filters/sorts; privacy; and audit history. Include one exemption and one reordered-import scenario.

## Handoffs

Rubric/quiz grading produces scores, assignment submission supplies status, learning progress may consume completion but not expose private grade details, and export/file skills handle grade data under privacy policy.