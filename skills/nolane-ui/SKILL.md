---
name: nolane-ui
description: Use when Nolane UI has been bootstrapped and the task needs lifecycle ownership, phase control, recovery, or a bounded completion claim.
---

# Nolane UI Lifecycle Controller

## Overview
`nolane-ui` owns the observable lifecycle. It does not design screens itself. It coordinates contracts, routing, obligations, evidence, critics, recovery, and closure so specialist skills cannot quietly lower the bar.

## Parent Contract
**Required parent:** `using-nolane-ui`.

Receive the original task, known context, available references, runtime capabilities, and any explicit reduced-scope justification. Preserve user authority verbatim where it changes design behavior.

## Canonical states
`INTAKE → CONTRACTED → ROUTED → DISCOVERED → ARCHITECTED → DIVERGED → DESIGN_SELECTED → SYSTEMIZED → SPECIFIED → IMPLEMENTABLE → RENDERED → CRITIQUED → VERIFIED → RELEASED`

Exception states: `RECOVERY`, `BLOCKED`.

A phase transition is a claim. Record the artifact/evidence that justifies it. Do not advance because “the next step is obvious.”

## Procedure
1. **INTAKE:** identify requested outcome, mutation scope, target fidelity, supplied references, and runtime capabilities. Keep unknowns explicit.
2. Invoke `ui-contracting`. Do not route specialist design work until authority, success, constraints, and non-goals are compiled.
3. Invoke `routing-ui-work`. Record selected faculties and justified inactive faculties.
4. Invoke `compiling-ui-obligations` before implementation. Every consequential design claim needs an observable obligation.
5. Move through design phases only when the selected skills have returned their declared artifacts. `DIVERGED` is required when aesthetic or structural exploration is valuable; it can be omitted only with a recorded reason such as an accepted reference/design system that already fixes the direction.
6. `IMPLEMENTABLE` means the design is sufficiently specified to build without inventing material product or visual decisions in code.
7. `RENDERED` requires an inspectable implementation or prototype, not source code alone.
8. Invoke `challenging-ui-designs` after a material render/spec exists. Criticism must be evidence-bound and logically separate from generation.
9. Invoke `binding-ui-evidence` for every release-relevant observation.
10. Invoke `gating-ui-completion`. Only a passing gate may transition `VERIFIED → RELEASED`.

## Transition invariants
- Risk/strictness may increase as new facts appear; they may not silently decrease.
- A failed check is preserved. Repair creates new evidence; it does not erase the failure record.
- A changed artifact invalidates evidence whose scope materially overlaps the change.
- If a requirement changes, return to the earliest phase whose assumptions it invalidates.
- A reference accepted as authoritative freezes only the axes it actually specifies; unspecified behavior still requires design reasoning.

## Output: `ui-session`
Return a compact record with `task_id`, `current_phase`, `contract_ref`, `task_profile_ref`, `obligation_refs`, `artifact_refs`, `evidence_refs`, `open_findings`, `unknowns`, `blocked_reason`, and `next_allowed_actions`.

## Rationalization table
| Rationalization | Required response |
|---|---|
| “The user approved the idea, so verification is unnecessary.” | Approval fixes intent; it does not prove implementation quality. |
| “This is only UI, not risky.” | UI can create irreversible user errors, exclusion, deception, or lost work. Route by consequence, not label. |
| “The design emerged during coding.” | If material decisions were invented during build, return to `SPECIFIED`, record them, then re-verify. |
| “I already inspected it once.” | Evidence is scoped and can become stale after overlapping changes. |

## Stop conditions
Stop in `BLOCKED` when a required capability or authoritative input is unavailable and guessing would change a material requirement. Stop in `RECOVERY` when an obligation fails, evidence conflicts, the design target changes, or a critic finds a release blocker.

## V6 Root-System Integrity
Maintain a **lifecycle invariant map** for the full NUI process: product truth precedes craft, routed owners cannot be skipped, evidence remains version-bound, critics cannot self-certify, and completion cannot outrun unresolved non-waivable obligations. Use a **root delegation contract** so `nolane-ui` orchestrates ownership without duplicating specialist decisions.

Define a **global stop condition** for missing product truth, unsupported high-risk claim, unavailable required evidence capability, or contradictory authority that makes downstream work unsafe. Run an **artifact coherence check** across contracts, routes, graph outputs, evidence packet, implementation spec, runtime/render evidence, and release claim. Preserve a **versioned-system boundary** so v1–v5 historical invariants remain compatible while v6 adds stricter overlays.

### Falsification
Delete one required routed artifact or substitute evidence from another revision. If root completion still succeeds, orchestration is unsound.

### Recovery
Return to the earliest violated invariant, preserve valid downstream-independent artifacts, reroute/revalidate affected branches, and regenerate the completion packet.

## V8 Flagship Synthesis Lock
When `visual_ambition` is `flagship`, `exceptional`, or `experiential`, the lifecycle must bind the routed aesthetic and media owners into one `flagship-visual-synthesis` evidence packet before `VERIFIED`. This is an integration proof, not a new design owner: local decisions remain with their canonical skills.

The packet must show a concrete visual thesis, at least three materially divergent directions before selection, an explicit attention hierarchy, resolved typography/composition/color-material/motion systems, a domain-linked signature with a restraint rule, bounded reference mechanisms, generic-transfer resistance, structural responsive evidence, and at least two closed critique/correction cycles. The executable contract lives in `src/nolane_ui/flagship.py`; its decision vocabulary lives in `knowledge/flagship-visual-synthesis-v8.json`.

A high-ambition session cannot advance by presenting one polished screenshot, a beauty score, a fashionable component stack, or three cosmetic variants. If the direction candidates converge on the same solution, the generic-transfer test succeeds, responsive evidence is shrink-only, or critique has no re-observed correction, transition to `RECOVERY` and return to `DIVERGED` or the earliest affected craft phase.

### V8 falsification
Blind product name/logo and compare candidate silhouettes, type behavior, material logic and signatures. If the same shell can host an unrelated product without losing important structure or identity, the flagship claim remains unverified even when local implementation checks pass.

### V8 recovery
Preserve valid product truth and specialist evidence, discard only the collapsed visual basin, reopen reference frontier/divergence, choose a materially different mechanism set, render the affected viewport/state again, and close the critique loop before recomputing completion.
