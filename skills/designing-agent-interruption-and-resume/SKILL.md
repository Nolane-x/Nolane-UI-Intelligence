---
name: designing-agent-interruption-and-resume
description: Use when users, system events, policy changes, or external failures can interrupt a running agent and the UI must preserve what is valid, expose what stopped, and resume from a defensible checkpoint instead of restarting blindly.
---

# Designing Agent Interruption and Resume

## Interruption is a state transition, not a chat event
When an agent run is interrupted, the product needs to know which work is complete, which work is in flight, which assumptions are still valid, and what authority remains. This skill owns the contract for pausing execution and constructing a resumable checkpoint. The central decision is whether a future continuation can safely reuse the existing run context or must re-plan from newer evidence.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent establishes the permitted autonomy envelope. This specialist begins once an allowed run has started and something requires it to stop before its planned terminal state.

## Interruption taxonomy
Differentiate user stop, user redirect, permission revocation, dependency failure, system suspension, rate or budget exhaustion, policy block, network loss, and external-state invalidation. These are not interchangeable. A user stop may preserve completed side effects but cancel pending work; a policy block may prohibit resuming the same step; a network loss may leave the state of a dispatched operation unknown.

Attach interruption to a run revision and step boundary. Record whether each active operation is `not_started`, `safe_checkpoint`, `in_flight`, `cancel_requested`, `completed`, or `outcome_unknown`. The interface should never imply a clean pause if irreversible work may still be executing externally.

## Resume eligibility
Resume is allowed only when the checkpoint’s preconditions remain true. Revalidate mutable resources, permissions, approvals, tool availability, time-sensitive inputs, and user edits. If any material assumption changed, create a new plan revision and explain the delta. Resuming should not duplicate completed side effects; operations need stable identities or idempotency rules to determine what can be skipped.

A user may also resume with revised intent. Treat that as a fork from the checkpoint, not as if the original run had always meant the new instruction. Preserve the historical run so evidence remains coherent.

## Visible status and control
Show why the run stopped, what is definitely complete, what remains, and whether any outcome is uncertain. “Paused” is appropriate only when the system can actually hold the run; otherwise use interrupted or awaiting reconciliation. Resume affordances should state whether continuation uses the same plan, requires re-approval, or will re-plan.

## Evidence
Evidence includes interruption source, timestamp/order, active tool attempts, checkpoint revision, cancellation acknowledgements, preserved artifacts, invalidated assumptions, and resume validation results. Strong replay evidence demonstrates that resuming from the same checkpoint does not repeat completed side effects and produces a trace connected to the pre-interruption run.

## Failure modes
Characteristic Failure includes restarting from the beginning after a stop, losing artifacts that were already valid, claiming cancellation while external work continues, reusing expired approval, and resuming from stale task state without revalidation. Another failure is transcript continuity without execution continuity: the conversation appears uninterrupted but the runtime created a new run that silently forgot previous side effects.

## Falsification
Interrupt during each important lifecycle phase: before dispatch, after dispatch but before acknowledgement, after partial side effects, during a permission prompt, and after a dependency changes. The contract fails if resume duplicates work, if an uncertain side effect is treated as undone, if stale authority is reused, or if the user cannot identify the checkpoint from which execution continued.

## Recovery
For ambiguous in-flight work, reconcile external state first. For invalidated assumptions, keep completed artifacts but route back to planning. For revoked authority, preserve the checkpoint while blocking affected actions. Recovery ends only when every prior in-flight operation is classified as completed, cancelled, failed, or explicitly unknown with a safe downstream policy.

## Output and Handoff
Output: `agent-interruption-and-resume-contract`, containing interruption classes, checkpoint schema, resume eligibility, revalidation requirements, visible statuses, and evidence lineage. Handoff partial-result salvage to partial-completion recovery, execution ambiguity to tool-call lifecycles, and changed plan semantics to plan-preview surfaces.

## Sibling Boundary and delete-the-skill
Sibling background-run surfaces own visibility while a run continues away from the foreground; this skill owns a run that actually stops or loses continuity. Retry/replay owns repeating failed attempts, not restoration of the entire run checkpoint. The delete-the-skill test passes because no other owner decides which interrupted state is safe to resume and which must be re-planned.