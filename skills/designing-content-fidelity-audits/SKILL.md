---
name: designing-content-fidelity-audits
description: Audit shipped UI content against approved meaning, variables, states, localization, legal requirements, and data semantics instead of checking strings in isolation.
---

# Designing content fidelity audits

Copy can drift during implementation through placeholder text, stale translations, incorrect variable interpolation, fallback strings, or state-specific omissions. Use this skill when verifying that rendered content expresses the intended meaning across actual product states.

## Decision ownership

Own content source-of-truth comparison, state coverage, dynamic-variable checks, localization fidelity, legal/regulated copy verification, and severity. Decide when wording differences are acceptable adaptation versus semantic change.

## Inputs and evidence

Collect approved content, content IDs, localization files, product state matrix, variables, plural rules, error messages, legal disclosures, data labels, and rendered builds. Include missing/null data and permission variants.

## Procedure

Audit rendered content in context rather than diffing source strings only. Verify the correct copy appears in the correct state and that variable values, units, names, dates, and plurals preserve meaning. Compare localized versions with language-specific review rather than English-source length alone.

Track intentionally adaptive copy by platform or space constraints. For legal or transactional text, require explicit approval provenance and check that implementation has not truncated or separated qualifiers.

## Failure topology

String equality can pass while the wrong state displays the string. Placeholder variables can leak. Another failure is a translation that is linguistically correct but paired with the wrong unit or action consequence.

Responsive truncation may remove material wording even when source content is correct.

## Falsification

Render every critical content state with extreme variable values, plural forms, nulls, long names, and locales. Compare action labels to actual consequence. Seed a stale translation or wrong variable and verify the audit process detects it.

## Output contract

Produce a `content-fidelity-audits-contract` defining source authority, state/content matrix, variable and localization checks, legal-content handling, responsive constraints, deviation severity, and rendered evidence.

## Handoffs

Use `designing-legal-and-disclosure-typography` for presentation, localization workflows for translation governance, `designing-ui-regression-evidence` for release automation, and `designing-design-decision-records` for approved content changes.