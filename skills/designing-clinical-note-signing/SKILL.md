---
name: designing-clinical-note-signing
description: Use when clinical documentation moves from draft to signed, co-signed, amended, or addended states and the interface must preserve authorship, patient and encounter binding, attestation meaning, and revision history.
---

# Designing Clinical Note Signing

Signing a clinical note is an attestation event. It converts editable draft content into a governed clinical record state and must make authorship, context, completeness, and later amendment behavior explicit.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent supplies patient, encounter, and care context. This skill owns draft/final documentation state, signature meaning, co-signature, amendment, and revision evidence.

## Draft Boundary
Bind every draft to patient, encounter or episode as applicable, author, note type, creation time, and current revision. Autosave should preserve content without implying attestation. A “Saved” indicator must never look equivalent to “Signed.” If the context changes, keep the draft bound to its original clinical target unless a governed move/copy operation exists.

Templates and imported data need provenance. Distinguish clinician-authored text, copied-forward material, structured data insertion, and system-generated content when policy requires. Do not silently refresh imported values immediately before signature if that would change what the clinician reviewed.

## Signing Review
Before signing, expose unresolved required fields, conflicting data, unsigned orders if the workflow couples them, and any materially changed content since the clinician's last review. Signing should bind to a specific revision hash or version so concurrent edits cannot slip under an already-reviewed attestation.

Co-signatures and attestations have role-specific meaning. Avoid one generic “approve” button for author signature, supervisor co-signature, witness, or addendum acknowledgment. Each action needs actor, timestamp, authority, and resulting state.

## Amendment and Addendum
After signature, corrections should create amended versions or addenda according to policy, preserving the original. Show what changed and whether the amendment supersedes specific content. Never reopen a signed record into an ordinary mutable draft if audit integrity requires immutability.

## Evidence
Test autosave failure, context switch, simultaneous editor, sign after another revision arrives, required-field block, co-signature, addendum, entered-in-error/correction if supported, and offline/degraded connectivity. Verify server revision and visible signed content are identical.

## Failure Modes
- “Saved” and “signed” use indistinguishable status treatment.
- Copy-forward content loses its provenance.
- Background data refresh changes the note after review but before signature.
- Concurrent edit lands inside the signed revision unnoticed.
- Co-sign and author-sign are represented as the same action.
- Amendment replaces the original signed text.
- Failed signature leaves the UI claiming final state.

## Falsification
Have two users edit the same draft, let one review revision A, then change content to revision B before signature. Falsify if revision B can be signed without re-review or if the audit trail cannot show which content was attested.

## Recovery
Keep the signed claim tied to confirmed server revision, preserve unsent drafts on failure, surface conflicts, and require explicit re-review after material change. Use addendum/amendment pathways instead of mutating finalized content.

## Handoff
Patient/encounter binding coordinates with identity/context owners; problems and medications referenced in notes remain governed by their domain owners; handoff summaries use finalized evidence but must not convert note signature into workflow resolution.

## Output Contract
Return a `clinical-note-signing-contract` with `draft_identity`, `content_provenance`, `review_requirements[]`, `signature_types[]`, `revision_binding`, `co_sign_rules`, `amendment_model`, `failure_recovery`, `audit_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.