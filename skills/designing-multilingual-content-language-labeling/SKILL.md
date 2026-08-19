---
name: designing-multilingual-content-language-labeling
description: Use when pages, messages, user-generated text, or embedded documents contain content in languages different from the interface and those language boundaries must be exposed for pronunciation, translation, search, and comprehension.
---

# Designing Multilingual Content Language Labeling

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns language metadata on content units. It does not choose the UI shell locale. It ensures assistive technology, translation features, search analyzers, and users can distinguish the language of content that differs from its surroundings.

## Decision Boundary
Decide language at the smallest meaningful stable unit: page, article, message, quoted passage, code-switch span, or imported document. Use authoritative author metadata when available; automatic detection can suggest but should expose uncertainty before driving consequential behavior. Short strings, names, and code are notoriously hard to detect and may be left under surrounding language rather than confidently misclassified.

Language metadata should inform pronunciation and processing without creating noisy visible badges everywhere. Visible labels are useful when users need to choose translation, filter languages, or understand why content is not localized. Mixed-language text may require nested metadata. Do not translate user-generated content automatically merely because its language differs from the shell.

## Failure Topology
- Screen reader pronounces an embedded French paragraph using English rules because no language boundary exists.
- A two-word name is misdetected and receives an incorrect language badge.
- Search sends every message through the shell-language analyzer regardless of content language.
- Automatic translation replaces original user content without an explicit choice.
- Language metadata is stored only on the page while individual quoted passages switch language.
- A visible badge is shown for every chat message, overwhelming the conversation.

## Falsification and Recovery
Test shell/content language combinations, mixed paragraphs, quotes, names, code, short messages, auto-detection uncertainty, screen-reader pronunciation, search, and translation entry points. The design fails if incorrect metadata causes worse pronunciation/matching than leaving language unknown or if users cannot access original content after translation.

Recover by preferring explicit metadata, limiting automatic detection to sufficiently strong evidence, allowing nested language spans, and separating processing metadata from optional visible labels. Preserve original text and expose translation as a reversible layer.

## Output Contract
Return `content-language-label-contract` with language-metadata granularity, authority/detection rules, uncertainty handling, nested-language behavior, visible-label criteria, assistive/search/translation consumers, and multilingual-content verification cases.
