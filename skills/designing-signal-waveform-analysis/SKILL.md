---
name: designing-signal-waveform-analysis
description: Own analytical interaction with scientific waveforms, including cursors, regions, measurements, baselines, channel math, uncertainty, annotations, and reproducible analysis state.
---
# Designing Signal Waveform Analysis

## Decision ownership

Own detailed time-domain analysis of measured waveforms after or alongside acquisition. Decide range selection, measurement cursors, amplitude/time calculations, baseline/reference handling, channel math, filtering/display transforms, annotations, and reproducibility of analysis state. This is not media waveform navigation: numerical measurement and provenance are primary.

## Inputs and evidence

Require sample timestamps, units, calibration/quality, channel synchronization, measurement operations, filter/transform options, uncertainty requirements, baseline definitions, and raw-versus-processed data access. Identify destructive versus display-only transforms.

## Procedure

Keep raw data immutable and distinguish display/analysis transforms from source measurements. Range and cursor operations should expose exact coordinates, units, and uncertainty/resolution where relevant. Baseline subtraction or normalization must state the chosen reference and remain reversible. Derived channels and math expressions need explicit formulas and source channels. Filters should disclose parameters and whether measurements use filtered or raw data. Save analysis state—selected range, cursors, transforms, formulas, annotations—so results can be reproduced.

## Failure topology

Failures include filtered data presented as raw, cursors snapping invisibly, derived traces losing formula provenance, baseline changes silently altering measurements, mixed timebases treated as synchronized, and exported screenshots with no scale or measurement context. Another failure is rounding display values so aggressively that engineering conclusions cannot be reproduced.

## Falsification

Reject if a displayed/derived waveform cannot trace to raw channels and transforms; if measurement values omit units; if changing a baseline updates prior results with no provenance; if synchronized comparison ignores known clock offset; if filter parameters cannot be recovered; or if saved analysis cannot recreate the same selected region and derived channels.

## Output contract

Return a `signal-waveform-analysis-contract` containing: raw-data identity; selected ranges/cursors; measurement operations; units/resolution; baseline/reference; derived-channel formulas; filter/transform chain; synchronization assumptions; annotations; saved analysis state; and export evidence. Include one filtered-versus-raw comparison.

## Handoffs

Live signal monitoring handles acquisition/navigation state, spectrum analysis handles frequency transforms, model fitting consumes selected data, and experimental provenance records analysis inputs and parameters.