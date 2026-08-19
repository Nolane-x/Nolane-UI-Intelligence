---
name: designing-permission-onboarding
description: Use when a product must ask for device, browser, account, or workspace permission and needs to explain purpose, timing, consequences, denial recovery, and system-prompt handoff before requesting authority.
---

# Designing Permission Onboarding

## Parent Contract
**Required parent:** `designing-permissions-and-consent`.

This faculty owns the teaching and request sequence around a permission boundary. It does not own the underlying authorization policy or platform system dialog. The central obligation is to ask only when the capability is relevant, explain the benefit and consequence truthfully, and preserve a usable path after denial.

## Decision Architecture
Request at the moment of use when the relationship between permission and capability is concrete. Asking for camera, notifications, contacts, microphone, filesystem, location, or workspace access immediately on first launch without context increases refusal and distrust. A pre-prompt is justified when the system prompt is terse or irreversible, but it must not imitate native permission UI or coerce users into continuing.

Explain what the permission enables, what data or capability scope it exposes, whether access is one-time/while-using/persistent where the platform provides those choices, and what happens if the user declines. Do not promise that the app “never stores” data unless that is independently true. When a platform prompt follows, the product should not show contradictory labels or a fake button whose visual design can be mistaken for the OS decision.

Denial is a supported state. If a request can be asked again directly, define when. If the platform requires Settings to reverse denial, provide exact current guidance without trapping users in a dead-end overlay. Permission revocation after prior success should degrade the affected capability locally rather than crash unrelated parts of the product.

## Failure Topology
- App asks for five permissions on first launch before any relevant feature is used.
- Custom pre-prompt uses “Allow” styling identical to the OS dialog and tricks users about where authority is granted.
- Denying microphone closes onboarding entirely even though text interaction remains usable.
- Product keeps re-prompting after every denial and turns consent into harassment.
- Settings instructions are stale and send users to the wrong platform screen.
- Permission is revoked later but UI still displays the capability as available until an operation fails.

## Falsification and Recovery
Falsify with first-use request, denial, restricted/parental-control state, OS “ask next time,” permission revoked in settings, platform prompt unavailable, multiple related permissions, keyboard/screen-reader use, and a user who never needs the capability. The design fails if declining an optional permission blocks unrelated product use or if the custom interface implies authority it does not possess.

Recover by contextual request timing, accurate purpose/scope explanation, platform-distinct pre-prompts, bounded recurrence, denial-safe alternatives, live permission-state checks, and authoritative settings recovery guidance verified for the current platform.

## Output Contract
Return `permission-onboarding-contract` with permission purpose, request trigger, pre-prompt content, system-dialog handoff, denial/retry semantics, alternate capability path, revocation detection, settings recovery, platform/version verification obligations, accessibility behavior, and falsification cases.