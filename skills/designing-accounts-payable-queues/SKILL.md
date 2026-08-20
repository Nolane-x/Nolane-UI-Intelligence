---
name: designing-accounts-payable-queues
description: Use when this specialist's decision ownership is materially in scope. Own accounts-payable operational queues across vendor invoices, coding, duplicate detection, three-way evidence, approvals, holds, due dates, payment readiness, exceptions, and audit status.
---
# Designing Accounts Payable Queues

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the operational lifecycle of obligations owed to vendors before payment. Decide invoice intake state, vendor/entity identity, amount/currency/tax, coding, purchase-order/receipt matching where used, duplicate evidence, approval, hold/dispute, due/discount dates, payment-ready state, and exception prioritization. This owner does not execute bank transfers.

## Inputs and evidence

Require invoice identity/document, vendor master, entity, PO/receipt data, account/dimension coding, tax, payment terms, duplicate signals, approval policy, holds, due dates, currency, and payment-run integration. Identify OCR/extraction confidence and fraud-sensitive vendor changes.

## Procedure

Present a queue prioritized by operational risk—due, discount deadline, blocked exception, high value—not just arrival time. Extracted invoice fields show confidence and source-highlight for review. Duplicate signals compare vendor/invoice number/amount/date/document fingerprint without auto-rejecting legitimate repeats. Matching surfaces distinguish quantity/price/receipt differences. Coding and approvals operate on a stable invoice version; material changes invalidate approval. Hold/dispute states need owner/reason. Payment-ready means required validation/approval complete, not that payment occurred.

## Failure topology

Failures include duplicate invoice paid twice, OCR amount accepted with low confidence, approval surviving material vendor/bank change, hold reason invisible, due-date urgency hidden, and payment-ready mistaken for paid. Another failure is one queue mixing invoices across legal entities with insufficient context.

## Falsification

Reject if invoice/vendor/entity identity is ambiguous; if extraction confidence/source cannot be inspected; if duplicate evidence cannot be reviewed; if material changes do not invalidate approval; if held invoice can enter payment-ready silently; if status paid/payment-ready/pending are conflated; or if due/discount logic is unexplained.

## Output contract

Return an `accounts-payable-queues-contract` with: invoice/version identity; vendor/entity; amount/currency/tax; extraction confidence; duplicate checks; PO/receipt match; coding; approval; holds/disputes; due/discount dates; exception priority; payment-ready state; and audit lineage. Include one duplicate and one post-approval edit case.

## Handoffs

Expense review handles employee spend, journal/ledger records posting, approval workflows govern decisions, and financial transaction/payment systems handle actual disbursement.