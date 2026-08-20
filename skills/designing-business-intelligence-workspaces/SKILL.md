---
name: designing-business-intelligence-workspaces
description: Use when a BI product must let people move from governed metrics to dashboards, ad hoc analysis, drill paths, freshness evidence, and reusable analytical work without losing semantic context.
---

# Designing Business Intelligence Workspaces

BI is not a gallery of charts. It is an analytical environment in which every visible number carries a semantic definition, data state, filter context, and path back to the evidence that produced it.

## Parent Contract
**Required parent:** `designing-data-dense-interfaces`.

Inherit dense-surface legibility, comparison, keyboard access, and state accounting. This skill owns the workspace-level analytical grammar: how metric discovery, query construction, dashboard consumption, investigation, sharing, and return-to-work fit together without silently changing meaning.

## Decision Architecture
Start by declaring the analytical objects that can survive navigation: metric, dimension, filter, time window, query, visualization, dashboard, saved analysis, alert, and lineage reference. Decide which objects are governed and which are exploratory. A governed metric must not become an unlabelled calculation simply because the user entered an editor.

Model the workspace as transitions among consumption, exploration, and authoring rather than as unrelated pages. When a dashboard tile is opened for analysis, preserve the tile's metric definition, effective filters, comparison period, timezone, aggregation grain, and data snapshot. When returning, state explicitly whether the dashboard remained unchanged or inherited edits.

Expose semantic context close enough to the number that users can answer: what is this, what population does it cover, how fresh is it, what filters are active, and where did it come from? Do not force every answer into permanent chrome; use progressive disclosure while keeping critical ambiguity visible.

Saved work requires an identity model. Distinguish saved query, saved view, dashboard, personal draft, team artifact, and published governed asset. Make ownership, edit authority, sharing scope, and downstream dependencies inspectable before destructive changes.

## Evidence Model
Evidence for completion includes representative flows that cross modes: open a dashboard, inspect a metric, change a scoped filter, drill into a segment, open underlying analysis, save a personal variant, and return later. Capture the effective query/metric context at every handoff. Verify stale data, unavailable lineage, permission loss, partially loaded tiles, and schema change rather than only the happy path.

A screenshot of a polished dashboard is weak evidence. Strong evidence demonstrates that identical analytical intent produces traceable context across routes and that different intent is visibly distinguished.

## Failure Classes
- **Semantic evaporation:** a governed metric loses definition during ad hoc exploration.
- **Filter ambiguity:** the same control visually appears active while applying to different scopes.
- **Mode collapse:** edit and view capabilities are mixed so consumption changes production assets accidentally.
- **Context fork:** drilldown opens a view with different time, timezone, or population without disclosure.
- **Artifact confusion:** personal drafts and shared governed assets look operationally equivalent.
- **Freshness blindness:** a number looks current after upstream data has stopped updating.

## Falsification
Give an analyst and a dashboard consumer the same metric starting from different entry points. Ask each to explain the effective definition, filters, freshness, and saved-state ownership after three navigation transitions. The workspace model is falsified if either person must infer hidden state, if two visible numbers claim equivalence while using different semantics, or if returning from exploration mutates a shared asset unintentionally.

## Recovery
Repair the semantic chain before polishing layout. Add explicit context carriers, separate personal exploration from governed artifacts, restore scope indicators, bind freshness to data evidence, and make transitions reversible. If the product cannot prove what context survived a route transition, downgrade the claim to UNKNOWN rather than presenting continuity as certain.

## Handoff
Coordinate with `designing-semantic-metric-browsing`, `designing-dashboard-filter-scope`, `designing-query-provenance-inspection`, `designing-data-lineage-exploration`, and `designing-saved-analysis-workspaces`. Hand off chart encoding questions to `designing-data-visualization`; do not redefine visualization semantics here.

## Output Contract
Return a `business-intelligence-workspaces-contract` containing `analytical_objects[]`, `governance_boundaries`, `mode_transitions[]`, `context_carriers[]`, `saved_artifact_model`, `freshness_policy`, `permission_boundaries`, `cross_mode_evidence[]`, `failure_findings[]`, and `recovery_actions[]`.