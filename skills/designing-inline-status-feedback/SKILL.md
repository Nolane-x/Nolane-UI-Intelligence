---
name: designing-inline-status-feedback
description: Use when status belongs next to the object or control it describes and must remain causally attached through pending, success, warning, and failure states without becoming notification chrome.
---

# Designing Inline Status Feedback

## Parent Contract
**Required parent:** `designing-notifications-and-interruptions`.

This faculty owns feedback colocated with the affected object: a saved-state label beside an editor title, upload status in a file row, sync warning beside a device, or validation result near a control. It differs from toast feedback because location, not transience, is the primary carrier of causality.

## Decision Boundary
Place status where users naturally inspect the affected thing. Decide whether it describes the object, the latest operation, or a persistent condition; those states must not be collapsed. “Saved” is an operation outcome, while “Offline” is an environment condition. If both matter, the interface needs a precedence or composition model rather than one label that flips ambiguously.

Inline status should reserve enough layout stability that common transitions do not cause surrounding controls to jump. Icons may supplement text, but color and icon alone are weak evidence for warnings or failures. If a status contains a repair action, it must remain present until resolved or explicitly dismissed according to consequence.

Status freshness matters. Do not let an old success label survive a new edit or an out-of-order async response. When multiple operations affect the same row, associate feedback with operation identity so completion of an earlier request does not overwrite a newer pending state.

## Failure Topology
- “Saved” remains visible after new unsaved edits begin.
- Status text replaces an object label and users lose identity context.
- A row jumps horizontally as “Uploading…” becomes “Failed—retry,” moving adjacent destructive controls.
- Failure uses only a red dot with no accessible name or repair explanation.
- Old request completion overwrites the status of a newer operation.
- Persistent warning is dismissed by a generic toast timeout because both use one notification system.

## Falsification and Recovery
Falsify with rapid repeated operations on one object, reordered network responses, long localized status text, narrow tables, screen-reader reading order, status plus repair action, and a persistent condition coexisting with transient operation progress. The design fails if the visible status cannot be tied unambiguously to an object and a current state source.

Recover by separating condition from operation state, keying updates by object/operation revision, reserving layout space, keeping identity labels intact, adding explicit repair actions for durable failures, and using semantic text plus appropriate live announcements.

## Output Contract
Return `inline-status-feedback-contract` with status ownership, state sources, precedence/composition rules, object/operation identity, placement, layout-stability policy, stale-response protection, repair actions, accessibility semantics, and falsification cases.