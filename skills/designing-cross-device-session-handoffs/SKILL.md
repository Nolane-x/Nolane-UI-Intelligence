---
name: designing-cross-device-session-handoffs
description: Use when a user intentionally moves an active task from one device or surface to another and the product must transfer session identity, task position, authority, privacy context, pending operations, and recovery state without duplicating or losing work.
---

# Designing Cross-Device Session Handoffs

## A handoff moves work, not merely a deep link
Opening the same route on another device is not enough when a task has unsaved edits, pending operations, focus/selection context, approvals, or privacy constraints. This skill owns the explicit transfer contract that moves an active session from source to destination while preserving one coherent task identity.

## Parent Contract
**Required parent:** `routing-ui-work`.

The routing parent selects this specialist when continuity across devices is a material product behavior. Task-state preservation, capability negotiation, and conflict resolution are neighboring skills; this owner governs the handoff transaction itself.

## Handoff record
Represent a handoff using source device/session, destination device/session, task identity, checkpoint revision, transferable artifacts, nontransferable state, pending side effects, authority/credential requirements, and completion status. The decision owner is when the destination has accepted enough state for the source to relinquish ownership.

Avoid instant source shutdown before destination acceptance. A two-phase model—offer/prepare, then accept/commit—prevents lost work. If both devices remain active after handoff, define whether the source becomes read-only, stays a peer, or requires explicit “continue here” reclaim behavior.

## Security and privacy
Re-authenticate or step up authentication when the destination’s trust level requires it. Do not transfer sensitive content to a lock-screen, shared TV, vehicle, or unmanaged device merely because it is nearby. A session token copied across devices must be scoped according to product security policy rather than inferred from UX convenience.

## Pending operations
A handoff may occur while uploads, agent runs, payments, or other async actions are active. Preserve their execution identity and show them on the destination rather than starting duplicates. If an operation is source-local and cannot continue remotely, classify it explicitly and keep the source active or pause safely.

## Evidence
Evidence includes handoff offer, checkpoint revision, destination acceptance, credential/authority validation, transferred artifacts, pending-operation identity, source disposition, and recovery after failed transfer. Test destination timeout, source disconnect after offer, destination denial, and handoff during an in-flight side effect.

## Failure modes
Characteristic Failure includes opening a stale snapshot on the new device, duplicate background operations, source and destination both believing they are sole owner, sensitive data appearing on an inappropriate surface, and lost drafts when the source closes too early. Another failure is ambiguous completion: both devices show “continue” but neither reflects later edits from the other.

## Falsification
Interrupt transfer at every phase, reject authentication on destination, mutate task state during handoff, and complete a pending operation while ownership changes. The contract fails if work is lost or duplicated, if destination authority is assumed rather than proven, if the source relinquishes before acceptance, or if session ownership cannot be reconstructed afterward.

## Recovery
If destination acceptance fails, retain source ownership and invalidate the pending transfer token. If ownership is ambiguous, freeze side-effecting actions, compare session revisions, and choose/reconcile a canonical continuation. Preserve pending operation identities so recovery does not create duplicates.

## Output and Handoff
Output: `cross-device-session-handoffs-contract`, containing transfer phases, checkpoint identity, source/destination disposition, credential validation, pending-operation handling, and evidence. Handoff state payload preservation to task-state-across-device switching and capability gaps to cross-device capability negotiation.

## Sibling Boundary and delete-the-skill
Sibling notification-to-app continuation starts from an asynchronous notification rather than an explicit live transfer. This skill owns deliberate session ownership movement. The delete-the-skill test passes because without a handoff transaction, cross-device continuation devolves into deep links that cannot protect unsaved state, in-flight work, or single-session ownership.