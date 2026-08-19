---
name: designing-invitation-flows
description: Use when access is offered to a person who is not yet an active member and the UI must represent invitation creation, delivery, acceptance, expiry, resend, revocation, identity mismatch, and onboarding consequences.
---

# Designing Invitation Flows

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns the lifecycle between “we want this identity to gain access” and “that identity has become an active member.” It does not own general email delivery or effective permission calculation. An invitation is a pending capability with a recipient, scope, role, expiry, and acceptance state—not an already-established collaborator.

## Decision Model
Bind invitations to a stable intended identity whenever possible: verified email, directory identity, organization account, or explicit invite token. Decide whether the invitation grants access immediately on authentication or requires an acceptance act. If the invited address authenticates through a different account, the flow must detect identity mismatch rather than silently attaching access to whoever opened the link.

Represent states explicitly: creating, queued/delivered if known, pending, accepted, expired, revoked, failed delivery, superseded. “Resend” should usually preserve or rotate invitation authority according to security policy; it must not create multiple independent valid invitations whose effects are hard to revoke. Revocation should invalidate the capability, not merely remove the row from the UI.

Acceptance may require product onboarding, profile completion, terms, or workspace selection. Keep the invitation context visible through those steps so users know which organization/object they are joining and under what role. If access changed after invitation creation, show the current offered role at acceptance rather than stale copy.

## Failure Topology
- Pending invite is shown as an active member and counted in licensed seats incorrectly.
- Forwarded invitation link grants access to an unintended account because recipient identity is never checked.
- Resend creates a second valid token while the first remains active indefinitely.
- Expired invite opens a generic 404 and loses organization/context needed for recovery.
- Revoked invitation still succeeds because UI deletion was not connected to server authority.
- Acceptance flow redirects into generic onboarding and forgets the invited destination.

## Falsification and Recovery
Falsify with already-existing members, unregistered recipients, identity mismatch, expired token, resend, revoke-before-open, acceptance after role change, recipient account switch, multiple concurrent invitations, screen-reader use, and delivery failure. The design fails if pending and active membership are indistinguishable or if invitation authority can be consumed by an identity outside the intended policy.

Recover by storing canonical invitation IDs, intended recipient/scope/role, server-enforced expiry/revocation, token rotation rules, explicit mismatch handling, context-preserving acceptance, and authoritative member transition only after acceptance criteria are met.

## Output Contract
Return `invitation-flow-contract` with invite identity, recipient binding, scope/role, lifecycle states, delivery evidence, expiry/resend/revocation semantics, acceptance requirements, identity-mismatch recovery, onboarding handoff, membership transition, and falsification cases.