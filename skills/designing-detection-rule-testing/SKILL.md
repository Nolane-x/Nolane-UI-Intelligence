---
name: designing-detection-rule-testing
description: Use when security teams must evaluate a detection against historical or synthetic evidence and understand coverage, misses, noise, regressions, and deployment readiness before enabling it.
---
# Designing Detection Rule Testing

## Parent Contract

**Required parent:** `designing-security-operations-workspaces`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own the evaluation surface for candidate detection logic. Decide how tests select datasets, label expected matches, compare versions, expose false positives and false negatives, measure data-source coverage, and communicate uncertainty before promotion. This faculty does not author the detection condition and does not decide incident response after a production alert. Its concern is whether the rule behaves as claimed under observable evidence.

## Inputs and evidence

Require rule version, test data provenance, historical time ranges, known-positive examples, benign controls, synthetic fixtures, source coverage, expected grouping behavior, latency constraints, prior production outcomes when available, and any ground-truth limitations. Include datasets with class imbalance, missing telemetry, schema migrations, seasonal behavior, duplicated events, and attacker variations that are semantically similar but syntactically different. Record whether labels come from analyst judgment, confirmed incidents, simulations, or external corpora.

## Procedure

Separate syntax validation from behavioral testing. Run the rule over an explicitly bounded dataset and retain the exact rule version, schema version, query parameters, and time interval. Present matched and unmatched expected positives, unexpected matches, per-source coverage, execution cost, and delay characteristics. Support side-by-side comparison of old versus candidate rules at the event and aggregate levels; a lower alert count is not automatically an improvement if it removes meaningful coverage. Allow analysts to inspect representative examples, annotate label uncertainty, and define acceptance criteria before reading results to reduce hindsight bias. Treat synthetic test success as evidence of plumbing, not proof of real-world detection quality.

## Failure topology

- The interface reports “100% success” because only known-positive fixtures were tested.
- Alert-count reduction is celebrated without showing which behaviors stopped matching.
- Historical replay uses fields or enrichments that were unavailable at event time.
- Label uncertainty disappears and analyst assumptions become fake ground truth.
- A candidate passes on one source while another required source has no data.
- Version comparisons aggregate away entity-level regressions.
- Performance cost is ignored until a rule overloads production execution.

## Falsification

Evaluate a candidate against confirmed positives, benign high-volume traffic, synthetic variations, a period with missing telemetry, and the previous rule version. Introduce one changed field mapping and one intentional exception that suppresses a positive. The design fails if the regression is not obvious, if dataset provenance cannot be reconstructed, or if the pass/fail summary can hide missing evidence.

## Output contract

Return `detection-rule-testing-contract` containing test-dataset ledger, ground-truth confidence, match/miss taxonomy, version-comparison model, coverage and cost measures, acceptance criteria, regression evidence, synthetic-versus-observed distinction, and promotion-readiness findings.

## Handoffs

Rule construction stays with `designing-detection-rule-authoring`; production alert behavior routes to `designing-security-alert-triage`; broader empirical methodology may reuse evaluation faculties, but security-specific label provenance, source coverage, and miss analysis remain owned here.