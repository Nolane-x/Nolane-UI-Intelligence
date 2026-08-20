---
name: designing-skip-navigation-mechanisms
description: Use when repeated shell content would otherwise force keyboard and assistive-technology users through the same controls before reaching the task region on every navigation.
---

# Designing Skip Navigation Mechanisms

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

This faculty owns bypass paths across repeated interface regions. It decides what can be skipped, where bypass controls land, when they become perceivable, and how those destinations survive responsive shells and route transitions. It does not replace landmark semantics or ordinary keyboard order; a skip mechanism is an explicit shortcut over repetition, not a patch for chaotic focus order.

## Decision Boundary
Map repeated blocks that occur before task content: global navigation, organization switchers, banners, persistent filters, or other shell controls. A skip destination must correspond to a meaningful next working point rather than an arbitrary container. Landing focus should make subsequent navigation predictable and should not leave the viewport visually somewhere else from the active focus target.

Choose persistence deliberately. A bypass link may be visually revealed on focus while remaining first in the logical order, but it must not be hidden using techniques that remove it from the accessibility tree. Multi-region applications may need more than one bypass path, such as “skip to results” and “skip to filters,” but only when each shortcut removes a material traversal cost. Route changes should rebind targets by stable semantic identity rather than fragile element position.

## Failure Topology
- The skip control points to a wrapper that is not focusable and focus silently stays at the top of the page.
- The target exists on desktop but disappears when navigation becomes a mobile drawer.
- A shortcut labeled “Skip to content” lands before another long repeated toolbar, defeating the bypass.
- Multiple skip links accumulate without a clear task model and become another menu users must decipher.
- Client-side navigation preserves focus on a stale element while the new skip destination belongs to the next route.
- CSS makes the control technically focusable but clipped, transparent, or covered when it appears.

## Falsification and Recovery
Start each representative route from the browser or application entry focus and operate keyboard-only. Measure the controls traversed with and without the bypass. Test zoom, narrow viewports, sticky headers, route transitions, modal dismissal, and pages with optional banners. The mechanism fails if activation does not move both logical focus and perceived viewport to the promised destination, or if a user must discover implementation-specific knowledge to know where it lands.

Recover by using stable destination anchors, restoring visible focus at the target, removing low-value bypasses, and defining responsive target substitutions explicitly. Re-test after shell changes because skip paths are coupled to repeated structure even though they are not owned by the visual shell.

## Output Contract
Return `skip-navigation-contract` with repeated regions eligible for bypass, shortcut labels, invocation order, destination identities, focus/scroll landing behavior, responsive substitutions, route-transition behavior, visibility requirements, and keyboard verification cases.
