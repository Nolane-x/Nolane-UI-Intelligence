---
name: designing-semantic-metric-browsing
description: Use when users must discover and choose governed metrics from a semantic layer without confusing similarly named measures, hidden dimensions, grain, ownership, or deprecated definitions.
---

# Designing Semantic Metric Browsing

Metric discovery is a meaning-selection problem, not a search-box problem. The interface must help a person choose the right governed definition before any chart makes the wrong metric look authoritative.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent owns the overall BI workspace. This skill owns the catalog and selection behavior for metrics whose names may be similar while their populations, formulas, grains, owners, and validity windows differ.

## Meaning Before Popularity
Represent a metric as more than a label. At minimum, make discoverable its definition, business owner, calculation status, aggregation behavior, dimensional compatibility, time grain, unit, freshness expectation, and lifecycle state. Synonyms may improve retrieval, but a synonym must not erase the distinction between metrics that share casual language.

Rank search results by semantic fit and governed status before raw usage popularity. A heavily used legacy metric can be the wrong recommendation. Mark deprecated or replacement relationships explicitly and route users toward the canonical successor without hiding historical assets that still depend on the old metric.

Use comparison when ambiguity is costly. If two results differ primarily by inclusion rules, attribution window, currency basis, or entity grain, surface those differences side by side. Do not force users to open multiple detail pages and memorize definitions.

Dimension compatibility matters at selection time. If a metric cannot be segmented by a requested dimension or does not support additive aggregation, prevent a false affordance rather than allowing an invalid chart to be built and corrected downstream.

## Selection State
Distinguish browsing, previewing, and committing a metric. Preview can show sample trend or usage context, but visual popularity is not semantic authority. Committing a metric should capture the exact semantic identifier/version rather than only a display name so saved work remains auditable after labels change.

## Evidence
Test with intentionally confusable metrics: gross revenue versus net revenue, active accounts versus active users, event count versus distinct entity count, and current versus deprecated definitions. Evidence must show users can identify the correct metric from its contract without relying on tribal knowledge. Also test no-result, permission-restricted, stale-catalog, and renamed-metric cases.

Inspect the saved artifact after selection. If it stores only free text or a mutable name, selection evidence is incomplete even if the browser itself looked correct.

## Failure Modes
- Name similarity hides different populations or grains.
- Usage count is treated as proof of correctness.
- Deprecated metrics remain visually indistinguishable from current ones.
- Unsupported dimensional cuts appear selectable.
- The metric preview shows an attractive chart but omits definition and unit.
- A saved analysis points to a label instead of a stable semantic identity.
- Permission filtering removes context so users think a metric does not exist rather than that access is restricted.

## Falsification
Ask a user to choose among three nearly identical metric names for a stated business question, then explain why the other two are wrong. Falsify the design if the answer depends on external documentation, if incompatible dimensions can be selected, or if a deprecated metric can be chosen without a visible lifecycle warning.

## Recovery
Increase semantic contrast, not decorative contrast. Add explicit definition deltas, stable identifiers, compatibility hints, replacement relationships, and governed-state signals. When catalog evidence is stale or unavailable, expose uncertainty instead of presenting the browser as complete.

## Handoff
Send filter application to `designing-dashboard-filter-scope`, metric-to-metric difference analysis to `designing-metric-definition-comparison`, and source traceability to `designing-query-provenance-inspection`. The browser should not invent new metric formulas.

## Output Contract
Return a `semantic-metric-browsing-contract` with `metric_identity_fields`, `search_semantics`, `ranking_policy`, `comparison_fields[]`, `compatibility_rules[]`, `lifecycle_states[]`, `selection_persistence`, `ambiguity_tests[]`, `evidence[]`, and `recovery_actions[]`.