---
name: governing-design-system-adoption-migrations
description: Use when a product or product fleet must move from legacy UI contracts to a newer design-system version and coexistence, sequencing, codemods, manual decisions, and completion evidence need control.
---

# Governing Design-System Adoption Migrations

## Migration Scope
This skill owns the consumer-side transition from an old design-system contract to a new one. It is concerned with coexistence, sequencing, automation boundaries, state/behavior parity, product risk, and proof that legacy dependencies are gone. It does not decide the producer's compatibility promise.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent supplies the target component-system architecture. This specialist turns that target into a controlled multi-surface adoption program.

## Migration Map
Inventory legacy components/tokens/styles, target replacements, consumers, ownership teams, traffic/criticality, known customizations, and blockers. Classify mappings as mechanical one-to-one, semantic one-to-many, behavior-changing, unsupported, or requiring redesign. Only the first class is a safe default for codemods.

## Coexistence Strategy
Define whether old and new systems may coexist and at what boundaries. Prevent nested providers, CSS precedence, token namespace, focus management, or portal layers from producing cross-system interference. Establish a rule for new work so migration debt does not grow while old surfaces are converted.

## Evidence
Evidence includes migration inventory burn-down, before/after behavioral tests, rendered checks for high-risk states, accessibility/runtime verification, remaining legacy import scans, and product metrics where interaction materially changes. Record exact old/new revisions.

## Failure Modes
Failure includes a codemod that changes syntax but not semantics, partial migration with duplicate global styles, new components wrapped in legacy spacing hacks, “100% migrated” based only on imports while generated CSS remains, and teams recreating removed APIs as local compatibility layers.

## Falsification
Falsification scans for legacy runtime artifacts after source migration, exercises mixed old/new boundaries, and samples conversions marked mechanical for semantic drift. If a legacy dependency is still required to render or interact correctly, completion is falsified.

## Recovery
Recovery isolates mixed-system interference, reclassifies unsafe automated mappings as manual, and restores a known-good boundary before proceeding. When the target system lacks required capability, stop and route to contribution/exception governance rather than adding an invisible fork.

## Output
Output: `design-system-adoption-migrations-contract`, containing inventory, mapping class, sequencing, coexistence rules, automation limits, evidence gates, and completion criteria.

## Handoff
Handoff target support-matrix questions to version compatibility, system gaps to contribution workflow, and producer-side breaking release timing to rollout governance.

## Sibling Boundary and delete-the-skill
Migration impact auditing can predict a token change, but it does not govern fleet-wide component-system coexistence and cutover. Removing this skill leaves consumer transition execution without a bounded owner; the delete-the-skill test passes.