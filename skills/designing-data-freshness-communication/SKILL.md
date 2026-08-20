---
name: designing-data-freshness-communication
description: Use when analytical results can lag source reality and users need to distinguish query time, cache age, dataset update time, expected cadence, incidents, and intentionally historical snapshots.
---

# Designing Data Freshness Communication

“Updated 5 minutes ago” is meaningless unless the system specifies what updated: the UI, the query cache, the modeled dataset, or the underlying source. Freshness communication must name the clock being measured.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent owns analytical context. This skill owns temporal evidence about how current a result is and whether that currentness meets the product's declared expectation.

## Freshness Model
Separate relevant timestamps: source event time, ingestion time, transformation completion, semantic dataset publication, query execution, cache creation, and UI render. Not every product exposes every layer, but it must avoid collapsing distinct clocks into one deceptive label.

Define expected cadence per data product where available. Freshness is a comparison between observed state and expectation, not merely an age. A dataset refreshed daily can be healthy at 18 hours old; a five-minute operational feed can be stale at 20 minutes. Communicate both observed age and breached expectation when the distinction affects decisions.

Historical snapshots are not stale data. Mark intentionally frozen reporting periods or as-of analyses as snapshots so users do not interpret their age as an incident. Conversely, a dashboard showing yesterday's cached result during an outage must not masquerade as current because the page rendered successfully.

Propagate freshness to composed dashboards carefully. A page-level badge should represent the least-current material dependency or disclose mixed freshness. One fresh tile cannot make the whole dashboard “current” when a critical tile is delayed.

## Incident States
Handle delayed, failed, recovering, unknown, and intentionally paused pipelines. Unknown must remain distinct from healthy. Provide useful operational detail such as affected datasets and last confirmed complete period without exposing backend noise irrelevant to the decision.

## Evidence
Use controlled timestamps to verify the label at each layer. Test cache hit, source delay, partial pipeline completion, timezone boundary, daylight saving transition, intentional snapshot, and a dashboard composed from data sources with different cadences. Confirm the visible freshness statement is derived from actual metadata rather than browser time alone.

## Failure Modes
- Query execution time is shown as source freshness.
- Cache age is hidden so an old result looks live.
- A global green badge masks one stale dependency.
- “Last updated” omits timezone or relative-time reference around date boundaries.
- Missing freshness metadata defaults to healthy.
- A deliberately frozen snapshot triggers false stale-data alarms.

## Falsification
Freeze an upstream dataset while continuing to execute queries successfully. Falsify the design if users still read the result as current. Then open an intentionally historical snapshot; falsify if it is represented as a malfunction merely because it is old.

## Recovery
Bind labels to explicit timestamp semantics, surface expected cadence, aggregate mixed freshness conservatively, and introduce UNKNOWN when lineage metadata is missing. Use absolute time on inspection surfaces even when relative time is convenient in compact views.

## Handoff
Coordinate upstream dependency visualization with `designing-data-lineage-exploration`, alert routing with `designing-alert-to-analysis-handoffs`, and result provenance with `designing-query-provenance-inspection`.

## Output Contract
Return a `data-freshness-communication-contract` with `freshness_clocks[]`, `expected_cadence`, `health_states[]`, `mixed_dependency_policy`, `snapshot_semantics`, `incident_copy`, `time_display_rules`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.