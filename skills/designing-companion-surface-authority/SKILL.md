---
name: designing-companion-surface-authority
description: Use when a secondary device or companion surface can view, propose, or control state belonging to a primary product and the UI must define which surface is authoritative for each action, how conflicts are surfaced, and what happens when the primary is unavailable.
---

# Designing Companion Surface Authority

## Companion does not mean subordinate in every dimension
A phone controlling a TV, a watch approving a desktop action, a tablet supervising a machine, or a passenger device editing a vehicle route can each own different kinds of authority. This skill owns the authority partition between primary and companion surfaces rather than assuming one global master device.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent selects this specialist when two or more surfaces participate in one task with unequal or scoped control. Capability negotiation and state conflict resolution are siblings; this skill defines who is allowed to decide what.

## Authority map
For each action or state field, record authoritative source, proposal sources, required confirmation surface, fallback authority, and visibility. A companion may be authoritative for personal preferences but only advisory for shared playback; a watch may approve an action without being able to edit its parameters; a vehicle passenger device may propose a destination that the driver confirms.

The decision owner is action-specific authority. Do not infer authority from which surface was opened first or which one has richer UI. Surface role, authenticated principal, safety/privacy context, and domain rules determine ownership.

## Primary unavailable states
When the nominal primary surface disconnects, define whether companion capabilities persist, degrade, or stop. Some tasks can continue because authority lives in a backend account; others require proximity or a primary-device attestation. Make the degraded mode visible instead of letting stale controls appear active.

## Confirmation and feedback
A companion action needs authoritative feedback from the system that owns the state. Optimistic local feedback should be labeled pending until accepted. If an action requires confirmation elsewhere, show the waiting state and destination of the request. Do not let the companion claim success merely because it sent a command.

## Privacy and visibility
Companion surfaces may reveal data in different social contexts. Scope what can be mirrored to watches, shared TVs, vehicle displays, or guest devices. Authority to control does not necessarily imply authority to see all underlying data.

## Evidence
Evidence includes the action/state authority map, principal and device identity, proposal/confirmation flow, primary-unavailable behavior, command acknowledgements, and privacy boundaries. Test simultaneous actions from primary and companion, role changes, connectivity loss, and stale companion state.

## Failure modes
Characteristic Failure includes both surfaces believing they are canonical, a companion showing successful state before the primary/backend accepts it, controls remaining active after authority is lost, privacy-sensitive details mirrored solely because control permission exists, and a supposedly subordinate surface silently overriding the primary.

## Falsification
Disconnect the primary, swap principals, send conflicting commands, revoke companion capability, and delay authoritative acknowledgement. The contract fails if the companion cannot explain its current authority, if an unauthorized surface wins by event timing, if local success diverges from canonical state, or if protected data leaks across the authority boundary.

## Recovery
On authority ambiguity, freeze disputed side effects, resolve current principal/device roles, query the authoritative state source, and re-render controls from that result. If both surfaces issued conflicting writes, route to cross-device state conflict resolution. Revoke stale companion grants explicitly when role or trust changes.

## Output and Handoff
Output: `companion-surface-authority-contract`, containing action-level authority, proposal/confirmation paths, primary-unavailable policy, feedback truth, privacy scope, and evidence. Handoff conflicting writes to cross-device state conflicts and unsupported capability to capability negotiation.

## Sibling Boundary and delete-the-skill
Sibling second-screen control continuity owns uninterrupted control as users move between cooperating surfaces; this skill decides which surface is allowed to control each domain action in the first place. The delete-the-skill test passes because without an authority map, multi-surface products default to last-writer-wins or implicit “primary device” assumptions that break under disconnects and role changes.