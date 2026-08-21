---
name: designing-agent-retry-and-replay-controls
description: Use when users or agents may repeat a failed, timed-out, or disputed operation and the interface must distinguish safe retry, exact replay, modified rerun, and reconcile-first recovery so repeated side effects do not occur accidentally.
---

# Designing Agent Retry and Replay Controls

## Core distinction
Retry and replay are not synonyms. Retry means attempt the same intended outcome again under current conditions. Replay means reproduce a prior execution request or event sequence as faithfully as possible. Rerun means create a new attempt that may use changed inputs. This skill owns which of those controls are available and what semantic guarantee each one makes.

## Parent Contract
**Required parent:** `designing-agent-autonomy-and-control`.

The parent governs autonomous execution. This specialist starts after an attempt has reached failure, timeout, cancellation, or disputed completion and someone wants to repeat work.

## Attempt identity and preconditions
Every repetition needs a new attempt identity linked to the original logical action. Preserve the old attempt; do not overwrite it. Before offering Retry, classify the previous outcome as `definitely_not_applied`, `definitely_applied`, `partially_applied`, or `unknown`. Idempotency keys, external transaction IDs, and authoritative resource checks are evidence for that classification.

A safe retry requires still-valid preconditions and either idempotent semantics or evidence that the prior side effect did not happen. Exact replay additionally requires frozen inputs, tool version, relevant environment assumptions, and any deterministic seed or query scope that materially affects results. If those cannot be reconstructed, label the action as rerun rather than replay.

## Control design
Controls must communicate consequence, not implementation jargon. “Try again” is acceptable only when it truly preserves the intended operation and does not risk duplicate side effects. For dangerous ambiguity, prefer “Check status” or “Reconcile” before repetition. If a user edits parameters, the interface should create a modified rerun and invalidate any approval that no longer matches.

Batch retries need per-item disposition. Repeating the whole batch because two items failed can duplicate the successful subset. The UI should derive the minimal retry set from evidence rather than re-submit by convenience.

## Evidence
Evidence includes the original request, attempt result, idempotency capability, authoritative outcome check, changed preconditions, retry decision, new attempt identity, and link between attempts. For replay, evidence should additionally include the frozen input artifact and execution environment assumptions. The user should be able to inspect why the product considered repetition safe.

## Failure modes
Characteristic Failure includes a generic Retry button after an outcome-unknown send, silently changing parameters while calling it replay, overwriting failure history with the successful second attempt, reusing approval after the operation’s scope changed, and re-executing already-successful items in a batch. Another failure is false determinism: a “replay” produces different output because external data changed, yet the interface implies exact reproduction.

## Falsification exercises
Force a timeout after dispatch, a duplicated callback, a non-idempotent endpoint, a batch with mixed success, expired approval, and an external record that changes between attempts. The contract fails if an unsafe retry remains available, if a replay cannot identify its frozen inputs, if duplicate side effects occur without warning, or if attempt history becomes ambiguous.

## Recovery
When outcome is unknown, reconcile first. When only part of a batch failed, isolate that subset. When inputs changed, create a rerun with a new plan/approval lineage. If a duplicate side effect already occurred, stop automatic retries and route to side-effect recovery or compensation. Recovery should end with a traceable attempt graph rather than one flattened status.

## Output and Handoff
Output: `agent-retry-and-replay-controls-contract`, defining retry/replay/rerun semantics, attempt lineage, idempotency requirements, precondition checks, batch policy, evidence, and control labels. Handoff per-attempt execution states to tool-call lifecycles and authority validity to approval-scope drift.

## Sibling Boundary and delete-the-skill
Sibling partial-completion recovery derives what remains to be done at the task level. This skill decides how a particular operation may be repeated. Agent run branching creates divergent future execution paths; retry/replay primarily relates new attempts to prior failed or disputed attempts. The delete-the-skill test passes because without it, repetition controls become unsafe shortcuts that cannot distinguish recoverable failure from potentially duplicated side effects.