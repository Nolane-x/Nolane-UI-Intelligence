---
name: designing-message-reactions
description: Use when users can attach lightweight emoji or symbolic acknowledgements to messages and the UI must coordinate identity, counts, toggling, picker access, aggregation, permissions, and social meaning without replacing substantive replies.
---

# Designing Message Reactions

## Parent Contract
**Required parent:** `designing-chat-interfaces`.

This faculty owns lightweight structured acknowledgement attached to a message. It does not own comments, review outcomes, or workflow approvals. Reactions are intentionally low-friction social signals; products should not silently reinterpret them as formal decisions unless a separate domain contract explicitly defines that mapping.

## Decision Boundary
Define the reaction vocabulary and whether arbitrary emoji are allowed. A small curated set can provide stable semantics; a full emoji picker maximizes expression but creates localization, rendering, and moderation considerations. Toggling the same reaction should add/remove the current user’s membership rather than create duplicate entries.

Counts need provenance. The visible aggregate should make it possible, when appropriate, to inspect who reacted without exposing hidden participants or inaccessible accounts. Grouping variants that look similar but have different Unicode sequences may require normalization policy. Do not reorder reaction chips continuously by count if that makes click targets move under the pointer.

Reaction creation and removal should be optimistic only when the server can reconcile by user+message+reaction identity. If permissions change or a message is deleted, remove or disable reaction controls predictably. Keyboard and touch users need a discoverable picker path; hover-only “add reaction” buttons are insufficient.

## Failure Topology
- Clicking the same emoji twice creates two copies instead of toggling membership.
- Reaction chips reorder on every incoming event and users accidentally activate the wrong one.
- Tooltip leaks names of participants the viewer should not be able to identify.
- Full emoji picker is reachable only on mouse hover.
- Optimistic reaction remains visible after server rejection with no correction.
- Product treats 👍 as an approval decision even though users understand it as acknowledgement.

## Falsification and Recovery
Falsify with rapid add/remove, two devices for the same account, large group counts, permission changes, deleted messages, custom emoji removal, keyboard-only picker, touch, screen readers, and server rejection of optimistic updates. The design fails if aggregate counts cannot reconcile to unique participants or if reaction meaning is overloaded into a high-stakes workflow without explicit policy.

Recover by keying reactions on stable user/message/value identity, normalizing allowed values, stabilizing chip order, bounding identity disclosure, providing non-hover invocation, reconciling optimistic state, and keeping formal decisions in dedicated workflow owners.

## Output Contract
Return `message-reaction-contract` with allowed vocabulary, toggle identity, aggregation/count rules, participant disclosure, ordering, picker invocation, optimistic reconciliation, permission/deletion behavior, accessibility semantics, and falsification cases.