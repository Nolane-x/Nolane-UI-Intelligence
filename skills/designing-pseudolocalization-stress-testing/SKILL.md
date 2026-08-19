---
name: designing-pseudolocalization-stress-testing
description: Use when teams need a deterministic pre-translation stress mode that exposes hard-coded strings, expansion failures, bidi assumptions, missing glyphs, and locale-sensitive layout defects before real-language QA.
---

# Designing Pseudolocalization Stress Testing

## Parent Contract
**Required parent:** `designing-localized-interfaces`.

This faculty owns a test transformation and observation contract, not production language. Pseudolocalization intentionally distorts source strings, length, characters, and optionally direction to reveal structural defects while preserving enough source recognizability for engineers to trace the origin.

## Decision Boundary
Define transformations according to the failure class being tested. Expansion pseudo-locale adds length and marked characters; accent/glyph transformation reveals font and encoding assumptions; bidi pseudo-locale exposes hard-coded left/right layout. Protect placeholders, markup tokens, ICU syntax, IDs, and data values so the stress transformation tests UI rather than corrupting runtime grammar.

Ensure every user-facing source passes through localization boundaries. Hard-coded strings should stand out because they remain untransformed. Pseudolocalization must cover dynamic states—errors, loading, permission denial, menus, dialogs, notifications—not only static home screens. It should be deployable in CI/test builds without being accidentally available as a customer locale.

## Failure Topology
- The pseudo transform corrupts interpolation placeholders and produces false test failures.
- Only primary labels transform while validation and error strings remain hard-coded.
- Expansion is uniform and too mild to expose short-label blowups.
- A bidi pseudo-locale mirrors text characters rather than exercising layout direction.
- Pseudo strings leak into screenshots or production because environment gating is weak.
- Engineers treat a clean pseudo run as proof translations are linguistically correct.

## Falsification and Recovery
Run route/action coverage with expansion, glyph, and RTL stress variants; inspect overflow, clipping, missing fonts, logical properties, untranslated strings, and dynamic states. The design fails if the stress mode cannot distinguish localization plumbing defects from intentional non-localizable data, or if it corrupts message syntax.

Recover by protecting structured tokens, increasing context-sensitive expansion, routing all UI copy through localization resources, and separating pseudo locale from native-language QA. Bind screenshots/tests to the exact pseudo transform so regressions remain reproducible.

## Output Contract
Return `pseudolocalization-stress-contract` with transform variants, protected syntax, expansion model, bidi mode, environment gating, route/state coverage, hard-coded-string detection, expected false-positive boundaries, and stress-test evidence format.
