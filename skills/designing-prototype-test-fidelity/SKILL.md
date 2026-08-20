---
name: designing-prototype-test-fidelity
description: Match prototype fidelity to the research question so participants experience the behaviors under test without mistaking missing implementation for design intent.
---

# Designing prototype test fidelity

Higher fidelity is not automatically better. Use this skill when deciding how much visual, data, interaction, latency, error, or system behavior a prototype must reproduce for valid testing.

## Decision ownership

Own fidelity dimensions, question-to-fidelity mapping, simulation boundaries, participant briefing, and invalid-observation criteria. Decide which missing behaviors must be implemented versus explicitly excluded from interpretation.

## Inputs and evidence

Collect research questions, critical interaction states, target platform, realism needs, data sensitivity, prototype tooling limits, time, and known differences from production. Identify behaviors such as keyboard focus, drag, autocomplete, latency, or error recovery that static screens cannot represent credibly.

## Procedure

Decompose fidelity into visual, interaction, content/data, system response, performance/latency, and platform fidelity. Implement the dimensions required to answer the question. A navigation-label study may need low visual fidelity; a drag-and-drop study needs realistic input behavior; trust testing may require realistic error and loading states.

Document prototype gaps for moderators and analysts. During sessions, distinguish participant failures caused by prototype limitations from target-design failures.

## Failure topology

Polished visuals can cause teams to overtrust a prototype whose behavior is fake. Low-fidelity click-throughs can make participants fail tasks that depend on typing, scrolling, or system feedback. Another failure is telling participants so much about limitations that prompts them toward the intended path.

## Falsification

Pilot tasks and record every moment the moderator must say “pretend this works.” Frequent intervention indicates insufficient fidelity. Compare key behaviors with production or platform conventions. Identify findings that would reverse if missing behavior were real; treat those as invalid until retested.

## Output contract

Produce a `prototype-test-fidelity-contract` containing research questions, required fidelity by dimension, implemented states, known gaps, moderator guidance, invalidation rules, and pilot evidence.

## Handoffs

Use `designing-usability-test-protocols` for tasks, `designing-interaction-fidelity-audits` for behavior matching, `designing-content-fidelity-audits` for realistic copy/data, and research-question framing when fidelity demands are unclear.