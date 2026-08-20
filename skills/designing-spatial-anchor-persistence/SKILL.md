---
name: designing-spatial-anchor-persistence
description: Use when XR content should remain associated with a physical or world location across app sessions, tracking resets, devices, or shared users and the interface must expose anchor creation, localization, confidence, loss, relocalization, and deletion honestly.
---

# Designing Spatial Anchor Persistence

A persistent spatial anchor is a claim that digital content corresponds to a location beyond the current tracking session. The UI must distinguish a successfully stored anchor from a later successful relocalization and must not fake continuity when localization evidence is weak.

## Parent Contract
**Required parent:** `designing-spatial-xr-interfaces`.

The parent owns XR spatial composition. This skill owns anchor lifecycle and user-visible persistence confidence across sessions or devices.

## Anchor Lifecycle
Model creation/requested, local anchor established, persistence save pending, saved, localizing, localized with confidence, relocated, unavailable, lost, expired, and deleted states according to platform capability. “Pinned” should not mean durable if the anchor exists only in memory.

Capture anchor scope: current device, account/cloud, shared space, room/session, or local map. Users should know whether another device/person can see the same placement and what permissions are required.

## Localization
On reopen, do not render persisted content at a guessed pose while localization is unresolved. Provide a scanning/localization state and, where useful, spatial guidance. If confidence is low, choose whether to hide, ghost, or mark approximate content based on task risk.

When an anchor cannot be found, distinguish temporary localization failure from deletion/expiry. Offer rescan or deliberate relocation. Relocation should create a new anchor revision or explicit moved state so history does not claim the object never changed physical location.

## Shared and Sensitive Anchors
Shared anchors require ownership and conflict rules. Two users may relocalize with different confidence or attempt to move/delete the same anchor. Sensitive anchored content should not become visible solely because physical location matches; authorization remains separate.

## Evidence
Test save/reopen, app reinstall where supported, origin recenter, moving to another room, low-light/changed environment, device change, shared-user localization, anchor deletion, and explicit relocation. Record platform anchor IDs/confidence and rendered pose.

## Failure Modes
- Temporary local pose is labelled saved/persistent.
- Content appears at stale coordinates before relocalization.
- Low-confidence anchor is rendered as exact.
- Relocation overwrites history without an anchor revision.
- Physical location bypasses account/content authorization.
- Delete UI removes local representation but leaves shared/cloud anchor active.

## Falsification
Save an anchor, materially alter the environment, restart in a shifted origin, and attempt localization from a second device. Falsify if content appears exact before evidence supports it or if one user's relocation silently changes another's view without conflict state.

## Recovery
Return to localization state, expose confidence, require deliberate relocation, preserve revision/ownership, and verify remote deletion. Unknown anchor state remains unresolved rather than snapping to the last remembered transform.

## Handoff
Origin-reset recovery uses `designing-xr-recenter-and-origin-recovery`; panel geometry uses `designing-world-space-panel-placement`; authorization remains under privacy/permissions owners.

## Output Contract
Return a `spatial-anchor-persistence-contract` with `anchor_states[]`, `persistence_scope`, `localization_confidence`, `unresolved_render_policy`, `relocation_revision`, `shared_ownership`, `authorization_boundary`, `deletion_semantics`, `evidence_cases[]`, and `recovery_actions[]`.