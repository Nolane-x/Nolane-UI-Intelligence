---
name: designing-moderation-action-surfaces
description: Use when moderators or authorized participants must warn, mute, remove, ban, redact, restrict, lock, report, or reverse communication-space actions with clear scope, evidence, authority, duration, and audit consequence.
---

# Designing Moderation Action Surfaces

Moderation controls change other people's ability to communicate or the visibility of their content. The interface must make scope and consequence explicit, preserve evidence, and prevent high-impact enforcement from being hidden behind generic overflow actions.

## Parent Contract
**Required parent:** `designing-realtime-communication-systems`.

The parent owns communication state. This skill owns enforcement action selection, scope, reason, duration, confirmation, audit, and reversal. General room membership is coordinated but not redefined here.

## Action Taxonomy
Separate warn, local mute, server mute/restrict, remove from call, kick from room, ban, temporary timeout, delete/redact content, lock thread/channel, restrict posting, and report/escalate according to platform capabilities. A local personal mute must not look like a moderator action that affects everyone.

For every consequential action show target identity, scope (message/thread/room/community/call), duration, immediate effect, downstream effect on history/membership, and whether reversal is possible. High-impact actions should require confirmation proportional to consequence rather than every action receiving the same modal.

## Evidence and Reason
Moderators need relevant event/message/member context and policy reason. Preserve exact target event/revision; edited or redacted content should not cause the moderation record to lose what was reviewed where retention policy permits. Structured reason categories support audit, but free-form notes may be needed for nuance.

## Permissions and Concurrency
Derive controls from current moderation capability. Revalidate before commit because roles can change while the menu is open. If two moderators act concurrently, show confirmed final state and avoid duplicate/conflicting punishments. A ban already applied should not allow a stale client to issue an unrelated second ban record by accident.

## User-Facing Consequence
Affected users should receive the policy-appropriate explanation and appeal/review route without exposing confidential moderator information. Other members may need a bounded system event, but avoid unnecessary spectacle that amplifies abuse.

## Evidence
Test message redaction, temporary mute, kick, ban, role revocation mid-action, concurrent moderator actions, appeal/reversal, user on multiple devices, active call removal, and offline target client reconnect. Verify server enforcement and audit record.

## Failure Modes
- Personal mute and moderator mute are indistinguishable.
- Ban scope is unclear between room and whole service.
- Moderator role is revoked but stale menu still executes action.
- Redaction deletes audit evidence needed for review.
- Duplicate concurrent actions create inconsistent status.
- Affected user receives no reason or available review route when policy requires it.

## Falsification
Open a ban confirmation, revoke moderator permission from another session, then commit. Falsify if the stale action executes without authoritative revalidation. Apply two simultaneous actions to one user; falsify if the final enforcement/audit state cannot be reconstructed.

## Recovery
Reload capability and target state, deduplicate enforcement by canonical case/action identity, preserve evidence according to policy, and present the confirmed result. If moderation authority is uncertain, block enforcement rather than guessing from cached role labels.

## Handoff
Membership consequences use `designing-room-channel-membership`; end-to-end encryption limits on redaction/erasure claims use security owners; marketplace-specific party messaging has its own policy boundary.

## Output Contract
Return a `moderation-action-surfaces-contract` with `action_types[]`, `scope_model`, `duration_rules`, `consequence_preview`, `evidence_binding`, `reason_model`, `capability_revalidation`, `concurrency_rules`, `affected_user_copy`, `audit_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.