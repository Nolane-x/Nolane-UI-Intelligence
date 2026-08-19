---
name: designing-editorial-status-workflows
description: Use when content moves through drafting, review, revision, ready, scheduled, published, archived, or other editorial states and the interface must make transitions, owners, prerequisites, and version meaning explicit.
---

# Designing Editorial Status Workflows

## Parent Contract
**Required parent:** `designing-task-flows`.

This faculty owns the lifecycle status of a content item before and after release. It does not own comments/review mechanics, formal approval policy, or the publish transaction. Editorial status provides shared workflow meaning such as Draft, In review, Changes requested, Ready, Scheduled, Published, or Archived, but each label needs a precise state contract.

## Decision Architecture
Define statuses from work meaning rather than UI color. For each state, specify who can enter it, required evidence, allowed edits, downstream actions, and exits. Avoid status proliferation where every team habit becomes a new enum; use assignment, due date, review result, and flags as separate dimensions when they are not true lifecycle states.

Status and revision must relate explicitly. If a Published item is edited, does the same item become Draft while the published revision remains live, or does it contain a live revision plus an unpublished working revision? A single label cannot represent both without additional state. Similarly, “Ready” should identify readiness for what destination or action when multiple channels exist.

Transitions need concurrency protection. Another editor can change state while the user is viewing stale information. High-impact transitions such as archive, withdraw, or mark-ready should verify current revision/status before commit. Automated transitions—publish succeeded, schedule failed, review requested—must be visible as system-caused events rather than unexplained status jumps.

## Failure Topology
- “Published” switches to “Draft” after any edit, making users think the live page disappeared even though old revision remains public.
- Team creates twelve near-identical statuses to encode assignee and priority.
- Marking “Ready” is allowed while required review findings remain unresolved under policy.
- Stale browser changes status from In review to Draft and overwrites a newer Scheduled state.
- Automatic schedule failure leaves content labeled Scheduled indefinitely.
- Status color is the only indication and screen-reader users cannot determine workflow state.

## Falsification and Recovery
Falsify with simultaneous editors, published-plus-draft revision, review reopened, schedule failure, archive/unarchive, role restrictions, multi-channel readiness, browser back/refresh, and accessibility navigation. The design fails if one status label must carry several independent workflow dimensions or if status transitions can ignore current revision and authority.

Recover by keeping lifecycle state minimal, separating orthogonal metadata, modeling live versus working revisions, defining transition guards and owners, reconciling automated events, and exposing status text plus history independently of color.

## Output Contract
Return `editorial-status-workflow-contract` with state vocabulary, transition graph, transition authority, prerequisites, revision relationship, orthogonal metadata boundaries, automated transitions, stale-write protection, history/accessibility representation, and falsification cases.