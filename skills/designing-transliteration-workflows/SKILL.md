---
name: designing-transliteration-workflows
description: Use when a product needs alternate-script representations for search, travel, interoperability, pronunciation, or regulated documents and must distinguish transliteration from translation and from a user's canonical name/content.
---

# Designing Transliteration Workflows

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns creation, display, editing, and provenance of transliterated forms. It does not treat transliteration as a universal replacement for original script. The original content remains authoritative unless a specific external authority requires a particular romanization or script conversion standard.

## Decision Boundary
Identify why transliteration exists and which standard or user-entered form is authoritative. Machine-generated transliteration may be useful for search or suggestion but can be wrong for proper names; users need a way to confirm or override where consequence matters. Multiple standards can produce different spellings, so never label an output simply “English name” when it is actually a romanization under a defined scheme.

Keep original and transliterated forms linked but separate. Search may index both while display privileges the user's preferred form. Legal/travel documents may require a passport spelling that should not be regenerated algorithmically. Do not expose transliteration publicly if the user supplied it only for search discoverability.

## Failure Topology
- The system overwrites an original-script name with an automatic Latin approximation.
- Two romanization standards are mixed across profile and export.
- User correction is lost when the transliteration engine reruns after editing the original.
- Search reveals a private alternate spelling in public result snippets.
- Generated transliteration is presented as translation and changes meaning.
- A passport-required spelling is recomputed rather than preserved from authoritative input.

## Falsification and Recovery
Test names and content where common transliteration systems differ, ambiguous proper nouns, user overrides, search indexing, public/private display, export, and upstream source changes. The design fails if provenance is lost or if an algorithmic form can silently replace an authoritative/user-chosen representation.

Recover by storing original and alternate forms separately with source/standard metadata, protecting explicit overrides, scoping visibility, and using generated transliteration as suggestion rather than truth when appropriate. Re-index search without changing display authority.

## Output Contract
Return `transliteration-contract` with use purpose, original/alternate authority, transliteration standard, generated-versus-user provenance, override lifecycle, visibility/indexing scope, regulated spelling rules, and round-trip verification cases.
