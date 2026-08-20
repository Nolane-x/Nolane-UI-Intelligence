---
name: engineering-ui-evidence-workflows
description: Engineer the evidence lifecycle that connects UI hypotheses, observations, experiments, rendered verification, decisions, and follow-up into an auditable product-learning system.
---

# Engineering UI evidence workflows

UI quality degrades when research, analytics, design review, accessibility findings, and regression evidence live in separate silos that cannot influence decisions coherently. Use this skill to design the end-to-end evidence system rather than a single research method.

## Decision ownership

Own evidence classes, capture standards, provenance, confidence, linkage from hypotheses to observations and decisions, retention, and closure criteria. Decide what qualifies as evidence versus opinion, assumption, or unresolved question and how contradictory evidence is represented.

## Inputs and evidence

Collect existing research repositories, experiment dashboards, usability notes, analytics events, visual regression artifacts, accessibility audits, design review comments, support cases, and decision records. Map where evidence is lost between collection and product change.

## Procedure

Define a common evidence object with source, date, scope, method, population or environment, observation, interpretation, confidence, and linked decision. Keep raw observation distinct from synthesis. Connect hypotheses to the evidence that supports or challenges them and to the product decision that followed.

Create intake paths for qualitative, quantitative, rendered, and normative evidence without pretending they are interchangeable. Establish review and expiry rules for evidence that can go stale. Require unresolved contradictions to remain visible rather than averaging them away.

Make evidence retrieval task-oriented so teams can answer “why does this pattern exist?” and “what would falsify it?” quickly.

## Failure topology

A repository of screenshots without method or context creates anecdote, not evidence. Over-standardizing all methods into one confidence score hides important differences. Another failure is evidence accumulation without decision linkage, producing research archives that teams rarely consult.

Stale findings can remain authoritative after product or population changes.

## Falsification

Trace several current UI decisions backward to evidence and forward to verification. Pick conflicting studies and verify the workflow preserves disagreement. Remove a key assumption and check whether dependent decisions become visibly unsupported. Ask a new team member to reconstruct why a decision exists without private verbal context.

## Output contract

Produce a `ui-evidence-workflows-contract` defining evidence types, required metadata, observation/interpretation separation, hypothesis/decision links, confidence and contradiction handling, retention/expiry, retrieval, and audit scenarios.

## Handoffs

Use the specialist research skills for protocols, observation, synthesis, experiments, regression, fidelity, accessibility evidence, and decision records. Use `designing-ui-research-repositories` for the storage/retrieval surface.