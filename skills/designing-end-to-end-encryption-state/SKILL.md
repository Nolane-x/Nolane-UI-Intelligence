---
name: designing-end-to-end-encryption-state
description: Use when realtime communication uses end-to-end encryption and users need to understand room/session encryption, device trust, undecryptable content, key backup or recovery, and the limits of what encryption status proves.
---

# Designing End to End Encryption State

Encryption state is a cryptographic guarantee boundary, not a decorative lock icon. The interface must state what content is encrypted end-to-end, which devices can decrypt it, what trust/verification exists, and when key material is missing or recovery changes the guarantee.

## Parent Contract
**Required parent:** `designing-realtime-communication-systems`.

The parent owns the communication system. This skill owns user-visible encryption/decryption state; verification ceremony is delegated to `designing-key-verification-flows`.

## Guarantee Model
Separate transport security, room/session end-to-end encryption, device verification, participant identity, and key backup. A room can be end-to-end encrypted while containing unverified devices. A verified device does not imply every future device from that person is verified.

Expose the encryption state where it matters: room info, participant/device inspection, message decryption failures, call encryption if governed separately, and export/backup actions. Avoid permanent security chrome that users learn to ignore while hiding the rare degraded state.

## Undecryptable Content
An undecryptable message is not the same as deleted or corrupted content. Show that encrypted content exists but the current device lacks valid keys, and offer policy-approved recovery such as requesting keys, restoring backup, or verifying another device. Do not reveal ciphertext or technical identifiers as the primary user explanation.

## Membership and Device Change
When a new device joins or a participant's trust state changes, decide whether the protocol/security policy requires warning, re-verification, or no interruption. Preserve historical fact: messages already shared with a device cannot be “unshared” simply by later removing that device.

## Key Recovery and Backup
Backup/recovery state should distinguish enabled, current, stale, unavailable, restoring, and failed. A recovery key or secret phrase is sensitive; design copy/capture flows to avoid accidental disclosure. Restoring keys may unlock old messages but should not falsely mark a device as identity-verified.

## Evidence
Test encrypted room creation, new unverified device, verified device, key backup enabled/disabled, missing key, recovery restore, participant removal, session rotation, app reinstall, and encrypted call if supported. Validate visible claims against protocol/device state.

## Failure Modes
- Lock icon implies participant identity verification.
- Undecryptable content is labelled “deleted.”
- Key restore silently upgrades device trust.
- Removing a device implies old messages are recalled from it.
- Backup is shown healthy when stale or incomplete.
- Security warning appears on every normal key rotation and causes habituation.

## Falsification
Add an unverified device to an encrypted room and restore old keys onto it. Falsify if the UI now claims identity verification merely because decryption works, or if users cannot distinguish encryption availability from trust.

## Recovery
Recompute status from cryptographic/session evidence, separate decryption capability from identity verification, expose missing-key recovery, and downgrade stale backup claims. If the client cannot determine encryption guarantee, present UNKNOWN rather than an unconditional secure badge.

## Handoff
Verification ceremonies use `designing-key-verification-flows`; room membership changes use `designing-room-channel-membership`; call-specific device checks may coordinate with `designing-call-join-device-checks`.

## Output Contract
Return an `end-to-end-encryption-state-contract` with `guarantee_layers[]`, `room_encryption_state`, `device_trust_states[]`, `undecryptable_states[]`, `membership_device_change_rules`, `backup_recovery_states[]`, `security_claim_boundaries`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.