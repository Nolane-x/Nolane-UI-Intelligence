---
name: governing-cross-platform-component-parity
description: Use when a design-system capability exists across web, iOS, Android, desktop, or other platforms and semantic parity must be distinguished from intentional platform-native divergence.
---

# Governing Cross-Platform Component Parity

## Parity Is Not Pixel Identity
Cross-platform systems fail when parity is measured by screenshots. This skill owns which component semantics, states, actions, accessibility outcomes, and product obligations must remain equivalent across platforms, and which presentation or interaction details should intentionally follow platform convention.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent owns the shared component model. This specialist governs the correspondence between platform implementations of that model.

## Parity Ledger
For each capability record semantic purpose, supported states, user actions, emitted outcomes, accessibility role/name/state, content model, and error/recovery behavior. Mark each dimension as invariant, equivalent-with-native-expression, intentionally unsupported, or temporarily divergent with debt owner.

Do not force a web menu interaction onto mobile if the native platform expresses the same user decision through another pattern. Conversely, do not call a missing destructive-action confirmation “native divergence” when the safety obligation is actually lost.

## Platform Decision Rules
A divergence is legitimate when platform input model, OS convention, capability, or accessibility API changes the best expression while preserving task outcome. A divergence requires evidence; “engineering was easier” is not a platform rationale.

## Evidence
Evidence includes behavioral comparison, state matrices, accessibility-tree/platform semantics, representative input modalities, and recovery paths across implementations. Pin platform/library versions because native conventions and APIs evolve.

## Failure Modes
Failure includes visually matching components with different disabled semantics, one platform lacking an error state, action labels diverging in meaning, unsupported platform capability hidden behind a dead control, or lowest-common-denominator APIs that erase useful native behavior.

## Falsification
Falsification executes the same user intent on each platform, injects equivalent failure conditions, and compares observable outcome rather than gesture sequence. If an invariant task or safety/accessibility property cannot be achieved on one supported platform, parity is false.

## Recovery
Recovery restores the missing semantic outcome, documents intentional divergence, or narrows the shared abstraction so platform-native capabilities remain honest. Avoid patching screenshots toward visual sameness when behavior is the actual defect.

## Output
Output: `cross-platform-component-parity-contract`, a capability/state/outcome ledger with invariant and divergent dimensions, evidence, platform constraints, and debt.

## Handoff
Handoff component API redesign to the parent and consumer migration to adoption-migration governance.

## Sibling Boundary and delete-the-skill
Version compatibility concerns producer/consumer revisions; this skill concerns simultaneous platform implementations. Removing it leaves semantic-equivalence versus native-divergence decisions unowned, satisfying the delete-the-skill test.