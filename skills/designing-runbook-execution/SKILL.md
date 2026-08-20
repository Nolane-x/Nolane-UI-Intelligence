---
name: designing-runbook-execution
description: Use when this specialist's decision ownership is materially in scope. Own guided execution of operational runbooks, including prerequisites, step state, evidence, branching, automation boundaries, side-effect warnings, and deviation capture.
---
# Designing Runbook Execution

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the responder experience for following a known operational procedure during an incident or maintenance event. Decide runbook version, prerequisites, step sequencing, optional/conditional branches, completion evidence, automated versus manual actions, pause/abort, deviation notes, and handoff. This skill does not author remediation commands; it controls how a procedure is understood and safely executed.

## Inputs and evidence

Require runbook structure/version, step prerequisites, commands/actions, expected observations, branching conditions, permissions, automation capabilities, rollback/abort points, side-effect severity, and audit requirements. Identify steps that are advisory versus mandatory and those requiring independent approval.

## Procedure

Show the selected runbook version and applicability context before execution. Each step needs objective, action, expected result, and evidence field; checkboxes alone are insufficient for high-consequence work. Automated actions must display target and consequences before launch and record machine result separately from human verification. Conditional branches should state why a path is chosen. Allow pause, skip-with-rationale where policy permits, and abort/rollback at defined safe points. If responders deviate, capture the deviation and preserve runbook progress without forcing the real incident to match the document.

## Failure topology

Failures include executing an outdated runbook, blind checkbox completion, copy/paste commands with unclear target, automation shown as successful before outcome verification, skipping steps without provenance, and runbook state lost during shift handoff. Another failure is a rigid flow that blocks responders when the incident no longer matches assumptions.

## Falsification

Reject if runbook version/applicability is unknown; if a side-effecting automated step can execute without target/consequence review; if a completed step has no expected-result verification where required; if deviations cannot be recorded; if pausing/reloading loses state; or if a conditional branch hides the evidence that selected it.

## Output contract

Return a `runbook-execution-contract` containing: version/applicability; prerequisites; step schema; manual/automated distinction; expected-result evidence; branch conditions; skip/deviation policy; pause/abort/rollback; side-effect confirmation; audit trail; and handoff persistence. Include one failed expected-result branch.

## Handoffs

Mitigation tracking owns incident-level action progress, high-stakes controls govern irreversible operations, maintenance windows may host planned runbook execution, and postmortem can consume deviations as improvement evidence.