---
name: designing-permissions-and-consent
description: Use when a UI asks for access to data, sensors, contacts, files, location, notifications, AI training, tracking, sharing, delegated actions, or any user permission that should be informed, scoped, and revocable.
---

# Designing Permissions and Consent

## Overview
Consent is a meaningful decision, not a banner-clearing event. Ask at the moment value is understandable, request the smallest scope needed, make refusal viable, and keep later review/revocation accessible.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require data/action requested, purpose, duration, audience/recipient, necessity, platform permission behavior, consequences of denial, and revocation mechanism. Applicable law/policy may impose stricter requirements and must outrank this skill.

## Decision Model
Separate **required capability** from **optional enhancement**. If a function cannot operate without a permission, explain that relation before the system prompt where possible. If optional, allow the core task to continue after denial. Avoid pre-prompts whose only purpose is to pressure users into accepting an OS permission.

Apply progressive scope. Request one-time/session/selected-item access when sufficient rather than indefinite/global access. For AI agents, permission can include action authority — sending mail, spending budget, editing files — and must use the autonomy envelope, not a generic data-consent dialog.

Choice architecture must be symmetric enough to support a real decision. Labels state the consequence: “Allow location while using the app” versus vague “Continue.” Do not hide reject, bundle unrelated purposes, preselect broad sharing, or use guilt/fear copy. If consent is recorded, preserve what version/scope the user accepted.

Review and revocation are part of the design. Show active permissions in understandable categories, allow narrowing/turning off, and explain what already-shared data or executed actions cannot be revoked retroactively.

## Evidence
Test accept, deny, partial scope, repeated prompt suppression, OS-level revocation, stale permissions, shared device, accessibility, localization, and whether denied users can still perform promised core tasks. Audit labels for dark patterns and scope mismatch.

## Output Contract
Return a `consent-contract` with `requested_capabilities[]`, `purpose_map`, `required_vs_optional`, `scope_options[]`, `request_timing`, `choice_copy`, `denial_behavior`, `recorded_consent`, `review_surface`, `revocation_behavior`, `irreversible_effects[]`, and `consent_tests[]`.

## Failure Traps
- Giant “Accept all” with hidden reject.
- Asking for contacts/location on first launch before value is clear.
- Bundling unrelated purposes under one checkbox.
- Re-prompting after every denial until the user gives in.
- “Revoke” implying already-sent data is deleted when it is not.
- Agent tool authority hidden inside a privacy consent.
- Permission scope broader than the feature actually requires.

Consent quality is measured by informed control, not acceptance rate.