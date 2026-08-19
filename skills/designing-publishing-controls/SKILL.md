---
name: designing-publishing-controls
description: Use when draft content crosses into an externally visible or otherwise committed published state and the UI must make authority, destination, validation, review evidence, side effects, and reversibility explicit.
---

# Designing Publishing Controls

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns the commitment boundary between draft/private content and a published state. It does not own the editor, preview, or editorial review process itself. Publishing is a consequence-bearing action because it can expose content, notify audiences, invalidate caches, trigger integrations, or alter canonical URLs.

## Decision Architecture
Define what “Publish” means for the product: become publicly visible, become visible to an internal audience, replace a currently published revision, push to selected channels, or create a new release. Show the destination and audience before commitment. If multiple channels can be published independently, do not use one ambiguous button unless its scope is visible and reviewable.

Gate on authoritative prerequisites. Required fields, content validity, permissions, approval state where policy demands it, schedule conflicts, and destination availability should be checked near commitment. Do not require every advisory quality suggestion to pass as though it were a hard publishing rule. Separate blockers, warnings, and optional recommendations.

Publishing state needs transaction semantics: submitting, accepted, propagating, published, partially published, failed, or outcome unknown after timeout. Disable duplicate submission or use release identity/idempotency. If unpublish/revert exists, explain whether caches, notifications, syndication, or already-delivered content can actually be withdrawn.

## Failure Topology
- Button says Save but actually publishes externally.
- Publishing to three channels partially succeeds and the UI reports one global success.
- User lacks publish authority but discovers that only after completing the final modal.
- Timeout triggers retry and creates two releases or duplicate notifications.
- “Unpublish” implies full removal although emails/social syndication cannot be recalled.
- Advisory SEO warning blocks a safety-critical internal announcement even though it is not a true prerequisite.

## Falsification and Recovery
Falsify with multiple destinations, stale approval, permission revoked before commit, publish timeout with unknown outcome, partial channel failure, replacement of an existing published revision, unpublish after external syndication, keyboard/screen-reader confirmation, and preview revision differing from the commit revision. The design fails if users cannot identify the exact revision, destination, audience, and side effects being committed.

Recover by binding publish to revision identity, separating blockers/warnings, checking current authority, previewing destination/audience, using release transaction IDs, representing partial outcomes per channel, and describing rollback limits truthfully.

## Output Contract
Return `publishing-control-contract` with publish definition, revision/destination/audience scope, prerequisite gates, blocker/warning policy, commit labeling, transaction states, idempotency, partial outcomes, unpublish/revert limits, accessibility confirmation, and falsification cases.