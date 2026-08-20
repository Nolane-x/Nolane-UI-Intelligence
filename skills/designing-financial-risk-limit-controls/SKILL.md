---
name: designing-financial-risk-limit-controls
description: Own governed financial exposure and transaction limits, including metric definition, scope, utilization, warning/breach states, effective dates, approval, override, reset, and evidence without recommending financial decisions.
---
# Designing Financial Risk Limit Controls

## Decision ownership

Own the UI for configured financial risk limits that constrain operations such as position, notional, concentration, loss, currency exposure, or order size. Decide metric/denominator, scope, threshold bands, utilization, warning/breach, effective dates, authority, change approval, override/break-glass, and audit. This owner does not choose optimal limits or provide investment guidance.

## Inputs and evidence

Require limit type/metric definition, entity/account/book/instrument scope, currency/valuation basis, threshold, soft/hard behavior, current exposure, data freshness, effective period, approvers, override policy, reset cadence, and downstream order/control actions. Identify aggregate limits dependent on stale market prices.

## Procedure

State the metric and scope in operational terms, not just a number. Show current utilization with amount and denominator; stale/unknown exposure prevents false green. Distinguish advisory warning, soft breach requiring approval, and hard block according to policy. Limit changes bind to version/effective time and preserve prior values. Override requires exact transaction/scope or bounded duration, authority, reason, and expires automatically where applicable. Order/deployment-style actions blocked by a limit should link to the relevant limit and current exposure evidence.

## Failure topology

Failures include green utilization from stale prices, one limit applied to wrong account/entity, percent utilization with unknown denominator, override becoming permanent, limit edit changing historical breach interpretation, and hard block surfaced only as generic "not allowed". Another failure is presenting a risk-limit warning as a recommendation to trade less/more rather than a policy constraint.

## Falsification

Reject if metric/scope/valuation basis is unknown; if stale exposure can show safe state; if warning/soft/hard semantics are conflated; if limit changes lack effective-version history; if override lacks authority/reason/expiry; if blocked action cannot reveal the governing limit; or if UI language recommends investment action.

## Output contract

Return a `financial-risk-limit-controls-contract` with: limit identity/type; metric/denominator; scope; currency/valuation source/freshness; threshold bands; current exposure/utilization; warning/breach/block states; version/effective dates; approval; override scope/expiry; audit; and non-advice boundary. Include one stale-market-data and one temporary-override case.

## Handoffs

Portfolio positions/FX exposure supply metrics, trading order entry consumes pre-trade checks, approval/high-stakes owners govern overrides, and organization permissions define who may configure limits.