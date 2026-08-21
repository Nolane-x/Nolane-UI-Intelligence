---
name: designing-device-proximity-handoff-cues
description: Use when nearby-device discovery, proximity, presence, or physical co-location can trigger or suggest a task handoff and the UI must communicate readiness, destination identity, consent, and transfer state without accidental switching.
---

# Designing Device Proximity Handoff Cues

## Intent and decision boundary
Proximity can make a handoff feel effortless, but it also creates ambiguity: several devices may be nearby, presence can fluctuate, discovery names can be weak identifiers, and an automatic transfer may interrupt the wrong task. This skill owns the Decision about when proximity is strong enough to surface a handoff cue, what that cue must disclose, and when a suggestion may advance to an explicit transfer request.

## Parent Contract
**Required parent:** `routing-ui-work`.

The parent identifies a multi-surface continuity need. Cross-device session handoff owns the actual transfer protocol; companion authority owns which surface may control the task. This specialist owns the pre-transfer and in-transfer cues produced by physical or radio proximity. It does not treat proximity as authorization.

## Proximity state machine
Model the interaction as `not-discovered → candidate-discovered → identity-resolved → eligible → offered → confirmed → transferring → transferred | declined | lost | failed`. A candidate can regress at any point because signal quality, discovery state, user movement, or device lock changes.

Eligibility combines proximity confidence with destination identity, task relevance, capability, and policy. A nearby display that cannot continue the task is not a valid handoff target. A device whose user identity cannot be established may be discoverable without being eligible.

## Cue invariants
- proximity never grants action authority by itself;
- the cue identifies the destination in a way the user can distinguish from nearby peers;
- transient discovery does not cause repeated banners, focus theft, or modal churn;
- auto-dismissal cannot be mistaken for successful transfer;
- confirmation happens before a disruptive or privacy-sensitive move unless a previously established policy explicitly permits otherwise;
- transfer progress distinguishes “preparing,” “waiting for destination,” “sent,” and “accepted” when those states differ;
- losing proximity mid-transfer has an explicit recovery state rather than leaving both surfaces uncertain.

## Evidence and observability
Evidence should include discovery traces, destination identity data, signal/proximity confidence where available, the eligibility decision, the cue shown, and the resulting transfer state. Exercise multiple nearby devices, one ineligible device, a device that disappears, a locked destination, and a candidate whose display name collides with another.

Useful Evidence also records debounce/suppression behavior: walking past the same device repeatedly should not produce an endless cascade of offers. For privacy-sensitive surfaces, verify what information is visible before confirmation versus after destination identity is trusted.

## Failure topology
Characteristic Failure includes transferring to the wrong nearby device, presenting raw hardware identifiers that users cannot distinguish, prompting continuously as signal strength oscillates, treating discovery as consent, exposing task contents before the destination is trusted, or declaring success when only transport initiation occurred. Another failure is invisible loss: the cue disappears after proximity drops and the user cannot tell whether the task stayed local, moved remotely, or duplicated.

A subtler failure is destination ambiguity caused by shared room devices. “Living Room Display” may be insufficient when several similarly named surfaces exist; the cue must use location, account, iconography, recent interaction, or another trustworthy disambiguator rather than guess.

## Falsification scenarios
Falsification moves devices across discovery thresholds, introduces two same-type devices, locks and unlocks the destination, disables its required capability, changes the signed-in user, and breaks proximity immediately after confirmation. Replay discovery events rapidly to test suppression. The contract is falsified if a handoff is initiated without a valid destination identity, if oscillating presence causes disruptive prompt storms, if the user cannot determine where the task resides after failure, or if task content leaks before consent/policy permits it.

## Recovery when presence changes
Recovery returns ownership to a known surface before attempting another transfer. Preserve the task locally until destination acceptance is authoritative. If the destination disappears before acceptance, cancel the offer and explain that nothing moved. If transport completed but acknowledgement is uncertain, reconcile session ownership rather than repeating blindly. Suppress the vanished candidate for an appropriate cooling interval while allowing manual discovery when the user explicitly asks.

## Output and Handoff
Output: `device-proximity-handoff-cues-contract`, containing discovery states, identity requirements, eligibility rules, cue priority and suppression, consent boundary, transfer-progress semantics, loss recovery, and evidence scenarios. Handoff actual session movement to cross-device session handoffs, destination capability checks to capability negotiation, and state reconstruction to task-state preservation.

## Sibling boundary
Notification continuation begins from an asynchronous alert, not physical presence. Second-screen continuity owns an already-established control relationship. Companion authority owns action rights. This skill alone owns the UX semantics that convert nearby-device evidence into a bounded, non-coercive handoff opportunity.

## Delete-the-skill test
Delete-the-skill test: without this owner, transfer protocols can still discover peers and move sessions, but no canonical contract governs when proximity is trustworthy enough to surface, how users identify the destination, or what happens when presence oscillates. That gap permits accidental transfer, privacy leakage, prompt storms, and ambiguous ownership, so proximity cues are a distinct material responsibility.