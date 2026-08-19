---
name: designing-conversation-search
description: Use when users search within one or many conversations and results must preserve message context, author/time scope, thread location, permissions, highlighting, and jump-to-message behavior.
---

# Designing Conversation Search

## Parent Contract
**Required parent:** `designing-chat-interfaces`.

This faculty owns retrieval inside conversational history. It does not own the general search platform; its special obligation is reconstructing enough temporal and thread context around a matched message that users can understand and navigate to it without losing chronology.

## Decision Model
Define search scope visibly: current conversation, current thread, all channels in a workspace, direct messages, or an authorized subset. Author, date range, attachment/type, and channel can be structured refinements when the domain supports them. Do not search hidden or departed spaces merely because an index still contains their content.

A result should identify conversation/thread, author, timestamp, matched excerpt, and enough surrounding text or parent context to disambiguate. Highlight only the evidence that truly matched. When a user activates a result, load the target message plus surrounding history and anchor it stably; “jump to message” must not land at the newest message because the target was outside the initially loaded window.

Deleted, edited, or retention-expired messages create drift. Search indexes must not surface stale content users can no longer inspect. If indexing is delayed, disclose scope/freshness rather than claiming exhaustive results. Search query should remain recoverable after opening a result so users can return to the result set.

## Failure Topology
- Result shows matching text but not which channel/thread it came from.
- Jump loads conversation bottom and target message is nowhere in view.
- Search result exposes a deleted message still present in an index.
- Permission revocation removes route access but snippet remains visible.
- Edited message result highlights text that no longer exists.
- Opening one result clears query/filter state and makes comparison impossible.

## Falsification and Recovery
Falsify with deep historical matches, thread replies, deleted/edited messages, retention expiry, permission changes, indexing lag, duplicate text across channels, keyboard navigation, screen-reader result context, and browser Back after jumping to a match. The design fails if users cannot reconstruct the matched message’s conversational context or if index visibility exceeds current authorization.

Recover by permission-filtering at query and render time, including stable conversation/message IDs, loading context windows around targets, invalidating stale index entries, preserving query state, and labeling freshness/coverage limits.

## Output Contract
Return `conversation-search-contract` with searchable scopes, refinements, result schema, match/context highlighting, permission/index freshness rules, thread identity, jump-to-message anchoring, deleted/edited handling, query-return behavior, accessibility semantics, and falsification cases.