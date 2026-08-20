---
name: designing-locale-selection
description: Use when users can choose language or regional conventions and the product must separate content language, formatting locale, persistence, scope, and fallback behavior.
---

# Designing Locale Selection

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns the user-facing control model for choosing locale. It distinguishes interface language from regional formatting and defines when a choice applies to an account, workspace, device, session, or document. It does not own translation production or the syntax of every localized value.

## Decision Boundary
Start by identifying which dimensions are actually selectable: language, region, numbering, calendar, time zone, or a bundled locale. Do not expose a single “country” selector if the product uses it to infer unrelated preferences such as language and time zone without allowing correction. A user who speaks French in Canada may still want a different date or number convention; scope those decisions explicitly.

Define discovery and persistence. A selector may appear during onboarding and remain reachable in settings. Changing language should not make the selector impossible to find because its own label becomes unfamiliar; stable iconography or current/target language labels can help. Apply changes atomically enough that users are not left with a half-translated shell. For signed-in users, decide whether account preference overrides device/browser negotiation and whether workspace policy can lock part of the locale.

## Failure Topology
- Language is inferred permanently from IP country with no visible correction path.
- Selecting “English” silently changes currency, measurement, and time-zone behavior users did not ask to change.
- The locale selector displays language names only in the currently selected language, making recovery difficult after an accidental change.
- A language switch refreshes the route and discards unsaved form state.
- Account and device preferences fight on every login, causing the interface to oscillate.
- Unsupported locales disappear rather than explaining the nearest fallback.

## Falsification and Recovery
Test first visit, browser-language negotiation, explicit changes, signed-in persistence, multi-device use, workspace scope, unsupported locale, and switching while unsaved work exists. The contract fails if users cannot predict which parts of presentation will change or if an explicit choice is later overridden silently by automatic detection.

Recover by separating language from regional dimensions, defining precedence among explicit/account/device/browser signals, persisting choices at the declared scope, preserving task state through reloads, and exposing fallback transparently. Test the selector itself in every supported script and narrow viewport.

## Output Contract
Return `locale-selection-contract` with selectable dimensions, preference scope, precedence order, discovery/recovery location, switch transaction behavior, persistence, unsupported-locale fallback, policy locks, and multi-device verification cases.
