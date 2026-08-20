---
name: designing-variance-analysis
description: Own financial variance analysis across actual, budget, forecast, prior period, volume/rate/mix or other explainable drivers with sign conventions, materiality, drill-down, and commentary provenance.
---
# Designing Variance Analysis

## Decision ownership

Own comparison of financial measures across two defined bases and decomposition of differences. Decide comparison basis, absolute/percentage variance, favorable/unfavorable semantics, materiality, driver decomposition, period/entity/currency alignment, drill-down, commentary, and unresolved variance state. This owner does not invent causal explanations automatically.

## Inputs and evidence

Require actual/budget/forecast/prior datasets, report/account identities, period/entity/currency basis, sign/favorability rules, driver formulas if used, materiality thresholds, dimensions, and commentary workflow. Identify cases where percentage variance is meaningless due zero/small denominator.

## Procedure

Name both comparison bases explicitly. Compute absolute variance and percentage only when denominator makes sense; represent zero/near-zero cases safely. Favorable/unfavorable depends on account/context, not green/red by arithmetic sign alone. Driver decompositions must expose formulas and reconcile back to total variance, with residual/unexplained amount when incomplete. Allow drill-down by account/dimension to source transactions. Commentary remains attributed human explanation and should not be auto-promoted to fact. Materiality thresholds show why items are prioritized.

## Failure topology

Failures include +10% shown favorable for expenses, division by near-zero producing dramatic percentages, drivers not reconciling, mixed period/currency bases, AI-generated commentary presented as causal truth, and unexplained residual hidden. Another failure is sorting by percentage and surfacing tiny immaterial amounts above large business-impact variances.

## Falsification

Reject if comparison bases are unclear; if percentage is shown with invalid denominator; if favorable semantics ignore account context; if driver sum fails to reconcile without residual; if currency/period mismatch is hidden; or if commentary lacks author/evidence distinction.

## Output contract

Return a `variance-analysis-contract` with: base A/B identity; entity/period/currency; absolute/percentage rules; favorability semantics; materiality; driver decomposition/formulas; residual; drill-down; commentary attribution; and prioritization. Include one near-zero denominator and one unreconciled-driver case.

## Handoffs

Budget planning and financial statements supply comparison sources, ledger browsing supports drill-down, and data visualization renders selected variance encodings.