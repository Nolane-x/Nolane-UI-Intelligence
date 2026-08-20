---
name: designing-journal-entry-workflows
description: Own creation, validation, approval, posting, reversal, and correction of journal entries with balanced lines, dimensions, period/entity controls, attachments, and immutable audit history.
---
# Designing Journal Entry Workflows

## Decision ownership

Own operational entry of accounting journals. Decide header/line model, debit-credit balance validation, account/dimension selection, currency, effective/posting date, attachments/evidence, draft/submit/approve/post states, recurring/template usage, reversal/correction, and closed-period behavior. This owner does not decide accounting treatment; it prevents invalid or unauditable postings.

## Inputs and evidence

Require entity, fiscal periods, accounts, dimensions, currency rules, line limits, balancing policy, approval roles, posting permissions, close/lock state, supporting-document requirements, recurring journal policy, and reversal methods. Identify intercompany or multi-currency journals requiring extra controls.

## Procedure

Keep entity and posting period visible while editing. Lines show account, debit/credit or signed amount, currency where applicable, dimensions, description, and validation. Continuously show total debits/credits and imbalance without blocking intermediate entry. Draft can be incomplete; submit requires balanced and policy-complete data. Approval binds to a specific immutable journal version. Posting produces a durable journal/ledger identity. Corrections after posting use reversal/adjusting entry under policy rather than editing history. Closed periods block or route to controlled exception with effective date/rationale.

## Failure topology

Failures include approving a journal then editing lines before posting, hidden imbalance due rounding/currency, selecting accounts valid for another entity, posting to closed period, attachment requirements discovered after approval, and editing posted entries in place. Another failure is copy-from-template carrying stale date/dimensions unnoticed.

## Falsification

Reject if approval does not bind to exact journal contents; if submit can hide an imbalance; if entity/period/account eligibility is not validated; if posted lines can mutate invisibly; if closed-period exception lacks authority/rationale; or if reversal cannot trace to original journal.

## Output contract

Return a `journal-entry-workflows-contract` with: journal/version identity; entity/period/date; line schema; balance calculation; dimensions/currency; draft validation; submit/approval/post states; evidence attachments; template/recurring safeguards; closed-period policy; reversal/correction lineage; and audit history. Include one post-approval edit invalidation case.

## Handoffs

General ledger consumes posted entries, approval workflows supply decision mechanics, chart of accounts validates accounts, and period/financial operations root supplies lock authority.