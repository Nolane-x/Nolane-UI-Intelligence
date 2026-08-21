---
name: designing-cross-device-capability-negotiation
description: Use when a task can move among devices or surfaces whose input, output, security, connectivity, sensor, or execution capabilities differ and the UI must negotiate what remains possible without lying about equivalence.
---

# Designing Cross-Device Capability Negotiation

## Problem ownership
Multi-device products often say a task is “available everywhere” when the surfaces are not actually equivalent. A phone may have a camera and secure enclave; a desktop may have a full keyboard and large viewport; a TV may have only remote focus; a wearable may permit glanceable confirmation but not long-form editing. This skill owns the Decision that maps a task requirement set against device capabilities and chooses full transfer, degraded transfer, delegated action, deferred action, or refusal.

## Parent Contract
**Required parent:** `routing-ui-work`.

The parent routes multi-surface continuity work. This specialist begins when two candidate surfaces disagree on capabilities. It does not own responsive layout, platform styling, or generic permissions; it owns the negotiation contract that determines whether the destination can faithfully continue the task.

## Capability vocabulary
Describe a surface with typed capabilities rather than product names: `input`, `display`, `compute`, `network`, `identity-assurance`, `sensors`, `storage`, `background-execution`, `media`, and `regulated-action` constraints. Each task declares hard requirements, soft preferences, and compensating alternatives.

The negotiation result is one of `equivalent`, `adapted`, `delegated`, `deferred`, or `blocked`. “Adapted” means the task remains semantically complete with a different interaction. “Delegated” means another surface must perform a sub-operation. “Deferred” means state can transfer but execution waits for a required capability. Those states must not be collapsed into “unsupported.”

## Non-negotiable invariants
- a destination never claims full continuation when a hard capability is absent;
- a softer interaction substitute cannot weaken identity, safety, or regulatory requirements;
- capability detection is fresh enough for volatile properties such as network, attached controller, permission, or nearby hardware;
- the user can understand which part of the task moved and which part did not;
- negotiation is based on task semantics, not device prestige or screen size alone;
- loss of a capability after transfer triggers renegotiation instead of silent feature disappearance.

## Evidence model
Evidence must include a capability matrix with at least one missing-hard-requirement case, one viable adaptation, one delegation path, and one capability that changes during the session. Record the task requirements, the detected device facts, the negotiation verdict, and the visible UI result. For security-sensitive capabilities, retain the authoritative source of the claim rather than trusting a frontend flag.

Useful Evidence also includes replay traces from real or emulated devices showing capability arrival/removal, permission revocation, connectivity loss, and external-accessory disconnect.

## Characteristic Failure classes
Failure appears when a transferred task reaches a dead-end control that the destination can never satisfy, when a weaker device silently skips required verification, when the UI shows an action that depends on an absent sensor, or when a capability is inferred from form factor instead of detected state. A subtler failure is false degradation: the product sends the user back to another device even though an equivalent accessible interaction was available locally.

Another failure is negotiation drift, where two surfaces independently decide compatibility and disagree, producing oscillating handoffs or contradictory calls to action.

## Falsification procedure
Falsification removes or mutates one capability at a time: disconnect the camera, deny microphone permission, remove the hardware keyboard, disable secure authentication, drop network transport, revoke background execution, or switch to a device with a different controller model. Also introduce an alternative capability that should satisfy the same semantic need. The contract fails if the UI continues as though nothing changed, blocks an actually equivalent path, weakens a hard requirement, or sends the user into a handoff loop.

## Recovery and renegotiation
Recovery recomputes from authoritative capabilities and preserves task state while changing only the execution plan. Explain the missing requirement in task language, then offer viable adaptations or delegation targets. If a required capability returns, allow resumption without forcing the user to restart unrelated completed work. If no safe path exists, preserve a bounded checkpoint and state exactly what capability is needed next.

## Output and Handoff
Output: `cross-device-capability-negotiation-contract`, containing task requirements, capability taxonomy, verdict rules, adaptation/delegation policies, renegotiation triggers, evidence fixtures, and blocked-state obligations. Handoff platform detection to platform specialists, permission acquisition to permission owners, and task-specific business rules to their domain owners.

## Sibling exclusions
Session handoff owns the movement of an active session. Task-state preservation owns reconstructable work state. Proximity cues own when nearby-device transfer should be suggested. This skill does not decide whether transfer is desirable; it decides whether the receiving surface can actually satisfy the task and under what semantic degradation.

## Delete-the-skill argument
Delete-the-skill test: without this owner, multi-device flows can still transfer identifiers and UI state, but there is no canonical decision point that compares task requirements against destination capabilities. The result is either false equivalence or blanket incompatibility. Because that missing decision changes safety, completion, and accessibility, capability negotiation cannot be reduced to responsive design or platform adaptation.