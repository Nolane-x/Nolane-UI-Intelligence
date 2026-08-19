---
name: designing-collaboration-permissions
description: Use when a shared artifact exposes collaborator roles and capabilities and the interface must show effective access, inheritance, role changes, unavailable actions, and consequence without becoming a generic RBAC administration matrix.
---

# Designing Collaboration Permissions

## Parent Contract
**Required parent:** `designing-permissions-and-consent`.

This faculty owns object- and collaboration-facing permission UX: who may view, comment, edit, share, manage, or perform other collaboration actions on the current resource. It does not own organization-wide RBAC policy or the full administrative role matrix. Its emphasis is effective authority at the point where collaborators work together.

## Decision Model
Translate policy into capabilities users can reason about. Named roles such as Viewer, Commenter, Editor, or Manager are useful only when their effective actions are defined. If access is inherited from a workspace, group, or parent folder, show that origin; a role selector must not imply the caller can reduce inherited authority from the child resource.

Separate role labels from exceptional capabilities. Some products allow sharing without editing, download restrictions, external guest limits, or temporary access. Avoid adding a new pseudo-role for every exception if the policy model is actually role plus capability constraints. The UI should mirror the authoritative permission engine instead of reconstructing permission rules client-side.

Role changes can have immediate destructive effects: losing edit access, invalidating active sessions, removing comments, or preventing further sharing. Preview material consequences before high-impact changes. When another administrator changes permissions concurrently, reconcile to current effective authority rather than letting stale controls overwrite newer policy.

## Failure Topology
- Child-resource UI offers “Remove access” to someone whose access is inherited from a parent group.
- Role names look simple but hide a critical capability difference such as ability to reshare externally.
- Client hides an action but backend permits it, or exposes an action the backend rejects, creating contradictory authority cues.
- Downgrading an editor silently discards their unsaved work or active operation.
- Two administrators edit roles from stale screens and last-write-wins unexpectedly broadens access.
- Disabled actions have no explanation, making users think the product is broken rather than permission-bound.

## Falsification and Recovery
Falsify with direct plus inherited access, group membership, external guests, role changes while an editor is active, stale admin screens, owner-only actions, revoked caller authority, keyboard/screen-reader navigation, and a capability that is denied by policy despite the nominal role. The design fails if effective access cannot be explained from visible policy sources or if the UI can authorize more than the backend permission engine.

Recover by using server-computed effective capabilities, labeling access origin, separating nominal role from capability exceptions, invalidating stale mutations, surfacing change consequences, and explaining disabled controls without leaking sensitive policy detail.

## Output Contract
Return `collaboration-permission-contract` with collaboration roles, effective capability map, inheritance/source representation, exceptional constraints, mutation authority, concurrent-change handling, consequence preview, disabled-action explanations, active-session effects, and falsification cases.