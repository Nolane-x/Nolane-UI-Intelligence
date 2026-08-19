---
name: designing-two-factor-enrollment
description: Use when users add a second authentication factor and the interface must coordinate factor choice, setup, verification, naming, recovery, policy requirements, and safe completion without treating an unverified setup as active protection.
---

# Designing Two-Factor Enrollment

## Parent Contract
**Required parent:** `designing-authentication-and-passkeys`.

This faculty owns the enrollment lifecycle for an additional authentication factor such as authenticator app, hardware key, security key, SMS/voice where policy permits, or another service-supported factor. It does not decide which factor types satisfy current assurance requirements; that must come from the authentication architecture and current policy.

## Decision Architecture
Separate factor selection, provisioning, verification, recovery preparation, and activation. A QR code or shared secret being displayed does not mean the factor is enrolled. Require proof that the user can produce a valid response before marking it active. If organization policy requires a particular factor class, explain the requirement and unavailable alternatives rather than presenting all options as equivalent.

Provisioning material is sensitive. QR codes, setup keys, and hardware enrollment challenges should not be logged, cached indefinitely, or exposed in analytics. Provide a manual setup path when camera/QR scanning is unavailable. When the factor represents a physical device, let users assign a recognizable name after successful verification so later session/security management is comprehensible.

Recovery should occur before the user relies on the new factor. If recovery codes or backup methods are required, verify that the user has acknowledged or safely stored them according to product policy without forcing insecure behaviors such as copying secrets into ordinary notes. Completing enrollment may invalidate sessions or alter account-security posture; route those effects explicitly.

## Failure Topology
- QR code is shown and the settings page immediately marks 2FA enabled without verifying a generated code.
- Setup secret is sent to analytics because the QR component records its payload.
- User loses access to the authenticator during setup and has no way to restart provisioning cleanly.
- Mandatory organization policy says “Use any method” although only phishing-resistant factors actually satisfy the requirement.
- Recovery-code step is skippable despite account policy depending on it for safe recovery.
- Enrolling a second device accidentally replaces the first factor because factors lack stable identity.

## Falsification and Recovery
Falsify with invalid verification code, clock skew for TOTP, QR scanner unavailable, manual secret entry, hardware-key cancellation, duplicate factor name, organization-required factor type, session expiry mid-enrollment, recovery-code generation, screen-reader operation, and setup abandoned after secret issuance. The design fails if unverified provisioning becomes active authority or if secret setup material survives beyond its justified boundary.

Recover by treating enrollment as a server-backed state machine, verifying possession before activation, protecting provisioning material, supporting restart/manual paths, naming factors by stable identity, enforcing current policy, and completing required recovery preparation before declaring the account protected.

## Output Contract
Return `two-factor-enrollment-contract` with supported factor classes, policy eligibility, provisioning states, verification proof, secret-data boundaries, manual/alternate setup, factor naming, recovery preparation, abandonment/restart, post-enrollment session effects, accessibility behavior, and falsification cases.