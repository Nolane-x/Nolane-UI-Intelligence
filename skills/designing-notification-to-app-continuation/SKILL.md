---
name: designing-notification-to-app-continuation
description: Use when a notification, wearable alert, email deep link, or operating-system surface must continue into an application without losing task identity, authorization state, or the user's place in the work.
---

# Designing Notification-to-App Continuation

## Why this boundary exists
A notification is often only the first surface of a task. The dangerous simplification is to treat the tap as ordinary navigation. In reality the user may arrive from a stale alert, a different account, a locked device, a partially completed workflow, or a notification whose underlying object has changed. This skill owns the decision about how an external alert becomes a trustworthy in-app continuation rather than merely which route opens.

## Parent Contract
**Required parent:** `routing-ui-work`.

The parent decides that multi-surface continuity work is necessary. This specialist owns the continuation contract between a compact external signal and the richer application state that follows it. Generic deep-link routing owns URL or route resolution; this skill owns whether the resumed task still means what the notification claimed.

## Continuation model
Represent an alert handoff as `(notification-id, subject, account, task-intent, issued-state, arrival-state, authorization, continuation-target)`. The issued state is what was true when the notification was composed; the arrival state is what is true when the user opens it. Those states may differ materially.

The primary Decision is whether the app may continue directly, must refresh and reframe, must ask the user to choose context, or must refuse the continuation. A notification about “approve invoice 17” cannot silently open a generic invoice list after invoice 17 has already been paid; that destroys the user's causal model and can encourage duplicate action.

## State transitions and invariants
A continuation normally moves through `external-signal → identity-resolution → freshness-check → authorization-check → task-reconciliation → resumed | reframed | blocked`. The app must preserve the notification's intent long enough to explain any mismatch.

Invariants:
- the app never substitutes another account, tenant, patient, workspace, or document merely because it is currently active;
- stale notification state is visibly reconciled before an irreversible action is offered;
- dismissal of the notification does not imply task completion;
- a resumed task exposes enough context for the user to know why they arrived there;
- if the target no longer exists or is no longer actionable, the UI presents that fact rather than falling through to an unrelated default screen.

## Evidence that counts
Evidence includes replayable notification fixtures with issue timestamps, account and permission variations, screenshots or recordings of the issued alert and final destination, and traces showing freshness and authorization checks. Test at least one stale-object case, one account mismatch, one revoked-permission case, one already-completed task, and one notification opened after the app has been relaunched.

A successful route alone is insufficient Evidence. The proof must show that the semantic task survived the boundary.

## Failure topology
Characteristic Failure includes opening the right object under the wrong identity, acting on stale notification copy, landing on a generic home screen after a failed lookup, dropping an unsent reply that began from an alert, or allowing duplicate execution because the notification remains actionable after the server state changed. Another failure class is provenance loss: the app opens the task but no longer indicates the alert that initiated the context switch, making later recovery confusing.

## Falsification probes
Falsification deliberately changes reality between notification issue and tap. Complete the task on another device, revoke access, switch accounts, delete the target, mutate its status, expire the session, or open several notifications in reverse chronological order. The contract is falsified if any probe produces silent context substitution, stale action affordances, duplicate side effects, or an unexplained fallback destination.

## Recovery behavior
Recovery retains the original intent while discarding unsafe assumptions. Refresh authoritative state, re-resolve identity, and present a bounded explanation such as “This request was already approved” or “You no longer have access to this workspace.” If a safe adjacent destination exists, offer it as an explicit secondary choice rather than pretending it is the original continuation. Preserve draft text when the alert initiated composition and the user's input can still be safely associated with the intended subject.

## Output, Handoff, and consumers
Output: `notification-to-app-continuation-contract`, containing identity binding, freshness rules, reconciliation states, blocked-state copy obligations, continuation targets, and replay cases. Handoff route syntax to deep-link/navigation specialists, authentication repair to identity owners, and domain-specific action semantics to the task owner. Consumers should receive both the resolved target and the reason for any reframe.

## Sibling boundary and delete-the-skill test
Cross-device session handoff owns transfer of an active session between peer surfaces. Companion-surface authority owns which surface may act. Task-state preservation owns reconstructing longer-lived work. This skill alone owns the asymmetric transition from a compact, possibly stale notification into a semantically faithful in-app task.

Delete-the-skill test: if this skill disappears, a generic router can still open URLs, but no owner remains responsible for reconciling notification-time truth with app-arrival truth. That missing decision can cause wrong-account actions, stale approvals, duplicate side effects, and misleading destinations, so the skill is not a cosmetic variant.