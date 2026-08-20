---
name: designing-experiment-comparison
description: Use when this specialist's decision ownership is materially in scope. Own scientifically honest comparison of multiple runs across setup differences, normalization, alignment, cohorts, metrics, uncertainty, and provenance before claiming changes are comparable.
---
# Designing Experiment Comparison

## Parent Contract

**Required parent:** `designing-scientific-and-engineering-instrumentation`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the interface for comparing results from two or more experiments or engineering runs. Decide compatibility checks, matched metadata, normalization, alignment, selected metrics, uncertainty, cohort grouping, visual overlays, and explicit differences in setup. This owner prevents "overlay these curves" from implying equivalence when inputs differ materially.

## Inputs and evidence

Require run identities, protocol/version, instruments/calibration, samples/cohorts, parameters, environmental conditions, raw/derived metrics, units, time axes, normalization methods, uncertainty, and data completeness. Identify factors that make runs non-comparable or only conditionally comparable.

## Procedure

Begin with a comparison eligibility/differences panel showing material setup divergences. Require compatible units or explicit conversion. Alignment—time zero, event, phase, spatial registration—must be chosen and shown. Normalization needs method and reference; never auto-normalize invisibly. Visual overlays should preserve individual run identity and uncertainty. For cohorts, show sample count and aggregation method. Allow users to save the comparison definition so later readers know which runs, fields, transformations, and metrics were used.

## Failure topology

Failures include comparing different calibration states without warning, auto-scaling each plot independently, hidden normalization, overlaying runs with different time origins, averaging cohorts with unequal inclusion, and cherry-picked metrics with no definition. Another failure is a similarity score that hides meaningful setup differences.

## Falsification

Reject if materially different protocol/instrument/sample conditions are not surfaced; if unit conversion is implicit; if alignment reference is unknown; if normalization cannot be recovered; if aggregate sample count/inclusion is hidden; or if a saved comparison cannot recreate the same run set and transforms.

## Output contract

Return an `experiment-comparison-contract` with: run set; eligibility/difference matrix; unit compatibility; alignment rule; normalization; selected metrics; cohort inclusion/aggregation; uncertainty; visual identity; non-comparability warnings; and saved comparison definition. Include one calibration-mismatch scenario.

## Handoffs

Experimental provenance supplies setup/analysis identity, waveform/spectrum/microscopy provide domain data, model fitting may compare fitted parameters, and data visualization renders chosen comparison encodings.