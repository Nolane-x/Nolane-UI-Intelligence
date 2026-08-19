---
name: designing-recovery-code-management
description: Use when an account issues one-time recovery codes and the interface must coordinate generation, one-time display, storage acknowledgement, remaining-code status, regeneration, revocation, and use consequences without treating codes like ordinary passwords.
---

# Designing Recovery Code Management

## Parent Contract
**Required parent:** `designing-authentication-and-passkeys`.

This faculty owns the lifecycle of backup recovery codes after a stronger authentication method is configured. It does not own the whole account recovery flow. Recovery codes are scarce bearer secrets: possession can restore access, each code may be single-use, and regenerating a set can invalidate every previously stored copy.

## Decision Architecture
Separate code-set metadata from plaintext values. The settings surface can show whether recovery codes exist, when the set was generated, how many unused codes remain if the backend tracks that safely, and whether regeneration is available. Plaintext codes should normally appear only at generation/regeneration according to the authentication architecture; routine settings views should not reveal the existing set.

Provide safe storage options without pretending one medium is universally secure. Copy, download, print, or password-manager-compatible workflows may be offered according to product policy. Warn users not to store the only recovery method exclusively behind the account it is meant to recover. Avoid forcing a screenshot or blocking password managers. If the product requires acknowledgement, make it an acknowledgement of storage responsibility, not fake proof that a code is actually safe.

Regeneration is a destructive security transition because old unused codes generally become invalid. Explain that before commit and require current authentication/re-authentication when policy demands it. After a recovery code is used, do not reveal which plaintext code remains; update remaining count or security posture and encourage regeneration when the reserve is low.

## Failure Topology
- Settings page permanently displays every recovery code in plaintext to anyone with an unlocked session.
- Regenerate button instantly invalidates the old set with no warning or reauthentication.
- Downloaded file has an obvious filename and persists in a shared Downloads folder with no caution.
- UI says “8 codes remaining” based on stale cache after one was consumed on another device.
- A used code remains visibly marked as valid because usage state never refreshes.
- Product forces users to store codes in the same cloud account they may need the codes to recover.

## Falsification and Recovery
Falsify with initial generation, dismissal before saving, regeneration, use of one code on another device, stale remaining count, reauthentication failure, copy/download/print pathways, screen-reader secret reading, and a low-code warning. The design fails if plaintext is recoverable outside the intended generation boundary or if users can invalidate their only backup set without understanding the consequence.

Recover by one-time secret display, metadata-only routine management, explicit regeneration consequence, current-auth verification, freshness-aware remaining status, safe storage options, and a path to generate a new set when backup capacity becomes insufficient.

## Output Contract
Return `recovery-code-management-contract` with code-set metadata, plaintext-display boundary, storage/export options, acknowledgement, remaining-code freshness, regeneration/revocation semantics, reauthentication requirements, post-use updates, low-reserve guidance, accessibility/secret handling, and falsification cases.