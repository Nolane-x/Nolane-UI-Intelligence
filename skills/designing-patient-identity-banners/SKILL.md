---
name: designing-patient-identity-banners
description: Use when a clinical application needs persistent patient identity context that remains legible across navigation, supports disambiguation, and resists wrong-patient actions without exposing unnecessary sensitive data.
---

# Designing Patient Identity Banners

A patient banner is not branding chrome. It is a safety control that lets clinicians continually confirm which person the current clinical state belongs to, especially when multiple records are open or names are similar.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns global clinical context. This skill owns the visible identity anchor, its disambiguating fields, persistence rules, privacy boundary, and behavior during patient-context changes.

## Identity Selection
Choose disambiguators by clinical risk and local policy, not by how many fields fit in one line. Common candidates include full name, preferred name, date of birth/age, medical record identifier, sex or gender information when clinically required, patient photo where governed, and high-consequence status such as deceased. Avoid using room/bed as identity because location changes and can be shared over time.

Fields have different privacy sensitivity. The banner should expose the minimum identity evidence necessary for safe differentiation in the current context. On shared displays or screenshots, support privacy treatment without reducing identity certainty below the safety threshold.

## Persistence and Contrast
The banner must remain discoverable across scroll, nested modules, drawers, and embedded viewers when the product allows consequential actions there. “Sticky” is an implementation mechanism, not the requirement; the requirement is that patient identity remains readily confirmable before action. Verify real scroll containers and responsive states rather than assuming CSS positioning works.

Use visual distinction for material statuses only when meaning is explicit and remains accessible. A deceased-patient treatment, isolation status, or similar condition must not rely on color alone. Check foreground contrast, focus indicators, nested components, tags, icons, and loading states against any status-driven background change.

## Context Switching
Switching patients must invalidate or rebind dependent views deliberately. If a side panel contains unsaved content for Patient A, navigating to Patient B should not silently carry that draft across. Provide a transition guard for material unfinished work and confirm the new identity after switch.

## Evidence
Test same-name patients, similar dates of birth, missing identifiers, long names, deceased/status variation, narrow viewport, zoom, high contrast mode, scrolling through long charts, and multiple open tabs. Verify that the identity displayed in the banner matches the patient identifier used by every consequential request in the tested flow.

Include screenshot/privacy scenarios and screen-reader announcement of identity changes. Evidence should show that a context switch is perceivable without creating a noisy announcement on every internal tab change.

## Failure Modes
- The banner disappears while a medication or order action remains available.
- Location is the primary differentiator.
- Status is encoded only by background color.
- Long names truncate the only distinguishing field.
- Patient change updates the banner but leaves a stale action panel bound to the previous record.
- Privacy mode removes so much identity that same-name patients become indistinguishable.

## Falsification
Place two clinically distinct patients with similar names in adjacent tabs and switch rapidly between them before a consequential action. Falsify if the acting user cannot independently confirm identity from the current surface or if the server-bound patient differs from the visible banner.

## Recovery
Freeze consequential controls on identity mismatch, discard or quarantine stale bound state, re-fetch authoritative patient context, and restore a disambiguating banner. If privacy and safety requirements conflict, escalate the policy decision rather than guessing which field to expose.

## Handoff
Encounter-specific context belongs to `designing-clinical-encounter-context`; accessibility details coordinate with screen-reader and low-vision owners; app-switcher/screenshot privacy may use platform privacy owners where the clinical app runs natively.

## Output Contract
Return a `patient-identity-banners-contract` with `identity_fields[]`, `disambiguation_policy`, `privacy_boundary`, `persistence_requirements`, `status_treatments[]`, `context_switch_rules`, `accessibility_behavior`, `request_binding_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.