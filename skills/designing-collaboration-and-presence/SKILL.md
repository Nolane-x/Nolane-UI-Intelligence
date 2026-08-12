---
name: designing-collaboration-and-presence
description: Use when multiple people view, edit, comment, review, approve, assign, or coordinate in shared artifacts and the UI must represent presence, authorship, permissions, concurrent change, conflict, and notifications.
---

# Designing Collaboration and Presence

## Overview
Collaboration UI makes shared state and authorship legible without turning every coworker into visual noise. Distinguish who is present, what they are doing, what changed, and where conflict or authority actually matters.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require collaboration model (realtime/asynchronous), artifact granularity, roles/permissions, conflict semantics, offline behavior, comments/review states, notification channels, and privacy/presence policy.

## Decision Model
Separate **presence** from **activity** and **authorship**. Online status alone does not tell whether a person is viewing the same object, selecting a paragraph, editing a field, or merely connected. Reveal the minimum useful granularity. In sensitive work, presence itself may be private.

For concurrent editing, give remote selections/cursors stable identity but cap visual clutter. Changes require attribution and temporal order at the granularity users need to reason about them. If the system merges automatically, define what happens for semantic conflicts even when text merge is technically possible.

Permissions are visible at the point of action. Users should understand whether they can view/comment/edit/approve/share and who owns the final decision. Request/approval workflows must not look like edits already took effect.

Design offline and reconnect. Local edits need queued/synced/conflicted state; a reconnect should not silently overwrite newer shared work. Comments, suggestions, tasks, and approvals have different state machines — avoid one generic “activity” feed.

Notification strategy follows collaboration urgency. Mention, assignment, approval request, conflict, and ambient edit have different interruption budgets. Provide digest/batching and durable inbox/history so users do not rely on transient toasts.

## Evidence
Test simultaneous edits to same/different regions, permission changes during edit, offline edits/reconnect, comment resolution, approval/rejection, shared link audience, presence privacy, notification bursts, user rename/avatar change, and accessibility of remote change announcements.

## Output Contract
Return a `collaboration-contract` with `presence_levels`, `authorship_model`, `remote_selection_rules`, `concurrent_edit_model`, `conflict_resolution`, `role_permission_map`, `review_approval_states`, `offline_sync`, `activity_types[]`, `notification_policy`, and `collaboration_tests[]`.

## Failure Traps
- Green dot treated as proof someone is viewing the same object.
- Rainbow of cursors obscuring content with no prioritization.
- Offline reconnect silently last-write-wins.
- Suggested change visually identical to committed edit.
- Presence exposing sensitive attendance/activity unexpectedly.
- Every edit sending a push notification.
- Activity feed as the only way to recover what changed.

Collaboration is clear when people can answer “who changed what, is it committed, and what needs my attention?” quickly.