---
name: designing-privacy-sensitive-interfaces
description: Use when UI displays, collects, shares, searches, records, exports, or infers sensitive personal, health, financial, identity, location, communication, or organizational information, especially on shared or public devices.
---

# Designing Privacy-Sensitive Interfaces

## Overview
Privacy is boundary visibility. The interface should make clear what data exists, who can see it, where it will go, how long it remains, and how shared-device or screen contexts change exposure.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require data classes, audience/roles, device ownership, sharing/export paths, retention, notification surfaces, screenshots/previews, logs/history, and applicable privacy policy/law. Do not infer legal compliance from UI review.

## Decision Model
Map data from collection to display, action, sharing, persistence, and deletion. For each UI surface identify exposure: on-screen, lock-screen notification, recent-item history, autocomplete, analytics, clipboard, export, collaboration, AI context, logs, and support tooling. Minimize data shown or collected when it does not change the task.

Audience is a first-class state. Before sharing/publishing/export, show who receives the information and whether that audience is public, organization-wide, link-accessible, or specific people. Make permission inheritance visible when a folder/project/container changes child exposure.

Shared devices and screens need special rules: mask sensitive values until requested, clear previous session data, avoid revealing search/history in idle state, and make account identity visible before acting. Privacy screens must not make recovery impossible; users need to understand what was hidden and how to reveal it safely.

For AI, identify whether prompts, retrieved context, generated content, or feedback leave the local/project boundary. Provenance and consent skills apply where user decisions are needed.

## Evidence
Test shoulder-surfing/shared-screen scenarios, lock-screen notifications, autocomplete/history, copy/export, role changes, link sharing, session timeout, account switch, screenshots where platform exposes them, logs, and AI context boundaries. Use realistic sensitive data substitutes without leaking actual secrets in testing.

## Output Contract
Return a `privacy-contract` with `data_classes[]`, `exposure_map[]`, `audience_states[]`, `collection_minimization`, `display_redaction`, `shared_device_rules`, `history_and_logs`, `sharing_and_export`, `retention_and_deletion`, `ai_context_boundary`, and `privacy_tests[]`.

## Failure Traps
- Notification preview exposing sensitive content on a lock screen.
- “Share link” with unclear audience.
- Previous kiosk/session history visible to the next person.
- Hidden data copied/exported in full without warning.
- AI prompt silently receiving private project context.
- Account switch leaving prior user content cached onscreen.
- UI promising deletion without knowing backend retention behavior.

A privacy-safe UI makes invisible data boundaries visible before they surprise the user.

## V6 Privacy-Sensitive Surface Protocol
Build a **data-exposure map** for every screen/state: what personal/sensitive data appears, to whom, on which device/channel, and for how long. Define a **privacy expectation boundary** from user context—shared device, workplace, public space, notification preview, casting, screen sharing, recordings.

Use **sensitive-screen shielding** where platform capability supports it or reduce exposure in task switcher/previews/lock screen. Keep a **retention-disclosure link** between UI promises and actual save/history/delete/export behavior. Preserve **consent-context integrity** so permission to use data for one feature does not silently authorize unrelated personalization/training/sharing.

### Falsification
Share screen, lock device, switch account/workspace, export/delete, and revoke consent. Residual/expanded exposure falsifies privacy semantics.

### Recovery
Hide/clear data, narrow processing scope, repair retention/consent state, and explain material changes before re-enabling sensitive functionality.
