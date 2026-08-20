---
name: designing-effort-estimation
description: Own capture, communication, aggregation, uncertainty, and revision of project effort estimates without converting weak guesses into false precision.
---
# Designing Effort Estimation

## Decision ownership

Own estimate interaction and semantics: unit, range versus point estimate, confidence, unknown state, who may estimate, revision history, aggregation, and comparison with actuals. This owner does not prescribe story points, hours, t-shirt sizes, or a specific methodology; it makes the chosen model coherent and honest.

## Inputs and evidence

Require estimation unit(s), planning process, team norms, whether estimates are individual or collective, historical data use, uncertainty expectations, parent/child hierarchy, capacity integration, and reporting consumers. Identify whether different teams use incompatible units and prevent accidental aggregation.

## Procedure

Choose one estimate unit per comparable planning context and preserve explicit "unknown/unestimated" rather than zero. Where uncertainty matters, allow ranges or confidence bands instead of forcing a single number. Record estimate revisions when they affect commitments. Aggregation must respect hierarchy: if parent estimates include child work, do not sum both. For relative units, avoid automatic conversion to hours without validated calibration. Actual-versus-estimate comparisons should support learning at aggregate level and avoid turning estimates into performance quotas. Quick estimation interfaces can reduce friction but must still show the current unit and uncertainty.

## Failure topology

Failures include unestimated work counted as zero, story points summed across unrelated teams, parent and child estimates double-counted, estimates treated as deadlines, revision history erased, ranges collapsed into misleading averages, and individual performance inferred from estimate accuracy. Another failure is forcing all work to be estimated before capture.

## Falsification

Reject if unknown values reduce capacity demand as zero; if different units can be aggregated without a clear boundary; if hierarchy rollups double-count; if users cannot tell whether a number is point/range/relative; if estimate changes affecting commitments have no provenance; or if the UI encourages ranking people by estimate variance.

## Output contract

Return an `effort-estimation-contract` with: unit and scope; unknown state; point/range model; confidence; estimation roles; revision history; hierarchy aggregation; cross-team comparability rules; capacity integration; actual comparison; and anti-misuse notes for reporting. Include one unestimated item and one parent/child rollup case.

## Handoffs

Sprint planning and workload balancing consume estimates under this contract. Project health may use aggregate uncertainty but must not treat estimates as certainty. Time tracking provides actual evidence without redefining estimate semantics.