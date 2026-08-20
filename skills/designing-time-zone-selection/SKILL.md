---
name: designing-time-zone-selection
description: Use when users schedule, compare, audit, or display time across zones and the interface must make zone identity, defaults, daylight changes, and local-versus-absolute semantics explicit.
---

# Designing Time Zone Selection

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns choosing and communicating time-zone context. It does not format the resulting date/time string. Its central problem is that a local clock label is incomplete without a zone when people coordinate across places or future daylight-saving transitions.

## Decision Boundary
Determine the authoritative zone for each workflow: user profile, organization, event venue, device, data source, or explicit per-event choice. Use stable zone identifiers rather than fixed UTC offsets for future scheduling because offsets can change seasonally or by policy. Present human-friendly city/region labels while retaining canonical identifiers internally.

Defaults must be visible and editable when they affect consequence. A scheduler can preselect the user's zone but should show it near the time fields. For cross-zone collaboration, display both organizer/event zone and viewer-local equivalent when that prevents mistakes. Handle ambiguous/nonexistent local times during daylight transitions with explicit resolution rather than silent normalization.

## Failure Topology
- Future events store only `UTC+2` and become wrong after daylight-saving change.
- A meeting time field has no visible zone and users assume their own local time.
- Device zone silently overrides an organization's operational zone after travel.
- A nonexistent local time during spring transition is accepted and moved without explanation.
- Two identical local clock times during fall transition cannot be distinguished.
- Search uses city names as the data key and breaks when labels are localized.

## Falsification and Recovery
Test travel/device-zone changes, daylight transitions, future scheduling, organizer/viewer differences, ambiguous times, unsupported zones, and historical records. The design fails if two users can read the same displayed time and reasonably infer different instants.

Recover by storing canonical zone identifiers plus temporal type, exposing zone beside consequential input/output, offering explicit ambiguity resolution, and separating event/organization/device precedence. Re-test after locale formatting changes because local names and clock conventions should not obscure zone identity.

## Output Contract
Return `time-zone-selection-contract` with authoritative zone sources, default/precedence rules, canonical identifiers and labels, daylight ambiguity handling, viewer/event dual display, travel behavior, and cross-zone scheduling verification cases.
