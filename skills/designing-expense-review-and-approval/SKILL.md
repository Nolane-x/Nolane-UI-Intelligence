---
name: designing-expense-review-and-approval
description: Use when this specialist's decision ownership is materially in scope. Own employee or card expense review across receipt evidence, merchant/date/amount, category, policy, allocation, duplicates, personal/non-reimbursable flags, approval, reimbursement readiness, and audit.
---
# Designing Expense Review and Approval

## Parent Contract

**Required parent:** `designing-financial-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own operational review of expense claims/transactions before accounting or reimbursement. Decide receipt/document linkage, extracted fields, expense category, business purpose, dimensions, policy checks, duplicate detection, personal/non-reimbursable treatment, approval, exceptions, and reimbursement-ready state. This owner does not send reimbursement payments.

## Inputs and evidence

Require expense/card transaction identity, claimant, entity, merchant/date/amount/currency, receipt, extraction confidence, category/tax, project/cost allocation, policy rules, duplicate signals, approvers, reimbursement method, and audit retention. Identify split expenses and missing-receipt exceptions.

## Procedure

Keep imported transaction and submitted claim distinct but linkable. Extracted values show confidence/source. Policy findings state specific rule and whether blocking/advisory. Splits must reconcile to total across categories/projects. Missing receipt or out-of-policy exceptions capture rationale and required authority. Duplicate detection compares card/import/claim sources. Approval binds to exact claim version; material changes trigger re-review. "Approved" differs from "posted" and "reimbursed" and must not be collapsed.

## Failure topology

Failures include low-confidence OCR accepted silently, split lines not summing to total, personal expense coded as reimbursable, duplicate card and manual claim both paid, approval remaining after amount change, and approved shown as reimbursed. Another failure is reviewers seeing unnecessary personal details beyond policy need.

## Falsification

Reject if total/split cannot reconcile; if receipt/extraction evidence is unavailable; if policy exception lacks rule/rationale/authority; if duplicate source cannot be reviewed; if material edit preserves approval; if lifecycle states are conflated; or if privacy-sensitive detail exceeds reviewer need.

## Output contract

Return an `expense-review-and-approval-contract` with: transaction/claim identity; claimant/entity; amount/currency/date; receipt/extraction; category/dimensions/splits; policy findings; duplicate checks; personal/non-reimbursable state; exception; approval binding; posting/reimbursement handoffs; and audit. Include one duplicate-card/manual claim case.

## Handoffs

Accounts payable or reimbursement payment handles disbursement, journal/ledger handles posting, approval workflows provide decision mechanics, and privacy owners govern sensitive claimant data.