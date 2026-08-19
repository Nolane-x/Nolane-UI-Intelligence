---
name: designing-payment-failure-recovery
description: Use when a payment or renewal fails and the interface must distinguish recoverable decline, authentication, expired method, processor outage, retry schedule and entitlement impact without exposing sensitive or misleading processor details.
---

# Designing Payment Failure Recovery

## Parent Contract
**Required parent:** `designing-financial-transaction-ui`.

This faculty owns post-failure customer recovery for commercial payment. It does not diagnose card networks beyond authoritative processor signals or define dunning/grace policy.

## Decision Boundary
Translate payment outcomes into actionable user states without inventing reasons. The processor may provide categories such as authentication required, insufficient funds/decline, expired method, invalid details, temporary processor error or unsupported method. Some decline reasons intentionally remain generic; do not guess a sensitive cause from opaque codes.

Separate **payment state** from **subscription entitlement state**. A failed renewal may enter grace while service continues; another product may suspend immediately. Show current access and the deadline/next retry derived from billing policy. Do not make a red “Payment failed” banner imply data loss if no such consequence exists.

Recovery paths depend on failure class: retry, authenticate, update payment method, choose another method, contact bank, wait for automated retry, or contact support. Prevent repeated manual retries when the system is already processing or when rate/network policy makes them harmful.

Updating a default payment method can affect multiple invoices/subscriptions; scope the change. If an outstanding invoice must be paid separately after method update, explain that updating the card is not itself payment completion.

Sensitive data and processor messages require careful display. Never echo full payment credentials. Preserve transaction/invoice identifiers for support without showing raw internal error dumps.

## Failure Topology
- UI says “insufficient funds” based on a generic processor decline that did not reveal that reason.
- User updates card and banner disappears although the outstanding invoice remains unpaid.
- Repeated Retry creates duplicate payment attempts because request state is not idempotent.
- Service access is shown as suspended during a real grace period.
- Failure banner has no invoice/amount/scope context for organizations with several subscriptions.
- Processor outage prompts users to replace a perfectly valid card.

## Falsification and Recovery
Falsify with authentication-required, generic decline, expired card, temporary outage, grace period, automated retry, manual retry race and payment-method update. Reconcile visible recovery state to processor/billing events.

Recover by mapping only authoritative failure categories, separating method update from invoice settlement, exposing current entitlement/retry schedule and guarding duplicate attempts.

## Output Contract
Return `payment-failure-recovery-contract` with failure class/source, affected invoice/subscription, current entitlement, retry state/schedule, allowed recovery actions, payment-method scope, sensitive-message policy, idempotency feedback and failure-path tests.