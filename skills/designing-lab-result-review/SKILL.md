---
name: designing-lab-result-review
description: Use when clinicians review laboratory results over time and need specimen context, reference ranges, trends, corrections, units, abnormality evidence, and acknowledgement state without confusing display emphasis with clinical interpretation.
---

# Designing Lab Result Review

A laboratory value is inseparable from specimen, method, unit, reference context, time, and correction history. Result review must preserve those facts while helping clinicians detect change without overstating what the interface can clinically conclude.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns the clinical workflow context. This skill owns organized review of laboratory observations and their temporal/provenance evidence.

## Result Identity and Context
Bind every displayed result to analyte/test identity, specimen when relevant, collection time, result time, unit, reference range or interpretive range, performing source, status, and revision/correction state. Do not normalize units for visual convenience without retaining the original value and conversion provenance.

Group panels in ways that preserve clinical relationships while allowing individual analytes to be inspected. A panel status such as “final” does not guarantee every component has the same status if partial or corrected results are supported; expose exceptions.

## Trend Semantics
Trend visualization must account for unit changes, reference-range changes, method changes, and irregular sampling. Connecting every point with a smooth line can imply continuity that the data do not support. Mark discontinuities and allow users to inspect exact timestamps and source values.

Reference ranges can vary by patient characteristics, laboratory, method, or time. Render the range associated with each observation rather than applying today's range retroactively to historical points unless the product explicitly chooses a normalized analytical view and labels it.

## Corrections and Acknowledgement
Corrected/amended results must preserve the previous reported value, correction time, and reason if available. Never silently replace a critical value in history. Acknowledged/read status is workflow metadata, not evidence that clinical action was taken; keep it separate from resolution.

## Evidence
Test normal, high, low, critical, pending, preliminary, final, corrected, cancelled, and unable-to-result states. Include unit changes, reference-range changes, repeated samples in short intervals, external lab imports, and late-arriving corrections. Verify the displayed chronology against source timestamps.

## Failure Modes
- Historical values are judged against the current reference range without disclosure.
- Unit conversion hides the original result or rounding changes significance.
- Corrected value overwrites the prior report.
- Acknowledgement is rendered as “resolved.”
- Trend lines bridge a method/unit discontinuity as if the series were homogeneous.
- Specimen or collection time is missing for results where it materially affects interpretation.

## Falsification
Provide two years of a lab test with a unit/method change and one corrected critical result. Falsify if the interface creates a visually continuous but semantically invalid trend, or if reviewers cannot reconstruct which value was originally reported and what replaced it.

## Recovery
Break incompatible series, show per-result ranges/units, preserve correction lineage, and separate read state from clinical resolution. When conversion or reference metadata are unavailable, keep values comparable only within proven boundaries.

## Handoff
Abnormality emphasis belongs to `designing-clinical-result-abnormality`; downstream follow-up order state belongs to `designing-clinical-order-status`; alerting policy coordinates with `designing-clinical-alert-fatigue-controls`.

## Output Contract
Return a `lab-result-review-contract` with `result_identity_fields`, `panel_grouping_rules`, `trend_compatibility`, `reference_range_policy`, `unit_conversion_provenance`, `correction_lineage`, `acknowledgement_semantics`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.