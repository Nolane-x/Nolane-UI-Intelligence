---
name: governing-design-system-breaking-change-rollouts
description: Use when a design-system change intentionally breaks prior consumer assumptions and release waves, opt-in windows, rollback, escape hatches, and cutover authority must be controlled.
---

# Governing Design-System Breaking-Change Rollouts

## Rollout Authority
A breaking change is not complete when code merges; it is complete when affected consumers cross a controlled cutover with bounded risk. This skill owns producer-side release sequencing, wave criteria, opt-in/opt-out rules, rollback windows, and the point at which old behavior stops being available.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent approves the new shared contract. This specialist governs how that incompatible contract becomes authoritative across consumers.

## Change Envelope
State exactly what breaks: API shape, state semantics, token meaning, DOM/anatomy, styling assumptions, accessibility behavior, or platform support. Bind the envelope to versions and known consumer classes. A vague “major release” label is not enough to define rollout risk.

## Wave Design
Choose waves by risk and observability rather than organizational convenience. A pilot wave should expose representative integration complexity while retaining rapid rollback. Define entry criteria, observation period, failure thresholds, and promotion criteria for each wave. Old and new contracts may coexist only with an explicit compatibility boundary.

## Evidence
Evidence includes compatibility findings, pilot consumer results, migration completion, runtime/visual/accessibility regressions, rollback rehearsal, and a current list of consumers still relying on old behavior. Every promotion decision references evidence from the prior wave.

## Failure Modes
Failure includes a release train that advances by calendar despite unresolved regressions, rollback that restores package version but not migrated data/tokens, escape hatches with no expiry, consumer groups missed by telemetry, and forced cutover before critical consumers can migrate.

## Falsification
Falsification triggers a representative failure during pilot, rehearses rollback after partial consumer migration, and checks whether the old contract can be restored without hidden mixed state. If rollback or containment cannot recover the promised support state, rollout readiness is false.

## Recovery
Recovery freezes promotion, returns affected consumers to the last verified contract, preserves evidence from failed waves, and routes missing capability or compatibility defects to the correct owner. Do not reinterpret the regression threshold after failure merely to continue the schedule.

## Output
Output: `design-system-breaking-change-rollouts-contract`, defining break envelope, wave plan, gates, rollback, escape-hatch expiry, cutover authority, and final old-contract retirement evidence.

## Handoff
Handoff each consumer's concrete migration steps to adoption migration and long-horizon token removal policy to deprecation lifecycle governance.

## Sibling Boundary and delete-the-skill
Version compatibility defines supported combinations; adoption migration executes consumer change. Neither owns staged producer release authority and rollback across a breaking transition. Removing this skill leaves that material rollout decision unowned, satisfying the delete-the-skill test.