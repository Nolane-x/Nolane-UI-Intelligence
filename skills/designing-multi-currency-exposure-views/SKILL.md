---
name: designing-multi-currency-exposure-views
description: Own operational views of monetary balances and commitments by currency, entity, rate basis, maturity, hedge status, and translated reporting value without implying a trading recommendation.
---
# Designing Multi-Currency Exposure Views

## Decision ownership

Own visibility into foreign-currency balances, receivables/payables, cash, commitments, and optional hedge relationships. Decide native versus reporting amount, FX rate/source/time, exposure grouping, maturity buckets, entity, gross/net views, translation effects, and confidence. This owner does not recommend hedging or speculate on future rates.

## Inputs and evidence

Require monetary items by currency/entity, cash/AR/AP/commitments, reporting currency, FX spot/closing/rate sources, valuation timestamp, maturity dates, hedge relationships if tracked, and consolidation policy. Identify stale rates and items whose currency amount is estimated.

## Procedure

Keep native currency amount visible alongside translated reporting value. Every translated number exposes rate basis/source/time or a drill-down. Group exposure by currency, entity, maturity, and source type; gross and net exposure must be labeled because netting assumptions matter. Hedge-linked items, if shown, display relationship and scope without declaring effectiveness unless validated elsewhere. Stale/missing rates produce unknown translation rather than zero. Scenario rate changes, if supported, are clearly hypothetical and do not become advice.

## Failure topology

Failures include summing currencies before translation, hidden rate timestamps, stale rate appearing current, net exposure hiding large gross positions, hedge linkage treated as eliminated risk, and scenario changes presented as forecasts. Another failure is mixing transaction-date and closing rates in one total without basis disclosure.

## Falsification

Reject if translated values cannot reveal rate source/time; if missing rate becomes zero; if native amount disappears; if gross/net distinction is hidden; if different valuation bases are aggregated silently; if hedge relationship is represented as guaranteed protection; or if hypothetical scenarios are labeled predictions.

## Output contract

Return a `multi-currency-exposure-views-contract` with: entity/reporting currency; native items; currency amounts; valuation rate/source/time; translated value; gross/net grouping; maturity; source category; hedge linkage; stale/missing rate state; and hypothetical scenario labeling. Include one stale-rate and one gross-versus-net case.

## Handoffs

Cash forecasts, AR/AP, portfolio positions, and statements provide source items; financial risk limits may monitor exposure; market data authority supplies rates outside this UI contract.