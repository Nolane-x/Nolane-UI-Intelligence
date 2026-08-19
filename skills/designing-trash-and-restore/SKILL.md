---
name: designing-trash-and-restore
description: Use when file deletion is reversible for a retention window and the product must distinguish removal from active locations, trash retention, restore destination, permanent deletion, conflicts, and policy cleanup.
---

# Designing Trash and Restore

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns reversible deletion lifecycle for files/folders. It is distinct from generic undo because trash persists beyond one interaction session and may have retention, ownership, and permanent-delete semantics.

## Decision Boundary
Define what moving to trash does to references, shares, sync, collaborators, and storage usage. The object keeps stable identity while active-location membership changes. Expose retention duration and whether quota is reclaimed immediately or only after permanent deletion. Restore should attempt the original location when valid; if the parent folder no longer exists or a name collision now exists, surface destination/conflict resolution rather than silently relocating.

Permanent deletion needs stronger confirmation when irreversible and when child contents/shares are affected. Organization policy may automatically purge after a period; distinguish policy purge from user action. Restoring a folder should preserve hierarchy where possible and re-evaluate permissions that changed during retention.

## Failure Topology
- “Delete” looks permanent but actually moves to trash with no way to find it.
- Restore silently puts a file in root because the original folder was removed.
- Name collision overwrites a new file created after the original was trashed.
- Users expect quota relief but trash still counts and no retention policy is shown.
- Permanent deletion confirmation omits nested files or shared-link consequences.
- Auto-purge occurs without the retention window being visible in product policy.

## Falsification and Recovery
Test delete/restore across files/folders, missing original parent, same-name replacement, changed permissions, shared links, quota behavior, retention expiry, bulk restore, and permanent purge. The design fails if restore can overwrite newer content or if users cannot distinguish reversible from irreversible deletion.

Recover by preserving object/original-location metadata, resolving restore conflicts, showing retention/quota policy, and gating permanent deletion with consequence-aware confirmation. Keep audit evidence where policy or collaboration requires it.

## Output Contract
Return `trash-restore-contract` with trash lifecycle, identity/reference effects, retention/quota rules, restore destination/conflicts, permission revalidation, permanent-delete confirmation, auto-purge policy, and deletion recovery verification cases.
