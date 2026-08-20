---
name: designing-document-signing-workflows
description: Use when a file passes through signature preparation, signer assignment, consent, signing, decline, expiry, completion, and evidence retrieval and the UI must preserve document/version and signer intent.
---

# Designing Document Signing Workflows

## Parent Contract
**Required parent:** `designing-file-transfer-and-storage`.

This faculty owns the interaction lifecycle around signing a fixed document version. It does not claim legal validity by itself; jurisdictional/legal authority must define what signature method and evidence are acceptable. The UI binds signers, document version, fields, and consent to that authority.

## Decision Boundary
Freeze or otherwise identify the exact document version sent for signature. Preparing fields is distinct from signing. Assign each required field to the intended signer and preview the signer experience before dispatch. The signer must know what document they are signing, what action constitutes signature, and whether they can decline, delegate, or correct information. Multi-signer order may be sequential or parallel and should be visible where it affects completion.

After any material document modification, invalidate/restart signatures according to authority rather than leaving old signatures attached to changed content. Completion should provide durable evidence/audit artifact and a stable final copy. Expired links, identity verification, accessibility, and mobile signing need explicit recovery.

## Failure Topology
- Document changes after first signer, but existing signature remains represented as valid.
- Signature field is assigned to the wrong signer and cannot be corrected without hidden admin tools.
- Clicking a styled “Sign” button is treated as consent without adequate document context.
- Sequential workflow gives later signers no indication why they are still waiting.
- Expired signing link shows generic 404 with no resend/recovery path.
- Completed file and audit evidence are not bound to the same immutable document version.

## Falsification and Recovery
Test preparation, multiple signers/order, decline, expired link, identity challenge, field validation, document revision, partial completion, mobile/accessibility, and final evidence download. The design fails if signature intent cannot be tied to a specific immutable document/evidence chain.

Recover by version-binding signing packets, validating field ownership, making consent/decline explicit, invalidating on material revision, and preserving final signed artifact plus evidence. Keep legal assurance claims bounded to configured provider/jurisdictional authority.

## Output Contract
Return `document-signing-contract` with document-version binding, signer/field assignment, consent/sign action, signer order, decline/expiry/recovery, revision invalidation, final artifact/evidence, and signing verification scenarios.
