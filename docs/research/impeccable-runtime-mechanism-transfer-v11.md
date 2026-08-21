# Impeccable Research Inspiration for NUI V11

## Purpose

This record documents how NUI V11 studied `pbakaus/impeccable` as an external architectural reference while independently designing and implementing NUI's runtime layer.

The historical filename is retained only so existing links in this branch do not break. The term `mechanism-transfer` in that filename does **not** describe source-code or implementation transfer.

## Source boundary

Impeccable was inspected because it demonstrates useful workflow ideas around deterministic UI checks, edit/session feedback, browser-aware iteration, project-local maintenance, and live visual workflows.

NUI uses those observations only as **research inspiration**. V11 does not incorporate Impeccable source code, detector rule text, skill bodies, schemas, thresholds, state machines, configuration formats, or implementation artifacts.

Everything shipped under `src/nolane_ui/runtime_v11/`, `knowledge/runtime-detector-rules-v11.json`, the V11 schemas, tests, thresholds, finding semantics, adjudication semantics, evidence binding, Doctor behavior, and Live Lab protocol is independently designed and authored for NUI.

Impeccable's Apache-2.0 license is relevant metadata about a repository that was researched. It is not the license provenance of V11 implementation code because that implementation is not copied or adapted from Impeccable.

If a future change ever directly vendors or adapts third-party source, that would be a different integration mode and must be isolated, explicitly attributed, reviewed for license obligations, and never described as independent authorship.

## Ideas learned from research

The external research helped sharpen several general architectural questions:

- Which mechanically observable failures should be checked deterministically instead of rediscovered by a model?
- How should fast edit feedback differ from deeper session and release observation?
- How should source inspection and browser/runtime evidence complement one another?
- How should host capabilities be declared instead of simulated?
- How should project-local drift and evidence freshness be made reviewable?
- How should live iteration avoid destructive blind edits?

These questions are not implementation artifacts. NUI answers them through its own evidence, authority, routing, and completion architecture.

## What NUI does differently

- Runtime rules are subordinate evidence contracts, not design faculties.
- `mechanical`, `contextual`, `genericness`, and `advisory` observations have different authority and interruption rights.
- Contextual signals can remain `UNKNOWN` rather than being converted into universal taste bans.
- Genericness/advisory signals cannot silently become edit blockers.
- Runtime findings use NUI's existing finding vocabulary and route back to existing NUI owners.
- Evidence is revision/scope bound and can become `STALE` after overlapping source changes.
- Live source application is conflict-aware and recoverable.
- A clean runtime pass cannot self-certify `VERIFIED` or `RELEASED`.

## Research provenance semantics

Runtime rule provenance uses:

- `kind: independent-nui-rule`
- `implementation: independently-authored`
- optional `research_inspiration: [...]`

`research_inspiration` names conceptual areas that informed investigation. It must not be interpreted as copied source, adapted implementation, or transferred ownership. The legacy field name `mechanism_sources` is rejected by the V11 registry validator because it can imply a stronger relationship than actually exists.

## Concurrency boundary

This V11 work creates **no canonical skills** and intentionally does not modify `skills/skill-graph.json` or the concurrent `design/ui-industry-1000-batch-006` skill-expansion work. New faculties from that work can consume V11 runtime evidence through the existing NUI finding/evidence boundary without being regenerated or duplicated.
