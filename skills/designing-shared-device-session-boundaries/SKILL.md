---
name: designing-shared-device-session-boundaries
description: Use when multiple people use the same physical device and account/session state, cached files, notifications, recent activity, biometrics, and handoff must prevent one user's data from leaking into the next user's session.
---

# Designing Shared Device Session Boundaries

## Parent Contract
**Required parent:** `designing-device-integration-interfaces`.

This faculty owns privacy and state reset at human handoff on shared hardware: kiosks, tablets, scanners, terminals, family devices, classrooms, or shift workstations. It is not generic authentication; the device itself is a reused context that can retain state beyond sign-out.

## Decision Boundary
Define session start/end and what persists across users. On sign-out/timeout/handoff, clear or re-scope recent files, drafts, clipboard-like in-app data, search history, thumbnails, downloads, notifications, device selections, and cached credentials according to policy. Device-level preferences such as language or printer may persist when non-sensitive; user-specific settings should not bleed across sessions.

Biometric authentication on shared devices needs clear mapping to the current account and should not expose previous-user identity. Idle timeout must warn/preserve recoverable work according to policy while still completing privacy cleanup. Offline mode is especially risky because queued data may belong to a signed-out user; define ownership and sync after handoff.

## Failure Topology
- Next user sees previous user's recent files or autocomplete history after sign-out.
- Local offline queue syncs under the new user's account.
- Shared tablet retains a personal notification badge on the lock/login screen.
- Biometric unlock reopens whichever account was last active with no identity confirmation.
- Device-level printer preference is unnecessarily cleared, while sensitive file cache remains.
- Idle timeout hides UI but does not purge session-bound memory/downloads.

## Falsification and Recovery
Run user A → sign out/timeout → user B across online/offline, downloads, drafts, search, notifications, queued sync, biometrics, and device preferences. Inspect filesystem/cache where product controls it. The design fails if any user-specific artifact becomes visible or actionable after the session boundary without explicit shared intent.

Recover by classifying state as device/shared versus session/user, binding queues/files to owner identity, performing verified cleanup, and making handoff atomic before next login. Preserve only policy-approved device configuration.

## Output Contract
Return `shared-device-session-contract` with session boundaries, device-versus-user state classification, cleanup/persistence rules, offline queue ownership, biometric mapping, timeout/handoff behavior, and cross-user leakage verification cases.
