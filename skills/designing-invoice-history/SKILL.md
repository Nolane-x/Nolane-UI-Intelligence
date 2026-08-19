---
name: designing-invoice-history
description: Use when users inspect historical charges and documents and the interface must represent invoice identity, period, amount, tax, status, payment relationship, credit/refund adjustments and downloadable evidence accurately.
---

# Designing Invoice History

## Parent Contract
**Required parent:** `designing-subscription-management`.

This faculty owns invoice-list/detail interaction. It does not perform accounting, tax calculation or certify document validity beyond authoritative billing records.

## Decision Boundary
Each invoice needs a stable invoice number/ID, issue date, billing/service period where applicable, currency, subtotal/tax/total, status and relationship to payments/credits. “Paid,” “Open,” “Void,” “Uncollectible” or equivalent states come from the billing system; do not reduce them all to a green/red receipt icon.

History views should support scanning and retrieval by date, status, amount/currency and invoice identifier. Multi-entity products must show billing account/organization scope. Download links need document type (invoice, receipt, credit note) and availability; a receipt proving payment is not the same artifact as an invoice.

Adjustments matter. Refunds, credits and corrected invoices may not rewrite the original document. Show linked adjustment documents/events so historical totals remain explainable. If an invoice was voided/reissued, preserve the relationship rather than disappearing the old record.

Currency and tax formatting must reflect invoice facts, not current locale conversions. Do not convert historical amounts into today’s account currency unless explicitly shown as a separate informational conversion.

Large histories need pagination/search without losing chronological context. Accessibility requires structured tabular/list semantics and descriptive download/action labels, not identical “Download PDF” links with no invoice context.

## Failure Topology
- Refund changes original invoice total retroactively and audit history no longer matches issued document.
- “Receipt” and “Invoice” are used interchangeably.
- Organization admin downloads the wrong entity’s invoice because tenant scope is hidden.
- Historical USD invoice is displayed in EUR using current account currency.
- Multiple `Download` links have indistinguishable accessible names.
- Failed/open invoice disappears after later successful payment rather than showing settlement relation.

## Falsification and Recovery
Falsify with paid/open/voided invoices, partial refunds, credit notes, reissued documents, multiple currencies/entities and missing documents. Reconcile list/detail/download metadata to authoritative billing records.

Recover by preserving immutable invoice identity, linking adjustments/payments, keeping document types distinct, locking historical currency/tax facts and adding scoped retrieval/action labels.

## Output Contract
Return `invoice-history-contract` with invoice identity/status, dates/period, monetary/tax fields, billing scope, payment/credit/refund links, document types/download behavior, search/pagination, accessibility and accounting-record parity tests.