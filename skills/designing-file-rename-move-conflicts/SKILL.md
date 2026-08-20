---
name: designing-file-rename-move-conflicts
description: Use when renaming or moving a file can collide with destination names, concurrent edits, path permissions, sync state, or references and the operation must remain atomic and explainable.
---

# Designing File Rename Move Conflicts

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns conflict handling for mutations to file location/name after the object already exists. It is distinct from upload conflict because references, collaborators, locks, and sync clients may already point at the object.

## Decision Boundary
Use stable object identity so rename/move does not create a new file unless storage semantics require copy-delete. Define name normalization and case sensitivity per destination. Moving across workspaces may change permissions, ownership, retention, or external links; if so it is not a simple path update and must disclose consequences.

At commit, revalidate source version, destination occupancy, lock state, and permission. A conflict can be resolved by choose-new-name, replace/version, merge folder, cancel, or request permission depending on object type. If clients are syncing, represent pending move and eventual reconciliation without briefly showing duplicate objects as two independent files.

## Failure Topology
- Case-only rename creates duplicate objects on one platform and no-op on another.
- Move into another workspace silently strips collaborators or breaks shares.
- Destination name becomes occupied after dialog opens and commit overwrites it.
- Path-based references break even though the product promises stable links.
- Sync shows both old and new location and users delete one, accidentally deleting the same object.
- Moving a locked file succeeds locally but is rejected remotely after further edits.

## Falsification and Recovery
Test same-name/case-normalized collisions, concurrent destination creation, cross-workspace move, locks, shares/references, offline sync, folder moves, and rollback after partial server failure. The design fails if one logical object can appear as two independent identities or if move consequences exceed the confirmation shown.

Recover by stable identity, transactional destination revalidation, explicit cross-scope consequences, conflict-specific choices, and sync alias/reconciliation until move acknowledgment. Preserve original location for rollback where backend semantics allow it.

## Output Contract
Return `file-move-conflict-contract` with rename/move identity, normalization/case rules, destination revalidation, cross-scope consequences, reference/share behavior, sync reconciliation, conflict choices, and mutation verification cases.
