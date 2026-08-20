---
name: designing-design-hypothesis-ledgers
description: Maintain design hypotheses as explicit, testable claims with evidence, confidence, status, dependencies, and decisions so assumptions do not silently harden into doctrine.
---

# Designing design hypothesis ledgers

Teams carry many beliefs about users and interfaces that are never written down. Use this skill when a project needs durable tracking from assumption through evidence and eventual validation, revision, or rejection.

## Decision ownership

Own hypothesis schema, falsifiability, confidence/status, evidence linkage, dependency, owner, and lifecycle. Decide when a statement is too broad or normative to function as a testable hypothesis.

## Inputs and evidence

Collect assumptions from design reviews, product strategy, journey maps, research plans, experiments, support knowledge, and analytics interpretation. Identify statements framed as facts despite weak evidence.

## Procedure

Write hypotheses as specific claims about population, context, behavior or outcome, and intervention/mechanism where relevant. State what evidence would challenge them. Link supporting and conflicting evidence without deleting history when confidence changes.

Track status such as untested, testing, supported, challenged, rejected, or superseded. Record decisions made under uncertainty and the confidence at that time. Close or split hypotheses when scope changes rather than silently rewriting them.

## Failure topology

A ledger can become a backlog of vague statements like “users want simplicity.” Confidence scores can create fake precision. Another failure is only storing successful hypotheses, erasing learning from rejected ideas.

Dependencies matter: a downstream design assumption may remain marked supported after its parent assumption is overturned.

## Falsification

Select hypotheses and ask independent reviewers what observation would falsify them. If no clear answer exists, rewrite. Remove or overturn an upstream hypothesis and inspect dependent items. Audit whether current UI decisions still rely on hypotheses marked weak or stale.

## Output contract

Produce a `design-hypothesis-ledgers-contract` defining hypothesis fields, falsification criteria, status/confidence model, evidence and dependency links, ownership, change history, and review cadence.

## Handoffs

Use `designing-research-question-framing` to turn hypotheses into studies, `designing-a-b-test-interpretation` for experiment evidence, `designing-design-decision-records` for decisions, and `engineering-ui-evidence-workflows` for system integration.