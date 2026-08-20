---
name: designing-trade-blotters
description: Use when this specialist's decision ownership is materially in scope. Own operational trade and execution records across order/execution identity, account, instrument, side, quantity, price, timestamps, status, partial fills, corrections, allocations, settlement, and audit drill-down.
---
# Designing Trade Blotters

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own dense post-submission/post-execution monitoring of orders, fills, and trades. Decide record hierarchy, partial fills, order versus execution status, account/instrument, timestamps, price/quantity, venue, allocation/settlement state, corrections/cancels, filtering, and drill-down. This owner does not recommend trades or replace order entry.

## Inputs and evidence

Require order IDs, execution/trade IDs, account/book, instrument, side, quantity/order type, fills, prices, venues, timestamps, status lifecycle, corrections/busts, allocations, settlement, and market/session context. Identify out-of-order event arrivals and partial-fill aggregation.

## Procedure

Choose a clear hierarchy: one order with expandable executions or a trade-centric view with order linkage. Distinguish submitted/accepted/working/partially filled/filled/cancelled/rejected and execution settlement states. Aggregate filled quantity/average price while retaining every execution. Corrections/busts remain linked and visibly restate derived totals without deleting original records. Filters/sorts show active scope; totals state whether they cover visible rows, selected rows, or all query results. Streaming updates preserve row identity and do not reorder unexpectedly unless active sort demands it.

## Failure topology

Failures include accepted order shown as trade, partial fill rounded to complete, corrected execution replacing history, out-of-order events temporarily reducing filled quantity incorrectly, duplicate executions, and streaming sort making rows jump while user reviews them. Another failure is a filtered blotter total presented as firm-wide exposure.

## Falsification

Reject if order and execution identities are conflated; if partial fills cannot reconcile to executions; if corrections erase originals; if status event order is not robust to late arrival; if duplicate execution IDs can double-count; if total scope is hidden; or if instrument/account/side is ambiguous.

## Output contract

Return a `trade-blotters-contract` with: order/execution hierarchy; account/instrument/side; quantities/prices; status model; timestamps/venues; partial-fill aggregation; correction/bust lineage; allocation/settlement; streaming update policy; filters/sorts; scoped totals; and drill-down/audit. Include one corrected partial-fill scenario.

## Handoffs

Order entry produces submitted orders, portfolio positions consume settled/executed effects, risk limits monitor exposures, and audit/history captures administrative changes.