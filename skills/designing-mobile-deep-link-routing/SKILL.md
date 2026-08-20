---
name: designing-mobile-deep-link-routing
description: Use when URLs, universal/app links, notifications, QR/NFC intents, or other external entries must resolve into valid mobile application state without bypassing identity, prerequisites, or navigation semantics.
---

# Designing Mobile Deep-Link Routing

## Parent Contract

**Required parent:** `designing-mobile-native-application-shells`.

Deep links own **external intent resolution**, not ordinary in-app navigation. This skill decides how an external target is parsed, authorized, canonicalized, deferred through prerequisites, and represented in the app's navigation hierarchy. It must never treat an incoming URL as trusted proof that the target is accessible.

## Intent resolution pipeline

Model deep linking as a pipeline: receive external intent → parse/canonicalize → classify target → establish account/workspace/tenant context → authenticate if required → check capability/permission/object existence → satisfy prerequisites → construct valid destination history → present result or truthful fallback. Preserve the original intent across gates without blindly replaying it after context changes.

Route identity must be stable across web and app representations where universal links are used, but the mobile app may need richer state than the URL carries. Resolve durable IDs against current authoritative data. Never embed sensitive mutable state into links just to recreate a screen. Expired invitations, revoked objects, wrong organizations, deleted content and versioned routes require explicit outcomes.

Cold and warm entry differ. On cold launch, dependency initialization may not be complete. On warm entry, the user may have a modal, draft or transaction in progress. Decide whether the new intent queues, asks before replacing an active task, opens within the existing stack, or creates a new task context. A notification tap should not silently destroy unsaved work merely because the OS delivered it while the app was active.

Security and privacy matter at the route boundary. Validate scheme/host/path, reject unexpected parameters, avoid open redirects and privilege escalation, and keep link previews/logging from exposing secrets. If a link selects an account or workspace different from the current scope, require a visible context transition rather than silently switching authority domains.

## Evidence

Use route schema, universal/app-link association config, notification payloads, auth/workspace models, server permission checks, analytics for failed links, and real OS launch tests. Include stale/expired links, malformed parameters, deleted targets, logged-out state, multi-account state, cold launch, warm foreground, background resume, and links received during an unsaved flow.

## Failure topology

Failures include a deep link that shows a detail page before auth state is known; a route that loads data from the current workspace even though the URL names another; a fallback that dumps users on home with no explanation; duplicated history because repeated links push the same destination; and links that work only after the app has previously initialized a feature module.

Another failure is cosmetic history fabrication: constructing parent screens with guessed filters just to make back navigation look natural. Those screens can imply a context the user never established.

## Falsification

Open every material link from installed/uninstalled transition where supported, cold/warm/background states, logged in/out, wrong account, expired permission, missing object, and while a draft is active. The contract is falsified if a target can bypass a gate, if the eventual destination changes identity from the original intent without disclosure, if back history contains invented context, or if failure leaves the user unable to recover the intended task.

## Recovery

Retain a normalized pending intent through necessary gates, but revalidate it after each authority-changing step. Provide targeted fallbacks: request access, switch account, choose replacement object, or explain expiry. Build history from real prerequisite destinations only. If the current task cannot be safely replaced, surface a choice and keep the external intent recoverable.

## Output contract

Return a `mobile-deep-link-routing-contract` with accepted link classes, parser/canonicalizer, target identity, prerequisite graph, auth/scope transitions, cold/warm handling, active-task conflict policy, invalid/stale outcomes, history construction, security checks, pending-intent lifetime, and end-to-end test cases.

## Handoffs

Use stack ownership for final history, authentication/permissions for gates, invitation/link-sharing owners for domain semantics, device QR/NFC owners for acquisition, and app restoration for delivery after termination. This skill remains accountable for preserving the original external intent across those handoffs.