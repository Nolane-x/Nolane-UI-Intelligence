---
name: gating-ui-completion
description: Use when an agent is about to claim a material UI/UX task is complete, ready, verified, production-quality, faithful, accessible, or suitable for release.
---

# Gating UI Completion

## Overview
This is the final court. It does not improve the artifact; it decides whether the bounded completion claim is supported.

## Parent Contract
**Required parent:** `nolane-ui`.

Require the contract, task profile, obligation set, evidence ledger, critic session, current artifact revision, and explicit completion claim.

## Iron rule
**No completion from confidence. Completion is a packet of resolved obligations bound to evidence.**

If required evidence is missing, the decision is `BLOCKED`, not “probably fine.”

## Gate checks
1. **Phase:** lifecycle is at `VERIFIED`; no illegal phase jump occurred.
2. **Contract:** objective, authority, fidelity, scope, preservation boundaries, and unknowns are explicit.
3. **Routing:** selected skills cover material faculties; inactive relevant faculties have reasons.
4. **Obligations:** every release-critical obligation is `PASS` or explicitly `ACCEPTED_RISK` by an authority allowed to accept it.
5. **Evidence:** PASS obligations reference appropriate, fresh evidence scoped to the current artifact.
6. **Critics:** required independent critic lenses ran; no unresolved `critical` or `major` blocker remains.
7. **State coverage:** applicable critical component/flow states are specified and, where required, observed.
8. **Responsive/platform:** claims are limited to verified viewports/platforms.
9. **Accessibility:** claim wording distinguishes automated checks from broader accessibility verification.
10. **Fidelity:** when the contract requires fidelity, target-vs-render evidence exists for the accepted target.
11. **Integrity:** deterministic repository/project checks required by the adapter have passed.
12. **Bounds:** the claim names what was not tested and what could still differ.

## Decision types
- `PASS`: the exact bounded claim is supported.
- `BLOCKED`: a required obligation/evidence/critic/capability is missing or failed.
- `PASS_WITH_ACCEPTED_RISK`: only when a documented authorized party accepts specific non-critical failures; risks remain visible in the packet.

Never manufacture `PASS_WITH_ACCEPTED_RISK` to avoid doing work.

## Output: `completion-decision`
Return the bounded completion decision together with the completion packet. The decision and packet are one release artifact; a missing packet cannot be represented as PASS.

### Completion packet
Required fields:
- `packet_id`
- `artifact_revision`
- `phase: VERIFIED`
- `task_profile`
- `obligations`
- `evidence`
- `findings`
- `checks`
- `claim`
- `bounds[]`
- `unknowns[]`
- `decision`

## Claim calibration
Bad: “The UI is pixel perfect, accessible, and production ready.”

Good: “The current web implementation matches the accepted desktop target within the reviewed regions; keyboard focus and automated WCAG checks were verified for the primary flow; screen-reader behavior on native mobile and untranslated locales were not tested.”

The second claim can be true even when the first is unjustified.

## Rationalization table
| Excuse | Gate response |
|---|---|
| “Tests pass.” | Which UI obligations do those tests actually close? |
| “The reviewer found only small issues.” | Severity and status are explicit; unresolved major/critical still block. |
| “We cannot run the browser here.” | Scope the claim or block fidelity/runtime obligations. Do not infer. |
| “The user told us to ship.” | User authority can accept named risk, but cannot retroactively turn missing observation into evidence. |

## Red flags
Stop and route to `recovering-ui-work` when you are tempted to soften claim language without updating the packet, ignore a stale check, treat unknown as pass, or remove a failing obligation from the set.

## V5 High-Ambition Aesthetic Release Gate
For **high visual ambition** (flagship/exceptional/experiential), compile/render health is necessary but never sufficient. **Render health** cannot substitute for experiential intent, divergence/reference evidence, computed legibility, global attractor audit, signature depth, visual energy, and **aesthetic adequacy**. A basin decision of `RE_DIVERGE` blocks completion. Material visualization also requires encoding provenance; product-wide high-ambition work requires perceptual-diversity evidence. Preserve the bounded claim: repository CI proves the framework gates exist, not that every future UI is objectively beautiful.

## V6 Completion Gate Integrity
Define the **non-waivable gate set** from task risk, ambition, accessibility, product truth, source usage, runtime evidence, and explicit user constraints. Compute an **evidence lineage hash** or equivalent identity over the exact artifact/revision/configuration each gate judged so PASS cannot float to later unverified changes.

Detect **cross-gate contradiction** such as visual PASS with accessibility FAIL, source adoption PASS with license UNKNOWN, or runtime PASS against a different revision. Enforce **conditional pass prohibition** for material unknowns: “PASS if we assume…” is not PASS. Attach a **release-claim bound** stating exactly what was proven and what remains outside structural/behavioral evidence.

### Falsification
Modify the artifact after evidence capture or remove one gate's proof. If completion stays PASS, the gate is unsound.

### Recovery
Invalidate stale gates, rerun the minimum affected evidence, resolve contradictions, and downgrade the release claim rather than extrapolating.
