---
name: designing-content-taxonomy-management
description: Use when editors or administrators manage categories, tags, topics, collections, or controlled vocabularies and the UI must preserve hierarchy, identity, usage impact, merge, rename, deletion, and governance semantics.
---

# Designing Content Taxonomy Management

## Parent Contract
**Required parent:** `architecting-information`.

This faculty owns the managed vocabulary used to classify content. It does not own the whole information architecture or ordinary end-user filtering. Taxonomy terms are durable semantic objects whose rename, hierarchy, merge, or deletion can affect many content items, URLs, automation rules, navigation, and reporting.

## Decision Model
Distinguish controlled categories from free tags and from system-generated attributes. Define whether terms form a tree, polyhierarchy, flat set, or ordered collection. A parent-child relationship should encode meaningful classification, not merely visual indentation. Stable IDs must survive label changes; content should not become detached because “Machine Learning” was renamed “AI & ML.”

Management actions require impact evidence. Before deleting or merging a term, show usage count and affected structures where available. Deletion may unclassify content, move it to a fallback, or be blocked while in use. Merge should map old identities into one survivor and define what happens to duplicate assignments, redirects, analytics history, and child terms.

Governance can include ownership, allowed editors, localized labels, synonyms, deprecated terms, and publication status. Avoid letting every editor create near-duplicate terms during content composition if the taxonomy is intended to be controlled. Search/autocomplete should help detect existing terms before creation.

## Failure Topology
- Renaming a category changes its slug/ID and breaks URLs, saved filters, and analytics continuity.
- Deleting a heavily used term happens with one click and silently unclassifies thousands of items.
- Tags and categories share one control even though one is free-form and the other governed.
- Merge creates duplicate assignments and loses which term was historically used.
- Localized labels are edited as separate terms and split one concept into several identities.
- Editors create “AI”, “Artificial Intelligence”, and “artificial-intelligence” because creation never searches existing vocabulary.

## Falsification and Recovery
Falsify with term rename, merge of two used terms, deletion with child terms, localized labels, synonyms, saved filters referencing old IDs, content import introducing unknown terms, role-restricted taxonomy editors, and screen-reader tree management. The design fails if semantic identity is coupled to display label or if destructive vocabulary changes cannot enumerate their downstream impact.

Recover by using stable term IDs, separating vocabulary classes, previewing usage impact, defining merge/delete migrations, preserving aliases/redirects where needed, centralizing localization under one identity, and restricting creation according to governance policy.

## Output Contract
Return `content-taxonomy-contract` with vocabulary classes, hierarchy model, stable identity, labels/localization/synonyms, creation governance, usage impact, rename/merge/delete semantics, downstream references, permission model, accessibility management, and falsification cases.