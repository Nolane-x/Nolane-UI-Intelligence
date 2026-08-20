---
name: designing-design-system-adoption-migrations
description: Plan product migrations onto shared design-system contracts with staged evidence, coexistence rules, and measurable retirement of legacy implementations.
---

# Designing design-system adoption migrations

Adoption is not complete when a package is installed. Use this skill when products must move from bespoke UI, old system versions, or acquired libraries onto a canonical design system without destabilizing delivery.

## Decision ownership

Own migration segmentation, sequencing, coexistence policy, compatibility adapters, risk gates, rollback, and completion measurement. Decide whether migration should proceed component-by-component, route-by-route, workflow-by-workflow, or through a platform boundary.

## Inputs and evidence

Inventory legacy components, usage frequency, business-critical flows, visual differences, accessibility defects, downstream overrides, test coverage, release schedules, team capacity, and dependencies on old tokens or CSS. Identify shared names that hide incompatible semantics.

Measure current baseline so “adoption” can include quality and debt outcomes, not only replacement count.

## Procedure

Partition migration units by coupling and risk. Start with representative slices that expose integration problems early rather than only easy low-value components. Define adapters as temporary, named debt with removal conditions. Prevent new legacy usage once a replacement is approved.

For each slice, compare behavior, accessibility, responsive states, localization, analytics hooks, and performance before switching. Allow controlled coexistence only with clear boundary rules; two systems competing for global reset, tokens, or focus behavior can corrupt both.

Track remaining legacy surface and exception owners continuously.

## Failure topology

Big-bang migration concentrates risk and often stalls. Endless incremental migration creates permanent dual systems. A visual-only replacement may regress keyboard behavior or product-specific affordances. Another failure is counting files converted while legacy wrappers still control semantics underneath.

Adapters can become permanent if they make old APIs comfortable enough that consumers never complete migration.

## Falsification

Select migrated flows and search for hidden legacy dependencies. Disable the legacy package in a test build and observe what breaks. Compare baseline and migrated task behavior, accessibility, and bundle/runtime characteristics. Measure creation of new legacy call sites; any growth after freeze indicates policy leakage.

Review exceptions periodically and require renewed justification.

## Output contract

Produce a `design-system-adoption-migrations-contract` containing migration units, priority/risk model, coexistence boundaries, adapter policy, per-slice verification, rollout and rollback, freeze rules, exception ownership, legacy-retirement telemetry, and explicit completion criteria.

## Handoffs

Use `designing-token-deprecation-migrations` for token replacement, `designing-design-system-versioning` for version compatibility, `measuring-design-system-adoption` for ongoing telemetry, and `designing-cross-platform-component-parity` when products migrate on different platforms.