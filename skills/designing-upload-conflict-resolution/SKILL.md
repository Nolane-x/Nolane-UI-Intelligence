---
name: designing-upload-conflict-resolution
description: Use when an incoming file collides with an existing remote name, path, identity, or version and users must choose replace, keep both, merge metadata, skip, or resolve according to authoritative product semantics.
---

# Designing Upload Conflict Resolution

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns collisions discovered during upload. It does not own general collaboration conflict resolution. It decides what constitutes a file collision in this product and which consequences follow from replace, version, rename, or skip.

## Decision Boundary
Separate name collision from content identity. Two files can share a name but be intentionally distinct; the same content can arrive with a different name. Define conflict scope by folder, workspace, record attachment, or stable file object. Replacement may create a new version, overwrite bytes in place, or be forbidden when references/audit history exist. Make that consequence explicit before users commit.

Offer conflict strategies that the backend can honor atomically. “Keep both” requires deterministic naming and should preserve extensions. Batch uploads may support apply-to-all only for truly equivalent conflict classes; a global replace choice must not overwrite materially different records. If another collaborator changes the destination while the conflict dialog is open, revalidate before commit.

## Failure Topology
- Matching filenames automatically overwrite an existing referenced file.
- “Replace” actually creates a separate duplicate version but the UI implies destructive overwrite.
- Keep-both naming produces `file (1).tar.gz` incorrectly as `file.tar (1).gz`.
- Apply-to-all replaces files across unrelated folders or conflict types.
- Conflict resolution is based on stale destination state and overwrites a newer collaborator change.
- Content-identical uploads create duplicates because only names are compared.

## Falsification and Recovery
Test same name/different content, same content/different name, existing version history, references, simultaneous collaborator change, batch conflicts, locked files, and case-sensitive/case-insensitive stores. The design fails if users cannot predict whether references, history, or existing bytes survive the chosen option.

Recover by defining collision identity/scope, labeling replace/version/duplicate semantics accurately, revalidating destination state at commit, and limiting bulk conflict choices to equivalent cases. Preserve an audit trail where replacement has durable consequence.

## Output Contract
Return `upload-conflict-contract` with conflict identity/scope, available strategies and consequences, deterministic keep-both naming, version/reference behavior, batch apply rules, stale-state revalidation, and conflict verification cases.
