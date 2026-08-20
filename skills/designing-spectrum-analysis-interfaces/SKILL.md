---
name: designing-spectrum-analysis-interfaces
description: Use when this specialist's decision ownership is materially in scope. Own frequency-domain analysis interfaces, including transform configuration, frequency/amplitude axes, windows, averaging, peaks, bandwidth, reference levels, and trace provenance.
---
# Designing Spectrum Analysis Interfaces

## Parent Contract

**Required parent:** `designing-scientific-and-engineering-instrumentation`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own how users inspect measured data in the frequency domain. Decide transform settings, windowing, averaging, frequency span/resolution, amplitude representation, reference/normalization, peak finding, markers, overlays, and provenance from time-domain source to spectrum. This owner does not implement DSP algorithms.

## Inputs and evidence

Require source samples and rate, transform algorithm/options, window functions, FFT length/resolution bandwidth, averaging modes, amplitude units (linear, dB variants, PSD), calibration, channel count, expected frequency range, and peak-analysis tasks. Identify settings that change quantitative interpretation rather than only appearance.

## Procedure

Always expose enough transform context to interpret the spectrum: sample rate/source, frequency span, resolution, window, averaging, and amplitude units/reference. Changing display zoom should not silently change transform resolution unless the product intentionally recomputes and says so. Peak markers need frequency/amplitude with method/tolerance, and manual markers must remain distinct from detected peaks. Averaging state should show accumulation progress and reset conditions. Overlays require compatible units/references or explicit normalization. Preserve transform settings with exported or saved analysis.

## Failure topology

Failures include dB values with unknown reference, zoom triggering an invisible FFT change, window function hidden, averaged traces compared with single-shot traces as if identical, aliasing risk undisclosed, peak markers shifting due display interpolation, and spectra exported without transform settings. Another failure is using log axes without clearly treating zero/negative/invalid values.

## Falsification

Reject if a spectrum cannot reveal amplitude units/reference; if transform/window/resolution settings are irrecoverable; if display zoom changes analytical resolution silently; if averaging reset is hidden; if incompatible spectra can be overlaid without warning; or if a peak measurement cannot identify whether it is detected or manually placed.

## Output contract

Return a `spectrum-analysis-interfaces-contract` with: source identity/sample rate; transform method; window; resolution/span; amplitude units/reference; averaging; peak/marker behavior; overlay compatibility; aliasing/data-quality cues; zoom-versus-recompute policy; and saved/export settings. Include one averaged-versus-single-shot comparison.

## Handoffs

Waveform analysis supplies source ranges, live monitoring may stream source data, model fitting can consume peaks/spectra, and provenance records analytical parameters.