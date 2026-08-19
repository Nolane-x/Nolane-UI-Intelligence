---
name: designing-consent-preference-centers
description: Use when users need to review and change purpose-based consent or optional processing choices over time and the interface must preserve scope, current state, withdrawal, dependency, provenance, and authority without collapsing consent into general settings.
---

# Designing Consent Preference Centers

## Parent Contract
**Required parent:** `designing-permissions-and-consent`.

This faculty owns a durable surface for consent choices whose meaning is tied to a stated processing purpose or optional use. It does not determine legal basis, required disclosures, or jurisdictional obligations from memory; those must come from current authoritative policy/legal guidance. It also does not own all privacy controls, many of which are rights or account actions rather than consent.

## Decision Architecture
Model each choice by purpose, scope, current state, effective date/version where material, source of the choice, and whether withdrawal is available. Avoid one master “Privacy” toggle when separate purposes have materially different consequences. Necessary processing should not be presented as optional consent merely to create a tidy switch list.

Withdrawal must be as understandable as granting. Explain what stops, what may continue under another authority, and when the change takes effect based on current verified policy. If one purpose depends on another capability, show the dependency without coercing users into a broader consent than needed. Preserve a history/provenance record where required by the product's compliance architecture, but do not expose sensitive internal legal annotations to users unnecessarily.

Preference changes may propagate to multiple systems. The UI should distinguish submitted, effective, partially failed, or pending synchronization when the backend cannot apply changes atomically. Do not show a switch as off while downstream systems still process the optional purpose unless the system can truthfully guarantee immediate effect.

## Failure Topology
- Essential service processing is disguised as a required “consent” toggle that users cannot decline.
- One global switch withdraws several unrelated purposes without showing consequences.
- User turns a purpose off, UI updates instantly, but backend propagation fails silently.
- Consent state from a prior policy version is shown without indicating whether reconfirmation is needed under current authority.
- “Accept all” is prominent while granular withdrawal is buried several screens deep.
- Preference center mixes data-deletion, export, security sessions, and marketing consent into one undifferentiated list.

## Falsification and Recovery
Falsify with grant then withdrawal, policy/version change, multi-device state, partial backend propagation, dependent purposes, region/account scope changes, screen-reader operation, and a user whose optional consent is absent while required service processing continues. The design fails if a visible choice cannot be tied to a specific purpose and authoritative state or if withdrawal appears effective before the system can prove it.

Recover by purpose-scoped choices, current authority verification, symmetric change paths, explicit propagation states, separation from non-consent privacy controls, and provenance/history that supports compliance without overstating legal conclusions in UI logic.

## Output Contract
Return `consent-preference-center-contract` with purpose inventory, authority/source obligations, choice scope/state, grant/withdrawal semantics, dependency model, policy-version behavior, propagation evidence, failure recovery, separation from other privacy actions, accessibility requirements, and falsification cases.