# External UI Intelligence Network v12 — Implementation Plan

Date: 2026-08-22

## Scope

Extend the existing ecosystem/source-intelligence architecture. Do not fork it.

## Tasks

1. Add failing structural contract tests for source volume, pack volume, lifecycle persistence and license gating.
2. Add `external_ui_intelligence.py` with deterministic source ranking, pack resolution and network validation.
3. Add a broad source network covering motion, icon morphing, headless/accessibility, design systems, drag/drop, shadcn, agent UI, editors, canvas/diagram, data visualization, spatial/3D, native/mobile, tokens/styling and verification, plus discovery-only awesome radars.
4. Add task-shaped reference packs with permissive-first preferred sources and restrictive fallbacks.
5. Add license policy with GREEN / CONSENT / REFERENCE_ONLY / UNVERIFIED states, exact-scope revalidation and automatic permissive fallback.
6. Wire the persistence invariant into the canonical `using-nolane-ui` bootstrap. `AGENTS.md` already mandates that bootstrap for material UI/UX work, so the V12 gate inherits the root policy without duplicating it in two places.
7. Document the architecture, no-copy/provenance relationship and the fact that V12 extends rather than replaces the existing v4/v6 source planes.
8. Verify JSON validity, deterministic ranking behavior, source/pack referential integrity and the full Python test suite in repository CI.
9. Review the PR diff for accidental third-party source/prose inclusion, contradictory policy and overclaiming.

## Acceptance criteria

- >= 140 typed external sources.
- >= 30 task-shaped reference packs.
- Every source has mechanisms, license state, adoption mode, health/drift, fallbacks and lifecycle reconsult stages.
- Every restrictive/mixed direct-use candidate is consent gated.
- Discovery-only sources cannot be directly adopted.
- Every pack has a permissive preferred route unless an explicit exception is documented.
- Restricted sources lose to sufficiently capable GREEN alternatives and can win only for materially unique requirement fit.
- Active references persist through intent, design, implementation selection, license gate, critique, runtime verification and provenance.
- Existing deep-source archaeology/runtime evidence obligations remain intact.
