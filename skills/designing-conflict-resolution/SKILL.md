---
name: designing-conflict-resolution
description: Use when concurrent or divergent changes cannot be applied automatically and the interface must let users understand base, local and remote intent, choose or merge outcomes, preserve data and verify the resolved result.
---

# Designing Conflict Resolution

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns explicit human resolution of incompatible concurrent changes. It does not define the synchronization algorithm, CRDT/OT semantics, generic diff rendering or organization approval policy.

## Decision Boundary
A conflict exists only when the synchronization/merge authority says changes cannot be reconciled automatically or when an automatic merge needs human validation. Identify the **base state**, **local/current actor change**, **remote/other change**, and the target state that will receive the resolution. Two-way “mine vs theirs” without common ancestor can hide why both edits happened.

Choose resolution granularity from the artifact. Text may conflict by hunk; structured configuration by field; visual documents by object/property; spreadsheet data by cell/record; workflow state by domain action. Avoid forcing users to choose an entire file when only one field conflicts, but do not offer field-level merging if fields have coupled invariants that must be resolved together.

Language should describe consequences, not source-code jargon in nontechnical products. `Keep mine`, `Keep theirs`, `Combine`, `Edit result` can work only when ownership/context is obvious; otherwise label actors/timestamps/values directly. If both changes are valuable, support manual merged result and preview validation before commit.

Never destroy a losing version before the resolution is safely committed. Preserve recoverable snapshots or history according to system capability. If validation of the merged result fails, keep the resolution workspace and errors rather than discarding user choices.

Conflicts can become stale while open because another collaborator edits again. Bind the resolution to conflict/version IDs and revalidate on commit. A stale resolution should reopen/rebase with clear explanation instead of overwriting newer work.

Some “conflicts” are policy conflicts, not data collisions: changing a field the user no longer has permission to edit, deleting an object another workflow now depends on, or merging states that violate invariants. Route those to appropriate authority; do not offer arbitrary winner selection.

## Failure Topology
- UI shows only local and remote values with no base, so users cannot tell who changed what from which prior value.
- “Accept theirs” label is ambiguous after account/session roles change.
- Choosing one side immediately deletes the other version before Save.
- Manual merge passes visual comparison but violates domain validation and cannot be committed.
- Conflict dialog remains open for ten minutes and then overwrites newer remote changes.
- Entire document must be chosen even though only one independent field conflicts.
- Permission/invariant failure is presented as a merge conflict with a misleading `Keep mine` option.

## Falsification and Recovery
Falsify with independent changes, true same-field conflict, delete-vs-edit, rename/move, structured coupled fields, stale conflict while open, permission revocation, manual merge validation and failed network commit. Verify no source version becomes unrecoverable before authoritative resolution succeeds.

Recover by showing common base/provenance, narrowing conflict granularity only where semantics allow, binding choices to exact revisions, preserving both sources, validating the merged result and reopening/rebasing when the conflict record becomes stale.

## Output Contract
Return `conflict-resolution-contract` with conflict/base/local/remote identities, semantic conflict granularity, side provenance, available resolution operations, manual-merge/validation path, preservation/recovery guarantees, stale-conflict revalidation, policy-conflict handoff and end-to-end merge tests.