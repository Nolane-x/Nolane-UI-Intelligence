---
name: designing-app-lifecycle-state-restoration
description: Use when a mobile app may be backgrounded, killed, reclaimed, upgraded, or recreated and must restore only state that remains valid, safe, and comprehensible.
---

# Designing App Lifecycle State Restoration

## Parent Contract

**Required parent:** `designing-mobile-native-application-shells`.

This specialist owns what the application reconstructs after lifecycle interruption or process recreation. It is deliberately narrower than navigation persistence: a restored route is useful only when its product objects, identity, permissions, drafts and transactional state remain authoritative.

## Restoration classes

Inventory state by restoration semantics rather than storage API. **Authoritative durable state** should be reloaded from its source. **Recoverable local work** such as a draft may be persisted with revision/context metadata. **Presentation continuity** such as scroll or expanded panels can be restored when the underlying object version still matches. **Ephemeral capability state** such as an open camera session, permission prompt, socket, biometric challenge or transient animation must be reacquired, not serialized. **Sensitive state** may need deliberate non-persistence or encrypted/short-lived storage.

Define a restoration key that includes the authority context needed to decide whether saved state is still applicable: user/account, workspace or patient/project identity, object ID/revision, app/schema version, and timestamp where staleness matters. Do not restore a draft from one account into another because both routes have the same component name.

Restoration is a reconciliation operation. On resume/recreation, compare saved intent with current server/platform truth. An order may have completed while the process was gone; a permission may have been revoked; a message may now be deleted; a clinical encounter may be closed. Presentation must be rebuilt from current truth plus compatible local work, not from a serialized visual tree.

For long operations, distinguish **work continuing outside the UI** from **UI work that stopped with the process**. Background upload/task systems need stable operation identifiers so restored UI can query real status instead of restarting and duplicating side effects.

## Evidence

Use lifecycle traces, kill/relaunch tests, OS process-death simulation, persisted-state schema, migration tests, authentication/account-switch scenarios, offline/online transitions, long-running operation IDs, and privacy classifications. Capture before-interruption state and post-restoration authoritative data for comparison.

## Failure topology

Failures include serializing an entire navigation/component tree and rendering it before validation; restoring a modal whose prerequisite object is gone; reissuing a purchase/upload because the UI forgot the external operation ID; leaking one user's saved draft after logout/login; losing a valuable draft on routine memory reclamation; and crashing because saved state from an older app version no longer matches the schema.

False restoration is particularly dangerous: the screen looks exactly as the user left it but its status, authorization or object revision is no longer true.

## Falsification

Kill the process at multiple points in editing, upload, authentication, checkout and review flows. Change server state, permissions, account, app version and connectivity before relaunch. The contract is falsified if the app repeats irreversible work, presents stale state as current, attaches local work to the wrong authority context, cannot migrate/discard incompatible persistence safely, or loses explicitly promised recoverable work.

## Recovery

Restore intent and stable identifiers first, reload authority, then merge compatible local work. If a saved state cannot be proven applicable, downgrade to a safe checkpoint and explain what changed. Keep operation IDs idempotent and query external work before issuing another action. Version persisted schemas and provide bounded migration or explicit invalidation rather than best-effort decoding.

## Output contract

Return an `app-lifecycle-state-restoration-contract` with state classes, persistence boundaries, authority/context keys, schema versioning, reconciliation rules, long-operation identity, privacy treatment, invalidation events, safe fallback checkpoints, and kill/relaunch falsification scenarios.

## Handoffs

Use stack/tab specialists for presentation history, offline/sync owners for data reconciliation, authentication for account invalidation, background-task owners for continuing operations, and domain owners for draft/transaction semantics. Restoration never gains authority to invent domain state.