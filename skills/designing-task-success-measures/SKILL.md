---
name: designing-task-success-measures
description: Define task-success measures that capture outcome, assistance, efficiency, error, confidence, and consequence without reducing usability to a single completion percentage.
---

# Designing task success measures

“Completed the task” can hide severe confusion, dangerous mistakes, or moderator rescue. Use this skill when research or product analytics needs a precise success model for UI tasks.

## Decision ownership

Own success states, partial-success criteria, critical errors, assistance treatment, efficiency measures, and aggregation. Decide which outcomes are binary, graded, time-sensitive, or safety-sensitive.

## Inputs and evidence

Collect task goals, required end state, acceptable alternate paths, domain risks, expected duration, common errors, help mechanisms, and user roles. Identify tasks where a superficially correct outcome can be achieved with a harmful intermediate action.

## Procedure

Define observable end-state criteria first. Add categories such as unaided success, assisted success, partial completion, wrong-but-recoverable outcome, critical error, and abandonment when they change interpretation. Record time or steps only where efficiency matters and learning effects are controlled.

Separate user confidence from actual success; overconfident errors are often important. For high-stakes tasks, weight critical mistakes explicitly rather than allowing them to disappear inside average completion rates.

Document how retries and self-recovery are scored.

## Failure topology

Binary completion overstates usability. Time-on-task can punish careful users or reward reckless shortcuts. Another failure is averaging across tasks with radically different consequence and difficulty.

Moderator assistance may be counted as success if coding rules are vague.

## Falsification

Apply the rubric to recorded sessions using multiple coders and measure disagreement. Seed edge cases: completed after wrong irreversible action, completed with heavy help, abandoned after correct setup, or completed slowly but safely. Revise categories until materially different outcomes remain distinguishable.

## Output contract

Produce a `task-success-measures-contract` defining outcome taxonomy, critical errors, assistance/retry treatment, efficiency measures, confidence relationship, aggregation rules, and coded examples for ambiguous cases.

## Handoffs

Use `designing-usability-test-protocols` for task setup, `designing-behavioral-observation-capture` for raw events, `designing-experiment-guardrail-metrics` for production experiments, and high-stakes specialists for consequence weighting.