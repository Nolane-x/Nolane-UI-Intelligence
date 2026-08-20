---
name: designing-design-decision-records
description: Record material UI decisions with context, alternatives, evidence, constraints, consequences, and review triggers so rationale survives team turnover and future change.
---

# Designing design decision records

Design systems and products accumulate choices that later look arbitrary because the evidence and constraints are forgotten. Use this skill for decisions with meaningful tradeoffs, compatibility impact, accessibility implications, or likely future reconsideration.

## Decision ownership

Own decision-record schema, threshold for creating a record, evidence and alternative linkage, status, supersession, and review triggers. Decide which small implementation choices do not deserve durable records.

## Inputs and evidence

Collect the decision question, context, constraints, considered alternatives, research, analytics, standards, prototype evidence, technical limitations, affected components/products, and stakeholder responsibilities. Include uncertainty present at decision time.

## Procedure

Write the decision in concise terms, then record why it was necessary, the alternatives considered, evidence for and against, constraints, chosen option, expected consequences, and what would trigger reconsideration. Link to source evidence rather than copying entire reports.

Use statuses such as proposed, accepted, superseded, or reversed. Never rewrite historical rationale to make past decisions appear more certain; create a superseding record when understanding changes.

Make records searchable by affected surface and decision type.

## Failure topology

Records can become bureaucratic essays nobody reads. Decision logs that capture only the chosen answer become authority assertions rather than learning artifacts. Another failure is deleting or editing old rationale after reversal, erasing institutional learning.

If every tiny visual tweak requires a record, teams will stop maintaining the practice.

## Falsification

Ask a new maintainer to reconstruct a material decision and identify what evidence would justify changing it. Follow links to ensure sources still exist. Review superseded decisions and verify history remains intact. Sample current contentious patterns for missing records.

## Output contract

Produce a `design-decision-records-contract` defining creation threshold, fields, statuses, evidence/alternative links, consequence and review-trigger requirements, supersession semantics, searchability, and examples.

## Handoffs

Use `designing-design-hypothesis-ledgers` for testable assumptions, `engineering-ui-evidence-workflows` for evidence lifecycle, design-system governance for system-level policy, and `designing-ui-regression-evidence` when decisions become release constraints.