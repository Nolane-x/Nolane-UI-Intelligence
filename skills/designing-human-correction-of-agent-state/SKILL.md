---
name: designing-human-correction-of-agent-state
description: Use when a human needs to correct what an agent currently believes about task facts, intent, constraints, entities, or progress and the interface must propagate that correction into execution state without rewriting history or leaving stale assumptions active.
---

# Designing Human Correction of Agent State

## Correction target
A user correction is not always a new prompt. “That account is not the production account,” “I already completed step three,” or “use the revised date” may invalidate internal task state, tool preconditions, plan branches, and generated UI at once. This skill owns the contract for turning a human correction into explicit state mutation with known blast radius.

## Parent Contract
**Required parent:** `designing-human-ai-interaction`.

The parent governs broad collaboration and correction affordances. This specialist begins when the product must decide exactly which agent-held facts or assumptions are replaced, which derived state becomes stale, and how execution reconciles with the correction.

## Correction object
Represent a correction with `(target_state_key, prior_value_or_claim, corrected_value, authority_source, effective_revision, dependent_state, propagation_status)`. The user need not see this tuple literally, but the product needs equivalent semantics. A correction can target user intent, an entity binding, a factual assumption, a completion claim, or a derived plan constraint.

Do not rewrite the transcript as though the earlier belief never existed. Historical statements remain historical evidence; mark them superseded where necessary. Current execution state should reference the correction revision so later tool calls cannot accidentally use cached assumptions.

## Propagation policy
The decision owner is the dependency cone. If the corrected fact affected a plan step, a tool argument, a generated summary, and an approval, each dependent artifact needs one of `still_valid`, `recompute`, `reapprove`, or `invalidate`. Recomputing everything is wasteful; invalidating too little leaves stale state active.

When the correction conflicts with authoritative external evidence, distinguish user preference from factual authority. A user may choose a different target, but cannot make a failed transaction become successful by assertion. Surface the contradiction and define which source governs which field.

## Interaction design
Offer correction near the state being corrected when possible: editable entity chips, plan-step edits, “mark as not done,” or structured fact review. Free-text correction still needs to resolve to concrete state changes before execution continues. If the system is unsure what the correction applies to, block dependent side effects and ask for disambiguation instead of silently guessing.

## Evidence
Evidence includes the prior state revision, user correction, normalized target, dependent artifacts, invalidation/recomputation decisions, changed approvals, and post-correction execution trace. Strong evidence proves that stale values no longer appear in tool requests or generated controls after the correction becomes effective.

## Failure modes
Characteristic Failure includes acknowledging correction conversationally while runtime state stays unchanged, rewriting history so audit becomes impossible, failing to invalidate approval based on old semantics, over-propagating a small change into unnecessary task reset, and letting a user assertion override authoritative external outcome without distinction.

## Falsification
Correct a value after it appears in a plan, after approval but before dispatch, after a generated component renders, and after one dependent step already completed. The contract fails if stale values survive in pending execution, if unrelated work is discarded, if the historical record becomes misleading, or if the system cannot explain which downstream artifacts were invalidated.

## Recovery
On suspected stale propagation, stop dependent side effects, compute the correction’s dependency cone from the last known-good revision, invalidate only affected artifacts, and regenerate or reapprove as needed. If a prior action already used the wrong state, preserve the correction separately and route the action’s consequence to side-effect recovery.

## Output and Handoff
Output: `human-correction-of-agent-state-contract`, containing correction targets, authority classes, dependency propagation, invalidation semantics, history preservation, and evidence. Handoff concurrent write conflicts to shared-state reconciliation and changed approval semantics to approval-scope drift.

## Sibling Boundary and delete-the-skill
Sibling shared-state reconciliation handles concurrent versions from multiple writers; this skill handles an explicit human declaration that some agent-held state should change. AI feedback/correction may collect preference or quality feedback, but this owner governs runtime task-state correction. The delete-the-skill test passes because without it, products can appear to accept corrections while stale assumptions continue to drive actions.