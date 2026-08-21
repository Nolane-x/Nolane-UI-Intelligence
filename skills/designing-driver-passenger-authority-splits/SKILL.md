---
name: designing-driver-passenger-authority-splits
description: Use when the same vehicle system exposes different controls, content, permissions, or interaction depth to driver and passenger surfaces and the UI must preserve role authority as occupants, seats, devices, and driving state change.
---

# Designing Driver-Passenger Authority Splits

## Occupant role changes what interaction is appropriate
A passenger may safely perform tasks that are inappropriate for the driver while moving: detailed search, long-form typing, media browsing, trip planning, or account management. This skill owns the authority model that separates driver-facing and passenger-facing interaction without assuming that every screen, touch, or device belongs to the same principal.

## Parent Contract
**Required parent:** `designing-high-stakes-decisions`.

The parent defines conservative behavior for high-stakes decisions. This specialist begins when occupant role materially affects access or task depth.

## Role and surface identity
Represent interaction authority using occupant role, seat/surface identity, driving state, authenticated account where relevant, and capability. The decision owner is not merely “driver versus passenger”; it is whether the system can establish who is interacting strongly enough to permit the requested task.

A center display shared by occupants may not have reliable actor identity. Do not grant passenger-level interaction just because a passenger is present if the system cannot determine who is using the control. Dedicated passenger displays, paired personal devices, or explicit handoff mechanisms may provide stronger evidence.

## Authority transfer
Trip planning or media selection can move between driver and passenger. Transfer should preserve task state while re-evaluating permissions. If a passenger starts a detailed flow and hands it back to the driver while moving, the driver surface may need a simplified review/accept action rather than full editing.

When occupants change seats or leave, revoke role-specific capabilities and protect personal data. Passenger privacy may matter even inside the vehicle; sensitive account details shown on a passenger display should not automatically mirror to the cluster or driver surface.

## Shared outcomes
Some passenger actions affect shared vehicle state: navigation destination, climate, media, charging plan, or seat-dependent settings. Define which require driver awareness or confirmation and which can apply directly. Do not make every passenger action subordinate to the driver if product/system authority says otherwise; instead model the actual shared-state owner.

## Evidence
Evidence includes occupant/surface identity, role resolution, driving state, capability matrix, handoff traces, seat-change behavior, shared-state changes, and data-visibility boundaries. Test unknown actor on a shared center screen, passenger exit mid-task, role transfer during motion, and personal-device continuation.

## Failure modes
Characteristic Failure includes passenger presence unlocking a shared driver screen, driver inheriting a passenger’s high-demand task while moving, sensitive passenger data mirrored globally, stale passenger privileges after seat change, and shared settings modified with no visible ownership. Another failure is role confusion after profile switching or valet/guest modes.

## Falsification
Change occupant role, remove actor identity, transfer an active task between surfaces, switch profiles, and alter driving state during handoff. The contract fails if a lower-confidence actor gains stronger capability, if sensitive data crosses surfaces unexpectedly, if task state bypasses driver lockout after transfer, or if shared-state authorship becomes ambiguous.

## Recovery
On role uncertainty, reduce to the safest capability appropriate for the known surface while preserving task data privately. Re-resolve occupant identity, invalidate stale grants, and present a deliberate handoff if a task must continue elsewhere. For accidental cross-role disclosure, stop further propagation and record the affected surfaces for privacy recovery.

## Output and Handoff
Output: `driver-passenger-authority-splits-contract`, containing role evidence, surface identity, capability matrix, handoff rules, shared-state ownership, data boundaries, and recovery. Handoff driver action availability to driving-state lockouts and cross-device continuation to multi-surface continuity.

## Sibling Boundary and delete-the-skill
Sibling driving-state lockouts decide whether driver actions are available under motion/workload. This skill decides which occupant principal owns which capability. The delete-the-skill test passes because without a role authority owner, passenger capability is easily implemented as a loophole around driver restrictions or privacy boundaries.