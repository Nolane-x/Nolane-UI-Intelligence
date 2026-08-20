---
name: designing-portfolio-position-monitoring
description: Own monitoring of financial positions across account, instrument, quantity, cost basis, market value, P&L, exposure, stale prices, pending activity, and reconciliation without giving investment advice.
---
# Designing Portfolio Position Monitoring

## Decision ownership

Own operational display of holdings/positions and their valuation state. Decide position identity, account/book, instrument, quantity, settled versus pending, cost basis, price timestamp/source, market value, realized/unrealized P&L, currency, exposure, aggregation, and drill-down to transactions/orders. This owner does not tell users what to buy or sell.

## Inputs and evidence

Require accounts/books, instrument identifiers, quantities, settlement state, cost basis methodology, market prices and timestamps, currencies/FX, corporate actions if relevant, pending orders/trades, P&L definitions, and reconciliation state. Identify illiquid instruments with stale or model-derived prices.

## Procedure

Anchor positions to stable account/book and instrument identifiers. Show quantity plus price timestamp/source; stale, missing, indicative, or model-derived values must not look like fresh traded prices. Distinguish settled position from pending/unsettled activity when it affects available exposure. P&L labels state realized/unrealized and basis. Aggregates by asset/currency/sector or other dimension expose inclusion and FX basis. Drill-down traces a position to trade/transaction history. Sorting by P&L or value must not hide data quality flags.

## Failure topology

Failures include stale price used as if real-time, pending trade double-counted, cost basis methodology hidden, market value summed across currencies without basis, short/negative positions losing sign, and instrument aliases confused. Another failure is operational metrics styled as recommendations or gain/loss colors implying a suggested action.

## Falsification

Reject if price freshness/source is unknown; if settled/pending distinction is hidden; if P&L basis cannot be explained; if multi-currency aggregate lacks FX basis; if position sign/quantity is ambiguous; if instrument identity cannot be disambiguated; or if interface language recommends a trade from monitored performance.

## Output contract

Return a `portfolio-position-monitoring-contract` with: account/book; instrument identity; quantity/sign; settled/pending; cost basis method; price/source/time/quality; market value; realized/unrealized P&L; currency/FX; aggregation scope; drill-down; and explicit non-advice boundary. Include one stale-price and one unsettled-trade case.

## Handoffs

Trade blotters provide executed trade history, order entry/order book supply pending market activity, FX exposure handles currency risk views, and financial risk limits consume positions for governed thresholds.