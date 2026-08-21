# Impeccable → NUI V11 Runtime Mechanism Transfer

## Purpose

This record documents how NUI V11 learned from `pbakaus/impeccable` without turning that project into a second design authority or a copied skill pack.

## Source boundary

Impeccable is licensed under Apache-2.0 and exposes several mechanisms that are relevant to NUI's runtime gap: deterministic detector rules, source/browser detector separation, edit-time and stop-time hook feedback, project-local context/drift handling, and live browser iteration.

V11 treats those mechanisms as research inputs. The implementation in `src/nolane_ui/runtime_v11/`, the rule wording in `knowledge/runtime-detector-rules-v11.json`, the thresholds, schemas, tests and NUI finding/adjudication model are **independently authored** for NUI. No Impeccable detector source file is vendored into this slice.

If a later change directly vendors or adapts Apache-2.0 source, that code must be isolated, retain required notices/license terms, and be recorded as direct reuse rather than described as an independent rewrite.

## What transfers

- Deterministic observation belongs below model judgment for mechanically observable defects.
- Per-edit feedback should be small/high-precision; deeper session/release passes should carry broader rules.
- Browser/runtime observation should complement source inspection rather than be inferred from it.
- Host hook capabilities should be explicit because pre-write blocking, post-write feedback and stop events differ by harness.
- Context/drift state should be reviewable and project-local.
- Live iteration should be transactional and recoverable rather than a sequence of destructive blind edits.

## What does not transfer as authority

- Impeccable's taste heuristics do not become universal NUI bans.
- A common font, palette, gradient, glow, card pattern or motion treatment is not automatically a release failure.
- NUI does not adopt a one-skill/23-command architecture as its cognition model.
- Detector rules do not become canonical NUI skills.
- A clean detector does not certify accessibility, usability, product completeness, visual quality or release readiness.

## NUI-specific advancement

V11 separates `mechanical`, `contextual`, `genericness` and `advisory` rules. Contextual signals can remain `unknown` until product/design authority or rendered evidence resolves them. Genericness and advisory signals cannot silently become edit blockers. Explicit exceptions require narrow file scope, authority, rationale and revision provenance.

This makes the runtime layer subordinate to NUI's existing contract/routing/evidence lifecycle rather than a second taste engine.

## Concurrency boundary

This V11 work creates **no canonical skills** and intentionally does not modify `skills/skill-graph.json` or the concurrent `design/ui-industry-1000-batch-006` skill-expansion work. New faculties merged from that branch can use V11 runtime evidence through the existing NUI finding/evidence boundary without being regenerated or duplicated.
