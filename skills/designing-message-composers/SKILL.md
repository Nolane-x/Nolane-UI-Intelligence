---
name: designing-message-composers
description: Use when conversational text entry needs draft persistence, multiline behavior, shortcuts, rich input, send boundaries, editing context, and safe handoff to attachment or mention systems.
---

# Designing Message Composers

## Parent Contract
**Required parent:** `designing-chat-interfaces`.

This faculty owns the state of composing a message before send. It does not own message delivery, attachments, or mention resolution; those are separate protocols. The composer must make it impossible to confuse draft text, editing an existing message, replying in a thread, and sending to a different conversation.

## Decision Model
Define send semantics by modality and audience. Enter-to-send may serve keyboard-heavy chat, but multiline content needs a discoverable newline path and settings may alter the shortcut. On touch, a visible Send action is usually primary. Never let IME composition completion trigger an accidental send.

Drafts should be scoped by conversation/thread identity and preserved according to product promise. If the user begins editing a sent message, represent that mode explicitly and give a route to cancel without losing the prior unsent draft. Reply context, quote context, and thread target should be visible near the composer so the user can verify where the message will land.

Rich input—emoji, formatting, slash commands, mentions—must not turn the text area into an inaccessible custom editor unless necessary. Character limits need to communicate how rich entities count. Disable Send only for reasons users can understand; if permission changes, explain the disabled state instead of silently consuming the draft.

## Failure Topology
- Pressing Enter during IME candidate selection sends an incomplete message.
- Switching channels sends a draft into the newly selected channel because composer state is global.
- Editing a sent message overwrites the unsent draft with no recovery.
- Reply target is hidden above the viewport and users answer the wrong thread.
- Character count treats a mention token inconsistently between client and server.
- Permission loss disables Send with no explanation and users copy text manually to avoid losing it.

## Falsification and Recovery
Falsify with IME composition, multiline paste, long draft, conversation switch, edit/cancel, reply/thread mode, screen readers, keyboard shortcut customization, permission change while typing, and reconnection after draft persistence. The design fails if send destination or message mode cannot be verified immediately before submission or if ordinary navigation destroys valuable draft state unexpectedly.

Recover by scoping drafts to conversation identity, separating compose/edit/reply modes, guarding IME events, making destination context visible, preserving drafts through permission/connectivity changes, and delegating rich entity/attachment behavior to dedicated contracts.

## Output Contract
Return `message-composer-contract` with draft identity, send/newline shortcuts, IME handling, compose/edit/reply modes, destination context, rich-input boundaries, character-limit semantics, permission state, draft persistence, accessibility behavior, and falsification cases.