---
name: designing-time-tracking-workflows
description: Own project time-entry and timer interactions, including attribution, rounding, corrections, approvals, overlapping timers, privacy, and planned-versus-actual comparison.
---
# Designing Time Tracking Workflows

## Decision ownership

Own how users record actual time against project work. Decide timer versus manual entry, required attribution, start/stop state, overlap policy, rounding, edit/correction, notes, approvals, locking periods, and how actual time compares with estimates. This owner does not decide payroll or billing policy; it exposes those consequences when integrations make them relevant.

## Inputs and evidence

Require time-entry granularity, allowed work targets, timer support, rounding policy, overlapping-work policy, timezone/date rules, approval/locking process, privacy expectations, billing/payroll integrations, and reporting cadence. Determine whether time tracking is mandatory compliance, optional planning evidence, or personal productivity.

## Procedure

Make the currently running timer persistent enough to prevent accidental forgetting, with explicit work-item attribution and elapsed time. Starting a second timer must follow a defined policy: stop previous, allow overlap, or ask. Manual entry should separate duration from start/end when precision is unnecessary. Corrections need history after approval or lock. If rounding occurs, show recorded versus rounded value before submission when it affects billing/payroll. Planned-versus-actual views should compare compatible units and avoid judging individuals from noisy estimates. Privacy rules must limit who sees detailed notes or activity patterns.

## Failure topology

Failures include invisible running timers, overlapping entries double-counting time, timezone boundaries assigning work to the wrong day, edits after approval erasing history, rounding surprises, timers continuing on deleted/closed work items, and managers using precise-looking utilization from optional incomplete tracking. Another failure is forcing minute-level detail for planning use cases that need only rough actuals.

## Falsification

Reject if users can unknowingly run two forbidden timers; if a timer can continue after its work item becomes inaccessible with no recovery; if rounding changes submitted totals without preview; if approved entries can be altered with no audit; if timezone changes can duplicate/misdate entries; or if optional/incomplete data is presented as comprehensive utilization.

## Output contract

Return a `time-tracking-workflows-contract` with: entry modes; work attribution; timer persistence; overlap policy; timezone/date basis; rounding display; edit/correction history; approval/lock states; closed-item behavior; privacy scope; planned-versus-actual comparison; and missing-data disclosure. Include one overnight/timezone and one correction-after-approval scenario.

## Handoffs

Use effort estimation for planned values, financial operations only when time feeds billing/accounting, approvals for governed submission, and project health cautiously when time data is sufficiently complete.