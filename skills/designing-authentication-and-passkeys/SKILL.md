---
name: designing-authentication-and-passkeys
description: Use when a UI handles sign-in, sign-up, passkeys, passwords, MFA, reauthentication, account switching, device transitions, credential recovery, or authentication errors where security and user mental models interact.
---

# Designing Authentication and Passkeys

## Overview
Authentication is a continuity problem across person, account, credential, and device. Make the user understand which account they are entering, what credential is being used, what happens on another device, and how recovery works without leaking account existence.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require authentication methods, account identifiers, device/platform, risk class, recovery channels, MFA/reauth rules, and privacy/security constraints. The interface does not define authorization; backend security controls remain authoritative.

## Decision Model
Model the lifecycle: discover/sign in, credential selection, authentication, optional challenge, session state, reauthentication for sensitive action, sign out, lost/new device, and account recovery. Keep account identity stable through the flow so users do not authenticate successfully into the wrong profile.

For passkeys, explain them in outcome terms rather than cryptography. Show where the passkey is available when platform UX allows, distinguish passkey from account, and provide another supported path when the expected device/provider is unavailable. Encourage passkey creation at a moment where the user can connect it to successful account access, not as an unexplained modal interruption.

Error messages balance recovery with enumeration resistance. Authentication responses should not expose more about whether an account, credential, or MFA factor exists than security policy permits. Yet generic errors still need actionable next steps: retry, use another method, recover account, or contact support.

Reauthentication is contextual. Make clear why verification is requested and preserve the intended sensitive action afterward. Do not use cognitive puzzles or memory tasks as a substitute for authentication where accessibility requirements prohibit that pattern.

## Evidence
Test existing/non-existing account behavior for information leakage, passkey creation/use on supported devices, cross-device fallback, lost device, disabled biometrics, MFA failure, session expiration, reauthentication return, screen-reader labels, password-manager/autofill behavior, and recovery abuse. Use FIDO/platform/security guidance where applicable.

## Output Contract
Return an `authentication-contract` with `account_identity_model`, `methods[]`, `passkey_lifecycle`, `method_selection`, `error_disclosure_policy`, `reauthentication_triggers[]`, `session_expiry`, `recovery_paths[]`, `cross_device_behavior`, `enumeration_resistance`, and `auth_tests[]`.

## Failure Traps
- Treating passkey and account as the same concept.
- “Use passkey” with no fallback when the credential is on another ecosystem/device.
- Different error wording that reveals account existence.
- MFA loop that discards the action the user was trying to confirm.
- Recovery weaker than normal authentication with no compensating control.
- Blocking password managers/paste in the name of security.
- UI sign-out implying server tokens/sessions were revoked when they were not.

Good authentication keeps security state precise while making recovery understandable.

## V6 Authentication Ceremony Protocol
Model a **ceremony-state model** across identifier discovery, device/account selection, authenticator invocation, user verification, server challenge, success/failure, and fallback. Track **account-device binding** so users understand which account and device/passkey they are using, especially with shared devices or multiple profiles.

Protect **recovery-channel integrity**: fallback must not negate the security of the primary path. Prefer a **phishing-resistant path** where supported and avoid UI that trains users to enter credentials into ambiguous contexts. Provide **credential-discovery fallback** for users who do not know where a passkey lives, changed devices, revoked credentials, or platform sync differences.

### Falsification
Use multiple accounts, no matching passkey, cancelled platform UI, offline/clock issues, and compromised weaker fallback. If the user can be tricked into a lower-assurance flow without clear context, the model fails.

### Recovery
Return to known account/device context, surface secure recovery options, and preserve intent without repeatedly firing opaque platform prompts.
