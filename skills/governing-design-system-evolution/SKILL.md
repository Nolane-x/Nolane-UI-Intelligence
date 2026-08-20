---
name: governing-design-system-evolution
description: Govern how a design system changes without turning local improvements into cross-product breakage, drift, or migration debt.
---

# Governing design-system evolution

Use this skill when a design system must change while multiple products, teams, versions, or platforms still depend on its current contracts. The problem is not choosing a prettier component. It is deciding which changes may enter the shared system, how their blast radius is understood, and how consumers move from old semantics to new semantics without silent divergence.

## Decision ownership

Own the evolution policy that separates additive extension, compatible refinement, deprecation, migration, and intentional breakage. Decide what evidence is required before a shared primitive changes, which consumers are considered authoritative, and when a local exception should remain local instead of contaminating the common layer.

Do not own the detailed token ontology, component implementation, or product-specific rollout plan. Those are handoffs after the evolution class and compatibility obligations are known.

## Inputs and evidence

Collect the current public component and token contracts, adoption telemetry, known forks, product release cadences, platform implementations, accessibility behavior, visual-regression evidence, issue history, and migration cost. Identify consumers that cannot upgrade synchronously. Distinguish documented API from accidental behavior that teams nevertheless rely on; accidental dependencies still create migration risk even when they were never intended as contract.

Evidence should answer four questions: what behavior changes, who observes it, whether old and new behavior can coexist, and what proves the transition is complete.

## Procedure

Classify the proposal by semantic impact before discussing implementation. For an additive change, verify that existing call sites remain stable and that the new option does not create mutually inconsistent ways to express the same intent. For a refinement, test whether output changes under unchanged inputs; if so, treat it as observable even when the API shape is identical.

For deprecation, define the replacement, detection mechanism, support window, and exit criterion at the same time the deprecation is accepted. For a breaking change, require a consumer inventory, migration path, rollback story, and explicit version boundary. Track exceptions as named debt with owners rather than allowing undocumented forks.

Review evolution at system level: token changes may alter component contrast, spacing changes may reflow layouts, and focus behavior may change automation or accessibility. Require cross-layer evidence when the blast radius crosses layers.

## Failure topology

A system stagnates when governance makes every change prohibitively expensive. It fragments when governance is absent and teams fork whenever a shared primitive is inconvenient. More subtle failure occurs when a change is labeled compatible because TypeScript or build tooling accepts it while visual, keyboard, localization, or motion behavior changes materially.

Another failure is indefinite deprecation: old and new paths coexist forever, increasing test matrices and making documentation contradictory. A migration that has no measurable completion condition is not a migration plan.

## Falsification

Attempt to falsify compatibility using representative old consumers, constrained layouts, high zoom, alternate themes, keyboard-only operation, localization expansion, and downstream overrides. Search repositories for undocumented usage patterns. If a supposedly additive option changes default behavior, forces synchronized upgrades, or requires consumers to reinterpret an existing semantic name, reclassify the change.

The evolution policy is inadequate if two independent teams can follow it faithfully and reach incompatible conclusions about whether the same proposal is breaking.

## Output contract

Produce a `design-system-evolution-contract` containing the change class, affected contracts, consumer/blast-radius inventory, compatibility statement, evidence required, versioning decision, migration and rollback obligations, deprecation window where relevant, exception policy, and measurable completion criteria. Record unresolved uncertainty explicitly; do not encode uncertainty as optimistic compatibility.

## Handoffs

Hand token-structure changes to `designing-token-taxonomies` or `designing-semantic-token-aliasing`; component interface changes to `designing-component-api-governance`; release boundary questions to `designing-design-system-versioning`; consumer transition mechanics to `designing-design-system-adoption-migrations`; and cross-platform divergence to `designing-cross-platform-component-parity`. Return to `governing-design-systems` when the issue is organizational ownership rather than evolution semantics.