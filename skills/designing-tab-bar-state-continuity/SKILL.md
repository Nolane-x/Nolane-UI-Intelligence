---
name: designing-tab-bar-state-continuity
description: Use when persistent mobile tabs represent peer destinations that should preserve independent navigation, scroll, selection, badges, and task state across repeated switching.
---

# Designing Tab Bar State Continuity

## Parent Contract

**Required parent:** `designing-mobile-native-application-shells`.

This faculty owns continuity between top-level peer destinations represented by a native-style tab bar. It is not a generic tabs component and it does not own the internals of each child stack. The key question is what state a user expects to remain when they leave one top-level area and later return.

## Continuity decisions

Treat each persistent tab as a workspace with identity, not as a filter that swaps one panel. Record which state is independently retained per tab: child navigation stack, scroll anchor, query/filter, selected object, draft, media playback, badge/attention state, and last refresh time. Some state should survive tab switching but not process death; some may be durable; some must be revalidated whenever the tab becomes active.

Define re-selection behavior intentionally. On many mobile products, tapping the already-selected tab can pop to that tab's root, scroll the root to top, or do nothing. These are distinct commands and must not be guessed from framework defaults. If double-tap or long-press has a secondary meaning, it needs discoverable platform-consistent behavior and an accessible equivalent.

Badges are not state storage. A badge can summarize unread/attention debt, but opening a tab should not blindly clear server-side state unless the user's actual action satisfies the product's read/resolve semantics. Keep notification counts, route selection, and content freshness separate so switching tabs does not fabricate acknowledgment.

Deep links and notifications may target a child inside one tab. Decide whether the system activates the target tab and pushes into its existing stack, resets that stack, or constructs a bounded destination. Preserve other tabs unless product semantics require invalidation. If authentication or account/workspace scope changes, all child stacks may need coordinated reset because their objects belong to a different authority domain.

## Evidence

Use platform tab-navigation guidance, navigation-state traces, real long-running sessions, badge source semantics, accessibility focus observations, and task research showing whether people mentally model tabs as independent places. Test enough content to create meaningful scroll positions and nested histories; empty demo tabs hide continuity defects.

## Failure topology

Failures include every tab resetting to root on switch; the opposite extreme where stale nested routes survive an account change; reselect unexpectedly destroying a draft; badges disappearing merely because a tab became visible; deep links replacing another tab's history; and focus returning to the tab bar instead of a meaningful destination after programmatic activation.

Another failure is carrying one global filter or selected object across unrelated tabs because the implementation stores it at shell level. Shared state is correct only when the product concept itself is shared.

## Falsification

Build nontrivial state in at least three tabs: nested route plus scroll in one, draft/filter in another, unread badge in a third. Switch repeatedly, reselect current tab, enter from a notification/deep link, background/resume, change account or workspace, and restore after process recreation. The contract is falsified if state preservation cannot be explained per class, if tab switching acknowledges data accidentally, or if a scope change leaves a user inside an object from the previous scope.

## Recovery

Separate per-tab workspace state from shared application state. Make invalidation events explicit: logout, account switch, permission loss, object deletion, schema migration. For stale content, refresh underlying data while preserving safe local presentation state such as scroll anchor when possible. If re-selection commands are destructive to navigation depth, protect unsaved work before executing them.

## Output contract

Return a `tab-bar-state-continuity-contract` containing tab identities, retained state classes, invalidation events, re-selection semantics, badge rules, deep-link targeting, account/workspace reset behavior, accessibility focus expectations, lifecycle persistence, and a continuity test matrix.

## Handoffs

Route child history to `designing-native-navigation-stacks`, deep-link parsing to `designing-mobile-deep-link-routing`, restoration persistence to `designing-app-lifecycle-state-restoration`, message/unread semantics to the appropriate communication owner, and account scope changes to authentication/workspace lifecycle owners.