---
name: designing-mitigation-action-tracking
description: Use when this specialist's decision ownership is materially in scope. Own incident mitigation actions from proposal through authorization, execution, verification, rollback, and outcome attribution, including concurrent or conflicting actions.
---
# Designing Mitigation Action Tracking

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the lifecycle of actions intended to reduce incident impact. Decide proposal, owner, target, expected effect, risk, authorization, start, completion, verification, failure, rollback, and interaction among concurrent mitigations. Generic tasks do not capture the operational consequence and verification needed here.

## Inputs and evidence

Require mitigation types, targets, action authority, reversibility, expected signals, rollback procedures, dependencies/conflicts, automation hooks, and observation windows. Identify actions that change production state or customer behavior and therefore require stronger confirmation.

## Procedure

Represent each mitigation with hypothesis/rationale, target, owner, expected observable effect, risk, rollback, and verification metric before execution where feasible. Separate "executed" from "worked": completion of a command is not proof of impact reduction. Track concurrent mitigations and warn when two target the same resource or produce confounded evidence. Verification should include a defined observation window. Failed or harmful actions need rollback state and resulting evidence. Preserve discarded proposals with concise rationale when they influenced decisions.

## Failure topology

Failures include actions marked done on command success, no owner, duplicate responders applying conflicting mitigations, rollback undocumented, evidence attribution impossible because several changes happen simultaneously, and action state hidden in chat. Another failure is requiring lengthy documentation before an emergency action when policy permits urgent execution; the UI must support immediate capture followed by evidence completion.

## Falsification

Reject if an executed mitigation can be shown as successful before outcome verification; if two conflicting actions can proceed with no warning; if rollback availability is unknown; if the target is ambiguous; if completed actions cannot link to resulting health evidence; or if urgent execution cannot be recorded immediately with later completion of rationale/evidence.

## Output contract

Return a `mitigation-action-tracking-contract` with: proposal schema; owner/target; expected effect; risk/reversibility; authorization; execution state; verification metric/window; success/failure distinction; concurrency/conflict cues; rollback; evidence linkage; and emergency-capture path. Include one successful command with failed outcome scenario.

## Handoffs

Runbook execution may generate mitigations, command controls approve high-consequence actions, service health provides verification evidence, and incident timeline records state transitions.