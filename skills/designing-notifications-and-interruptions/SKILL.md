---
name: designing-notifications-and-interruptions
description: Use when a product sends push, desktop, in-app, wearable, email-like, alert, badge, toast, or escalation signals that compete for attention or require users to return to work later.
---

# Designing Notifications and Interruptions

## Overview
A notification spends user attention. Assign interruption level from consequence and timing, not from what a feature team wants noticed, and provide a durable place for important items after the transient signal disappears.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require event types, urgency, decay over time, required response, channel availability, quiet-hours policy, user roles, privacy, and whether missing the event creates harm. Safety-critical alarms also route to human factors.

## Decision Model
Create an event taxonomy: **critical immediate**, **time-sensitive**, **action-needed but deferrable**, **informational**, **ambient/history-only**. Choose channel and persistence accordingly. Push/wearable/audio are high interruption; badge/inbox/digest are lower. Do not map every event to every channel.

Define aggregation. Ten comments on one thread are usually one summary, not ten pushes. Repeated sensor/monitor changes need stateful escalation instead of notification spam. Set deduplication, cooldown, bundling, escalation, and decay semantics. A notification should become stale or resolved when its underlying issue changes.

Make actions precise. A toast can confirm an operation the user just performed; it should not be the only place to recover a critical task. Persistent notification center/inbox/history supports missed items. Deep links restore enough context to act and handle expired permissions/data gracefully.

Privacy changes channel content. Lock-screen/watch previews may reveal sensitive information; allow redaction or generic wording while preserving urgency. Respect system notification permission and user category preferences without repeatedly nagging denial.

## Evidence
Test burst events, repeated same event, quiet hours, role changes, stale/deleted target deep links, lock-screen privacy, notification permission denial, wearable mirroring, timezone, accessibility announcements, and whether users can find missed actionable events later. For critical alerts, validate prioritization under realistic workload.

## Output Contract
Return an `interruption-contract` with `event_taxonomy[]`, `urgency_rules`, `channel_map`, `aggregation_rules`, `deduplication`, `escalation`, `decay_resolution`, `actionability`, `durable_inbox`, `privacy_redaction`, `user_preferences`, and `notification_tests[]`.

## Failure Traps
- Push notification for every background change.
- Badge count that can never reach zero because resolved items remain.
- Toast containing the only recovery link.
- Notification deep link opening a generic homepage.
- Sensitive message text exposed on lock screen by default.
- Re-prompting OS notification permission after denial.
- Critical and promotional alerts sharing the same sound/style.

Notifications should help users allocate attention, not convert product activity into a demand for attention.