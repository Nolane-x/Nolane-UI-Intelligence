---
name: designing-high-stakes-decisions
description: Use when an action can cause material financial, medical, safety, privacy, security, legal, deletion, publication, permission, or other difficult-to-reverse consequences.
---

# Designing High-Stakes Decisions

## Overview
High stakes require consequence clarity and error resistance, not indiscriminate friction. Design the decision so the person can identify the object, action, consequence, alternatives, and recovery boundary before commitment.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require risk class, consequence severity, reversibility, frequency, authorization model, and relevant standard/regulator constraints. If risk is unknown, do not default to either instant action or modal confirmation.

## Decision Model
Classify the action along four axes: consequence magnitude, reversibility, detectability of error, and action frequency. Use that to choose controls. Low-consequence reversible actions favor direct action plus undo. High-consequence or irreversible actions need stronger pre-action verification. Repeated operational actions require friction designed to resist habituation rather than a generic “Are you sure?” every time.

Build a decision preview that answers: **what** object/account/person is affected; **what action** will occur; **what consequence** follows including amount, audience, dose, permission, or deletion scope; **when** it takes effect; **whether/how** it can be reversed; and **who** has authority. Use differentiated confirmation when a plausible confusion pair exists: recipient, environment, production versus test, similarly named patient, file version, or account.

Avoid memory tests as security or safety. Re-entering arbitrary values can increase transcription error; when verification is needed, show the critical value and ask the person to confirm the meaningful relationship. For batch actions, expose aggregate scope and exceptions. After commit, provide durable receipt/state and recovery/dispute path when possible.

## Evidence
Evidence includes critical-task analysis, error scenarios, domain requirements, authorization tests, realistic usability sessions, and incident patterns. Confirm dialogs alone are not evidence of safety. For regulated domains, formal validation remains external where required.

## Output Contract
Return a `high-stakes-decision-contract` with `action`, `risk_class`, `consequence`, `reversibility`, `confusion_pairs[]`, `precommit_information[]`, `confirmation_strategy`, `authorization_checks[]`, `postcommit_feedback`, `recovery_or_dispute`, `evidence_required[]`, and `residual_risk`.

## Failure Traps
- Generic confirmation text detached from the actual object or consequence.
- Red styling as the only risk communication.
- Confirmation on every routine action until users click reflexively.
- Hiding fees, audience, recipient, dose, or scope until after commit.
- Using undo for an action that is not reliably reversible.
- Asking users to remember/retype information unnecessarily.
- Assuming the person who can see the button is authorized to execute it.

The best high-stakes UI makes the safe action obvious and the dangerous misunderstanding difficult, rather than merely making every action slower.