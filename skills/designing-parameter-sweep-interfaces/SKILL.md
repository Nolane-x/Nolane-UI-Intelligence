---
name: designing-parameter-sweep-interfaces
description: Own configuration and review of multi-run parameter sweeps across dimensions, ranges, sampling strategy, run count, resource bounds, validity, progress, and result indexing.
---
# Designing Parameter Sweep Interfaces

## Decision ownership

Own design of experiments where one or more parameters vary across many runs. Decide sweep dimensions, range/list/distribution definitions, combination strategy, generated run count, constraints, resource estimate, invalid combinations, execution progress, and mapping from result back to parameter point. This owner does not optimize the scientific strategy itself.

## Inputs and evidence

Require parameter schema/units/bounds, discrete/continuous types, allowed combinations, sweep strategies (grid/random/other authorized), resource/time cost estimates, parallelism, run manifest template, failure policy, and result metrics. Identify combinatorial explosions before execution.

## Procedure

Make each sweep dimension explicit with unit and valid domain. Continuously calculate generated run count and estimated resource envelope as dimensions change. If constraints eliminate combinations, show retained/skipped counts and reasons. Provide a preview table or sampled points before launch. Execution view should show queued/running/completed/failed counts and permit mapping any run back to exact parameter values. Failed runs remain in the design space and are not silently omitted from visual result surfaces. Changes to the sweep after execution begins create a new sweep version.

## Failure topology

Failures include accidental combinatorial explosion, units mixed across range endpoints, invalid parameter combinations discovered only after costly execution, failed runs missing from plots, random sweeps unreproducible due absent seed, and editing a live sweep changing the interpretation of completed results.

## Falsification

Reject if total run count/resource estimate is unknowable before launch; if parameter bounds/units are not validated; if skipped/invalid combinations are hidden; if a result cannot map to exact parameter values; if stochastic sampling lacks reproducibility metadata where required; or if live sweep edits mutate the existing design identity.

## Output contract

Return a `parameter-sweep-interfaces-contract` with: sweep identity/version; dimensions/units/domains; sampling/combination strategy; seed if applicable; constraints; generated/skipped count; resource estimate; preview; execution counts; failure inclusion; run-to-parameter mapping; and version-on-edit behavior. Include one 5-dimensional explosion example.

## Handoffs

Experiment setup supplies the run template, run control executes instances, comparison/result visualization consumes completed/failed points, and model fitting may summarize response surfaces.