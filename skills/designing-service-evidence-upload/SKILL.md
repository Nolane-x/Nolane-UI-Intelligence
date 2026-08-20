---
name: designing-service-evidence-upload
description: Use when a public service requires documents, photographs, statements, or other evidence and users must understand what is acceptable, what was received, how it is protected, and what happens when evidence cannot be supplied digitally.
---

# Designing Service Evidence Upload

Evidence upload is not generic file attachment. The service is asking a person to prove a fact, and the interface must connect each requested item to that fact, acceptance criteria, privacy treatment, receipt state, and alternatives.

## Parent Contract
**Required parent:** `designing-public-service-experiences`.

The parent owns the public-service case. This skill owns evidence request semantics and digital submission of evidence into that case.

## Evidence Request
Name the fact being evidenced before listing file types. Explain accepted documents or alternatives, date/validity requirements, whether every page is needed, image quality expectations, and whether redaction is allowed. Avoid requesting “proof of address” with a file picker and no examples or validity window.

When multiple documents can satisfy the same requirement, model them as alternatives, not as independent mandatory uploads. When one document can satisfy multiple requirements, decide whether the service can reuse it transparently rather than asking for duplicate copies.

## Capture and Upload State
Separate local selection/capture, upload in progress, server receipt, validation/virus scanning, human review, accepted, rejected, and superseded states. A thumbnail after local selection is not proof of receipt. If background processing occurs, show the durable state attached to the application record.

For camera capture, support cropping and legibility checks without implying automated image quality means evidential acceptance. Preserve orientation and avoid destructive compression of small text.

## Privacy and Alternatives
Explain why sensitive evidence is requested and how it will be used according to policy. Do not expose filenames, thumbnails, or personal details on shared surfaces unnecessarily. Provide postal, in-person, assisted-digital, or later-submission routes where the service permits them.

## Evidence
Test multi-page documents, large files, unsupported format, corrupted file, password-protected file, mobile camera capture, slow upload, network loss, server rejection, duplicate evidence, and returning in a later session. Verify the case record shows the same evidence status the user sees.

## Failure Modes
- “Uploaded” means only selected locally.
- Generic file constraints explain format but not evidential requirement.
- Rejected evidence disappears without reason or replacement path.
- One requirement causes unnecessary duplicate upload of the same document.
- Sensitive thumbnail remains visible after logout/session handoff.
- Failure at virus scan is presented as user wrongdoing.
- No alternative exists for users unable to digitize evidence.

## Falsification
Select a file, interrupt the network after local preview, and return from a clean device. Falsify if the service claims evidence is present when the case has none. Submit a technically valid but policy-invalid document; falsify if technical acceptance is shown as evidential acceptance.

## Recovery
Restore the durable server receipt state, preserve rejected-item explanation, offer replacement or alternative evidence routes, and maintain requirement-to-document mapping. Where evidence review has not occurred, use pending/received language rather than accepted.

## Handoff
Application sequencing belongs to `designing-government-application-journeys`; assisted capture may route through `designing-assisted-digital-handoffs`; post-submission evidence status appears in `designing-public-service-status-tracking`.

## Output Contract
Return a `service-evidence-upload-contract` with `evidence_requirements[]`, `acceptable_alternatives`, `document_reuse_rules`, `upload_processing_states[]`, `privacy_treatment`, `capture_rules`, `alternative_channels[]`, `server_receipt_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.