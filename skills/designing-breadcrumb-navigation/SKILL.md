---
name: designing-breadcrumb-navigation
description: Use when users need compact hierarchical orientation and ancestor navigation through nested content, routes, or objects without confusing history with structure.
---

# Designing Breadcrumb Navigation

## Parent Contract
**Required parent:** `designing-navigation`.

This faculty owns structural ancestry trails. Breadcrumbs answer “where is this within the product hierarchy?”; they are not browser history, a generic back button, or a second copy of every navigation level. The parent information architecture remains authoritative for what counts as an ancestor.

## Decision Boundary
Construct crumbs from stable semantic hierarchy, not merely URL segments. Technical routes often contain IDs, modes, or implementation nesting that users should never see. Decide whether the current page is represented as the final non-link item, whether the root is product home or a narrower workspace, and how object names are resolved when they are long, mutable, or temporarily unavailable.

Breadcrumb compression must preserve orientation. On narrow surfaces, collapsing middle ancestors into an overflow menu is usually safer than dropping the root or immediate parent. Truncation needs a way to inspect the full label. If a hierarchy can have multiple parents, declare the canonical path for the current context rather than presenting a misleading universal ancestry.

Navigation consequences matter when there is unsaved work. Clicking an ancestor is a normal navigation action and inherits route-leave safeguards; breadcrumbs do not bypass them because they look lightweight.

## Failure Topology
- Breadcrumbs mirror raw URL segments such as UUIDs and internal route names.
- A history-like trail changes based on the path used to arrive, so deep links show no useful ancestry.
- Current page is a link to itself and creates ambiguous keyboard behavior.
- Responsive layout removes the immediate parent, the most useful recovery target.
- Renaming an object leaves stale breadcrumb text or breaks route identity.
- Multiple-parent content presents a path that implies false ownership.

## Falsification and Recovery
Falsify with direct deep links, object rename, missing/deleted ancestor, multiple-parent placement, very long localized labels, narrow viewport, keyboard traversal, screen-reader landmarks, and unsaved changes followed by ancestor activation. The design fails if a breadcrumb cannot be regenerated from current structural context alone or if it exposes implementation topology as user hierarchy.

Recover by deriving from semantic ancestry IDs, resolving human labels independently, defining a canonical contextual path, preserving root/immediate-parent under compression, marking the current item correctly, and routing navigation through normal leave protections.

## Output Contract
Return `breadcrumb-navigation-contract` with ancestry source, root definition, current-item semantics, label resolution, multi-parent policy, responsive compression, truncation behavior, navigation safeguards, accessibility semantics, missing-ancestor handling, and falsification routes.