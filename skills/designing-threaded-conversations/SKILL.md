---
name: designing-threaded-conversations
description: Use when replies branch from a parent message or object and the interface must preserve conversational context, thread identity, unread state, collapse, navigation, and relationship to the main timeline.
---

# Designing Threaded Conversations

## Parent Contract
**Required parent:** `designing-chat-interfaces`.

This faculty owns reply-thread topology. It does not own the base chat timeline; it decides how a parent message, its replies, and the surrounding conversation remain connected without forcing every discussion into a flat stream or hiding important activity in side branches.

## Decision Boundary
Define what creates a thread and whether one level of replies is the maximum. Deep arbitrary nesting often destroys scanability; many products keep a single parent plus flat replies. Decide whether thread replies also appear in the main timeline, appear only as summaries, or remain isolated. The choice affects chronology, unread counts, search, and notification semantics.

Opening a thread must preserve the parent context and a route back to its location in the main conversation. If the parent is deleted or unavailable, the thread needs a tombstone policy rather than losing identity. Unread state should distinguish unread main-channel messages from unread thread replies; a global badge can aggregate them, but clearing one scope should not silently clear the other.

Thread previews need enough evidence—reply count, recent participants, last activity—to help users decide whether to enter, without leaking hidden reply content or overcrowding the timeline. Keyboard and screen-reader navigation should communicate parent/reply relationship explicitly.

## Failure Topology
- Replies are duplicated fully in main timeline and thread pane, causing users to read/send in two places without knowing canonical context.
- Thread reply increases a badge but there is no visible route to discover which thread changed.
- Deleting the parent makes replies unreachable even though they still exist.
- Nested reply controls create five levels of indentation on a narrow screen.
- Marking the channel read clears unread thread replies the user never opened.
- Thread panel closes and returns users to the top rather than the parent anchor.

## Falsification and Recovery
Falsify with hundreds of threads, deleted parent, permission-restricted replies, thread activity while reading the main timeline, narrow viewport, keyboard-only entry/exit, deep-link to a reply, and search result opening directly inside a thread. The design fails if parentage or unread ownership becomes ambiguous or if users cannot return from the branch to its main-context anchor.

Recover by enforcing a bounded thread model, defining main-timeline mirroring, separating unread scopes, preserving parent identity/tombstones, exposing active-thread discovery, and anchoring navigation between parent and thread.

## Output Contract
Return `threaded-conversation-contract` with thread creation rules, nesting limit, parent/reply identity, main-timeline mirroring, preview metadata, unread aggregation, deletion/tombstone policy, deep-link/navigation behavior, accessibility relationship semantics, and falsification cases.