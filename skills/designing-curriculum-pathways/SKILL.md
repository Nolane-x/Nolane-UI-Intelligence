---
name: designing-curriculum-pathways
description: Own multi-course learning paths, prerequisites, alternatives, electives, equivalencies, branching, transfer credit, progress, and next-step recommendations grounded in curriculum rules.
---
# Designing Curriculum Pathways

## Decision ownership

Own sequencing and requirement logic across courses/modules in a curriculum or program. Decide prerequisite graph, required versus elective components, alternative/equivalent choices, branches, transfer/exemption treatment, path progress, and what qualifies a learner to move forward. This differs from a simple course catalog or project dependency graph because educational requirements and equivalencies matter.

## Inputs and evidence

Require program version, required courses/credits, prerequisites/corequisites, elective groups, equivalencies, transfer-credit rules, exemptions, learner completions/attempts, course availability, and credential requirements. Identify rules that vary by cohort or program version.

## Procedure

Represent requirements as explainable groups: complete all, choose N of M, complete one equivalent, satisfy prerequisite, or earn credit. A learner's path view must show satisfied, in-progress, eligible-next, unavailable, and blocked states with reason. Transfer/exemption credit should satisfy requirements without pretending the original course was taken. Recommendations may prioritize efficient next options but must distinguish advice from mandatory sequence. Program/version changes require a comparison/migration rule so learners do not lose earned credit silently.

## Failure topology

Failures include a linear path drawn for a branching curriculum, elective choice counted twice, transfer credit shown as course completion, prerequisites using old program rules, unavailable courses trapping progression, and recommendation presented as required. Another failure is a progress bar whose denominator changes after electives are selected with no explanation.

## Falsification

Reject if a requirement cannot explain why it is satisfied/blocked; if equivalent courses can double-count; if transfer/exemption provenance is hidden; if program version affecting rules is unknown; if an unavailable required course has no alternative/escalation path; or if learner progress changes retroactively after curriculum update without migration evidence.

## Output contract

Return a `curriculum-pathways-contract` with: program/version; requirement groups; prerequisite/corequisite graph; elective/alternative/equivalence rules; transfer/exemption handling; learner state per requirement; progress derivation; eligible-next logic; availability blockers; recommendation distinction; and curriculum migration policy. Include one transfer-credit and one choose-two-of-four case.

## Handoffs

Course catalog provides offering availability, learning progress consumes requirement state, credential completion uses the final program contract, and generic dependency graph may render prerequisite relationships without owning educational logic.