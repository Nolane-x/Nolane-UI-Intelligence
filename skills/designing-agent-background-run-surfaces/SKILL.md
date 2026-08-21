---
name: designing-agent-background-run-surfaces
description: Use when an agent continues working after the initiating view loses focus, closes, or hands off to another surface and the product must preserve run identity, progress truth, notification boundaries, and re-entry without pretending the work is synchronous.
---

# Designing Agent Background Run Surfaces

## Background work changes the interaction contract
A long-running agent task may outlive the page, device session, or conversational focus that started it. Once that happens, ordinary loading UI is no longer enough. This skill owns how a background run remains findable, truthful, interruptible where possible, and reconnectable to the context that initiated it.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent defines whether the agent may continue autonomously. This specialist begins when allowed execution can persist without the user actively watching the initiating surface.

## Run identity and persistence
Every background run needs a stable run ID, initiating intent revision, owner/principal, start state, current lifecycle state, last confirmed event, notification policy, and re-entry target. The run must not be represented only by transient toast state. If the page reloads or a second device opens, the same run should be recognizable rather than accidentally duplicated.

Separate `backgrounded` from `paused`. Backgrounding changes visibility, not necessarily execution. A run can be actively executing, queued, awaiting approval, blocked, interrupted, or complete while it is in the background. The interface should preserve those states rather than flattening everything into “working in background.”

## Progress and attention policy
Only show progress that the runtime can substantiate. When exact percentage is unavailable, use milestone or state-based progress. Define which transitions deserve notifications: completion, user input required, authority request, safety block, material failure, or approaching cost/time ceilings. Avoid notifying for every internal step, but do not hide a state that requires timely human action.

Re-entry should restore the execution context that matters: current plan revision, completed work, pending obligations, approvals, tool results, and any unresolved ambiguity. Opening a background run should not create a fresh conversation that merely paraphrases the old one.

## Multi-surface behavior
A background run may be viewed from desktop, mobile, notification center, task list, or a dedicated runs dashboard. One surface may have reduced control capability. The decision owner is which actions are safe from each surface and how stale views refresh. Cancellation from one surface must propagate as a lifecycle request, not just locally hide the card.

## Evidence
Evidence includes run identity across surfaces, lifecycle events while no foreground view is connected, notification delivery state, user actions from notifications, re-entry snapshots, and cancellation acknowledgements. Test at least one case where the initiating tab closes, the run completes, and a different surface reopens the exact run with intact evidence.

## Failure modes
Characteristic Failure includes “background” runs that die when the tab closes, duplicated work when a user reopens the task, stale notifications after a run was cancelled elsewhere, progress percentages fabricated from elapsed time, and re-entry that loses prior approvals or side effects. Another failure is silent attention theft: the agent keeps requesting permission in a hidden surface with no notification path.

## Falsification
Close the initiating surface during each lifecycle phase, reconnect from another device, issue cancellation from a secondary surface, expire an approval while backgrounded, and deliver a late completion after the user thought the run had stopped. The contract fails if run identity forks, if actions taken elsewhere are not reflected, if required attention is missed, or if re-entry cannot reconstruct current execution truth.

## Recovery
If persistence is lost, reconstruct from authoritative run and side-effect records before offering continuation. If duplicate runs exist, freeze automatic side effects and reconcile which attempt is canonical. For stale notifications, bind notification actions to current run revision so an old button cannot authorize or cancel a newer semantic state.

## Output and Handoff
Output: `agent-background-run-surfaces-contract`, defining persistent run identity, background lifecycle semantics, progress evidence, notification policy, cross-surface controls, re-entry, and stale-action protection. Handoff actual interruption to interruption/resume and cross-device continuation to the multi-surface continuity court.

## Sibling Boundary and delete-the-skill
Sibling interruption/resume owns execution that stops; this skill owns execution that continues while foreground attention stops. Tool-call lifecycles operate at the operation level, while this skill owns the long-lived run surface. The delete-the-skill test passes because without it, background execution becomes invisible asynchronous behavior with weak re-entry and duplicate-run risk.