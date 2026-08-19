---
name: designing-privacy-control-centers
description: Use when users need one coherent place to understand and act on privacy-related account controls such as visibility, personalization, data use, export, deletion, blocked entities, or retention, without treating every control as consent.
---

# Designing Privacy Control Centers

## Parent Contract
**Required parent:** `designing-privacy-sensitive-interfaces`.

This faculty owns the architecture of a durable privacy-management surface. It does not decide legal rights, consent requirements, retention law, or account security from memory; material obligations require current authoritative verification. It coordinates distinct privacy actions while preserving their different semantics, prerequisites, and consequences.

## Decision Architecture
Group controls by user mental model rather than internal data systems: who can see me/my content, how my activity influences recommendations, communication/discovery preferences, data access/export, deletion/retention actions, blocked entities, or other product-specific privacy domains. Do not place a switch beside a destructive right request simply because both are “privacy.”

For every control, identify whether it is a reversible preference, visibility rule, consent choice, rights request, account action, or informational state. The interaction must match the class. A reversible toggle may apply immediately; an export request may become a background job; deletion may require identity re-verification and a grace period; a legal retention exception may prevent immediate erasure. Keep those state machines distinct.

Effective scope matters. A user may manage account-wide privacy, workspace-specific visibility, public profile fields, or device-level history. Show inherited/locked settings and current effective value when organization policy constrains choice. Link to deeper specialist flows rather than duplicating their full mechanics inside one overloaded page.

## Failure Topology
- Privacy center presents Data deletion as a simple toggle next to newsletter preferences.
- Workspace policy locks a visibility setting but UI shows it editable until save fails.
- “Private profile” is enabled while individual public fields remain exposed with no effective-state explanation.
- Export request starts but disappears from the center and users cannot find status later.
- Privacy copy promises complete deletion despite verified retention obligations or technical exceptions.
- Consent, security sessions, personalization, and visibility use identical control patterns despite different authority and consequences.

## Falsification and Recovery
Falsify with organization-managed settings, multiple workspaces, visibility inheritance, export in progress, deletion requested, retention exception, locale/policy differences, screen-reader operation, and account plan/role changes. The design fails if users cannot distinguish reversible settings from process requests or determine the effective privacy state after inheritance and exceptions.

Recover by classifying every control, showing scope/effective origin, delegating complex actions to specialist flows, verifying current policy/authority, preserving request status, and writing consequence copy from actual system behavior rather than aspirational privacy language.

## Output Contract
Return `privacy-control-center-contract` with privacy domains, control classification, scope/effective-state model, inheritance/locks, specialist-flow handoffs, request-status surfaces, authority-verification obligations, exception/retention communication, accessibility navigation, and falsification cases.