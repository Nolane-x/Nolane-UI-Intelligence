---
name: designing-chat-interfaces
description: Use when a product needs real-time or asynchronous conversational messaging and must coordinate identity, chronology, composer, delivery, unread state, history, presence, and failure without reducing chat to bubbles.
---

# Designing Chat Interfaces

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns the conversational container: participants, timeline, chronology, message grouping, unread boundary, composer relationship, and navigation through conversation state. Specialized children own delivery receipts, reactions, attachments, and other message-level protocols.

## Decision Architecture
Define the conversation identity and participant model first. One-to-one, group, channel, support thread, room, and object-scoped chat have different membership and history semantics. A message timeline must clarify sender, timestamp context, ordering, and whether history is complete. Do not visually group messages so aggressively that author/time evidence disappears when it matters.

Chronology needs a stable policy. New messages may arrive while the user is reading older history; avoid snapping to bottom unless the user is already anchored at the latest edge. Preserve an unread separator and make “jump to latest” explicit. Loading older history should prepend without moving the currently read message.

Composer state must bind to the active conversation and survive reasonable context changes according to product promise. Switching rooms with an unfinished draft should not accidentally send it elsewhere. Membership changes, deleted conversations, moderation, and permission loss need terminal states rather than silent composer failure.

## Failure Topology
- Incoming message forces scroll to bottom while the user is reading earlier context.
- Switching conversation carries the previous room’s draft into the new room.
- Aggressive bubble grouping hides which user authored a sequence after membership changes.
- History pagination prepends items and shifts the viewport by hundreds of pixels.
- User loses send permission but composer remains active until submission fails.
- Unread badge clears merely because the conversation route opened, although unread messages are below the viewport.

## Falsification and Recovery
Falsify with rapid incoming traffic, reading far above latest, reconnect after offline send, membership changes, deleted messages, long localized content, keyboard/screen-reader navigation, conversation switching with drafts, and loading older history. The design fails if chronology cannot be reconstructed or if a message can be composed/sent under the wrong conversation identity.

Recover by anchoring scroll to message IDs, separating route-open from read position, scoping drafts by conversation, tracking membership/permission in real time, preserving author/time context, and delegating specialized message states to dedicated child contracts.

## Output Contract
Return `chat-interface-contract` with conversation identity, participant/membership model, timeline chronology, grouping, history loading, scroll anchoring, unread boundary, composer binding, draft scope, permission/deletion states, accessibility navigation, and falsification cases.