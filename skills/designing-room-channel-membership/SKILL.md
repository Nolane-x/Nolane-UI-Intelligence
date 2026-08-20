---
name: designing-room-channel-membership
description: Use when realtime communication spaces have joins, invites, requests, leaves, kicks, bans, roles, guests, history visibility, and membership changes that affect what a participant may see or do.
---

# Designing Room and Channel Membership

Membership defines the social and authorization boundary of a communication space. It is not equivalent to presence: a member can be offline, and a present guest may have limited history or action rights.

## Parent Contract
**Required parent:** `designing-realtime-communication-systems`.

The parent owns communication-system orchestration. This skill owns room/channel membership lifecycle, role capability, invite/request flows, history visibility, and membership-change consequences.

## Membership States
Model invited, join-requested, joined, guest/limited, left, removed, banned, and pending verification states where the protocol supports them. Distinguish local optimistic state from accepted server membership. A join button should not immediately expose private history before authorization has actually succeeded.

Roles and capabilities should be derived from the current room policy rather than hardcoded labels. Moderator, owner, guest, external participant, or custom roles may have different abilities to post, invite, call, redact, pin, or view history. Show relevant capability differences without forcing users to reverse-engineer a permission matrix.

## History and Privacy
Joining can expose historical messages according to room policy; leaving or being removed may revoke future access without necessarily erasing previously downloaded content. Communicate the policy accurately. Never imply that removing a participant cryptographically removes information already obtained unless the system can prove it.

Invites should identify inviter and destination room safely. For federated or cross-organization systems, show the room/community identity and trust boundary before accepting. Handle revoked or expired invites distinctly from network failure.

## Membership Changes During Use
If a user's permission changes while composing, calling, or sharing a screen, revalidate actions. Preserve unsent content locally when safe but do not keep sending after permission removal. For other participants, show join/leave/kick changes in a way that maintains conversational context without overwhelming the timeline.

## Evidence
Test invite, join request, approval, guest access, role promotion/demotion, leave, kick, ban, rejoin, expired invite, and permission change during an active session. Verify server membership and visible controls align after reconnect on multiple devices.

## Failure Modes
- Presence dot is treated as membership authority.
- Optimistic join exposes history before authorization.
- Leaving is described as deleting prior access or copies.
- Role change does not update active call/share capabilities.
- Expired invite looks like a generic connectivity error.
- Removed member can continue posting from a stale client.

## Falsification
Open the same room on two devices, demote/remove the user from one administrative session, then attempt to post and share from the stale device. Falsify if the UI predicts authorization incorrectly or continues consequential activity without revalidation.

## Recovery
Refresh authoritative membership/capability state, stop disallowed live actions, preserve local unsent drafts without transmitting, and explain whether history remains locally available. Avoid fake certainty about erasure or revocation beyond protocol guarantees.

## Handoff
Moderation enforcement uses `designing-moderation-action-surfaces`; call participation uses `designing-call-participant-layouts`; encryption membership implications coordinate with `designing-end-to-end-encryption-state`.

## Output Contract
Return a `room-channel-membership-contract` with `membership_states[]`, `capability_derivation`, `invite_request_flows`, `history_visibility_policy`, `role_change_behavior`, `active_action_revalidation`, `privacy_claim_boundary`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.