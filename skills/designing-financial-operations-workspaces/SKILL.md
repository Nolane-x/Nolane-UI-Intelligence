---
name: designing-financial-operations-workspaces
description: Use when this specialist's decision ownership is materially in scope. Own the interaction architecture for operational finance workspaces where ledger truth, approvals, reconciliation, reporting, cash, positions, and risk controls must remain traceable and internally consistent.
---
# Designing Financial Operations Workspaces

## Parent Contract

**Required parent:** `designing-financial-transaction-ui`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the top-level information and interaction model for finance operations after or outside checkout/payment collection. Decide how legal entities, accounting periods, accounts, transactions, journals, balances, reconciliations, payables/receivables, budgets, cash, reports, positions, approvals, and risk controls relate. This owner does not provide investment advice or accounting policy; it ensures the interface preserves authoritative financial state, provenance, and period/entity context.

## Inputs and evidence

Require organization/legal-entity model, base/reporting currencies, chart of accounts, fiscal periods, transaction/journal sources, approval controls, close/lock policy, banking/payment feeds, budget model, reporting definitions, permissions, audit retention, and if relevant market/trading position models. Inspect month-end close, corrections, multi-currency, partial reconciliation, and concurrent approvals—not only a clean dashboard.

## Procedure

Persistently establish entity, period/date range, currency basis, and accounting status. Distinguish source transactions, accounting entries, derived balances, forecasts, and market-valued positions rather than presenting all as interchangeable numbers. Every material balance or report total should drill to contributing records and state whether it is posted, pending, estimated, or restated. Corrections use reversals/adjustments or policy-approved edits with history, never invisible overwrites. Period locks and approval authority must be visible before edit. Large operational tables need stable identifiers, totals whose filtered scope is explicit, and export that preserves currency/entity/period context.

## Failure topology

Failures include editing the wrong legal entity/period, totals mixing posted and pending data, filter-scoped totals presented as global, currency conversion basis hidden, corrections overwriting audit history, closed periods appearing editable, and dashboard amounts with no drill-down. Another failure is a single "balance" label that could mean ledger, available cash, forecast, or market value.

## Falsification

Reject if users cannot identify entity/period/currency basis; if a material total cannot trace to source records; if posted/pending/forecast values are visually conflated; if a locked period accepts edits without a controlled exception; if corrections can erase prior values; or if two finance surfaces show different balances without explaining scope/timing.

## Output contract

Return a `financial-operations-workspaces-contract` containing: entity/period/currency context; financial record taxonomy; authoritative-versus-derived states; drill-down lineage; posting/pending/forecast distinctions; correction/audit model; approval/lock authority; filtered-total semantics; export context; and cross-surface reconciliation rules. Include one multi-entity and one closed-period correction scenario.

## Handoffs

Delegate ledger, journals, reconciliation, AP/AR, expenses, budgets, cash forecasts, statements, variance, accounts, tax mapping, FX exposure, portfolio positions, order entry, watchlists, order books, blotters, and risk limits to dedicated owners. Generic transaction, approvals, data-grid, and audit skills remain supporting authorities.