---
name: designing-qr-code-scanning
description: Use when QR codes can contain URLs, invitations, payments, credentials, Wi-Fi data, or product payloads and the interface must preview meaning, validate origin, and avoid executing untrusted content immediately on decode.
---

# Designing QR Code Scanning

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns QR-specific interpretation and safety after camera decode. Unlike generic barcode lookup, QR payloads can encode active actions or arbitrary data. Decode is evidence of content, not user consent to navigate, pay, join, authenticate, or install.

## Decision Boundary
Classify decoded payload before action: product-owned signed token, web URL, payment request, contact, Wi-Fi, plain text, or unsupported/custom scheme. Show a human-readable preview and origin/consequence for high-impact actions. Product-owned codes should be authenticated cryptographically or by backend validation where required; visual branding inside a QR image is not proof of origin.

Prevent repeated decoding while a result sheet is open. External URLs need hostname and scheme visibility plus safe-browser policy. Payment/login/invitation codes require current validity and anti-replay behavior from their domain authority. Manual upload-from-photo can be supported but must follow the same validation path.

## Failure Topology
- Camera automatically opens any decoded URL without showing destination.
- A fake QR with product logo is trusted as an authentic invite.
- Payment payload executes before user confirms amount/recipient.
- Continuous decode reopens the same result sheet after dismissal.
- Custom URL scheme can launch privileged app behavior with no validation.
- Expired one-time token produces generic scanner failure instead of domain-specific recovery.

## Falsification and Recovery
Test product tokens, benign/malicious URLs, custom schemes, payment/invite payloads, expired/replayed tokens, repeated frames, screenshot import, offline state, and permission denial. The design fails if decoding alone can cause consequential external navigation or transaction.

Recover by separating decode/classify/validate/confirm/execute, previewing destination/consequence, authenticating owned payloads, rate-limiting repeated scans, and routing expired/invalid data to the relevant domain recovery.

## Output Contract
Return `qr-scanning-contract` with payload classes, preview fields, authenticity/validation rules, confirmation gates, external URL handling, replay/expiry behavior, duplicate suppression, and adversarial QR verification cases.
