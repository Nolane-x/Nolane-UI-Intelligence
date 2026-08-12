---
name: recovering-ui-work
description: Use when UI evidence conflicts, a gate fails, the target or requirements change, an implementation drifts, or a repair invalidates earlier design assumptions.
---

# Recovering UI Work

## Overview
Recovery is controlled backtracking. It fixes the earliest invalid assumption while preserving evidence of what failed.

## Parent Contract
**Required parent:** `nolane-ui`.

Receive the failed obligation/finding/evidence conflict, current lifecycle phase, affected artifacts, and current authority set.

## Diagnose before repair
Classify the failure:
- `contract-drift`: requirements/authority changed or were misread.
- `routing-gap`: a relevant faculty was omitted.
- `design-defect`: architecture, interaction, visual, system, or inclusive design is wrong.
- `implementation-drift`: the design is valid but the built artifact diverged.
- `evidence-defect`: evidence is stale, ambiguous, too weak, or bound to the wrong scope.
- `tool/capability-gap`: the required oracle cannot be run.
- `critic-disagreement`: two legitimate lenses reach incompatible conclusions.

Do not start editing until the failure class identifies the earliest invalid phase.

## Backtrack map
- contract drift → `CONTRACTED`
- routing gap → `ROUTED`
- IA/task model defect → `ARCHITECTED`
- aesthetic direction invalid → `DIVERGED` or `DESIGN_SELECTED`
- token/component system defect → `SYSTEMIZED`
- missing state/spec detail → `SPECIFIED`
- implementation drift → `IMPLEMENTABLE`/render repair
- stale/weak evidence with unchanged artifact → stay at current artifact, return to evidence collection

## Repair discipline
1. Freeze unaffected decisions. Recovery is not permission for a gratuitous redesign.
2. Preserve the failed finding/evidence as historical truth.
3. Record the repair hypothesis: what change should remove the failure and what must remain unchanged.
4. Apply the smallest repair that addresses the mechanism, not the screenshot symptom.
5. Re-run directly affected obligations first.
6. Re-run transitive obligations when the repair changes global tokens, shared components, navigation, typography, interaction semantics, or content geometry.
7. Return to the critic/gate only with fresh evidence.

## Critic disagreement
Do not average opinions. Trace each finding to authority, user impact, and evidence. Higher authority wins when there is a real conflict; otherwise design an experiment or expose a trade-off. If both options are defensible and the choice is aesthetic, return it to the design direction rather than pretending there is an objective answer.

## Capability gaps
If runtime verification is impossible, do not keep “repairing” based on imagination. Narrow the claim or mark the obligation `UNKNOWN/BLOCKED` and report the missing capability.

## Output: `recovery-record`
Return `failure_class`, `failed_refs`, `earliest_invalid_phase`, `preserved_decisions`, `repair_hypothesis`, `changed_scope`, `invalidated_evidence`, `required_retests`, and `return_phase`.

## Common failures
- Deleting the original failing record after repair.
- Fixing a global design-system problem with a page-specific override.
- Responding to an accessibility finding by hiding the element rather than preserving the task.
- Solving fidelity drift by changing the accepted target instead of the implementation.
- Using recovery as an excuse to redesign areas outside the failure scope.
