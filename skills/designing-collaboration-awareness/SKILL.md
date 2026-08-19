---
name: designing-collaboration-awareness
description: Use when collaborators need a compact understanding of meaningful recent shared activity—who changed, commented, reviewed, or joined—without turning raw event telemetry into an overwhelming audit log.
---

# Designing Collaboration Awareness

## Parent Contract
**Required parent:** `designing-collaboration-and-presence`.

This faculty owns ambient awareness of meaningful shared activity. It differs from live presence, which answers who is here now; notification centers, which hold personal attention debt; and audit logs, which preserve authoritative historical evidence. Awareness helps collaborators form a current mental model of what changed around them without requiring forensic completeness.

## Decision Boundary
Choose events by collaborative relevance, not by whatever telemetry is easiest to emit. Examples include significant edits, comments, review requests, resolved feedback, new collaborators, ownership changes, or a branch/version becoming current. Cursor movements, every autosave, and every keystroke usually create noise rather than awareness.

Aggregate events into human-meaningful statements while preserving attribution and scope. “Mai edited 12 fields in Customer A” can be more useful than twelve separate entries; “3 people made 47 changes” may be too compressed when the changed areas differ materially. Define time windows, grouping keys, and a route from summary to supporting context.

Awareness has freshness but not necessarily permanence. A “since you were away” summary can expire after being consumed, while important activity may remain discoverable through history/audit systems. Respect permission boundaries at render time: losing access to an object must also remove its sensitive activity details from awareness summaries.

## Failure Topology
- Every autosave generates an activity item and meaningful collaborator actions disappear in noise.
- Aggregation says “5 updates” but offers no way to learn what areas changed.
- Awareness feed is treated as an audit log even though events are sampled, grouped, and expire.
- User sees the title of a private document they can no longer access because an old activity card cached it.
- Live presence and historical activity share identical avatars/status styling, so “here now” and “acted yesterday” are confused.
- New activity continually inserts above the viewport and moves content while the user is reading a summary.

## Falsification and Recovery
Falsify with hundreds of low-level edits, a few high-impact ownership changes, permission revocation, returning after a week, simultaneous comments/reviews, object rename/deletion, keyboard/screen-reader navigation, and real-time arrivals while reading older awareness. The design fails if users cannot distinguish current presence from historical activity or if summaries claim completeness that the event source does not guarantee.

Recover by defining relevance thresholds, semantic grouping keys, explicit freshness/completeness bounds, stable insertion behavior, permission-filtered rendering, and deep links to authoritative context when more detail is needed.

## Output Contract
Return `collaboration-awareness-contract` with eligible event classes, aggregation rules, attribution, time/freshness model, scope, summary-to-detail navigation, permission/redaction behavior, distinction from presence/notifications/audit, insertion policy, accessibility semantics, and falsification cases.