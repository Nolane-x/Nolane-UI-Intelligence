---
name: designing-assignment-and-ownership
description: Use when responsibility for work can move among people, teams or automated actors and the interface must distinguish accountable owner, assignee, collaborator, watcher and queue membership with clear transfer consequences.
---

# Designing Assignment and Ownership

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns user-facing responsibility assignment semantics. It does not define organization roles/permissions or queue ordering.

## Decision Boundary
Name the responsibility model before drawing an avatar picker. Some products have one accountable owner; others allow multiple assignees, team ownership plus individual handler, rotating on-call responsibility, or unassigned queue membership. Do not use the word “owner” casually if it implies legal/account authority elsewhere.

Assignment changes should expose consequence: notifications, SLA responsibility, access changes, workload accounting, auto-routing override or task visibility. A simple avatar replacement can hide a material transfer. If reassignment requires acceptance, model `offered → accepted|declined|expired` rather than claiming ownership immediately.

Search/select controls should show enough identity to avoid collisions—name, team, role, location or email where appropriate—and should respect eligibility. Disabled/ineligible candidates need reasons when users reasonably expect them to be selectable.

Concurrent assignment requires authoritative conflict handling. If two managers assign different people at the same time, the UI must reconcile to the actual final owner and preserve history. Do not let stale tabs silently overwrite newer assignment.

Bulk assignment should communicate exact scope and whether current owners are replaced, added or left on in another role. Automated routing may reassign later; label auto-assignment vs manual override and how long the override persists.

## Failure Topology
- “Owner” picker actually changes only notification recipient while users assume accountability transferred.
- Team and individual assignment are shown in the same chip with no distinction.
- User assigns someone who lacks access; the item disappears for that assignee and remains unresolved.
- Two stale tabs alternate ownership without conflict notice.
- Bulk assign silently replaces secondary collaborators as well as primary owner.
- Automatic router immediately overwrites a manual assignment with no visible policy.

## Falsification and Recovery
Falsify with unassigned → user, team → user, reassignment acceptance, ineligible target, permission change, concurrent edits, bulk assignment and auto-routing override. Trace current accountability and historical transitions. If users cannot answer “who is responsible now, and why?”, the design fails.

Recover by formalizing responsibility roles, exposing transfer effects, validating eligibility at commit, versioning assignment changes and distinguishing manual/automatic source.

## Output Contract
Return `assignment-ownership-contract` with responsibility roles, eligible target model, assignment/transfer state machine, consequence disclosure, concurrency/version handling, bulk semantics, automation override policy, history and responsibility tests.