---
name: designing-global-navigation-shells
description: Use when a product needs a persistent top-level navigation frame that establishes scope, primary destinations, account/workspace context, and orientation across routes.
---

# Designing Global Navigation Shells

## Parent Contract
**Required parent:** `designing-navigation`.

This faculty owns the persistent navigation shell shared across major product areas. It does not decide the complete information architecture or every local navigation pattern. Its job is to make top-level scope, current context, global actions, and escape routes stable enough that users can orient after any deep link.

## Decision Boundary
Start from destination classes, not visual chrome. Separate product-level destinations, workspace or organization switching, global search/command access, account controls, and transient contextual actions. A global shell becomes incoherent when route-local commands migrate into it merely because space is available.

Define persistence by surface. On wide screens the shell may remain visible; on compact screens the same ownership may be re-authored into a tab bar, header, drawer trigger, or compact switcher. Responsive change must preserve destination reachability and current-location evidence rather than blindly collapsing all items behind a hamburger.

Current state should survive deep linking. A user landing directly on `/projects/abc/settings` should see which product area and workspace they inhabit without visiting a home page first. If the shell carries a workspace selector, switching contexts needs explicit consequences for the current route and unsaved work.

## Failure Topology
- Global navigation mixes destinations with page-local actions, so items change unpredictably between screens.
- Workspace switching silently drops the user onto an unrelated default route.
- Mobile collapse removes a destination rather than rehoming it.
- Active-state styling follows URL prefixes incorrectly and highlights two top-level sections.
- A deep link hides product context, leaving users unable to answer where they are.
- Global shell height or density expands per page and causes layout instability.

## Falsification and Recovery
Falsify with deep links, unauthorized destinations, workspace switching from nested routes, compact viewport, browser back/forward, keyboard traversal, long localized labels, and a product area with no direct shell item. The design fails if top-level orientation depends on having followed a particular path from home or if a destination becomes unreachable after responsive transformation.

Recover by separating stable destination taxonomy from contextual commands, declaring context-switch routing policy, deriving active state from canonical route ownership, preserving reachability across breakpoints, and giving deep links the same orientation evidence as in-app navigation.

## Output Contract
Return `global-navigation-shell-contract` with destination classes, persistent regions, context selectors, active-state rules, deep-link orientation, responsive re-authoring, context-switch consequences, keyboard/focus behavior, permission handling, and falsification routes.