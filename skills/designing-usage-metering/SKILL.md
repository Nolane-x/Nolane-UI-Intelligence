---
name: designing-usage-metering
description: Use when products charge or constrain customers by measured consumption and the interface must show meter definition, period, freshness, included amount, billable excess, forecast and source without presenting delayed estimates as exact billing truth.
---

# Designing Usage Metering

## Parent Contract
**Required parent:** `designing-subscription-management`.

This faculty owns consumption-meter UX. The billing engine defines what events count, aggregation rules and final invoice quantities.

## Decision Boundary
Define the meter in domain language: API requests, tokens, storage GB-month, compute minutes, active users, messages or another billable quantity. Expose unit, billing period, included allowance, consumed quantity, pending/unprocessed usage where known, reset/renewal boundary and overage pricing reference.

Freshness is part of the number. Usage dashboards are often delayed or eventually consistent; show last updated time and whether current figures are estimated. Do not animate a gauge as real-time if billing ingestion settles hours later. When adjustments/credits exist, explain why displayed raw usage may differ from billable usage.

Meters can have several dimensions: workspace and project breakdown, model/service type, region, team, or rate tier. Drilldown should reconcile to the headline total. If totals cannot reconcile because of delayed pipelines, surface that state instead of forcing perfect-looking sums.

Forecasts need separation from actuals. Projected end-of-period usage/cost should name assumptions and confidence where available. Alerts and thresholds are controls around the meter, not evidence the meter itself is current.

## Failure Topology
- Progress bar reaches 80% based on yesterday’s data but label implies current consumption.
- UI says `800/1000` without identifying the billing period or reset date.
- Breakdown categories add to more than total because adjustments are missing from explanation.
- Forecast is styled identically to actual usage.
- Decimal storage units mix GB and GiB across pages.
- Usage counter becomes the invoice authority even though final billing applies deduplication/credits later.

## Falsification and Recovery
Falsify with delayed ingestion, corrections, period rollover, multi-unit breakdown, credits, overage and estimated forecast. Reconcile visible meter to billing-source records and timestamps.

Recover by binding every meter to unit/period/freshness, separating raw/billable/forecast quantities, exposing adjustments and refusing false real-time precision.

## Output Contract
Return `usage-metering-contract` with meter definition, unit, period/reset, included/overage boundaries, actual/pending/adjusted quantities, freshness, breakdown reconciliation, forecast distinction, alert handoff and billing-reconciliation tests.