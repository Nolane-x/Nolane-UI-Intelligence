---
name: designing-mentions-and-references
description: Use when users reference people, teams, objects, messages, or entities inside conversational text and the interface must resolve stable identity, suggestion scope, rendering, notification, permission, and broken-reference behavior.
---

# Designing Mentions and References

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns inline references that bind human-readable tokens to canonical entities. It does not own generic autocomplete or notification delivery. Its primary concern is preserving semantic identity when display names change, access differs, or referenced objects disappear.

## Decision Boundary
Define mentionable entity classes and trigger syntax. `@` may refer to people/teams; `#` may refer to channels/issues; rich editors may support object cards. Suggestions must be scoped by current membership and permission, not the entire organization directory. Ranking can use recent collaborators or exact matches but must not leak hidden entities through suggestions.

Store stable entity identity separately from rendered label. If “Mai Nguyen” renames to “Mai Tran,” old messages should display current or historical naming according to product policy without losing who was referenced. Pasted plain text that looks like a mention is not automatically a bound mention.

Notification semantics require explicit authority. Mentioning someone may trigger attention only if they can access the conversation and policy allows it; `@all`/team mentions need stronger friction, audience preview, or permission because their interruption radius is large. Deleted or permission-revoked references need safe tombstones rather than broken raw IDs.

## Failure Topology
- Autocomplete exposes names from a private team the sender cannot access.
- Mention is stored as display text, then breaks when the person changes name.
- Typing `@all` accidentally notifies thousands of users with no audience warning.
- Recipient gets a mention notification but cannot open the referenced conversation.
- Deleted object renders as a raw UUID.
- Keyboard selection inserts the wrong entity because suggestions reorder during async search.

## Falsification and Recovery
Falsify with duplicate display names, renamed users, hidden teams, revoked conversation access, deleted referenced objects, large audience mentions, keyboard/screen-reader suggestion use, slow asynchronous suggestions, and copy/paste between rich and plain-text surfaces. The design fails if a visible mention cannot be resolved to one stable authorized identity or if mentioning creates attention for users who cannot inspect the context.

Recover by storing canonical entity IDs, permission-filtering suggestions and notification recipients, stabilizing async result identity, adding large-audience friction, rendering safe tombstones, and separating bound references from look-alike text.

## Output Contract
Return `mention-reference-contract` with entity classes, trigger/input behavior, suggestion scope/ranking, stable identity representation, rename/deletion policy, notification eligibility, large-audience controls, permission handling, accessibility semantics, and falsification cases.