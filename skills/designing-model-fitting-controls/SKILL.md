---
name: designing-model-fitting-controls
description: Own interfaces for fitting analytical or statistical models to scientific data with explicit model form, parameters, bounds, weights, optimizer settings, residuals, uncertainty, convergence, and reproducibility.
---
# Designing Model Fitting Controls

## Decision ownership

Own the human interaction around fitting a declared model to measured data. Decide model selection/form, parameter initial values and bounds, fixed/free parameters, weighting, selected data region, fit execution state, convergence diagnostics, residuals, uncertainty, and saved fit provenance. This owner does not decide which model is scientifically valid.

## Inputs and evidence

Require source data identity, model equations/version, parameters and units, bounds, initial guesses, fit/optimizer algorithm options, weighting/noise model, selected range, convergence criteria, uncertainty/covariance outputs, and computational cost. Identify parameters that are strongly correlated or non-identifiable.

## Procedure

Show the model form and source data before controls. Parameter tables distinguish initial, bound, fixed/free, fitted value, unit, and uncertainty. Validate bounds and unit compatibility. Fit execution should expose progress/cancel for expensive jobs and preserve failed/non-converged attempts. Results must include convergence status, residual views, goodness metrics appropriate to the model, and uncertainty rather than only a smooth curve. Allow comparison of fit attempts with different settings. Saving/exporting a fit includes model/version, data range, algorithm, settings, parameter results, and diagnostics.

## Failure topology

Failures include a fitted curve shown as success despite non-convergence, hidden parameter bounds, uncertainty omitted, optimizer changed with no provenance, residual structure ignored, fitting a filtered/normalized dataset without disclosure, and retry replacing the failed attempt. Another failure is a single goodness score presented as proof the model is scientifically correct.

## Falsification

Reject if convergence status is absent; if fitted parameters lack units/uncertainty where available; if source data/selected range cannot be recovered; if model or optimizer settings are hidden; if failed attempts disappear; if residuals cannot be inspected; or if the UI equates goodness-of-fit with causal/model validity.

## Output contract

Return a `model-fitting-controls-contract` with: source data/range; model/version/form; parameter schema; initial/bounds/fixed state; weighting; optimizer/settings; execution state; convergence; fitted values/uncertainty; residual diagnostics; goodness metrics with limits; attempt history; and reproducible export. Include one non-converged attempt.

## Handoffs

Waveform/spectrum/microscopy provide source data, experiment comparison compares fit results, parameter sweeps may generate datasets, and provenance records model/algorithm versions.