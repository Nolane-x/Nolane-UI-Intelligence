---
name: designing-blocker-and-risk-registers
description: Own project blocker and risk records, including probability/impact evidence, mitigation, ownership, linkage to work, aging, escalation, and conversion from risk to active issue.
---
# Designing Blocker and Risk Registers

## Decision ownership

Own structured project uncertainty and impediment tracking. Decide the distinction between blocker, issue, risk, assumption, and dependency; impact/probability representation; owner; mitigation/contingency; linked work; review cadence; aging; escalation; and closure. This owner prevents risk from becoming a free-text color label disconnected from project action.

## Inputs and evidence

Require organizational risk terminology, impact dimensions, probability approach, severity thresholds if any, blocker linkage, mitigation workflow, review cadence, escalation policies, and project/portfolio rollup needs. Determine whether quantitative scoring is valid or whether ordinal categories are more honest.

## Procedure

Separate active blockers from future risks. Capture a concise statement, affected outcome/work, evidence, owner, impact, probability/confidence, mitigation, trigger, and next review. If a matrix or score is used, expose its factors and avoid implying scientific precision. Aging and stale review dates should surface neglected records. When a risk materializes, convert or link it to an active issue/blocker while preserving the original forecast history. Closing requires outcome or rationale; "ignored" should not disappear from portfolio evidence.

## Failure topology

Failures include risk registers that are static spreadsheets, red/yellow/green with no evidence, high risks with no owner, mitigations not linked to work, stale risks appearing current, duplicate blocker/dependency records, and realized risks losing their forecast history. Another failure is gamifying teams toward low reported risk rather than honest visibility.

## Falsification

Reject if a high-impact risk can exist with no owner or next review; if a score cannot show its factors; if stale records are visually indistinguishable from recently reviewed ones; if converting a risk to an issue erases original probability/trigger evidence; if mitigation work cannot be opened; or if portfolio rollup counts duplicates as separate risks.

## Output contract

Return a `blocker-and-risk-registers-contract` with: record taxonomy; required evidence; impact/probability model; owner; mitigation/contingency links; trigger; review cadence; aging/stale cues; conversion-to-issue behavior; closure outcome; deduplication/rollup identity; and escalation thresholds. Include one realized risk and one stale high-risk case.

## Handoffs

Dependency networks own structural blockers, project health consumes risk signals, portfolio rollups aggregate identity-aware risks, and incident operations take over when an operational event becomes active.