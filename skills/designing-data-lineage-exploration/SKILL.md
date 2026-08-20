---
name: designing-data-lineage-exploration
description: Use when analysts, data owners, or reviewers must trace upstream and downstream dependencies among sources, models, semantic objects, metrics, dashboards, and alerts without turning lineage into an unreadable graph.
---

# Designing Data Lineage Exploration

Lineage is a dependency investigation tool. Its interface should help answer a bounded question—where did this value come from, what depends on this model, or what will break if this field changes—rather than rendering every node in the warehouse at once.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent provides analytical context. This skill owns traversing dependency structure across analytical and data-product layers.

## Layered Lineage Model
Represent node types explicitly: source, ingestion, transformation/model, field, semantic entity, metric, analysis, dashboard, alert, and external consumer when available. Do not draw edges with one generic meaning; distinguish derives-from, reads-from, publishes-to, references, filters-by, and operational dependency.

Start from a focus node and reveal bounded neighborhoods. Users should be able to expand upstream, downstream, or both while retaining orientation. For dense estates, provide list/table alternatives, search within the current subgraph, path highlighting, and collapse by domain or layer. A huge force-directed map is not sufficient evidence of navigability.

Impact analysis and origin tracing are opposite traversal tasks. Downstream impact should surface production criticality, owners, and change sensitivity. Upstream origin should surface transformation chain, source freshness, and semantic boundaries. Tune detail for the question rather than giving both directions equal visual weight everywhere.

Version and time matter. A lineage edge may be current, historical, inferred, or unresolved. If lineage metadata is incomplete, show confidence/provenance of the edge instead of presenting the graph as a complete topology.

## Permission Boundary
A user may know that a restricted dependency exists without being allowed to inspect its name or fields. Preserve path continuity with bounded redaction when policy permits. Do not simply drop restricted nodes if doing so creates a false impression that two visible nodes connect directly.

## Evidence
Pick a metric with a multi-stage transformation chain and a dashboard with downstream alerts. Verify the UI can answer source origin, current metric derivation, and downstream impact of a field change. Include a missing-lineage edge, a deleted historical node, and a permission-restricted dependency. Compare UI paths with known metadata records.

## Failure Modes
- All edges look identical despite different dependency semantics.
- The default graph explodes into hundreds of unreadable nodes.
- Hidden restricted nodes create false direct connections.
- Historical lineage is shown as current.
- Impact view omits owners and production consumers.
- Inferred lineage is presented with the same certainty as observed lineage.

## Falsification
Ask users to identify every material downstream consumer of a proposed field change and separately trace a metric to its originating source. Falsify if the interface cannot keep direction/orientation clear, if a restricted or unknown edge is silently erased, or if a historical path is mistaken for current production lineage.

## Recovery
Use typed edges, focus-node traversal, direction-specific views, collapsed domains, confidence states, and permission-aware redaction. When metadata coverage is partial, show the known boundary and invite targeted investigation rather than implying saturation.

## Handoff
Use `designing-query-provenance-inspection` for one execution instance, `designing-data-freshness-communication` for temporal health, and `designing-metric-definition-comparison` for semantic definition differences.

## Output Contract
Return a `data-lineage-exploration-contract` containing `node_types[]`, `edge_types[]`, `focus_traversal_rules`, `upstream_view`, `downstream_impact_view`, `orientation_mechanisms`, `version_time_semantics`, `redaction_model`, `confidence_states[]`, `evidence_paths[]`, and `recovery_actions[]`.