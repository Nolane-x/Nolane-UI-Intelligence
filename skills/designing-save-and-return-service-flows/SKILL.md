---
name: designing-save-and-return-service-flows
description: Use when a public-service application must survive long interruptions and users need a secure, understandable way to resume the correct draft without duplicate cases, lost evidence, or unexpected expiry.
---

# Designing Save and Return Service Flows

Save-and-return is continuity infrastructure for services that cannot reasonably be completed in one sitting. It must balance durable recovery, identity assurance, privacy, expiry policy, and clarity about what has actually been saved.

## Parent Contract
**Required parent:** `designing-public-service-experiences`.

The parent owns the service journey. This skill owns draft identity, save confirmation, return authentication, expiry, multi-session behavior, and recovery of partially completed public-service work.

## Draft Identity
Create a stable draft/application reference before users depend on save-and-return. Decide whether drafts are account-bound, magic-link/recovery-code based, identity-proofed, or associated by another governed mechanism. Avoid generating multiple hidden draft identities as users revisit the service from different entry points.

Clearly separate local transient state from server-saved state. Autosave may reduce effort, but provide a durable indicator only when the server confirms persistence. If some fields or evidence are not yet saved, name the boundary.

## Returning
On return, restore the same application version, relevant section progress, evidence receipt state, and outstanding requirements. If policy or form structure changed during absence, migrate the draft explicitly and tell the user which answers need review. Do not silently discard fields that no longer map.

Authentication for return should be proportionate to the sensitivity of the saved application. Do not let convenience links become durable bearer access to sensitive case data beyond policy. Conversely, do not force users to repeat full identity proof simply to resume if the service's assurance model does not require it.

## Expiry and Abandonment
State expiry before it surprises users and, where possible, warn before deletion. Distinguish inactive draft, expired draft, submitted application, and withdrawn case. An expired draft should not look like a technical error. Provide restart or recovery routes governed by service policy.

## Evidence
Test closing the browser mid-section, save failure, return from another device, forgotten recovery credential, expired link, policy/schema update during inactivity, concurrent sessions, evidence uploaded before exit, and accidental second application start. Verify draft identifiers and server records.

## Failure Modes
- “Saved” appears before server persistence.
- Return flow creates a new application instead of restoring the existing draft.
- Draft migration silently deletes answers after policy change.
- Recovery link grants more access or longer access than intended.
- Users learn about expiry only after data is gone.
- Submitted applications still appear editable as drafts.
- Two devices overwrite one another without revision awareness.

## Falsification
Save a partially completed application with evidence, change the service schema, then resume on a second device while the first session remains open. Falsify if the resumed state loses evidence, creates a duplicate case, or permits stale-session overwrite without conflict handling.

## Recovery
Rebind to authoritative draft identity, compare revisions, migrate fields with explicit review, and preserve recoverable data where policy permits. If a draft is genuinely expired, state that outcome and provide the next valid service route rather than presenting an ambiguous error.

## Handoff
Identity assurance belongs to `designing-identity-proofing-service-flows`; evidence durability to `designing-service-evidence-upload`; section progression to `designing-government-application-journeys`.

## Output Contract
Return a `save-and-return-service-flows-contract` with `draft_identity_model`, `save_confirmation`, `return_assurance`, `revision_concurrency`, `schema_migration`, `expiry_policy`, `submitted_vs_draft_boundary`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.