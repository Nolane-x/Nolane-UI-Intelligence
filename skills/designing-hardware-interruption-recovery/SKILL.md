---
name: designing-hardware-interruption-recovery
description: Use when a physical device can disconnect, jam, reboot, sleep, lose power, be taken by another app, or otherwise interrupt an in-progress operation and the product must reconcile whether work completed, can resume, or must restart safely.
---

# Designing Hardware Interruption Recovery

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns recovery after an operation has already started on hardware. It is distinct from initial device availability. The hardest state is uncertainty: software may lose contact after the device partially or fully completed a physical action.

## Decision Boundary
For each hardware command, define acknowledgment stages and idempotency. A scanner may have captured pages before USB disconnect; a printer may have physically printed labels before the app lost spooler status; a camera may have written a file before stream interruption. Never retry a potentially non-idempotent physical action automatically without reconciling evidence.

Classify interruption as resumable transfer/session, recoverable after device returns, terminal restart, or uncertain completion requiring user inspection. Preserve task state while connection is restored and show the exact point of uncertainty. Provide safe “check device then continue” steps when software cannot know physical outcome. If the OS owns queue recovery, hand off instead of duplicating it.

## Failure Topology
- App resends a print command after timeout and produces duplicate shipping labels.
- Scan session drops after page 20 and restarts from page 1 without preserving captured pages.
- Device reconnects but UI retains a permanent error until app restart.
- “Retry” is offered even though completion status is unknown and action is non-idempotent.
- Interruption message says nothing about whether physical output may already exist.
- Partial device-side data is imported twice after reconnect.

## Falsification and Recovery
Interrupt every major hardware operation at pre-ack, mid-operation, post-physical/pre-software-ack, and reconnect stages. Test power loss, cable/network drop, OS preemption, device busy, and app crash. The design fails if automatic recovery can duplicate or omit physical outcomes without revealing uncertainty.

Recover by recording operation IDs/ack stages, reconciling device state before retry, preserving partial results, making uncertain-completion state explicit, and routing non-idempotent actions through user/device verification.

## Output Contract
Return `hardware-interruption-recovery-contract` with operation acknowledgment stages, idempotency classification, partial-result preservation, reconnect reconciliation, uncertain-completion UI, retry/restart policy, and fault-injection verification cases.
