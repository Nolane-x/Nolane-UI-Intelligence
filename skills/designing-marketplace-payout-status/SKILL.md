---
name: designing-marketplace-payout-status
description: Use when sellers need to understand pending balance, available balance, fees, reserves, refunds, disputes, payout batches, bank transfer state, holds, failures, and reconciliation from buyer transaction to received funds.
---

# Designing Marketplace Payout Status

Seller payout UI must reconcile commercial events to money movement. “Paid” is ambiguous when a buyer has paid the marketplace but the seller's funds are still pending, reserved, batched, sent, failed, reversed, or under dispute.

## Parent Contract
**Required parent:** `designing-marketplace-operations`.

The parent owns seller/order/dispute context. This skill owns the seller-visible financial lifecycle after a transaction, including amounts, deductions, eligibility, payout transfer, and failure recovery.

## Money State Model
Separate gross order amount, taxes, shipping, marketplace fees, payment fees, seller adjustments, refunds, dispute reserves, available balance, pending balance, payout amount, and net received. Every monetary line should have currency and reference to source transaction/event.

Payout eligibility has timing rules: delivery confirmation, return window, reserve period, verification status, minimum balance, or risk hold. Surface the rule and expected release condition rather than showing an unexplained “pending.” If timing is estimated, distinguish estimate from guaranteed release date.

## Batch and Transfer
A payout may aggregate many orders. Let sellers traverse payout → component transactions and transaction → payout. Preserve batch identity, destination account summary, initiated time, processor/bank state, expected arrival, and final settlement evidence when available.

Failed or returned transfers need specific reasons and next action. Invalid bank details, closed account, verification hold, processor outage, and compliance review are not equivalent. Do not encourage repeated retries when the underlying condition has not changed.

## Disputes and Reversals
Show how refunds, disputes, chargebacks, or platform adjustments affect available balance and already-sent payouts. A negative balance should explain source events and recovery/offset rules. Avoid rewriting prior successful payout history when a later reversal occurs.

## Evidence
Test pending-to-available transition, fee calculation, payout batch, failed transfer, changed bank account, partial refund before payout, dispute after payout, reserve release, negative balance, and multi-currency seller. Reconcile UI totals to ledger/payment records.

## Failure Modes
- Buyer payment success is shown as seller payout complete.
- Net amount cannot be reconciled from components.
- Hold reason and release condition are hidden.
- Failed bank transfer offers retry without fixing destination.
- Later dispute edits historical payout amount rather than recording reversal.
- Currency conversion lacks rate/time evidence.

## Falsification
Take one order through payment, partial refund, payout, then dispute. Falsify if seller cannot trace every amount into a final net position or if the interface reports transferred funds before settlement evidence exists.

## Recovery
Reconcile from immutable ledger events, separate eligibility from transfer state, expose hold/failure reason, and append reversals rather than mutating history. If provider state is unavailable, mark payout transfer UNKNOWN rather than assuming completion from elapsed time.

## Handoff
Buyer dispute decisions come from `designing-marketplace-dispute-resolution`; seller verification gates from `designing-seller-onboarding`; order-level exceptions must reference their financial impact through canonical transaction IDs.

## Output Contract
Return a `marketplace-payout-status-contract` with `money_components[]`, `balance_states`, `eligibility_rules`, `payout_batch_model`, `transfer_states[]`, `failure_reasons[]`, `reversal_model`, `reconciliation_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.