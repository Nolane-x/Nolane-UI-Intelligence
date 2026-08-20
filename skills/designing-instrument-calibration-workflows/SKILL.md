---
name: designing-instrument-calibration-workflows
description: Use when this specialist's decision ownership is materially in scope. Own calibration state, reference standards, procedure execution, validity, uncertainty, acceptance, expiry, and measurement consequences for instruments.
---
# Designing Instrument Calibration Workflows

## Parent Contract

**Required parent:** `designing-scientific-and-engineering-instrumentation`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own how an instrument's calibration is established and communicated. Decide calibration type, reference standard identity, procedure/version, readings, fit/offset results, acceptance criteria, uncertainty, validity interval, operator approval, and consequences of expired/failed calibration. This skill does not invent metrology formulas; it preserves their evidence and operational meaning.

## Inputs and evidence

Require instrument/channel identity, calibration procedure, certified reference or standard, standard validity, environmental conditions, measurement sequence, expected ranges, computation result, tolerance, uncertainty model, operator/reviewer roles, and expiration policy. Identify calibrations that apply to one channel versus entire instrument.

## Procedure

Before calibration, verify instrument and reference identities plus reference validity. Guide measurements in the required sequence while showing stabilization or repeat requirements. Keep raw observations distinct from computed correction coefficients. Present acceptance criteria and uncertainty, not merely pass/fail. Failed calibration should affect measurement trust and experiment eligibility according to policy. Successful calibration records effective time, validity/expiry, procedure version, reference certificate, coefficients, and operator. Recalibration must preserve prior records rather than overwriting them.

## Failure topology

Failures include using an expired reference standard, calibration marked pass with raw data missing, coefficients updated without linking to procedure/version, instrument measurements continuing to look fully valid after calibration expiry, and recalibration replacing historical evidence. Another failure is one calibration status badge hiding that only some channels were calibrated.

## Falsification

Reject if calibration cannot trace to reference standard and procedure; if raw observations are irrecoverable; if acceptance tolerance/uncertainty is hidden; if expired/failed calibration has no effect on downstream trust cues; if channel scope is ambiguous; or if new calibration erases the previous effective interval.

## Output contract

Return an `instrument-calibration-workflows-contract` containing: instrument/channel scope; procedure/version; reference identity/validity; measurement sequence; raw observations; computed correction; uncertainty; acceptance criteria/result; effective/expiry interval; operator/reviewer; and downstream measurement eligibility. Include one failed and one expired-reference scenario.

## Handoffs

Experiment setup consumes calibration validity, telemetry displays measurement trust, provenance stores calibration lineage, and safety interlocks may impose stronger blocking rules.