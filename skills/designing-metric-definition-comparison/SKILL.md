---
name: designing-metric-definition-comparison
description: Use when people must compare two or more metric definitions, revisions, or near-duplicates and understand exactly which semantic changes explain different values.
---

# Designing Metric Definition Comparison

Metric comparison should answer “why are these numbers different?” by comparing the rules that produce them, not by placing two trend lines side by side and leaving interpretation to the analyst.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

This skill narrows the parent workspace to definition-level comparison among governed or exploratory metrics.

## Decision ownership

This skill owns the decision about which differences between metric definitions are semantically consequential and which are implementation noise. It must compare population, aggregation, time semantics, units, null policy, lineage, lifecycle and ownership on a common frame, then preserve UNKNOWN where evidence cannot establish equivalence. Creating or governing the metric itself belongs elsewhere; this skill is accountable for whether a reviewer can justify why two definitions should or should not be treated as the same business meaning.

## Comparison Dimensions
Normalize definitions into comparable fields: entity/population, numerator and denominator when relevant, aggregation, deduplication, inclusion/exclusion predicates, attribution window, time grain, currency/unit treatment, null policy, dimensional availability, source lineage, owner, and lifecycle status. Preserve raw formula or SQL as supporting evidence, not as the sole comparison representation.

Highlight semantic deltas by consequence. A wording change in description is less important than moving from order date to settlement date or from gross to net amount. Rank differences according to their likely effect on interpretation and show when the system cannot estimate the effect.

For revisions of the same metric, separate intended semantic change from incidental implementation change. A query optimization that preserves semantics should not be presented as a business-definition change. Conversely, an upstream model change that alters population must appear even if the metric expression text stayed identical.

If values are available, pair definition diff with controlled result comparison across representative slices. Do not imply causality from correlation; use it to show where a semantic change becomes observable.

## Evidence
Compare a current metric with a deprecated predecessor and a similarly named sibling. Verify that a reviewer can identify which definition is canonical, which dimensions changed, and which dashboards depend on each. Include a case where formula text is identical but semantic-layer source changes, and another where implementation text changes with no semantic effect.

## Failure Modes
- Raw SQL diff overwhelms the business-semantic difference.
- Description text is treated as authoritative while calculation metadata differs.
- Same-name metrics from different entities appear equivalent.
- No lifecycle or owner context is shown during comparison.
- A dependency impact is omitted before a definition migration.
- A numeric delta is shown without matching time range and population.

## Falsification
Give a reviewer two metrics whose formulas differ syntactically but are semantically equivalent and two whose text is similar but population differs. Falsify if the interface prioritizes textual change over semantic change or cannot explain the direction of a known value difference.

## Recovery
Build a structured semantic diff, surface high-consequence dimensions, include canonical/replacement relationships, and connect comparison to downstream impact. Where metadata is unavailable, mark the specific comparison dimension UNKNOWN instead of pretending equivalence.

## Handoff
Discovery of candidates belongs to `designing-semantic-metric-browsing`; downstream dependency traversal belongs to `designing-data-lineage-exploration`; execution-instance inspection belongs to `designing-query-provenance-inspection`.

## Output Contract
Return a `metric-definition-comparison-contract` containing `comparison_dimensions[]`, `semantic_delta_ranking`, `lifecycle_context`, `implementation_vs_semantic_change_rules`, `representative_value_checks[]`, `dependency_links`, `unknown_fields[]`, `evidence[]`, `failure_findings[]`, and `recovery_actions[]`.