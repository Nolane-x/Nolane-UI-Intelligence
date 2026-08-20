---
name: designing-course-catalogs
description: Use when this specialist's decision ownership is materially in scope. Own discovery and selection of learning offerings across subject, level, prerequisites, duration, modality, availability, enrollment status, credentials, and learner fit without conflating marketing with curriculum truth.
---
# Designing Course Catalogs

## Parent Contract

**Required parent:** `designing-digital-learning-experiences`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own course/program discovery before enrollment. Decide catalog taxonomy, search/filter, course summary fields, level/difficulty, prerequisites, expected effort/duration, modality, schedule/availability, credential relation, enrollment state, saved interest, and how learner-specific eligibility is explained. Generic product catalogs do not own prerequisite or educational-path semantics.

## Inputs and evidence

Require offering taxonomy, course metadata, instructors/providers, prerequisites, level, language, duration/effort, modality, cohort dates, enrollment limits, price if applicable, credentials, accessibility/accommodation info, and learner enrollment/history. Identify fields that are estimates versus fixed requirements.

## Procedure

Expose enough course truth in results to compare meaningful options: subject/outcome, level, effort/duration, modality, availability, prerequisite status, and credential/path context. Filters should reflect educational intent rather than only marketing tags. Learner-specific states—enrolled, completed, eligible, prerequisite missing, waitlisted—must be clear but not reveal sensitive history publicly. Course detail links to curriculum/path requirements and states what completion actually means. Dates/effort estimates need confidence/definitions. Saved courses should not imply enrollment.

## Failure topology

Failures include difficulty labels with no basis, prerequisites hidden until checkout/enrollment, duplicate course versions indistinguishable, "8 weeks" confused with fixed calendar duration, completed courses resurfacing as new with no version cue, and catalog ranking driven by popularity while learner eligibility is obscured. Another failure is inaccessible offerings with no accommodation/contact information.

## Falsification

Reject if a learner can attempt enrollment without seeing a known blocking prerequisite; if versions/cohorts cannot be distinguished; if duration/effort meaning is ambiguous; if saved and enrolled states look the same; if completed-history personalization leaks to unauthorized viewers; or if catalog filters exclude relevant offerings because taxonomy cannot represent multidisciplinary paths.

## Output contract

Return a `course-catalogs-contract` with: offering taxonomy; result-card fields; search/filter facets; version/cohort identity; level/effort/duration semantics; prerequisite/eligibility state; enrollment/saved/completed states; credential/path linkage; modality/language/accessibility information; and detail comparison behavior. Include one prerequisite-blocked and one course-version scenario.

## Handoffs

Curriculum pathways own program sequencing, course enrollment/onboarding mechanics may reuse generic flows, lesson navigation begins after entry, and completion/credentials consume canonical course identity.