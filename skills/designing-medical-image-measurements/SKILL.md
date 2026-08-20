---
name: designing-medical-image-measurements
description: Use when diagnostic imaging workflows create, edit, compare, label, or report measurements and the interface must preserve image frame, geometry, units, calibration, author, revision, and clinical provenance.
---

# Designing Medical Image Measurements

An imaging measurement is a clinical annotation bound to specific image geometry and calibration. A distance, angle, area, SUV, or region-of-interest value is unsafe if detached from the frame, series, units, or revision that produced it.

## Parent Contract
**Required parent:** `designing-clinical-care-workflows`.

The parent owns clinical context. This skill owns measurement creation and lifecycle within medical imaging; navigation among studies and priors remains with `designing-radiology-study-navigation`.

## Measurement Binding
Bind every measurement to patient, study, series, image/frame, spatial transform/calibration, measurement type, units, author, creation time, and revision. For multi-frame or reconstructed images, record the exact frame/slice and orientation. Do not rely on screen pixel distance; measurements require image-space calibration.

Tool state must make active geometry obvious before commit. Handles, labels, snapping, and selected viewport should distinguish the in-progress measurement from saved annotations. If zoom/pan changes, the measurement must remain anchored to image coordinates rather than screen coordinates.

## Editing and Comparison
Editing should create traceable revision state where policy requires. If one clinician changes another's measurement, preserve original author and change history. Deletion may mean hide, invalidate, or remove according to system governance; avoid generic trash semantics for clinical evidence.

Longitudinal comparison requires matching lesions/findings or measurement entities across studies. Do not assume nearest spatial location across different acquisitions is the same lesion. Surface explicit linkage and allow uncertainty or unmatched state.

## Units and Calibration
Show units consistently and protect against calibration changes. If metadata required for a quantitative measure are missing or invalid, disable that quantitative result rather than computing from display pixels. Derived values should expose the formula/input measurements and rounding policy.

## Evidence
Test length, angle, area, ROI, multi-frame measurement, zoom/pan, orientation changes, missing calibration, reconstructed series, prior comparison, concurrent edit, and report export. Verify stored coordinates and values against known image geometry.

Include loading transitions: an old annotation must not appear on a newly selected series until identity is confirmed.

## Failure Modes
- Measurement is anchored to screen pixels rather than image coordinates.
- Label remains after switching series and appears to belong to new imagery.
- Missing calibration still produces a numeric distance.
- Editing destroys original author/revision history.
- Units change without recalculating or invalidating the value.
- Longitudinal lesion matching is inferred solely by visual proximity.

## Falsification
Create a known calibrated object, measure it, then zoom, rotate, switch frames, and reload. Falsify if the value drifts or attachment changes. Remove calibration metadata; falsify if the UI continues to claim a quantitative measurement.

## Recovery
Invalidate quantitative output when calibration is uncertain, rebind annotations only after frame identity is confirmed, preserve revision history, and expose unmatched longitudinal findings rather than forcing false equivalence.

## Handoff
Study selection and prior pairing route to `designing-radiology-study-navigation`; result abnormality and report lifecycle belong to clinical result owners; generic CAD measurement tools cannot substitute for medical imaging calibration/provenance.

## Output Contract
Return a `medical-image-measurements-contract` with `measurement_identity`, `image_geometry_binding`, `tool_states[]`, `revision_policy`, `longitudinal_linkage`, `unit_calibration_rules`, `derived_value_provenance`, `evidence_cases[]`, `falsification_cases[]`, and `recovery_actions[]`.