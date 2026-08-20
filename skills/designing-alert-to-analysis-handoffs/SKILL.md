---
name: designing-alert-to-analysis-handoffs
description: Use when a BI alert, anomaly, threshold breach, or scheduled notification must open a reproducible analytical context rather than dropping the user into a generic dashboard.
---

# Designing Alert to Analysis Handoffs

An alert is a claim about a condition at a particular moment. The analysis experience must preserve the evidence behind that claim even when the user opens it minutes or days later.

## Parent Contract
**Required parent:** `designing-business-intelligence-workspaces`.

The parent provides the analytical workspace. This skill owns the boundary from notification/alert state into reproducible investigation state.

## Alert Evidence Packet
Bind each alert instance to the metric identity/version, evaluated threshold or detector, resolved filters, evaluated time interval, timezone, observed value, comparison baseline, data freshness, execution record, and recipient scope. Avoid reconstructing an old alert from current dashboard defaults; current defaults may have changed.

Opening an alert should initially preserve the triggered snapshot. From there, give the user a deliberate transition to live/current analysis. Label the transition because comparing the historical trigger with current data is often the core investigative task.

For anomaly systems, explain available detector context without claiming certainty. Show baseline window, expected range, and relevant model/version if that evidence exists. Do not convert “anomalous under detector X” into “business problem confirmed.”

Multiple alerts may refer to the same underlying incident. Support grouping or deduplication when the product can prove relationship, but preserve individual evidence packets so users can audit why each alert fired.

## Permission and Expiry
A recipient may lose access after notification. Handle this as an authorization state, not as “alert not found.” If the underlying analysis was deleted, retain enough alert metadata to explain what happened if policy permits. Sensitive values in notifications must respect channel-specific disclosure rules.

## Evidence
Trigger alerts under controlled data, then change dashboard defaults and metric definitions before opening the alert. Evidence passes only if the original trigger remains reproducible or explicitly records what can no longer be reconstructed. Test stale data, alert recovery, duplicate alerts, revoked access, and opening from email, mobile push, and in-product center when supported.

## Failure Modes
- Alert link opens today's dashboard instead of the triggered state.
- Threshold text differs from the actual rule that executed.
- Current metric definition silently replaces the historical version.
- The interface confuses detector anomaly with confirmed causal problem.
- A revoked user sees a generic 404 and cannot distinguish access loss.
- “Resolved” status hides whether the data recovered or the alert rule was muted.

## Falsification
Trigger a known threshold breach, then modify the dashboard and wait for data to normalize. Open the old alert. Falsify if the user cannot reconstruct why it fired or cannot distinguish historical evidence from current state.

## Recovery
Persist immutable trigger metadata, open in snapshot-first analysis, add explicit “compare with current” behavior, and separate access/deletion states. If some historic dependency is irretrievable, state the missing evidence instead of fabricating a reconstructed result.

## Handoff
Use `designing-data-freshness-communication` for stale-data semantics, `designing-query-provenance-inspection` for execution details, and notification owners for channel interruption policy. This skill owns the analytical continuity after the alert is activated.

## Output Contract
Return an `alert-to-analysis-handoffs-contract` with `alert_evidence_packet`, `snapshot_entry_state`, `current_comparison_transition`, `detector_explanation`, `grouping_policy`, `permission_states`, `retention_rules`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.