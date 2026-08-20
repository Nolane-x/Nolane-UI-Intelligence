---
name: designing-usability-test-protocols
description: Design usability protocols that elicit realistic task behavior with controlled prompts, observation criteria, counterbalancing, and evidence suitable for decisions.
---

# Designing usability test protocols

A usability test can easily become a guided demo if prompts reveal labels, paths, or expected behavior. Use this skill to create test protocols that expose how participants actually understand and operate an interface.

## Decision ownership

Own task construction, moderator script, ordering, prompting limits, counterbalancing, observation criteria, recovery rules, and session evidence. Decide what participants may be told before a task and what assistance invalidates unaided success.

## Inputs and evidence

Collect research questions, target population, realistic goals, prototype fidelity, task dependencies, data setup, privacy constraints, and metrics. Identify tasks whose wording repeats UI labels or tells participants exactly where to click.

## Procedure

Write scenario-based goals in participant language. Remove feature names that disclose the path unless discovery is not under test. Define success, partial success, critical errors, abandonment, and assistance thresholds before sessions begin. Order tasks to minimize learning contamination; counterbalance alternatives when comparison would otherwise favor the first experience.

Prepare realistic data and failure conditions. Script neutral prompts for silence or confusion. Capture both behavior and concise post-task reflection without letting opinions overwrite observed performance.

Pilot the protocol and revise ambiguous tasks before formal sessions.

## Failure topology

Leading prompts inflate success. Prototype limitations can be mistaken for design failures, or vice versa. Another failure is changing moderator help across participants, making results incomparable.

Testing too many tasks creates fatigue that contaminates later observations.

## Falsification

Pilot with internal users who do not know the expected route and inspect where wording leaks answers. Have multiple moderators run the same script and compare assistance. Review recordings to verify success coding matches predefined criteria.

## Output contract

Produce a `usability-test-protocols-contract` containing research linkage, participant criteria, scenarios/tasks, success coding, moderator script, assistance rules, ordering/counterbalancing, data setup, pilot findings, and capture plan.

## Handoffs

Use `designing-task-success-measures` for metrics, `designing-behavioral-observation-capture` for logging, `designing-prototype-test-fidelity` for fidelity boundaries, and `designing-research-question-framing` when tasks do not clearly answer the decision.