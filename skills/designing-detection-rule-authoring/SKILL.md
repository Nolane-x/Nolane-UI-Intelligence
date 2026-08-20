---
name: designing-detection-rule-authoring
description: Use when security practitioners create or modify behavioral, query, signature, threshold, or correlation detections and need explicit scope, data dependencies, tuning, and expected evidence.
---
# Designing Detection Rule Authoring

## Decision ownership

Own the authoring experience for detection logic as an operational artifact. Decide how users express conditions, choose data sources, bind fields, specify time windows, thresholds, exceptions, severity, metadata, and downstream actions while understanding what evidence the rule can and cannot see. This faculty does not choose the organization's threat model and does not validate production effectiveness; testing is delegated to the dedicated rule-testing owner.

## Inputs and evidence

Require the detection language or builder grammar, supported data schemas, field types, event-time semantics, correlation capabilities, historical data availability, detector execution cadence, cardinality/cost limits, exception model, severity taxonomy, ownership metadata, deployment lifecycle, and representative existing rules including noisy and brittle ones. Capture schema drift cases, missing fields, sparse sources, high-cardinality dimensions, and conditions that are syntactically valid but operationally meaningless.

## Procedure

Start from detection intent: behavior to identify, evidence prerequisites, expected false-positive classes, and response significance. Keep that intent visible beside implementation. Provide schema-aware editing so fields expose type, source, freshness, and availability rather than appearing as arbitrary strings. Treat time-window and aggregation semantics as first-class controls; “five failures in ten minutes per user” is not equivalent to a global count. Make exclusions inspectable and scoped so broad suppressions cannot masquerade as harmless tuning. Separate authoring, save, test, stage, enable, and production promotion. Require ownership and rationale for high-impact rules, and surface cost or data-coverage warnings before activation.

## Failure topology

- A rule compiles but references a field absent from most production telemetry.
- Exceptions accumulate as opaque clauses and suppress unrelated attacks.
- Thresholds are entered without clarifying grouping key or time semantics.
- The builder hides operator precedence and users author a different condition than intended.
- Severity is copied from a template rather than derived from consequence.
- Save and enable are one action, making draft iteration operationally dangerous.
- Schema changes silently turn a formerly useful condition into a no-op.

## Falsification

Ask an author to express a multi-event rule with a grouping key, a narrow exception, a source-coverage caveat, and a deployment stage. Then remove a required field from one source and change operator precedence in a compound expression. Fail the design if the author cannot see the resulting semantic change before activation or if a draft can become live without a distinct operational transition.

## Output contract

Return `detection-rule-authoring-contract` containing intent metadata, rule grammar representation, schema/type assistance, aggregation/time semantics, exception model, severity rationale, draft-to-production lifecycle, cost/coverage warnings, ownership requirements, and authoring verification cases.

## Handoffs

Route simulation and regression evaluation to `designing-detection-rule-testing`; correlation concepts to `designing-security-event-correlation`; alerts emitted in production to `designing-security-alert-triage`; change approval can reuse high-stakes workflow faculties without replacing detection-specific authoring truth.