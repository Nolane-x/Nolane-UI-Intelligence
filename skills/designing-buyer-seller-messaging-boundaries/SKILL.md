---
name: designing-buyer-seller-messaging-boundaries
description: Use when buyers and sellers communicate inside a marketplace and the product must scope conversations to transactions, protect personal data, moderate abuse, preserve evidence, and distinguish messaging from formal support or dispute actions.
---

# Designing Buyer Seller Messaging Boundaries

Marketplace messaging connects parties who may not otherwise trust each other. The interface must help them coordinate legitimate transaction needs without exposing unnecessary contact information, enabling off-platform coercion, or confusing informal conversation with formal case actions.

## Parent Contract
**Required parent:** `designing-marketplace-operations`.

The parent owns marketplace party relationships. This skill owns buyer-seller conversation scope, identity/privacy, attachment rules, moderation hooks, and links into formal order/dispute workflows.

## Conversation Scope
Bind threads to a listing inquiry, order, item, shipment, return, or other explicit marketplace context. Keep that context visible so a user knows which transaction a message concerns. Do not merge multiple orders into one generic seller chat if policy, refunds, or evidence can differ by transaction.

Use marketplace identities according to privacy policy. Hide personal email/phone/address unless the transaction legitimately requires them and the platform permits disclosure. Detecting or preventing off-platform contact may be a policy feature, but do not distort ordinary messages without explaining enforcement where appropriate.

## Messaging Versus Formal Action
A seller writing “I'll refund you” is not the same as a refund event. A buyer saying “I want to return” is not necessarily a formal return request. Provide structured actions that can be launched from the conversation while keeping message evidence distinct from system state.

Attachments need type/size/safety constraints and sensitive-image handling. Preserve upload/receipt state and scan/moderation outcomes. Blocked attachments should not disappear in a way that makes the sender think the other party received them.

## Moderation and Safety
Support report, block/restrict where policy allows, abuse review, and platform intervention without destroying the transaction record. If a party is suspended, preserve access to necessary case evidence while preventing prohibited new contact.

## Evidence
Test pre-sale inquiry, active order, return discussion, harassment report, blocked contact details if policy applies, attachment rejection, seller suspension, dispute escalation, deleted listing, and multiple concurrent orders with one seller. Verify message and transaction identities stay aligned.

## Failure Modes
- Conversation loses the order/item context.
- Informal promise is rendered as completed marketplace action.
- Personal contact details leak through profile or notification preview.
- Attachment failure appears as sent.
- Blocking a user hides evidence needed for an open dispute.
- Report/moderation state is visible to the reported party when policy forbids it.

## Falsification
Have a buyer send a return request only as free text and a seller promise a refund. Falsify if the system updates formal order/refund state without a governed action. Then suspend the seller; falsify if the buyer loses necessary dispute evidence or can still initiate prohibited contact.

## Recovery
Rebind conversation to explicit transaction context, separate structured actions from messages, preserve evidential history under moderation rules, and redact personal data by policy. Unknown attachment/moderation delivery stays visibly unresolved.

## Handoff
Formal claims use `designing-marketplace-dispute-resolution`; order actions use order/fulfillment owners; general chat mechanics may reuse `designing-chat-interfaces` but marketplace policy and transaction boundaries remain here.

## Output Contract
Return a `buyer-seller-messaging-boundaries-contract` with `thread_context_types[]`, `identity_privacy_rules`, `formal_action_links[]`, `attachment_states`, `moderation_actions[]`, `suspension_behavior`, `evidence_retention`, `notification_privacy`, `falsification_cases[]`, and `recovery_actions[]`.