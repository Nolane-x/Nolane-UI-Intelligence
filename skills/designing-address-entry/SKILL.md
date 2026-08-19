---
name: designing-address-entry
description: Use when collecting postal or physical addresses across regions and the interface must balance localization, structured data, autocomplete, correction, and user-entered truth.
---

# Designing Address Entry

## Parent Contract
**Required parent:** `designing-forms`.

This faculty owns address capture as a locale-sensitive data problem. It does not assume one country's street/city/state/postcode schema is universal, and it does not make a third-party autocomplete provider authoritative over the address the user actually needs to provide.

## Decision Model
Start with the downstream need: shipping, billing, service eligibility, identity, emergency location, or display. The minimum fields and precision differ. Model country/region first when it materially changes field meaning, ordering, labels, requiredness, or postal-code syntax. Avoid forcing a “state” into countries without states or rejecting valid addresses because they do not match a familiar Western pattern.

Autocomplete is an accelerator, not the only path. Users must be able to enter a new development, rural address, unit, building, landmark, or provider-missing location manually. When a suggestion is selected, expose the resulting structured address so corrections remain possible. Distinguish suggestion confidence from validation; a provider finding an address does not prove deliverability or legal identity.

Preserve formatting where meaningful while storing normalized components as required by the system. Apartment/unit information needs an explicit home rather than being appended unpredictably. If the product supports multiple saved addresses, label/address-book semantics belong downstream, not inside basic capture.

## Failure Topology
- Form requires US-style state and ZIP fields globally.
- Autocomplete selection locks fields and prevents correcting a wrong unit or locality.
- “Address not found” blocks a legitimate new or rural address.
- Locale switch clears a partially entered address without warning.
- Billing address reuse silently copies fields that are invalid under a different country schema.
- Screen readers hear visual placeholder examples but not actual field labels.

## Falsification and Recovery
Falsify with countries using non-Latin scripts, no postal code, long administrative names, multi-line building descriptions, PO boxes, rural delivery, missing autocomplete coverage, keyboard-only suggestion selection, and manual override after a wrong suggestion. The design fails if valid user truth cannot be represented without lying to the schema.

Recover by using country-aware field definitions, manual fallback, editable structured results, explicit unit handling, tolerant normalization, and downstream validation appropriate to the actual business purpose.

## Output Contract
Return `address-entry-contract` with use purpose, locale field schema, ordering/labels, autocomplete role, manual fallback, normalization rules, unit/building handling, country-switch behavior, validation authority, accessibility behavior, and representative international falsification cases.