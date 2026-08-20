---
name: designing-agent-background-task-surfaces
description: Design persistent surfaces for agent work that continues after the initiating view is left, with durable status, notifications, return paths, and resource control.
---

# Designing agent background task surfaces

Long agent jobs should not require users to keep a chat tab open. Use this skill when tasks can continue in the background, survive navigation, or complete asynchronously through external jobs.

## Decision ownership

Own backgrounding triggers, task identity, persistence, notification policy, return/navigation, pause/cancel controls, expiry, and relation between foreground conversation and durable task record. Decide which tasks may outlive a session.

## Inputs and evidence

Collect task durations, external job semantics, app/session lifecycle, notification permissions, device switching, resource cost, stale-task behavior, and user follow-up needs. Identify tasks that continue server-side even if the client disconnects.

## Procedure

Give each background task a stable identity, title, owner, start time, current state, and originating context. Allow users to leave without losing progress. Provide a task center or equivalent where active, blocked, failed, and completed jobs can be found.

Notify only on meaningful transitions: completion, failure requiring attention, or permission/blocking request. Deep-link notifications back to the exact task. Define cleanup/retention for old tasks and what happens when original context is deleted or permission expires.

## Failure topology

Background work can become invisible and continue consuming cost. Notifications without return context create confusion. Another failure is showing a task as cancelled locally while an external job still runs.

Tasks may also complete against stale context after the project changed.

## Falsification

Background tasks, close the client, switch devices, revoke permission, modify source context, and return later. Verify durable state and external-job truth. Test notification deep links and cancelled/expired states.

## Output contract

Produce an `agent-background-task-surfaces-contract` defining task identity, persistence, lifecycle states, task-center representation, notifications, deep links, cancellation, stale-context handling, retention, and cross-session tests.

## Handoffs

Use `designing-agent-action-progress` for progress, `designing-agent-interruption-and-cancel` for control, `designing-agent-partial-completion` for final mixed outcomes, and notification-center skills for cross-product delivery.