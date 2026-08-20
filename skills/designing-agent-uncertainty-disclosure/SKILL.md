---
name: designing-agent-uncertainty-disclosure
description: Surface uncertainty where it changes decisions, scope, or trust without turning every agent response into vague disclaimers or unsupported numeric confidence.
---

# Designing agent uncertainty disclosure

Agents can be uncertain about facts, interpretation, execution outcome, or whether they saw all relevant context. Use this skill when uncertainty should materially influence what the user does next.

## Decision ownership

Own uncertainty categories, display triggers, qualitative wording, placement, and escalation to verification or human review. Decide when uncertainty belongs beside a specific claim or action rather than in a generic footer.

## Inputs and evidence

Collect source quality, retrieval coverage, ambiguous instructions, conflicting evidence, execution acknowledgments, model/tool limitations, and historical false-certainty failures. Distinguish epistemic uncertainty from operational uncertainty such as “the request may have succeeded despite timeout.”

## Procedure

Classify uncertainty by object: fact, interpretation, recommendation, scope coverage, or side-effect outcome. Place disclosure adjacent to the affected claim or action. Explain the reason and, when possible, the next verification step.

Use calibrated qualitative language tied to evidence rather than arbitrary percentages. Avoid repetitive boilerplate when uncertainty does not change user decisions. For high-stakes actions, escalate unresolved uncertainty before mutation.

## Failure topology

Generic disclaimers are easy to ignore. False precision such as “83% confident” may imply measurement that does not exist. Another failure is hiding uncertainty inside long prose while the UI presents a strong action button as if the result were verified.

Over-disclosure can make reliable results seem equally doubtful and reduce usability.

## Falsification

Seed tasks with conflicting sources, ambiguous scope, incomplete retrieval, and ambiguous tool outcomes. Ask users whether they can identify exactly what is uncertain and how to verify it. Compare disclosure frequency against actual error/verification data where available.

## Output contract

Produce an `agent-uncertainty-disclosure-contract` defining uncertainty categories, triggers, placement, wording rules, evidence/reason fields, verification actions, high-stakes escalation, and examples of when disclosure should be omitted.

## Handoffs

Use `designing-agent-confidence-calibration` for systematic confidence behavior, `designing-agent-result-provenance` for evidence linkage, `designing-agent-side-effect-review` for uncertain mutations, and trust/high-stakes skills when stakes are material.