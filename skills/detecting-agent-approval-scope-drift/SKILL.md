---
name: detecting-agent-approval-scope-drift
description: Use when an agent is executing under a prior approval and later evidence, replanning, parameter substitution, retries, or delegated work may cause the actual operation to exceed the scope the user originally authorized.
---

# Detecting Agent Approval Scope Drift

## Detection mandate
Approval scope can be correct at capture time and become wrong later. This skill owns the continuous comparison between the authorized semantic action and the action about to execute. Drift is not merely a changed parameter; it is any material expansion, substitution, or reinterpretation that makes the current operation no longer equivalent to what the user reviewed.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent decides when authority is required. `designing-agent-approval-scope-boundaries` defines the normalized authorization envelope. This specialist consumes that envelope and decides whether subsequent execution remains inside it.

## Drift vectors
Track changes to action type, target identity, recipient set, quantity, cost, environment, data disclosure, reversibility, temporal validity, delegation path, and preconditions. Drift can arise from replanning, tool defaults, server-side canonicalization, retries with broadened filters, user edits after approval, or a tool response that redirects work to a new resource.

Compare semantic values, not just display strings. Two labels may refer to different resource IDs; one resource may change sensitivity classification after approval; a retry may preserve arguments but occur after the approval window expired. Normalize both the stored scope and the imminent action before comparison.

## Materiality policy
Some changes are harmless: canonical ordering of a set, equivalent formatting, or a narrower target may remain within scope. Others require re-approval even if superficially small, such as a recipient change in a send action or a switch from preview to publish. The decision owner here is the materiality classifier and the evidence needed to support “still in scope.”

Unknown comparison is not equivalent. If the system cannot resolve whether a resource alias maps to the approved resource, side-effecting execution should block or re-authorize rather than assume equivalence.

## Evidence trail
Evidence must bind the original approval scope, the normalized current operation, each material comparison dimension, the drift verdict, and the rule used. Preserve the first event that introduced drift. If a replanning step changed a target, the user should be able to trace that change from plan revision through drift detection to a new approval.

## Failure modes
Characteristic Failure includes checking only tool name while parameters broaden, ignoring expiry, comparing friendly labels instead of stable resource identity, allowing a retry to inherit approval after a material plan change, and detecting drift only after the side effect occurred. Another failure is false drift noise that forces re-approval for semantically equivalent normalization and trains users to approve mechanically.

## Falsification probes
Falsification should mutate one dimension at a time: recipient, amount, environment, resource version, disclosure field, delegation route, and time. Include equivalence cases that should not trigger. The detector fails if a material expansion passes, if an equivalent action is consistently blocked, if the verdict cannot cite the dimension that changed, or if the check happens after dispatch.

## Recovery behavior
On detected drift, preserve completed in-scope work, block only the affected pending operation, and present a concise delta between approved and current semantics. Ask for a fresh scope rather than silently editing the old authorization. If execution already occurred due to a race, mark the event as an authority violation and hand it to side-effect recovery and audit.

## Output
Output: `agent-approval-scope-drift-contract`, containing comparison dimensions, canonicalization, materiality rules, unknown-state handling, pre-dispatch gate timing, delta presentation, and evidence bindings.

## Handoff and Sibling boundary
Handoff authorization construction to `designing-agent-approval-scope-boundaries`, changed plan semantics to `designing-agent-plan-preview-surfaces`, and runtime permission growth to `designing-agent-tool-permission-escalation`. Sibling retry/replay controls may initiate a new attempt, but this skill decides whether the old approval still covers it.

The delete-the-skill test passes because a static approval boundary alone cannot protect against later semantic movement. Without this detector, a system can truthfully record an original approval yet execute something materially different under its authority.