---
name: designing-clash-and-collision-inspection
description: Own detection-review workflows for geometric clashes, clearances, interferences, contacts, and collision sets with scope, severity, evidence, deduplication, assignment, and resolution verification.
---
# Designing Clash and Collision Inspection

## Decision ownership

Own the interface for reviewing spatial conflicts between model entities. Decide check sets, clash type, tolerance/clearance, severity, pair identity, grouping/deduplication, focused viewpoint, assignment/status, ignore/exception rationale, and verification after model change. This owner does not implement collision algorithms.

## Inputs and evidence

Require geometry sets, transforms, collision results, penetration/clearance metrics, tolerance, component/assembly IDs, model revision, rule/check definition, issue workflow, and rerun capability. Identify repeated contacts that produce many near-duplicate clash pairs.

## Procedure

Bind each clash to exact entity pair, model revision, check rule, location, and measured penetration/clearance. Provide a focused 3D view that isolates both objects while retaining context. Group repeated/systematic clashes using transparent rules without hiding worst members. Distinguish new, active, reviewed, accepted/intentional, resolved, and stale-after-model-change. Ignoring requires reason/scope and remains visible. Rerun should verify resolved issues and flag changed identities rather than silently closing because old geometry IDs disappeared.

## Failure topology

Failures include thousands of duplicate clashes, accepted clashes disappearing entirely, clash coordinates no longer matching updated model, severity based on color alone, resolution declared because the check was not rerun, and entity names too ambiguous to identify occurrences. Another failure is clearance values shown with unknown unit/tolerance.

## Falsification

Reject if a clash cannot identify both exact occurrences; if tolerance/unit is absent; if accepted exceptions have no rationale; if model revision changes make an issue look resolved without rerun; if grouped clashes hide a more severe member; or if opening a clash cannot reproduce a meaningful viewpoint.

## Output contract

Return a `clash-and-collision-inspection-contract` with: check-set identity; entity pair; model revision; clash type; metric/unit/tolerance; location/viewpoint; severity; grouping; lifecycle; exception rationale; rerun verification; and stale identity handling. Include one duplicated-clash cluster and one stale-after-edit case.

## Handoffs

Assembly hierarchy supplies occurrence identity, dimensional tools provide clearance semantics, annotations/issues provide review workflow, and manufacturing handoff consumes unresolved clash status where relevant.