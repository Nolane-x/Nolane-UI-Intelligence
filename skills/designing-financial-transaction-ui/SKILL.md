---
name: designing-financial-transaction-ui
description: Use when a UI moves money, trades assets, pays bills, changes payment destinations, authorizes charges, commits financial terms, or performs other transactions where recipient, amount, fees, timing, and reversibility matter.
---

# Designing Financial Transaction UI

## Overview
Financial UI must make the economic action unambiguous before commit and durable afterward. Verify recipient/source/amount/fees/timing, resist confusion and duplicate actions, and provide a clear receipt, status, and dispute/recovery model.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require transaction type, authorization, reversibility/settlement, fraud/security controls, fees/rates, recipient identity, timing, regulatory obligations, and failure states. Pair high-consequence commits with `designing-high-stakes-decisions`.

## Decision Model
Model the transaction as intent → details → validation → authorization → commit → pending/settlement → receipt → reversal/dispute where possible. Keep draft and committed state visually distinct. A spinner after commit must not invite repeated submission; use idempotency and explicit pending state.

Before commit show meaningful identity: recipient/account plus disambiguating attributes appropriate to privacy, source account, amount/currency, fees, exchange rate when relevant, schedule/timing, recurring status, and whether the action can be cancelled. Do not hide a material fee or changed amount behind the final button.

Treat edits as invalidating assumptions. If recipient, amount, funding source, or price changes, re-evaluate required verification/authorization. For market transactions, separate quoted/estimated values from executable price and expose expiration/slippage semantics where product rules require them.

After commit provide a durable reference with status and what the user can do next. Pending does not mean completed. Failures must state whether money moved, whether retry is safe, and how to resolve uncertainty. Never recommend blind retry when state is unknown.

## Evidence
Test recipient confusion pairs, currency/locale formats, fee and rate changes, duplicate taps, network loss at commit, session reauth, pending-to-complete transitions, scheduled/recurring edits, accessibility, dispute/reversal, and account switching. Security/financial domain requirements remain external authority.

## Output Contract
Return a `financial-transaction-contract` with `transaction_states`, `identity_fields[]`, `amount_currency_rules`, `fees_rates_timing`, `precommit_summary`, `authorization`, `idempotency_and_duplicate_protection`, `pending_unknown_behavior`, `receipt`, `reversal_dispute`, and `transaction_tests[]`.

## Failure Traps
- Recipient shown only as avatar/first name.
- Fee appears after commitment.
- “Success” shown before settlement/acceptance is known.
- Retry button when prior submission status is unknown.
- Currency symbol without locale/currency disambiguation.
- Editing amount after authorization without re-evaluating risk.
- Destructive red styling substituted for actual consequence detail.

The user should be able to reconstruct exactly what financial action they authorized from the UI and receipt.

## V6 Financial Transaction Integrity
Treat **amount-currency identity** as inseparable: decimal precision, locale format, currency code/symbol ambiguity, converted amount, and source account must remain explicit. Time **fee-rate disclosure timing** before commitment, including spread, network/processing fees, exchange rate timestamp, taxes, and conditions that can change.

Perform **beneficiary verification** appropriate to risk: identity/name, destination/account, institution/network, saved-recipient provenance, and changed-recipient warnings. Mark the **irreversible settlement boundary** where cancellation/undo ceases to be possible. Issue a durable **reconciliation receipt** with transaction identifier, authoritative status, amounts/fees, parties, timestamps, and next steps for pending/failed states.

### Falsification
Change currency/account/beneficiary immediately before submission, delay exchange-rate refresh, and simulate duplicate/retried payment. If the UI can show a misleading final total or duplicate settlement, it fails.

### Recovery
Invalidate stale quotes, stop ambiguous retries, restore review with changed fields highlighted, and route disputes/failures through transaction truth rather than generic error copy.
