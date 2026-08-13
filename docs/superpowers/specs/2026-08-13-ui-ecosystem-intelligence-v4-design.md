# NUI v4 Design — UI Ecosystem & Rich Interaction Intelligence

**Date:** 2026-08-13

## Problem

NUI v3 can close product capability/action/navigation/state graphs and iterate visual evidence, but an agent can still create generic implementation because it lacks a governed way to discover current external UI primitives, animated components, motion engines, specialist SDKs and design-agent skills. A static list of links is insufficient: sources have different abstraction roles, drift, license terms, accessibility posture, dependencies and integration risks.

## Design principles

1. **Typed source roles, never one library leaderboard.** Animated galleries, motion engines, headless primitives, design systems, editors, data grids, canvas SDKs, 3D renderers and agent-skill catalogues are not interchangeable.
2. **Primary provenance.** Material decisions cite canonical primary URLs and inspected files/docs.
3. **Adoption is a decision, not retrieval.** Retrieval returns candidates; selection chooses `adopt/adapt/inspire/build/reject`.
4. **No popularity authority.** Stars/trending may aid discovery but may not justify a decision.
5. **High-drift means live verification.** Registry data is a cache.
6. **Mechanism over skin.** Inspiration extracts a mechanism and records the adaptation boundary rather than copying a foreign product identity.
7. **Local proof supersedes upstream demos.** Accessibility, behavior, hydration and performance are verified after integration.
8. **Rich interaction is stateful behavior.** Motion/direct manipulation owns interruption, modality equivalence, reduced motion, semantic commit, focus, SSR/hydration, performance, cleanup and exit strategy.

## Six decision owners

- `researching-ui-implementation-ecosystems` → `ui-ecosystem-query`
- `selecting-ui-building-blocks` → `ui-source-selection`
- `adapting-external-ui-patterns` → `ui-adaptation-contract`
- `engineering-rich-interactive-components` → `rich-interaction-contract`
- `auditing-ui-library-integration` → `ui-integration-audit`
- `maintaining-ui-resource-registry` → `ui-resource-registry-delta`

Discovery may not silently select. Selection may not silently adapt. Adaptation may not self-certify integration. Registry maintenance is separate from task-local research.

## Registry model

Each entry records ID/name/canonical URL, source role, categories, capabilities, stacks/platforms, allowed intents, license status/evidence, accessibility posture, drift, live-verification flag, provenance, when-to-use and when-not-to-use. No third-party implementation code is embedded.

The query engine ranks capability, stack, category, source-role and accessibility fit. It returns `live_search_required` when no adequate current candidates exist or the leading candidates all require fresh verification.

## Evidence contracts

A material reference ledger records source URL, usage, mechanism, inspected paths/docs and adaptation boundary. Adopt/adapt decisions require verified task-specific license posture and implementation inspection. Integration audit checks license, dependency, accessibility, reduced motion, SSR/hydration, performance, API drift, security, exit strategy and local runtime.

## Hard routing

External or named source → research + selection. `adapt` → adaptation + integration audit. `adopt` → integration audit. Rich interaction → rich-interaction engineering; if external code participates, integration audit is also mandatory.

## Falsification

Fourteen adversarial cases target popularity-only selection, unresolved license, screenshot-only inspection, stale API, wrong stack, wrong source role, copy-without-adaptation, missing reduced motion, drag without keyboard, hydration mismatch, dependency overkill, missing exit strategy, missing citation and upstream-demo/local-wrapper evidence confusion.

## Bounds

The registry cannot be permanently exhaustive and does not certify any source for every use. Live legal/license review may be necessary for real commercial decisions. NUI's deterministic gates can ensure evidence is present and internally coherent; they cannot guarantee external repositories remain unchanged after verification.
