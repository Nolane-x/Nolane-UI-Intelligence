---
name: designing-sharing-dialogs
description: Use when users need one bounded surface to inspect who can access an object, add people, change sharing mode, copy a link, and understand the consequences before permissions change.
---

# Designing Sharing Dialogs

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns the orchestration surface where multiple sharing mechanisms become understandable together. It does not define permission semantics, invitation lifecycle, or link-token security; those belong to dedicated owners. Its responsibility is to make current access truth, proposed changes, and the path to commit those changes visible without mixing them into one ambiguous control.

## Decision Architecture
Begin with the current access model: direct members, inherited organization/workspace access, groups, public/link access, and owner/admin authority. The dialog must distinguish access someone has because of inheritance from access this object grants directly. A user should not be offered a “Remove” action that cannot actually remove inherited access.

Separate adding recipients from changing their role. Resolve people or groups to stable identities, show destination context, then stage role/permission before committing. If changes apply immediately, say so; if invitations must be accepted, hand off to invitation state rather than displaying the recipient as an active member.

Link-sharing controls should show the current capability mode—restricted, organization-only, anyone-with-link, expiring, etc.—and delegate token details to the link-sharing contract. Copying a link is not equivalent to granting access unless the link itself changes authority. Keep destructive broadening/narrowing actions reversible where product policy allows and show audience impact before high-radius changes.

## Failure Topology
- Dialog lists inherited members with active Remove buttons that do nothing.
- Invited person appears identical to an accepted collaborator.
- Changing “Anyone with link” silently exposes an object beyond the current organization.
- Role dropdown is enabled for users whose role is fixed by group membership.
- Closing the dialog discards staged changes without telling users whether anything was applied.
- Search results expose directory members the current user is not allowed to discover.

## Falsification and Recovery
Falsify with direct plus inherited access, pending invitations, group membership, owner transfer restrictions, role changes, organization-only links, guest users, revoked sharing authority while dialog is open, keyboard/screen-reader operation, and a save failure after multiple staged edits. The design fails if visible controls imply authority the caller does not have or if a person’s effective access cannot be explained from the dialog.

Recover by labeling access origin, disabling impossible mutations with reason, separating pending invitations from members, previewing broad audience changes, permission-filtering identity search, and reconciling each committed mutation against authoritative effective access.

## Output Contract
Return `sharing-dialog-contract` with access-source representation, identity lookup scope, staged/direct changes, role controls, invitation handoff, link-sharing handoff, broadening warnings, commit/dismiss semantics, stale-authority recovery, accessibility behavior, and falsification cases.