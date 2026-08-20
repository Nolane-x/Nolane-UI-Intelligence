---
name: designing-public-service-experiences
description: Use when a public service must help people establish eligibility, provide evidence, save and return, receive assisted support, track outcomes, prove identity, understand entitlement, and report changes across a governed service journey.
---

# Designing Public Service Experiences

A public service interface is the visible edge of policy, operational capacity, and a person's rights or obligations. It must translate institutional rules into a journey that is understandable, recoverable, inclusive, and explicit about what the service can and cannot decide.

## Parent Contract
**Required parent:** `routing-ui-work`.

This owner routes a whole public-service journey. It does not replace generic forms, accessibility, identity, or content skills; it defines how those capabilities fit around policy eligibility, evidence, case progression, assisted support, and changes after submission.

## Service Contract
Start with the real service outcome, not the website structure. Identify who can use the service, what decision or transaction it produces, which evidence is legally or operationally required, what alternative channels exist, and what happens after submission. Separate eligibility rules from information-gathering questions so users understand when the service is assessing entitlement versus merely collecting details.

Map institutional boundaries that users would otherwise experience as unexplained dead ends: another agency owns the next step, a human caseworker must review evidence, a decision has statutory timing, or a digital route cannot support a particular circumstance. Explain those boundaries in user terms and provide the next viable route.

## Journey Continuity
Public services often span days or weeks. Preserve application identity, progress, submitted evidence, messages, decision state, and outstanding actions across sessions. Save-and-return is not a convenience add-on; for long or stressful services it can be part of accessibility and procedural fairness.

Treat digital assistance as a first-class route. A user may begin alone, continue with an adviser, submit through an assisted channel, and later return online. Preserve consent, identity, and audit boundaries when another person helps.

## Decision Transparency
When the service makes a decision, distinguish rule-based ineligibility, incomplete information, pending review, approved entitlement, refusal, and inability to determine. Provide reasons at the level policy permits and expose appeal/review or correction paths where they exist. Do not render institutional uncertainty as a generic error.

## Evidence
Test end-to-end journeys with eligible, ineligible, uncertain, low-digital-confidence, accessibility-needs, and interrupted users. Include missing evidence, failed identity proof, long inactivity, changed circumstances after submission, adviser-assisted completion, and a backend case status change. Evidence should connect the rendered service state to authoritative case/policy state.

## Failure Modes
- Policy questions are presented as arbitrary form fields with no decision context.
- A user reaches an ineligible dead end without knowing why or what alternative exists.
- Save-and-return loses evidence or creates duplicate applications.
- Assisted support requires staff to impersonate the applicant.
- “Submitted” is mistaken for “approved.”
- A service-status page hides outstanding user action.
- Generic failure copy masks a policy or operational decision state.

## Falsification
Run one journey that crosses digital, assisted, and return-to-service channels. Falsify if application identity, consent, or evidence state diverges between channels. Also falsify if an ineligible or refused user cannot distinguish a policy decision from a technical failure.

## Recovery
Restore a single authoritative service/case identity, expose the exact decision stage, recover saved evidence, and route users to the correct human or alternative service when the digital path cannot continue. Missing policy evidence stays UNKNOWN rather than being guessed by the interface.

## Handoff
Eligibility routes to `designing-service-eligibility-checkers`, application sequencing to `designing-government-application-journeys`, evidence to `designing-service-evidence-upload`, assisted support to `designing-assisted-digital-handoffs`, and post-submission state to status/change-reporting owners.

## Output Contract
Return a `public-service-experiences-contract` with `service_outcome`, `policy_boundaries[]`, `journey_states[]`, `channel_model`, `save_return_identity`, `decision_states[]`, `alternative_routes[]`, `assistance_boundaries`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.