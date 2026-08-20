---
name: designing-query-provenance-inspection
description: Use when analysts need to understand how a visible result was produced, including query transformations, parameters, semantic objects, execution context, and changes between authored and executed logic.
---

# Designing Query Provenance Inspection

A result is trustworthy only when the user can reconstruct the path from analytical intent to executed computation. Provenance inspection must reveal meaningful transformations without drowning the user in engine internals.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent defines BI workspace continuity. This skill owns inspection of the computation path behind a chart, table, alert, or saved analysis.

## Provenance Layers
Separate at least four layers when the product has them: semantic selection, generated logical query, engine-specific physical query, and execution record. Do not show generated SQL as if it were the only source of truth when a semantic layer, row policy, cached result, or post-processing transform changed the meaning.

Record parameters with resolved values and provenance. A template such as `region = {{region}}` is insufficient if the user cannot see that `region` resolved to APAC at execution time. For time-relative filters, capture the evaluated bounds and timezone so a historical run remains interpretable.

Show hidden transformations that materially change interpretation: row-level security predicates, currency conversion, null handling, deduplication, sampling, aggregation pushdown, calculated fields, post-query filters, and cache substitution. Engine optimization details can be collapsed unless they alter user-observable semantics.

Diffing is first-class. When a saved analysis changes, let users compare the provenance chain between revisions and identify whether the change came from authored logic, a semantic definition version, policy injection, or upstream schema. Avoid a single undifferentiated text diff for systems with structured transformations.

## Inspection Interaction
Provide a clear path from result element to provenance. Selecting a chart mark may narrow the relevant query slice; selecting a dashboard tile should still allow return to full tile provenance. Maintain stable references so copied provenance links remain useful to reviewers who have permission.

Do not leak restricted SQL, identifiers, or policy internals to users who can see a result but are not authorized to inspect all source details. Explain redaction explicitly so missing detail is not mistaken for absence of transformation.

## Evidence
Capture a known analytical result and independently reconstruct its effective filters, semantic metric version, generated query, execution timestamp, data source, and policy effects. Include cache hit, parameter substitution, query retry, and schema evolution cases. Evidence should prove that the inspector reflects what actually executed rather than what the editor intended to execute.

## Failure Modes
- Showing authored SQL while a different query executed.
- Omitting row-level security or post-processing from the provenance story.
- Losing resolved parameter values after the run.
- Presenting redacted details as though no transformation occurred.
- Comparing revisions only by text when semantic nodes changed outside the text.
- Linking to a mutable editor state rather than an immutable execution record.

## Falsification
Create two runs that look visually identical but differ by one hidden policy or semantic-version change. The inspector is falsified if a reviewer cannot identify why the runs differ. Also falsify if an unauthorized reviewer gains access to sensitive source details through provenance navigation.

## Recovery
Rebind inspection to immutable execution records, expose semantic and policy layers, separate redaction from absence, and add structured revision comparison. If the backend cannot supply an execution fact, label that field unavailable; do not infer it from editor state.

## Handoff
Use `designing-data-lineage-exploration` for upstream/downstream dataset relationships and `designing-metric-definition-comparison` for definition-level comparison. This skill follows a specific computation instance rather than modeling the entire data estate.

## Output Contract
Return a `query-provenance-inspection-contract` containing `provenance_layers[]`, `execution_identity`, `resolved_parameters[]`, `material_transformations[]`, `policy_visibility`, `redaction_rules`, `revision_diff_model`, `inspection_routes[]`, `evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.