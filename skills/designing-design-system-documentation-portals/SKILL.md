---
name: designing-design-system-documentation-portals
description: Structure design-system documentation so consumers can discover the right primitive, understand its contract, see live behavior, and distinguish stable guidance from examples.
---

# Designing design-system documentation portals

Documentation portals fail when they become galleries of components without decision guidance, or encyclopedias that cannot answer a task quickly. Use this skill to design the information architecture and evidence surface of a design system’s documentation.

## Decision ownership

Own documentation findability, page anatomy, status signaling, relationship between live examples and normative contract, cross-platform comparison, version visibility, and contribution feedback loops. Decide what belongs in reference, guidance, migration, or rationale content.

## Inputs and evidence

Collect search queries, support questions, onboarding observations, page analytics, broken links, stale examples, component status data, release notes, code/design artifacts, and common misuses. Interview both new consumers and expert maintainers; their navigation needs differ.

## Procedure

Organize around consumer decisions as well as component names. Each canonical item should expose purpose, when to use/not use, anatomy, states, accessibility, API/token links, responsive/platform behavior, live examples, and current status. Keep normative requirements visually distinct from illustrative examples.

Provide global search with aliases and deprecated names, relationship navigation among parent/sibling concepts, and version-aware migration links. Make examples executable or traceable to tested source when possible so docs do not drift from implementation.

Design landing paths for tasks such as “choose an input pattern” or “migrate deprecated token,” not only alphabetical browsing.

## Failure topology

Beautiful docs can still be operationally weak if examples are stale, status is hidden, or guidance lacks boundary conditions. Component-only navigation forces users to know the answer before searching. Another failure is mixing framework-specific API details into universal guidance so other platforms appear secondary.

Unversioned docs make old consumers read new contracts accidentally.

## Falsification

Give representative tasks to unfamiliar users and measure whether they find the canonical answer without maintainer help. Compare rendered examples against current package behavior. Search deprecated names and verify users reach migration guidance. Test deep links across versions.

Audit pages for unsupported claims that cannot be traced to tests, source, or policy.

## Output contract

Produce a `design-system-documentation-portals-contract` defining information architecture, page schema, search/alias behavior, status/version signaling, normative-vs-example distinction, live-example provenance, cross-platform presentation, migration linking, and research metrics for findability and freshness.

## Handoffs

Use `designing-design-system-contribution-workflows` for doc change ownership, `designing-design-system-versioning` for version semantics, `designing-design-system-adoption-migrations` for migration journeys, and `measuring-design-system-adoption` for usage telemetry surfaced in docs.