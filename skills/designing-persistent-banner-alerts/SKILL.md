---
name: designing-persistent-banner-alerts
description: Use when an important condition must remain visible across a page or workspace until resolved, acknowledged, or expired by authoritative state rather than disappearing like transient feedback.
---

# Designing Persistent Banner Alerts

## Parent Contract
**Required parent:** `designing-notifications-and-interruptions`.

This faculty owns persistent attention surfaces for conditions that materially affect the current scope: degraded service, expired billing method, policy change, unsaved migration, account restriction, or security action required. A banner is not a substitute for a blocking dialog when work must stop immediately, nor for a notification center when the condition is not tied to the current context.

## Decision Boundary
Define the banner’s scope and exit condition first. Page-scoped, workspace-scoped, and account-wide alerts must not look identical if their consequences differ. Dismissal can mean “hide this informational message,” “acknowledge but condition remains,” or “condition resolved”; do not use one close icon for all three.

Prioritize when multiple banners compete. The product should not build a stack of unrelated warnings that permanently consumes the viewport. Security/safety conditions may outrank maintenance information, but severity must be grounded in consequence, not color choice. If an alert has a repair action, make the action specific and preserve context when navigating to the repair flow.

Persistent placement must coexist with sticky headers, mobile safe areas, zoom, and long localization. Do not push critical page content below multiple screens of banner text. The banner’s live-region behavior should announce new material changes without re-announcing on every route render.

## Failure Topology
- Dismissing an unresolved account restriction makes it vanish forever, leaving users confused when actions keep failing.
- Three banners stack with equal visual weight and obscure the actual product.
- “Fix now” navigates away without a return path to the blocked task.
- Banner is re-mounted on every route and screen readers hear the same alert repeatedly.
- A supposedly page-local warning appears globally because implementation shares one shell slot.
- Success resolution leaves a stale warning visible until manual refresh.

## Falsification and Recovery
Falsify with multiple concurrent conditions, route changes, mobile viewport, zoom, long translations, acknowledge-vs-resolve distinctions, repair flow completion in another tab, and screen-reader navigation. The design fails if the banner can be dismissed into contradiction with authoritative state or if users cannot identify the affected scope and repair path.

Recover by binding banner visibility to condition state, distinguishing acknowledge/hide/resolve, ranking alerts by consequence, limiting simultaneous presentation, preserving repair-return context, and synchronizing resolution across routes/tabs.

## Output Contract
Return `persistent-banner-alert-contract` with condition source, scope, severity basis, visibility lifecycle, acknowledgement/dismissal semantics, priority stacking, repair actions, route persistence, responsive placement, accessibility announcement policy, and falsification cases.