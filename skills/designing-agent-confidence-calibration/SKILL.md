---
name: designing-agent-confidence-calibration
description: Calibrate agent confidence cues against observed reliability and evidence so stronger presentation corresponds to better-supported outcomes.
---

# Designing agent confidence calibration

Confidence presentation is useful only if it correlates with actual reliability. Use this skill when an agent ranks options, marks answers as verified, exposes confidence bands, or changes interaction based on certainty.

## Decision ownership

Own the mapping from evidence/reliability signals to confidence presentation, calibration measurement, thresholds for verification, and product behavior at different confidence levels. Decide whether explicit confidence should be shown at all for a task class.

## Inputs and evidence

Collect historical outcomes, correctness labels, tool verification, source agreement, retrieval completeness, model self-ratings if any, domain-specific validation, and user decisions influenced by confidence cues. Separate measured calibration signals from generated verbal confidence.

## Procedure

Prefer observable evidence features over unsupported self-assessment. Define confidence bands only where outcomes can be evaluated. Measure calibration: among items labelled high confidence, error rates should actually be lower. Use confidence to route behavior—such as requesting review or running extra verification—not merely to decorate answers.

Where ground truth is unavailable, disclose evidence strength or verification status instead of pretending to know calibrated probability.

Avoid mixing confidence about factual correctness with confidence that an external action completed.

## Failure topology

Agents often sound confident regardless of correctness. Numeric confidence without empirical calibration misleads. Another failure is a badge like “verified” that only means a tool ran, not that the output matched expected state.

Confidence cues can become self-fulfilling if users stop checking high-confidence outputs, reducing feedback on failures.

## Falsification

Evaluate confidence bands against held-out outcomes and reliability diagrams where feasible. Inject adversarial ambiguous cases and inspect whether confidence drops appropriately. Compare user behavior with and without cues to detect overreliance.

If no measurable outcome exists, remove numeric confidence and use explicit evidence/status instead.

## Output contract

Produce an `agent-confidence-calibration-contract` defining eligible task classes, signal sources, confidence bands, measured calibration, behavioral thresholds, verification escalation, and prohibitions on unsupported certainty claims.

## Handoffs

Use `designing-agent-uncertainty-disclosure` for claim-level communication, `designing-agent-result-provenance` for evidence, `engineering-ui-evidence-workflows` for evaluation data, and high-stakes review patterns when errors carry serious consequence.