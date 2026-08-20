---
name: designing-trading-order-entry
description: Own high-stakes financial order-entry interaction across instrument/account, side, quantity, order type, price, time-in-force, estimated consequence, validation, confirmation, submission, and status receipt without recommending trades.
---
# Designing Trading Order Entry

## Decision ownership

Own the UI contract for expressing and submitting a user-decided market order instruction. Decide instrument/account identity, buy/sell or side, quantity/notional, order type, price/trigger fields, time-in-force, venue/routing if applicable, estimated value/fees where available, validation, confirmation proportional to consequence, submission idempotency, and receipt. It explicitly does not recommend instruments, direction, size, or strategy.

## Inputs and evidence

Require account permissions, instrument identifiers, market/reference data, supported order types, tick/lot sizes, quantity/notional rules, price bands, trading session, time-in-force options, estimated fees, available cash/position/margin or policy checks, risk limits, and order API states. Identify delayed market data and instruments with special units.

## Procedure

Persistently show exact account and instrument with symbol plus disambiguating name/venue/currency. Side must be textually explicit and survive color limitations. Fields adapt to selected order type and explain trigger/limit relationships without hiding values. Validate tick/lot size, session, quantity, price bands, account eligibility, and risk limits before submission where possible. Confirmation summarizes side, instrument, quantity/notional, order type/prices, time-in-force, account, estimated consideration and data freshness. Submit idempotently and show accepted/rejected/pending receipt from the authoritative system; never infer execution from submission.

## Failure topology

Failures include wrong similarly named instrument, buy/sell encoded only by red/green, stale quote presented as current estimate, market versus limit fields confused, quantity unit ambiguity, double submission, rejected order shown as placed, and accepted order shown as executed. Another failure is prefilled values that appear advisory or persist dangerously from a different instrument/account.

## Falsification

Reject if instrument/account/side cannot be confirmed before submit; if market-data freshness is hidden where used for estimates; if order-type dependent fields are ambiguous; if tick/lot/risk validation can be known but is deferred without reason; if duplicate clicks can create multiple orders; if accepted/pending/executed are conflated; or if UI copy recommends the transaction.

## Output contract

Return a `trading-order-entry-contract` with: account/instrument identity; side; quantity/notional units; order type; limit/stop/trigger fields; time-in-force; market-data freshness; validations/risk checks; confirmation summary; idempotent submission; authoritative receipt/status; and explicit non-advice boundary. Include one stale-quote and one duplicate-submit case.

## Handoffs

Order book/watchlist may provide context but cannot pre-authorize decisions, risk-limit controls can block/require approval, trade blotter records executions, and financial high-stakes authority governs confirmation.