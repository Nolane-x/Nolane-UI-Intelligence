---
name: designing-secret-credential-management
description: Use when operators create, store, rotate, revoke, scope, and audit API keys, tokens, client secrets, or other credentials and the UI must minimize disclosure while preserving identity and operational control.
---

# Designing Secret Credential Management

## Parent Contract
**Required parent:** `designing-privacy-sensitive-interfaces`.

This faculty owns human interaction with secret-bearing credentials. It does not implement cryptographic storage or authentication protocols. Its design goal is to let operators manage a credential lifecycle without repeatedly exposing the secret value or confusing the credential's identity with the sensitive material itself.

## Decision Architecture
Separate credential metadata from secret material. Stable name/ID, owner, scope, environment, permissions, creation time, last use, expiration, fingerprint/prefix, and rotation state can remain inspectable; the secret should generally be shown only at creation/rotation when product architecture allows. A “Reveal” button that can always recover the plaintext is not a neutral convenience—it changes the security model and requires explicit authority.

Creation needs scope-first decisions. Users should understand which API/resources/environment a credential can access before the secret is minted. Copy/download controls require confirmation that this may be the only display opportunity and should avoid auto-copy telemetry. If a key is never copied before dismissal, offer regeneration rather than pretending the lost secret can be recovered.

Rotation is not simply create-new/delete-old. Define overlap windows, replacement identity, downstream update guidance, last-used evidence, and final revocation. Revocation is destructive and may break production systems; show affected integrations when evidence exists and distinguish revoke now from expire at a scheduled time.

## Failure Topology
- Full API token remains permanently visible in a settings table.
- Secret value is included in analytics events when Copy is pressed.
- Rotation instantly revokes old credential before dependent systems can switch.
- Key names such as “production” are editable but environment/scope is hidden, causing operators to rotate the wrong credential.
- “Last used” is presented as exact liveness although usage telemetry is delayed or incomplete.
- Revoked secret can still be copied from browser state because UI retained plaintext.

## Falsification and Recovery
Falsify with create-and-close before copy, multiple production/staging credentials, rotation overlap, permission downgrade, expired credential, revocation with active integration, delayed usage telemetry, keyboard/screen-reader copy flow, and a user lacking secret-management authority. The design fails if secret plaintext survives beyond its required display boundary or if a credential mutation can occur without clear scope/environment identity.

Recover by one-time secret display, metadata-first management, minimized client retention, scope previews, controlled overlap rotation, explicit revocation consequences, redacted audit/history, and server-authoritative permission checks for every lifecycle action.

## Output Contract
Return `secret-credential-management-contract` with credential metadata, secret-display boundary, creation/copy behavior, scope/environment representation, expiration, rotation overlap, usage-evidence caveats, revocation consequences, audit/redaction rules, authority checks, and falsification cases.