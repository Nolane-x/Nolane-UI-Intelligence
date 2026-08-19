---
name: designing-operational-inboxes
description: Use when incoming messages, alerts, requests or tasks arrive as a stream that users must notice, inspect and resolve, and the interface must distinguish unread, unresolved, assigned, snoozed and completed state.
---

# Designing Operational Inboxes

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns inbox-style arrival and resolution semantics for operational work. It does not own notification delivery channels, general work-queue prioritization or case lifecycle after an item becomes a larger managed case.

## Decision Boundary
An operational inbox is a **stream of actionable arrivals with attention state**, not merely a list sorted by newest. Model each item with stable identity, arrival/update timestamps, unread/read, unresolved/resolved, optional assignee/owner, priority, snooze/defer state and source/thread relationship. Reading an item must not automatically mean the underlying work is resolved unless the product explicitly equates them.

Define what causes an item to reappear. New activity on a resolved thread may reopen, create a new unread marker, or stay in history depending on domain semantics. Snoozing should specify whether updates wake the item early. Archived/closed items need a reachable history path when accountability matters.

Counts must state what they count. `12` can mean unread, unassigned, unresolved, due soon or total arrivals; badge meaning should be stable across navigation. If tabs or views partition inbox state, avoid double counting the same item without clear explanation.

Scanning needs information scent: source, subject/object, latest meaningful change, age, priority and responsibility. Do not fill every row with badges; encode only state that changes action. Keyboard workflows should support rapid next/previous, open, resolve, assign and return to list without losing position.

Real-time arrivals require stability. New items should not constantly jump under the pointer or reorder the item being read. Offer a “new items” insertion boundary or stable sort policy when live churn is high.

## Failure Topology
- Opening an item marks it “done,” causing unread/read to masquerade as work completion.
- Inbox badge counts unread while the page headline says unresolved, creating contradictory numbers.
- New arrivals reorder the list continuously and users click the wrong row.
- A resolved thread receives new activity but remains hidden with no wake-up policy.
- Snoozed items disappear permanently after timezone or clock changes.
- Keyboard next/previous loses the current filter and returns users to a different work set.

## Falsification and Recovery
Falsify with new arrival while reading, reply to resolved thread, snooze + update, assignment change, duplicate source events, live reorder, keyboard-only triage and large unread counts. Reconstruct an item’s attention/work state from the UI. If read/unread and resolved/unresolved cannot be independently identified, the model fails.

Recover by separating attention state from work state, stabilizing count semantics, defining wake/reopen rules and buffering live insertion so current interaction remains stable.

## Output Contract
Return `operational-inbox-contract` with item state algebra, arrival/update policy, read-vs-resolution semantics, count definitions, snooze/reopen behavior, live-insertion stability, scan information, keyboard flow and state-transition tests.