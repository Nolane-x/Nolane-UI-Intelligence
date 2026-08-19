---
name: designing-accessible-verification-challenges
description: Use when anti-abuse, bot detection, step-up verification, or human checks risk excluding users because the challenge depends on a single sensory, cognitive, or motor ability.
---

# Designing Accessible Verification Challenges

## Parent Contract
**Required parent:** `designing-authentication-and-passkeys`.

This faculty owns the user-facing accessibility boundary of verification challenges used to distinguish legitimate users or increase assurance. It does not decide fraud policy or cryptographic assurance. It ensures a required challenge does not make account access contingent on identifying distorted images, hearing audio, solving memory puzzles, or completing precise motor tasks with no equivalent path.

## Decision Boundary
Begin with the assurance goal and list challenge modalities capable of meeting it. Prefer risk signals or platform authentication that reduce interactive challenge burden. When a challenge remains necessary, provide materially equivalent alternatives that do not simply reproduce the same barrier in another format. An audio alternative to an image puzzle may still exclude deafblind users; a support escalation path may be required for edge cases.

Keep challenge instructions, timeout, retries, and failure reasons understandable without revealing security-sensitive detection logic. Preserve form/session state when switching challenge type. Do not trap users in escalating challenge loops after failed attempts. If third-party verification is embedded, the product remains responsible for the accessible end-to-end path and must define a fallback when the provider is unusable.

## Failure Topology
- Login requires identifying objects in images with no nonvisual equivalent.
- The “audio alternative” is noisy, time-limited, and impossible to replay.
- Verification expires while a screen-reader user is navigating instructions.
- Switching challenge method discards credentials or form progress.
- Repeated failure produces harder challenges without an accessible escalation route.
- A third-party iframe cannot be operated by keyboard and the host provides no alternative.

## Falsification and Recovery
Test verification using screen reader, keyboard-only input, high zoom, reduced dexterity, no audio, no vision, slow completion, provider failure, and repeated retries. The design fails if any required path assumes one sensory channel or if users can become permanently blocked without a proportionate recovery route.

Recover by reducing challenge use, adding independent modalities, extending timing where security permits, preserving session state, and routing inaccessible-provider cases to another assurance mechanism. Security review must confirm alternatives preserve the required assurance rather than accessibility silently lowering it.

## Output Contract
Return `accessible-verification-contract` with assurance goal, challenge modalities, accessible alternatives, timing/retry policy, state preservation, third-party fallback, escalation/recovery path, security handoff, and multi-ability verification cases.
