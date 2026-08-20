---
name: designing-native-navigation-stacks
description: Use when mobile navigation is represented as push/pop history with platform back behavior, nested stacks, modal routes, restoration, and transition-specific ownership.
---

# Designing Native Navigation Stacks

## Parent Contract

**Required parent:** `designing-mobile-native-application-shells`.

This skill owns ordered screen history and the semantics of moving deeper, back, replacing, resetting, or presenting a route outside the ordinary hierarchy. Generic information architecture defines destinations; this owner defines how a mobile stack represents the user's traversal and how platform back conventions interact with that history.

## Decision model

Model a stack as semantic route entries, not screenshots. Each entry needs route identity, stable parameters, ownership of child state, restoration policy, and whether it represents a new task level or merely a presentation state. Distinguish push, replace, pop, pop-to, reset, modal presentation, nested navigator handoff, and external exit. Using the same animation for several operations does not make their history semantics equivalent.

Decide where stack boundaries live. A tab commonly owns an independent child stack; authentication may temporarily replace the application graph; a checkout or creation wizard may be a bounded task flow with explicit exit behavior. Avoid one global stack that accidentally preserves private or irrelevant routes across context switches. Conversely, duplicating the same object route in several unmanaged stacks can cause inconsistent editing state and surprising back destinations.

Back is a product promise. On platforms with system back gestures/buttons, the visible route hierarchy must predict what back will do. Interactive back gestures need cancellation semantics: if the gesture is abandoned midway, focus, scroll, selection, media and draft state must remain on the current route. If a destructive or unsaved boundary changes normal back behavior, intercept only when there is real user value and explain the consequence; do not turn every screen into a confirmation trap.

Nested stacks require explicit context transfer. Parent and child navigators must agree on object identity, authentication state, result delivery, and whether returning should refresh or preserve the previous scene. Route parameters are not a substitute for durable application state; large mutable objects passed as navigation state can become stale copies.

## Evidence

Inspect platform navigation guidance, route graph, nested navigator configuration, real back-gesture behavior, accessibility focus after transitions, restoration logs, and analytics for abandoned/backtracked flows. Test with repeated pushes of the same route type, deep nesting, cross-tab entry, authentication changes, notification/deep-link entry, and modal-on-stack combinations.

## Failure topology

Typical failures include a back button that returns to an unrelated tab; duplicate detail screens piling up because selection always pushes; a replace operation presented as if the prior screen still exists; interactive back that discards a draft before commit; nested stacks that each think they own the same modal; and restoration that recreates historical routes whose underlying objects no longer exist.

A subtle failure occurs when app-header back and system back diverge. Another occurs when an external deep link constructs a stack with fake predecessor screens solely to make the back button look normal, even though those screens were never visited and may have unmet prerequisites.

## Falsification

Start the same destination from home, another tab, a notification, a deep link, a search result and a restored session. Repeatedly navigate into the same object, switch tabs, open/close modal routes, cancel an interactive back gesture, then trigger process recreation. The navigation contract fails if history cannot be predicted from visible context, if a canceled gesture mutates state, if back exposes inaccessible/stale routes, or if focus lands on an unrelated element after return.

## Recovery

Repair by defining route identity and stack ownership first. Collapse accidental duplicates, use replace/reset only when history is truly invalidated, rebuild a deep-linked stack from valid task prerequisites rather than cosmetic history, and restore product state before route presentation. Where a result must return to a parent, pass a stable result or refresh signal instead of an entire stale screen model.

## Output contract

Return a `native-navigation-stacks-contract` with route-entry schema, stack boundaries, operation semantics, back policy, nested-stack rules, modal relationship, duplicate-route policy, restoration rules, focus/scroll continuity, deep-link construction rules, unsaved-change exceptions, and adversarial navigation scenarios.

## Handoffs

Use `designing-tab-bar-state-continuity` for peer destination stacks, `designing-mobile-deep-link-routing` for external route construction, `designing-app-lifecycle-state-restoration` for process recreation, generic `designing-navigation` for information architecture, and task-specific owners for wizard/checkout flows. Handoff to accessibility focus owners when transition focus cannot be proven.