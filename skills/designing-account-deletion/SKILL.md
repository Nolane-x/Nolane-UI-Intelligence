---
name: designing-account-deletion
description: Use when a user closes or deletes an account and the interface must expose ownership dependencies, data consequences, retention exceptions, grace periods, reauthentication, cancellation, and irreversible boundaries using current policy authority.
---

# Designing Account Deletion

## Parent Contract
**Required parent:** `designing-authentication-and-passkeys`.

This faculty owns the consequence-bearing account-closure flow. It does not decide statutory erasure obligations, retention requirements, billing law, or organization ownership rules from memory; current legal/product authority must be verified. It also distinguishes deleting an account from leaving a workspace, deactivating a profile, cancelling a subscription, or deleting one content object.

## Decision Architecture
Resolve what entity is being deleted before showing a destructive control: personal account, profile, organization/workspace owner identity, or service login. Identify blockers such as sole ownership of a workspace, unpaid/active obligations, managed enterprise identity, pending transfer, or resources that need another owner. Do not tell users “delete all your data” if verified retention, shared-object, fraud/security, or legal obligations create exceptions.

Present consequences in concrete categories: sign-in/access loss, personal content disposition, shared content ownership, subscriptions/billing effects, active sessions/tokens, integrations, aliases/usernames, and whether restoration is possible. If a grace period exists, distinguish scheduled deletion from irreversible deletion and show the exact cancellation path and deadline in a timezone users can understand.

Require appropriate identity verification near the destructive boundary. Password re-entry may not be appropriate for passkey-only or federated accounts; use the authentication architecture's current reauth method. Typed confirmation phrases add friction only when they improve target awareness; do not use ritualistic text entry as a substitute for clear consequences and authoritative checks.

## Failure Topology
- “Delete account” actually only disables the profile while sign-in and billing continue.
- Sole workspace owner deletes account and strands organizational resources without transfer handling.
- UI promises immediate total erasure despite known retention/shared-content exceptions.
- Cancellation deadline says “7 days” but no absolute date/time or timezone is shown.
- Federated user is asked for a nonexistent local password before deletion.
- Confirmation page lists generic warnings but does not mention that a public username or shared content may remain or change ownership.

## Falsification and Recovery
Falsify with personal account, sole organization owner, federated/passkey-only auth, active subscription, shared authored content, grace-period cancellation, deletion request from another device, legal/retention exception, screen-reader operation, and the irreversible transition after grace expiry. The design fails if users cannot identify the exact account entity and durable consequences before commitment or if the UI states stronger erasure guarantees than current authority supports.

Recover by resolving account/ownership dependencies, verifying current policy, presenting concrete consequence categories, using architecture-appropriate reauth, separating scheduled from final deletion, enabling authoritative cancellation when allowed, and recording a clear completion state without exposing sensitive retention details unnecessarily.

## Output Contract
Return `account-deletion-contract` with target account entity, ownership/blocker checks, current-policy verification, consequence inventory, reauthentication method, confirmation design, grace/cancellation semantics, retention/shared-content communication, final state, accessibility behavior, and falsification cases.