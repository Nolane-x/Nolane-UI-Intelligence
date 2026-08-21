---
name: resolving-cross-device-state-conflicts
description: Use when the same task, object, or draft can be changed from more than one device and the UI must detect, explain, and resolve divergent state without silent last-write-wins corruption.
---

# Resolving Cross-Device State Conflicts

## Ownership statement
Cross-device continuity becomes dangerous when two surfaces are active at once. A draft may change on a laptop while a phone remains offline; a tablet may submit an action while a desktop still presents the pre-submit controls; two devices may both think they own the current step. This skill owns the Decision that classifies divergence and chooses automatic merge, authoritative refresh, user-assisted reconciliation, operation invalidation, or hard conflict blocking.

## Parent Contract
**Required parent:** `routing-ui-work`.

The parent routes multi-surface continuity concerns. Task-state preservation owns what state can be restored; this skill begins when there are two or more legitimate revisions whose relationship must be resolved. It is not generic optimistic concurrency logic: the UI must explain what changed, what remains safe, and whether user intent can survive the merge.

## Conflict model
Represent every conflict as `(entity-or-task, base-revision, local-revision, remote-revision, authority, semantic-delta, side-effects, mergeability)`. Revision identity may come from server versions, event sequence numbers, vector clocks, edit epochs, or another explicit mechanism; timestamps alone are weak when clocks or offline queues are involved.

Classify deltas into `disjoint`, `commutative`, `overlapping-compatible`, `overlapping-incompatible`, and `effect-conflict`. A text edit in one field and a tag edit in another may be disjoint. Two irreversible submissions are not a merge problem at all; they are an effect conflict and must be reconciled against authoritative operation state.

## Resolution invariants
- no conflict is silently converted into last-write-wins unless that policy is explicitly safe for the data class;
- user-authored content is never discarded without a visible recovery path;
- irreversible domain effects are reconciled from authoritative records, not merged from local UI state;
- conflict presentation distinguishes “your change,” “other-device change,” and current authoritative state;
- an automatic merge retains enough provenance to be audited or undone when the domain permits it;
- once a conflict is resolved, stale devices cannot continue presenting the rejected branch as current without a refresh boundary.

## Evidence package
Evidence should include a known common base, two divergent revisions, the computed delta class, the selected resolution policy, and the final authoritative revision. Include at least one offline edit, one simultaneous edit, one stale action after remote completion, one mergeable disjoint case, and one intentionally non-mergeable case. For user-assisted reconciliation, record the exact alternatives exposed and which content would be lost under each choice.

A pair of final screenshots is not sufficient Evidence; the proof must include revision identity and the transition from divergence to convergence.

## Failure classes
Characteristic Failure includes silent overwrite, duplicated side effects, presenting a merged document that never actually existed on the server, letting a stale device submit against an invalid base, losing attachments or annotations during a field-level merge, or offering “keep mine / keep theirs” when a more precise semantic merge exists. Another failure is false conflict: equivalent changes encoded differently trigger unnecessary user interruption.

Conflict loops are especially harmful: after a user resolves once, a stale queued mutation from another device recreates the same divergence because the rejected branch was not invalidated.

## Falsification attacks
Falsification intentionally creates divergent revisions under clock skew, offline queues, delayed sync, partial network failure, and repeated reconnect. Apply commutative edits in opposite order, perform the same irreversible action on two devices, and submit a stale edit after the server advances twice. The contract fails if content disappears, effects duplicate, a resolved conflict reappears without a new change, or the UI cannot identify which revision is authoritative.

## Recovery strategy
Recovery first freezes conflicting mutations, retrieves authoritative revision history, and preserves every recoverable user-authored branch. Recompute the semantic delta from a common base. Automatically merge only under an explicitly safe rule; otherwise present the smallest decision the user must make. For effect conflicts, report the already-performed action and invalidate duplicate controls. After resolution, propagate the accepted revision and rejection markers to other devices so convergence is durable.

## Output and Handoff
Output: `cross-device-state-conflicts-contract`, containing revision identities, delta classification, merge policy, effect-conflict rules, user-reconciliation UI requirements, invalidation behavior, and convergence evidence. Handoff persistence mechanics to storage/sync owners, task checkpoint reconstruction to task-state preservation, and domain-specific merge semantics to the owning workflow.

## Sibling exclusions and delete-the-skill
Session handoff moves control; companion authority decides who may control; task-state preservation reconstructs a single continuation. None of those owners decide how two valid divergent revisions converge.

Delete-the-skill test: remove this specialist and multi-device flows retain transport and persistence but lose an owner for divergent-state semantics. Silent last-write-wins, duplicate effects, and unrecoverable draft loss become implementation accidents. Because conflict classification and convergence materially change data truth and user intent, this skill cannot be folded into generic synchronization.