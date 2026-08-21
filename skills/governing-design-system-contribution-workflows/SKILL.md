---
name: governing-design-system-contribution-workflows
description: Use when product teams propose reusable components, tokens, patterns, fixes, or documentation upstream and acceptance authority, evidence, review stages, and ownership transfer need governance.
---

# Governing Design-System Contribution Workflows

## Contribution Is an Ownership Transfer
A contribution changes who maintains a UI contract. This skill owns the path from local need to accepted shared-system capability: intake quality, evidence threshold, semantic review, technical review, accessibility review, decision authority, maintenance assignment, and release eligibility.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent defines what the component system is. This specialist determines how new or changed shared capabilities legitimately enter it.

## Intake Gate
A proposal states the problem, affected user tasks, existing alternatives, evidence of repeated need, proposed ownership boundary, interaction/state requirements, and why local composition is insufficient. A screenshot of a desired component is not an adequate contract.

Classify proposals as bug fix, missing state, API extension, new primitive, new composed pattern, token change, or documentation/usage correction. Different classes require different evidence and reviewers.

## Review Authority
Assign decision roles rather than an anonymous “team review.” Semantic ownership, implementation quality, accessibility, design coherence, and release compatibility may have different authorities. Rejection must state which admission criterion failed so the proposal can recover without political guesswork.

## Evidence
Evidence includes representative consumers, state/failure cases, implementation prototype where needed, cross-platform implications, accessibility/runtime checks, migration cost, and maintenance commitment. For a new shared primitive, demonstrate at least two genuinely related use cases rather than one product-specific screen.

## Failure Modes
Failure includes contribution queues with no decision owner, shared components accepted because they look reusable, local abstractions dumped upstream without consumer evidence, accessibility review after API freeze, and contributions merged without long-term maintainer assignment.

## Falsification
Falsification attempts to satisfy the need with existing primitives, tests a second consumer, and removes product-specific assumptions. If the proposed shared contract collapses outside its originating page or duplicates an existing owner, contribution admission is disproved.

## Recovery
Recovery narrows the proposal, returns it to local composition, or strengthens missing evidence. If review exposes a system-level gap, revise the parent architecture explicitly instead of smuggling a workaround through a component patch.

## Output
Output: `design-system-contribution-workflows-contract`, defining intake class, required evidence, reviewers/authorities, decision record, maintenance owner, and release handoff.

## Handoff
Handoff approved breaking changes to rollout governance and time-bounded deviations to exception governance.

## Sibling Boundary and delete-the-skill
Exceptions govern deviations; adoption migrations govern downstream consumption. Neither owns admission of new shared capability. The delete-the-skill test exposes an unowned transition from local artifact to canonical system contract.