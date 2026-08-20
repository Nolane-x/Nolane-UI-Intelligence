---
name: designing-cash-flow-forecasting
description: Use when this specialist's decision ownership is materially in scope. Own cash forecast interfaces across opening balance, expected receipts/payments, timing assumptions, scenarios, confidence, bank/entity/currency aggregation, liquidity thresholds, and actual reconciliation.
---
# Designing Cash Flow Forecasting

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own forward-looking cash position projections. Decide opening-balance source, expected inflow/outflow events, timing, probability/confidence, scenario, entity/bank/currency aggregation, liquidity thresholds, forecast horizon, actual-versus-forecast update, and source drill-down. This owner does not predict markets or offer investment advice.

## Inputs and evidence

Require reconciled cash balances, receivables/payables/payment schedules, payroll/tax/other planned flows, budgets/contracts, bank/entity/currency structure, FX rates if consolidated, confidence/probability, horizon, scenario assumptions, and actual transaction feeds. Identify uncertain dates and double-counted sources.

## Procedure

Begin from a dated opening balance with source/freshness. Model each expected cash event with amount/currency/date range or expected date, source, confidence, and inclusion rule. Avoid converting uncertain timing into fake exact dates; use ranges/bands or scenarios. Consolidation must expose FX rate/basis and intercompany elimination where relevant. Show projected low points and threshold breaches with contributing flows. As actual cash arrives, reconcile/replace forecast events rather than counting both. Scenario changes preserve assumptions and comparison.

## Failure topology

Failures include stale opening balance, forecast and actual receipt both counted, uncertain invoice payment treated as guaranteed date, mixed currencies summed without rate, intercompany flows double-counted, and a single line suggesting false precision months out. Another failure is liquidity alert with no drill-down to the flows causing it.

## Falsification

Reject if opening balance source/date is unknown; if actualization can double-count forecast event; if currency consolidation lacks rate/basis; if uncertain events cannot express confidence/range; if intercompany treatment is hidden; or if projected threshold breach cannot identify contributing flows and scenario.

## Output contract

Return a `cash-flow-forecasting-contract` with: opening balance/source; forecast events; amount/currency; timing range/date; confidence; scenario/assumptions; consolidation/FX; intercompany policy; liquidity thresholds; low-point drill-down; actualization/reconciliation; and horizon uncertainty. Include one delayed-receivable scenario.

## Handoffs

AP/AR provide expected flows, bank reconciliation provides actual cash, budget supplies planned expenditures, FX exposure provides currency risk context, and financial statements remain historical/reporting authority.