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

## V9 Account Continuity Boundary
Authentication is only one segment of the **account/workspace lifecycle**. When the product is account-based, this faculty must bind its ceremony contract to the broader lifecycle owned by product/capability architecture: registration or invitation, account establishment, authenticated sessions, profile/account identity, workspace or organization membership where applicable, workspace switching, session/device continuity, credential/security management, recovery, sign-out/revocation, ownership or membership transition, deactivation and deletion. Do not claim the whole account experience is complete because login succeeds.

Keep the boundary precise. This faculty still owns authentication assurance, credential choice, reauthentication, enumeration resistance and secure recovery ceremonies. It does not invent organization policy, role authorization, billing or workspace product strategy. Instead, expose the identity/session facts those systems require: current account, current workspace/tenant context, current assurance level, active/revoked sessions, trusted or enrolled authenticators, and whether a sensitive action requires fresh authentication.

Model **session/device continuity** as visible product truth. Users may sign in on multiple devices, lose one, revoke a session, change credentials, create a passkey elsewhere, switch accounts or return after expiry. The UI must distinguish “signed out on this device” from “all server sessions revoked,” and must not imply that deleting a local credential deletes the account or workspace. Sensitive settings should preserve the user's intended destination through reauthentication when safe.

For multi-workspace products, prevent identity-context ambiguity. Switching workspace is not authentication, but authentication must not silently return a person to the wrong workspace when the intended action or deep link belongs elsewhere. A revoked membership, deleted workspace, transferred ownership or expired invitation needs an explicit recovery/next-step state instead of an auth loop.

### V9 Falsification
Start with a working sign-in screen and test lost device, session expiry during a sensitive setting, membership revoked while signed in, account deletion initiation, reauthentication return, and sign-out-all-devices. If the product cannot explain which account/workspace/session survives each transition, the account continuity model is incomplete.

### V9 Recovery
Return to canonical identity + session + workspace context, re-establish the minimum secure authentication ceremony required, then hand control back to the owning lifecycle surface with the user's safe intent preserved. Do not solve lifecycle ambiguity by repeatedly asking for credentials.

## V10 Account-Lifecycle Empirical Boundary
`H-ACCOUNT-CONTINUITY` tests a recurring AI failure: **a polished sign-in/sign-up flow is mistaken for a complete account system.** This owner should change behavior only when durable identity exists. It should surface lifecycle consequences around sessions/devices, secure recovery, membership/workspace context, revocation and terminal account states without inventing organizations for an anonymous or personal-only product.

The targeted mutation `account-login-only` deliberately stops at authentication ceremony. The `account-continuity` ablation removes the bridge into the wider account/workspace lifecycle. Benchmark judgment therefore focuses on **dead-end and wrong-context transitions**, not on whether the login screen contains more controls. Relevant probes include lost devices, session expiry during a sensitive action, invitation versus active membership, workspace switching, membership revocation, owner departure, account deletion with shared resources, and safe return after reauthentication.

### V10 evidence partition
Keep three evidence layers separate:
- **security ceremony evidence** — credential/factor, enumeration resistance, reauthentication and recovery assurance owned here;
- **product lifecycle evidence** — membership/ownership/account states supplied by product/capability architecture;
- **efficacy evidence** — matched baseline/full/ablation runs showing that this skill reduces lifecycle dead ends.

A good authentication artifact is not efficacy evidence. Likewise, a benchmark result may show better account-lifecycle completeness without proving the backend security design is correct. Security claims remain subject to their own authority and runtime evidence.

### V10 falsification
The hypothesis fails attribution if `account-login-only` performs equivalently on tasks that genuinely contain multi-device, recovery, membership or terminal-state consequences. It also fails by overreach if full NUI adds team/workspace machinery to `account-01` or an anonymous product. For `EMPIRICAL_TRANSFER`, require holdout account tasks and multiple model families; same-model architectural examples support only `STRUCTURAL_ONLY` until real comparative evidence exists.
