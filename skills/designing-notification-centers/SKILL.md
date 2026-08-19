---
name: designing-notification-centers
description: Use when a product needs a durable cross-session inbox of attention-worthy events with read state, grouping, retention, actions, preferences, and trustworthy object context.
---

# Designing Notification Centers

## Parent Contract
**Required parent:** `designing-notifications-and-interruptions`.

This faculty owns durable notification history. Unlike toast feedback, a notification center stores attention debt so users can return later. It does not replace operational inboxes whose items are assignable work; notifications report events or required attention but are not automatically workflow records.

## Decision Architecture
Define what earns durable storage. Mentions, approval outcomes, security events, task completions, invitations, billing failures, and system changes may qualify; trivial local successes usually do not. Each notification needs stable identity, event time, actor/source, affected object, destination, read/unread semantics, and permission-safe rendering.

Read state is not the same as handled state. Opening the center may mark items seen, but automatically declaring them resolved can hide unfinished attention. If the domain needs action completion, store a separate status or route to the workflow owner. Group repeated events only when aggregation preserves important actors, counts, and timestamps.

Retention and pagination must be explicit. Notification counts should reflect the same scope as the visible list. A badge saying “12” cannot mean unread account-wide while the panel only displays current-workspace items without explanation. When the referenced object is deleted or access is revoked, render a safe tombstone or remove the item according to privacy requirements.

## Failure Topology
- Opening the panel marks every notification “done” even though required actions remain.
- Badge count and panel scope use different definitions.
- Repeated notifications flood the list because identical events never aggregate.
- Aggregation hides a security-relevant actor or most recent timestamp.
- Permission loss leaves sensitive titles or snippets visible in old notifications.
- Clicking an old event navigates to a missing object with no contextual explanation.

## Falsification and Recovery
Falsify with hundreds of events, multi-workspace scope, permission changes, deleted objects, repeated mentions, notification preference changes, read state synchronized across devices, keyboard/screen-reader navigation, and stale deep links. The design fails if durable attention can disappear merely by being viewed or if notification metadata bypasses current permission rules.

Recover by defining event eligibility, separating seen/read/handled states, aligning badge and list scope, aggregating by semantic event key, rechecking object permissions at render/open time, and providing safe tombstones and destination failure states.

## Output Contract
Return `notification-center-contract` with event classes, notification identity/schema, retention, scope, seen/read/handled state, badge semantics, grouping, destination/action behavior, permission/tombstone handling, preference handoff, accessibility behavior, and falsification cases.