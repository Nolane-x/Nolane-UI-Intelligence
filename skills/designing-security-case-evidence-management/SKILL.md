---
name: designing-security-case-evidence-management
description: Use when a security investigation becomes a durable case and analysts must preserve evidence lineage, hypotheses, decisions, actions, scope, custody, and reviewability across people and time.
---
# Designing Security Case Evidence Management

## Decision ownership

Own the durable evidence and reasoning model for security cases. Decide how raw observations, derived findings, analyst notes, hypotheses, decisions, response actions, attachments, external references, and case scope are stored and linked so another reviewer can reconstruct what was known at each point. This faculty does not own generic case assignment or incident command. It protects evidentiary continuity and prevents later edits from rewriting the investigation's historical basis.

## Inputs and evidence

Require case identifiers and lifecycle, actor/role model, evidence source types, immutable event references, attachment handling, retention and access rules, chain-of-custody requirements where applicable, note/edit history, investigation hypotheses, related entities, response actions, external ticket or incident links, classification labels, export needs, and handoff patterns. Include deleted upstream telemetry, corrected enrichments, reclassified findings, redacted material, duplicate evidence, late evidence, and cases spanning multiple data sources or organizational boundaries.

## Procedure

Separate source evidence from interpretation. A case should reference immutable or versioned source artifacts whenever possible, then layer analyst annotations and derived conclusions on top. Preserve the timestamp and author of every material reasoning step. Allow hypotheses to remain open, contradicted, superseded, or supported rather than forcing one narrative too early. Pin exact time windows, queries, entity identifiers, and analysis-run IDs when evidence is imported from exploratory tools. Track response actions as evidence-bearing events with scope and outcome, not merely checklist completion. For redaction or access restriction, preserve the existence and provenance of withheld material so downstream reviewers know the record is intentionally incomplete. Make exports self-describing with source references and integrity metadata appropriate to the organization.

## Failure topology

- Copying a screenshot into a case loses the query, time range, and source event identities behind it.
- Analyst notes can be edited in place with no history, silently changing the rationale for prior actions.
- Enrichment updates overwrite the value that was actually visible when a decision was made.
- Hypotheses are stored as findings and later readers cannot distinguish speculation from evidence.
- Deleted upstream events leave unexplained gaps in the case.
- Redaction removes all trace that evidence existed.
- Case closure freezes assignment status but not the evidentiary state needed for audit or later reopening.

## Falsification

Create a case from alert, timeline, entity, malware, and network evidence; later update one enrichment, remove one upstream event, redact one attachment, contradict an early hypothesis, and reopen the case after handoff. The design fails if a reviewer cannot reconstruct the original decision basis, tell source facts from analyst interpretation, or identify why a referenced artifact changed or disappeared.

## Output contract

Return `security-case-evidence-management-contract` containing evidence classes, immutable-reference strategy, provenance fields, hypothesis lifecycle, note/version history, action evidence, redaction semantics, upstream-deletion handling, access boundaries, export integrity, reopening behavior, and case-reconstruction tests.

## Handoffs

Operational assignment and escalation may reuse generic case/workflow faculties; investigation surfaces feed this contract through stable evidence references. Shift transitions route to `designing-security-operations-handoffs`; post-incident governance may reuse audit-log and incident faculties. This skill remains authority for durable security evidence and reasoning lineage.