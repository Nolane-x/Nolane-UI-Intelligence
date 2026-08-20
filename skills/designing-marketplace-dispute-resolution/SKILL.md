---
name: designing-marketplace-dispute-resolution
description: Use when buyers and sellers contest delivery, condition, payment, return, refund, or policy outcomes and the marketplace must collect evidence, preserve timelines, support responses, adjudicate, and communicate enforceable resolutions.
---

# Designing Marketplace Dispute Resolution

A dispute is a governed case with competing claims. The interface must preserve each party's evidence and deadlines while making the platform's adjudication role explicit and preventing support conversation from replacing formal case state.

## Parent Contract
**Required parent:** `designing-marketplace-operations`.

The parent owns marketplace entities and responsibility. This skill owns dispute case creation, evidence, response windows, escalation, decision, remedy, and appeal/review where supported.

## Case Scope
Bind the dispute to exact transaction entities: order, item, shipment, payment/refund, seller, buyer, and relevant policy version. A single order can contain undisputed items; do not freeze unrelated funds or fulfillment without policy authority.

Capture structured claim category plus free-form narrative and evidence. Categories might include not received, not as described, damaged, unauthorized, return not acknowledged, refund missing, or seller policy violation. Categories should route the case, not predetermine outcome.

## Procedural Fairness
Show each party what is alleged, what response/evidence is requested, deadline, what happens after no response, and which information is visible to the other party. Preserve submission receipts. If the platform adds evidence from carrier/payment systems, distinguish that source from party-submitted material.

Moderators/adjudicators need a timeline and decision options tied to policy. Avoid exposing internal risk signals to parties unless authorized. High-impact remedies—refund, chargeback response, payout reversal, seller penalty—should show scope before final decision.

## Decision and Enforcement
Separate decision from execution. A refund decision can be final while payment processor execution is still pending. Communicate the remedy, amount, affected item, funds movement, seller consequence, and appeal/review route when applicable.

## Evidence
Test buyer claim, seller response, missing response deadline, contradictory carrier evidence, partial refund, adjudication reversal, payout already released, and processor failure after decision. Verify immutable case timeline and party-specific visibility.

## Failure Modes
- Chat messages are treated as formal evidence without source/timestamp binding.
- Dispute on one item freezes unrelated order components.
- Party cannot tell whether evidence was received before deadline.
- Decision status is shown as refund-complete before funds move.
- Internal fraud/risk data leak through dispute explanation.
- Appeal erases the first decision instead of adding a review layer.

## Falsification
Resolve a partial-item dispute in favor of the buyer while the seller payout is already partly released. Falsify if the UI cannot represent decision versus enforcement state or if unrelated items/funds are affected.

## Recovery
Re-scope the case, reconstruct immutable evidence/timeline, separate decision from financial execution, and expose pending enforcement. Where evidence visibility is restricted, state that additional protected evidence was considered without leaking its contents.

## Handoff
Order/shipment exceptions route from `designing-order-exception-management`; seller financial consequences use `designing-marketplace-payout-status`; party communication boundaries use `designing-buyer-seller-messaging-boundaries`.

## Output Contract
Return a `marketplace-dispute-resolution-contract` with `case_binding`, `claim_categories[]`, `party_evidence_rules`, `response_deadlines`, `protected_evidence_boundary`, `adjudication_states[]`, `remedy_execution_states[]`, `appeal_lineage`, `evidence_cases[]`, and `recovery_actions[]`.