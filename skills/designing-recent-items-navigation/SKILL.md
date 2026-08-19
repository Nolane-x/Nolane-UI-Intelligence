---
name: designing-recent-items-navigation
description: Use when a product exposes recently opened, edited, visited, or used objects as a fast return path and must define recency, privacy, deduplication, scope, and stale-item behavior.
---

# Designing Recent Items Navigation

## Parent Contract
**Required parent:** `designing-navigation`.

This faculty owns recency as a navigation accelerator. It does not own version history or audit logs: “recent” is about helping a user return to an object, not proving what changed. The product must define which interaction earns recency and whose activity contributes.

## Decision Model
Choose the recency event deliberately: opened, meaningfully viewed, edited, executed, or explicitly pinned. Mouse hover or accidental preload must not promote an item. Define scope—device, account, workspace, organization—and whether private/incognito contexts are excluded. A shared workspace should not silently mix colleagues’ activity into a personal “Recent” list unless the feature is explicitly team activity.

Order should usually be stable by most recent qualifying event, with repeated access deduplicating rather than creating multiple copies. Pins/favorites are a different intent signal and should not be disguised as recency; if both coexist, separate them visually and behaviorally.

Stale objects need graceful treatment. Renamed items should resolve by identity, not old label. Deleted, moved, revoked, or archived objects should disappear or explain unavailability according to privacy policy. Never leak a title or path after the user loses permission merely because it exists in local history.

## Failure Topology
- Prefetched objects appear in Recent despite never being opened.
- A permission-revoked document title remains visible and leaks sensitive context.
- Recent list duplicates the same object after every visit.
- Sorting by “recently modified” is labeled “recently viewed,” confusing different event semantics.
- Workspace switching shows objects from the wrong tenant with no scope cue.
- Clearing history only hides UI while local cache continues restoring entries.

## Falsification and Recovery
Falsify with rename, move, deletion, permission revocation, workspace switch, offline cache, private browsing mode, repeated opening of one item, cross-device sync, and a user clearing history. The design fails if an entry cannot be explained by a qualifying event or if an inaccessible object leaks identifying metadata.

Recover by recording stable object IDs plus explicit recency event type, scoping storage correctly, deduplicating on identity, enforcing permission at render time, defining clear-history semantics across local/remote storage, and separating pins from automatic recency.

## Output Contract
Return `recent-items-navigation-contract` with qualifying events, scope, ordering/deduplication, object identity, pin/favorite separation, rename/move handling, permission/deletion policy, sync/cache behavior, clear-history semantics, privacy boundaries, and falsification cases.