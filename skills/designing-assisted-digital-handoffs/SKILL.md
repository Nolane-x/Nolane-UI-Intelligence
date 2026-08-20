---
name: designing-assisted-digital-handoffs
description: Use when a person receives help from staff, advisers, carers, interpreters, or support channels while using a public service and the interface must preserve consent, role, privacy, continuity, and responsibility across the handoff.
---

# Designing Assisted Digital Handoffs

Assisted digital support should help a person use a service without collapsing the distinction between applicant and helper. The interface must preserve whose application it is, what the helper is authorized to do, and what information can be seen or changed.

## Parent Contract
**Required parent:** `designing-public-service-experiences`.

The parent owns the service journey. This skill owns transitions between self-service and supported completion, including role/consent boundaries and continuity of the application state.

## Assistance Roles
Define helper roles rather than using one generic “agent.” A contact-center worker entering information with the applicant present, an authorized representative acting independently, an interpreter, a carer, and a technical support adviser have different authority. The UI should reflect these differences in permitted actions and audit records.

Do not require support staff to impersonate the applicant or share credentials. Establish a separate authenticated staff/helper context and bind actions to both helper identity and applicant/case identity where policy requires.

## Consent and Visibility
Record whether the applicant consents to the assistance and its scope. Sensitive sections may require re-confirmation or applicant-only entry. Explain to both parties when the helper can see data, upload evidence, submit, or only guide navigation.

Remote support needs screen-sharing or co-browsing boundaries if used. Avoid exposing unrelated browser content, other applications, or hidden case data merely to solve a navigation issue. If control is delegated, provide obvious start/stop state and revocation.

## Handoff Continuity
A person may start online, call for help, continue with staff, and later resume independently. Preserve the same draft/case state, show which answers were entered or changed during assisted support when useful, and ensure responsibility for final declaration/submission remains explicit.

## Evidence
Test adviser-assisted start, mid-application escalation, interpreter role, representative authority, applicant revoking consent, helper disconnection, return to self-service, and staff action on the wrong case. Verify audit identity for each change and ensure no credential sharing is required.

## Failure Modes
- Staff log in as the applicant.
- Helper role grants broad case access unrelated to the task.
- Consent is assumed from the fact a support call exists.
- Applicant cannot see what changed during assisted completion.
- Co-browsing exposes unrelated sensitive data.
- Final declaration is submitted by a helper whose role cannot attest it.
- Handoff creates a duplicate draft instead of continuing the same case.

## Falsification
Start a self-service application, transfer to an adviser with limited authority, make changes, revoke assistance, and resume independently. Falsify if the audit trail attributes helper changes to the applicant, if consent scope is unenforceable, or if the application forks.

## Recovery
Separate helper authentication, restore explicit consent scope, rebind to the canonical case, and require applicant review for actions outside helper authority. If identity/authority cannot be verified, downgrade the session to guidance-only rather than granting case control.

## Handoff
Draft continuity uses `designing-save-and-return-service-flows`; identity proof uses `designing-identity-proofing-service-flows`; evidence capture may use `designing-service-evidence-upload`.

## Output Contract
Return an `assisted-digital-handoffs-contract` with `assistance_roles[]`, `authority_matrix`, `consent_scope`, `helper_authentication`, `visibility_rules`, `co_browsing_boundary`, `handoff_continuity`, `audit_identity`, `evidence_cases[]`, and `recovery_actions[]`.