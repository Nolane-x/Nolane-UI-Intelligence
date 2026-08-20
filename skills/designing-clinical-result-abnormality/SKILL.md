---
name: designing-clinical-result-abnormality
description: Use when diagnostic results carry normal, abnormal, critical, indeterminate, or context-dependent significance and the interface must encode source flags, thresholds, uncertainty, and escalation without practicing medicine by presentation alone.
---

# Designing Clinical Result Abnormality

Abnormality is a source-backed classification, not a color palette. The interface must communicate what the reporting system or configured rule declared, how severe the state is, and what remains context-dependent for clinical interpretation.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent supplies clinical context. This skill owns abnormality/status encoding across diagnostic result surfaces while preserving the distinction between source flags and clinician judgement.

## Abnormality Taxonomy
Enumerate states supported by the data source: normal, high, low, abnormal, critical high/low, positive/negative, indeterminate, preliminary, corrected, and unknown when applicable. Do not force incomparable domains into one universal “red/yellow/green” scale. A microbiology positive result and a numerical critical threshold carry different semantics.

Bind abnormality to explicit evidence: source flag, reference interval, configured decision threshold, or validated rule. If the UI derives a visual indicator locally, document the derivation and ensure it cannot disagree silently with the source's authoritative status.

Severity and urgency are related but not identical. A critical result may require acknowledgement/escalation workflow; an abnormal result may simply require review. Use wording, iconography, ordering, and color redundantly so users with low vision or color-vision differences retain the distinction.

## Context and Change
Patient-specific context can alter interpretation, but the UI should not infer clinical diagnosis from generic thresholds. When ranges vary by age, sex, pregnancy, method, or lab, show the applicable source range and leave clinician interpretation separate. If a result changes classification after correction, preserve both the original and corrected state.

## Evidence
Test every supported abnormality code, missing flag, contradictory value/range, corrected result, preliminary-to-final transition, and critical escalation. Verify screen reader output, forced colors/high contrast, print/export where clinically used, and compact list versus detailed review.

Use data where a numeric value appears inside the displayed range but arrives with a source abnormal flag, and vice versa. The interface should expose the discrepancy rather than silently choosing one authority.

## Failure Modes
- Red text is the only signal of criticality.
- The client recalculates abnormality and hides disagreement with the source.
- Unknown or missing classification renders as normal.
- “Abnormal” is visually conflated with “requires immediate action.”
- Corrected status removes evidence of the earlier critical flag.
- One generic severity scale is reused across clinically different result types.

## Falsification
Inject contradictory source flag and local threshold data. Falsify if the UI silently resolves the conflict without provenance. Test without color perception; falsify if severity or actionability becomes ambiguous.

## Recovery
Surface the authoritative source flag, label derived indicators as derived, introduce explicit UNKNOWN/conflict states, and use redundant non-color encoding. Escalation actions should reference the actual result revision that triggered them.

## Handoff
Detailed laboratory chronology belongs to `designing-lab-result-review`; order lifecycle belongs to `designing-clinical-order-status`; alert routing and interruption load belong to `designing-clinical-alert-fatigue-controls`.

## Output Contract
Return a `clinical-result-abnormality-contract` with `abnormality_taxonomy`, `evidence_sources[]`, `derived_indicator_rules`, `severity_vs_urgency`, `redundant_encodings[]`, `conflict_state`, `correction_behavior`, `accessibility_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.