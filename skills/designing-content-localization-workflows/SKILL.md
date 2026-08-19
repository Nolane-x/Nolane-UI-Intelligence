---
name: designing-content-localization-workflows
description: Use when one content object is authored across languages or markets and the interface must coordinate source locale, translation status, inheritance, locale-specific overrides, review, synchronization, and publication independently per locale.
---

# Designing Content Localization Workflows

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns the production workflow for localized content, not the localization of the product UI itself. It models how a source content revision becomes one or more locale variants with translators, reviewers, fallback, synchronization, and publication state. It does not assume translation is a mechanical string-copy operation.

## Decision Architecture
Define the source-of-truth relationship. Some organizations have one canonical source locale; others author markets independently. If a source field changes, locale variants may become stale, inherit automatically, or remain intentionally overridden. The interface must distinguish untranslated, inherited, translated-current, translated-stale, in-review, approved, and intentionally divergent states rather than one binary “translated” flag.

Translation units should follow content semantics. Title, body, CTA, alt text, metadata, taxonomy labels, and embedded structured blocks may have different localization needs. Reusing source content as fallback can be acceptable for an incomplete locale only if the audience and policy permit it; fallback must not be mistaken for completed translation.

Review and publication can vary by locale. A French translation may be approved while Japanese remains stale. Bulk publishing every locale because the source version is ready can expose unfinished content. Provide translators with source context and previous/current diffs, but avoid automatically overwriting human translations when machine translation or source sync runs.

## Failure Topology
- Source title changes and all locale variants still show green “Complete” despite being based on the old source.
- Automatic source sync overwrites a legally required local-market override.
- Untranslated fallback content is counted as translated coverage.
- Publishing the source revision automatically publishes locales still in review.
- Translator sees isolated strings with no content structure or media context and produces ambiguous wording.
- Deleting a source block leaves orphan translated blocks in some locales with no stale-state warning.

## Falsification and Recovery
Falsify with source revision changes, partial locale translation, intentional local override, machine-translation suggestion, translator/reviewer separation, missing fallback, locale-specific media, deleted source block, multi-locale publication, and RTL/long-text preview. The design fails if users cannot determine which source revision a locale derives from or whether localized content is inherited, human-authored, stale, or independently approved.

Recover by version-binding locale content to source units, recording override provenance, separating fallback from completion, maintaining per-locale workflow status, exposing source diffs/context, protecting human overrides, and gating publication by locale-specific readiness.

## Output Contract
Return `content-localization-workflow-contract` with source-locale model, translation-unit identity, locale status vocabulary, source-change staleness, inheritance/override rules, translation/review roles, fallback semantics, locale publication gates, context/preview needs, and falsification cases.