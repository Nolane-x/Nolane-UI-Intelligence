# External UI Intelligence Network v12 — Design

Date: 2026-08-22

## Goal

Make external UI implementation intelligence a persistent, license-aware part of NUI rather than a passive source list. When a task benefits from a known external repository, NUI must resolve a small capability-specific reference pack, prefer permissive implementations, retain the active references through design/implementation/critique/verification, and require user consent before materially adopting a restrictive source when no sufficiently capable permissive alternative exists.

## Non-goals

- Do not vendor third-party source code, assets, prose, or design-system trade dress.
- Do not make popularity or stars an authority signal.
- Do not turn awesome lists into implementation authority.
- Do not load the whole catalog into every prompt.
- Do not let license permissiveness override semantic, accessibility, safety, platform, or product correctness.

## Architecture

The v12 layer extends the existing v4 ecosystem registry and v6 source-intelligence invariants with three machine-readable artifacts and one resolver module:

1. `knowledge/external-ui-intelligence-network-v12.json` — compact catalog of canonical external sources with role, capability family, mechanisms, adoption posture, license gate, health, drift, fallbacks, and lifecycle reconsult stages.
2. `knowledge/external-ui-reference-packs-v12.json` — task-shaped packs such as button feedback, semantic icon transitions, AI chat, rich text, drag/drop, data table, canvas, spatial UI and visual verification.
3. `knowledge/external-ui-license-policy-v12.json` — permissive-first selection policy, consent semantics, scope-aware license verification, and fallback rules.
4. `src/nolane_ui/external_ui_intelligence.py` — deterministic validation, ranking and pack resolution. It does not fetch the web; live re-verification remains an execution obligation.

The existing `ui-source-intelligence-v6.json`, `ui-ecosystem-registry.json`, source archaeology and runtime attribution remain authoritative for deep material use. v12 is a routing and persistence layer, not a replacement.

## Selection policy

Selection is lexicographic in spirit but implemented with bounded scoring:

1. Hard product/safety/accessibility/platform fit.
2. Mechanism and capability fit.
3. Exact stack/runtime fit.
4. Source health and integration cost.
5. License preference.
6. Visual specificity.

A GREEN permissive source may outrank a slightly better restrictive source. A restrictive source may outrank permissive alternatives only when its unique requirement fit is materially higher. Direct adoption then requires explicit user consent. If the user declines, NUI automatically falls back to the strongest GREEN candidate or to independent mechanism synthesis.

## License states

- `green`: verified permissive scope such as MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause or ISC; still re-check exact upstream/component/asset scope before material use.
- `consent`: custom, copyleft, source-available, Commons-Clause-like, commercial/mixed or otherwise materially restrictive terms; direct adoption requires user consent.
- `reference-only`: proprietary, no-license, unclear rights, or a source whose value is mechanism research only.
- `unverified`: exact current scope has not been established; cannot direct-adopt until live verification resolves it.

License is scoped. Repository code, package, component, example/template, asset, icon, font and trademark terms may differ. Aggregator metadata is never canonical license evidence.

## Reference persistence

Every resolved pack carries the same mandatory stages:

- `intent`
- `design`
- `implementation-selection`
- `license-gate`
- `critique`
- `runtime-verification`
- `provenance`

The agent must re-surface active reference IDs at each material stage. Starting implementation does not discharge the reference obligation.

## Discovery radar

Awesome lists and aggregators are `discovery-only`. They can nominate a candidate, but NUI must resolve the canonical upstream repository and current license before influence or adoption.

## Testing

Structural tests require at least 140 typed sources and 30 task-shaped packs, validate consent/reference-only invariants, verify lifecycle persistence, and prove permissive-first ranking while allowing a restrictive source to win only for a materially unique requirement.

These tests establish repository behavior and policy integrity only. They do not claim model-independent UI quality improvement.
