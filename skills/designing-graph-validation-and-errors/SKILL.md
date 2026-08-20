---
name: designing-graph-validation-and-errors
description: Use when this specialist's decision ownership is materially in scope. Own presentation, localization, prioritization, suppression, and repair of structural graph-rule findings without turning normal editing into an error storm.
---
# Designing Graph Validation and Errors

## Parent Contract

**Required parent:** `designing-diagramming-and-node-graph-editors`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own how graph-structure rules become actionable UI findings. Decide validation timing, severity, node/port/edge/container localization, issue-panel organization, canvas markers, explanations, quick fixes, suppressions, publish/execute gates, and treatment of incomplete intermediate edits. This owner does not invent domain rules; it makes their results understandable and repairable.

## Inputs and evidence

Require the validator's rule catalog, severities, affected object IDs, whether findings are blocking or advisory, rule evaluation cost, expected finding volume, incomplete-edit states, permission to auto-fix, and lifecycle gates such as save, publish, deploy, or execute. Identify rules that span multiple objects so the UI does not misleadingly pin them to one node.

## Procedure

Separate transient edit incompleteness from committed invalid structure. Lightweight inline cues can appear early, but blocking language should wait until the user reaches a relevant commit boundary unless safety demands immediate interruption. Every finding needs a stable identity, affected objects, plain explanation, evidence/context, and next action. Canvas markers should aggregate at low zoom and remain discoverable through an issue list. Selecting a finding must reveal every relevant object, including collapsed/virtualized regions. Quick fixes need preview and undo; suppression needs scope, rationale, and visibility to collaborators.

## Failure topology

Failures include red markers everywhere while the user is mid-connection, findings that say only "invalid graph", issue lists that cannot navigate to hidden objects, fixes that mutate unrelated structure, duplicate findings for the same root cause, suppressed warnings becoming invisible institutional debt, and blocking validators that run so slowly users cannot tell whether the graph is valid.

## Falsification

Reject if an issue cannot identify the affected semantic objects; if selecting it fails to reveal a collapsed/virtualized target; if quick-fix effects cannot be previewed or undone; if incomplete connection gestures immediately trigger persistent blocking errors; if a suppressed blocking rule can reach publish/execute unnoticed; or if validation freshness is unknown after edits.

## Output contract

Return a `graph-validation-and-errors-contract` with: validation trigger matrix; severity model; finding identity; object localization; canvas/list representations; aggregation at scale; reveal behavior; explanation/evidence fields; quick-fix protocol; suppression governance; freshness state; and lifecycle gates. Include one multi-object finding and one transient-incomplete edit case.

## Handoffs

Domain owners provide rule semantics. Graph search/navigation reveals findings, containers/virtualization expose hidden targets, and graph history records structural fixes. Global empty/error-state design does not replace this fine-grained structural validation contract.