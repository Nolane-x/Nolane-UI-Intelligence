---
name: designing-radiology-study-navigation
description: Use when clinicians or imaging specialists navigate studies, series, instances, priors, reports, and related exams and must preserve study identity, chronology, modality, laterality, and comparison context.
---

# Designing Radiology Study Navigation

Imaging navigation is a hierarchy and comparison problem. Users need to know which patient, study, series, acquisition, and prior they are viewing while moving quickly through large image sets and related reports.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns patient and clinical context. This skill owns study/series navigation and comparison orientation; actual measurement interaction is delegated to `designing-medical-image-measurements`.

## Imaging Hierarchy
Represent patient → study → series → instance relationships explicitly enough to prevent context loss. Study labels should include clinically useful attributes such as modality, description, acquisition date/time, body region, accession/order context, and status when available. Series need sequence/description and acquisition context rather than only index numbers.

Priors are not ordinary siblings. When comparing current and prior studies, identify which is current, which is prior, the time interval, and whether the comparison is linked by body region/protocol or manually selected. Preserve the comparison set across layout changes and series navigation.

## Navigation Behavior
Support rapid traversal without losing orientation. Thumbnail strips, series lists, keyboard shortcuts, scout/localizer references, and synchronized viewport selection can all be appropriate, but each must map to the same underlying study/series identity. Selecting a new series should not silently repurpose a viewport that the user believed was locked to a prior.

For very large studies, loading state must distinguish metadata availability from pixel availability. A visible series card does not mean all instances are loaded. Progressive loading should retain correct instance numbering and never display stale pixels from a previous series under a new label.

## Report and Order Context
Link images to report and originating order without implying the report is final when it is preliminary or amended. If report and image study identifiers disagree, expose the mismatch as a safety issue instead of guessing the relationship.

## Evidence
Test current/prior comparison, multiple studies on the same date, series with similar names, partial image loading, failed instance, changed patient, amended report, and a study with hundreds of series. Verify viewport labels against DICOM/study metadata and source identifiers.

## Failure Modes
- Current and prior studies become visually indistinguishable.
- A viewport title updates before pixels, showing stale imagery under new metadata.
- Series are identified only by ordinal index.
- Layout changes silently replace a locked comparison viewport.
- Report status is hidden so preliminary text looks final.
- A failed instance causes numbering to shift and landmarks to be misreferenced.

## Falsification
Load two near-identical studies with similar series names, intentionally delay one series, and switch rapidly. Falsify if a user can see pixels from one study with labels from another or cannot state which prior/current pair is active.

## Recovery
Freeze mismatched viewports, rebind labels and pixels to the same study/series revision, expose failed instances, and restore explicit prior/current markers. Treat identity mismatch as BLOCKED until reconciled.

## Handoff
Measurement tools belong to `designing-medical-image-measurements`; abnormal findings and clinical result state route to result owners; general 3D/CAD navigation must not override radiology study identity semantics.

## Output Contract
Return a `radiology-study-navigation-contract` with `study_identity_fields`, `series_identity_fields`, `prior_comparison_model`, `viewport_binding_rules`, `progressive_loading_states`, `report_order_links`, `keyboard_navigation`, `identity_evidence[]`, `falsification_cases[]`, and `recovery_actions[]`.