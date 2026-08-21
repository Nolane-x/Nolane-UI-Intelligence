---
name: preserving-task-state-across-device-switches
description: Use when a user moves an in-progress task between devices and the product must preserve meaningful work state, provenance, progress, and recoverability without serializing every transient UI detail.
---

# Preserving Task State Across Device Switches

## Scope
Moving a task between devices is not equivalent to copying application state. Cursor positions, hover state, transient menus, local caches, draft edits, selected records, unsaved calculations, upload progress, approval context, and optimistic mutations do not all deserve the same persistence treatment. This skill owns the Decision about which state is semantically necessary for the task to remain continuous and which state must be recomputed, discarded, or explicitly re-confirmed.

## Parent Contract
**Required parent:** `routing-ui-work`.

The parent establishes that multi-surface continuity is in scope. This specialist owns the durable task-state boundary. Session handoff owns transfer mechanics; capability negotiation owns destination suitability; cross-device conflict resolution owns competing edits. This skill defines the canonical checkpoint that a destination can safely reconstruct.

## Task-state decomposition
Partition state into five classes: `authoritative-domain-state`, `user-authored-uncommitted-state`, `task-navigation-state`, `ephemeral-presentation-state`, and `execution-state`. Each class has a persistence authority, freshness rule, and replay rule.

Authoritative domain state should usually be re-read from its source rather than serialized blindly. User-authored drafts may require durable transfer with ownership and revision identity. Task-navigation state can include selected object, wizard step, filter intent, or review position when those are necessary to understand what remains. Ephemeral presentation state such as hover or animation phase normally should not survive. Execution state such as an upload or background job requires a stable operation identifier rather than pretending the destination inherited the process.

## Invariants for continuity
- preserved state represents task meaning, not implementation accident;
- destination reconstruction never overwrites fresher authoritative state merely to match the source screen;
- user-authored unsaved content carries revision identity and provenance;
- irreversible progress cannot be replayed just because the destination lacks a local marker;
- the destination can distinguish resumed state from freshly created state;
- secret or device-bound state is never transferred simply because it was convenient locally;
- restoration is idempotent: reopening the same checkpoint cannot duplicate side effects.

## Evidence required
Evidence includes checkpoint fixtures captured at meaningful interruption points, restoration traces on at least two materially different surfaces, draft preservation examples, stale-domain-state reconciliation, and an operation-in-progress case. The record should show what was serialized, what was deliberately omitted, what was re-fetched, and how the destination reconciled revisions.

Strong Evidence includes a source/destination pair where the task is interrupted mid-edit, resumed after domain data changed elsewhere, and still preserves the user's draft without presenting stale committed facts as current.

## Failure topology
Characteristic Failure includes copying too little and dropping drafts, copying too much and reviving stale presentation state, replaying a side effect from serialized execution state, restoring a wizard step whose prerequisites are no longer true, or hiding a conflict by overwriting the destination's fresher server read. Another failure occurs when local-only identifiers are serialized and become meaningless on the receiving device.

A continuity illusion is also a failure: the destination visually resembles the source but silently loses pending attachments, selected scope, or review context that changes what the next action means.

## Falsification exercises
Falsification switches devices at adversarial moments: immediately before submit, during upload, after local draft change but before sync, after another actor changes the object, while a step-specific permission is revoked, and after the source device goes offline. Restore the same checkpoint twice and restore it after a long delay. The contract is falsified by duplicate effects, silent draft loss, stale prerequisite assumptions, secret leakage, or a resumed UI that cannot explain what was restored versus refreshed.

## Recovery semantics
Recovery preserves the highest-value user work first, then reconstructs authoritative context around it. If a checkpoint is incompatible with current domain state, open a reconciliation state rather than discarding it. If only part of the task is restorable, enumerate the preserved and invalidated portions. Maintain an export or copy path for user-authored content when automatic merge is unsafe. Expired checkpoints should fail with an intelligible reason and a path to restart without pretending continuity succeeded.

## Output and Handoff
Output: `task-state-across-device-switches-contract`, containing state classes, persistence authority, checkpoint schema, freshness and replay rules, restoration sequence, invalidation conditions, and recovery evidence. Handoff transport and session identity to session-handoff specialists; route conflicting concurrent revisions to cross-device conflict resolution; route device-bound capability gaps to capability negotiation.

## Sibling boundary
This skill does not decide which surface may act, whether the destination has required capabilities, or how simultaneous edits are merged. It owns only the preservation and reconstruction of one task's meaningful state across a surface change.

## Delete-the-skill proof
Delete-the-skill test: if this owner is removed, session transfer can still move credentials or routes, but no one defines the semantic checkpoint that distinguishes durable task meaning from ephemeral UI implementation. The result is either lost user work or dangerous over-serialization. Because this choice directly controls replay safety, draft survival, and task comprehension, it is a distinct canonical responsibility.