---
name: governing-design-system-version-compatibility
description: Use when design-system producers and consumers evolve independently and support guarantees, compatibility matrices, peer constraints, and mixed-version behavior must be explicit.
---

# Governing Design-System Version Compatibility

## Compatibility Question
A design system is consumed as a versioned dependency, not an instantaneous synchronized whole. This skill owns the decision “which producer versions are supported with which consumer, runtime, framework, token schema, and companion package versions?” It separates support policy from the mechanics of migrating a particular application.

## Parent Contract
**Required parent:** `architecting-component-systems`.

The parent owns component architecture and shared-system composition. This skill begins where those contracts cross version boundaries.

## Compatibility Surface
Inventory public component APIs, token/schema versions, CSS/runtime assumptions, peer dependencies, rendering framework versions, and coupled tooling such as icons or codemods. Define a compatibility tuple rather than a single package number. Mixed versions must have either tested semantics or an explicit unsupported status.

Backward compatibility means previously valid consumer behavior remains valid within the promised window; it is not merely successful installation. Forward compatibility is a separate claim and should rarely be inferred.

## Matrix Decisions
For each supported line declare: producer version, consumer/runtime range, known degradations, required adapters, and test evidence. Distinguish “works,” “supported,” and “certified by this evidence.” Keep a bounded support horizon so the matrix does not become fictional.

## Evidence
Evidence comes from representative consumer builds, interaction tests, rendered-state comparisons, token resolution checks, and upgrade/downgrade rehearsal across matrix edges. Include a mixed-version case when packages can be upgraded independently. Pin exact versions used by evidence.

## Failure Topology
Failure includes components rendering but losing focus behavior, new tokens consumed by old CSS, peer dependency ranges that install an untested combination, minor versions introducing state semantics old consumers cannot express, or documentation claiming support beyond tested matrix edges.

## Falsification
Falsification chooses boundary combinations—oldest supported consumer/newest producer and inverse where claimed—then exercises behavior, not just compilation. A single material state or accessibility regression inside a claimed supported cell disproves that cell.

## Recovery
Recovery narrows the support claim to observed evidence, introduces a compatibility adapter only with explicit ownership, or restores a producer behavior required by the promised window. Do not widen semver ranges to silence installation errors without runtime proof.

## Output and Handoff
Output: `design-system-version-compatibility-contract`, a version matrix with claims, evidence, degradations, and unsupported edges. Handoff a specific application's transition steps to adoption migration; handoff API redesign to component-system architecture.

## Sibling Boundary and delete-the-skill
Adoption migration owns movement between versions; breaking rollout owns release sequencing. Neither defines which combinations are valid before or during that movement. The delete-the-skill test leaves support claims without a bounded compatibility owner.