---
name: designing-person-name-localization
description: Use when collecting, displaying, sorting, addressing, or exporting people's names across cultures and the product must avoid assuming a universal given-name/family-name structure.
---

# Designing Person Name Localization

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns the interface model for personal names. It rejects the assumption that every person has exactly a first name and last name in Western order. It does not define legal-identity verification requirements, which may impose separate authoritative fields.

## Decision Boundary
Ask what the product actually needs: a display name, a name for addressing, a legal name for a regulated process, a searchable identifier, or structured components for an external system. Collect the minimum structure justified by that purpose. Preserve user-entered spelling, diacritics, script, spacing, prefixes, patronymics, mononyms, and order. A single display-name field is often safer when structured decomposition is unnecessary.

When multiple scripts are relevant, allow an alternate/transliterated form only when there is a concrete use such as travel documents or search interoperability; do not force Latin transliteration for ordinary identity. Sorting and salutations must not infer family/given components from word position. Respect user preferences for how their name is presented.

## Failure Topology
- Both “First name” and “Last name” are mandatory for a mononymous user.
- The UI reverses name order based on locale even though the user supplied an intentional display order.
- Validation rejects apostrophes, spaces, diacritics, non-Latin scripts, or long family structures.
- Email greetings guess a given name by taking the first token.
- Export truncates or normalizes characters differently from the profile display.
- A Latin transliteration is displayed publicly instead of the person's chosen script.

## Falsification and Recovery
Test mononyms, multi-part family names, patronymics, East Asian order, prefixes/suffixes, non-Latin scripts, diacritics, long names, and explicit display preferences. Follow data through profile, search, sorting, messaging, export, and legal flows. The design fails if the product rewrites a person's identity merely to fit a two-field model.

Recover by reducing unnecessary decomposition, labeling legal structured fields precisely when required, preserving original user input, and storing explicit display preferences. Coordinate sorting/search separately instead of overloading display-name structure.

## Output Contract
Return `person-name-localization-contract` with name purposes, required fields by authority, display-order preservation, supported characters/scripts, alternate-script policy, salutation restrictions, sorting/search handoffs, and multicultural name verification cases.
