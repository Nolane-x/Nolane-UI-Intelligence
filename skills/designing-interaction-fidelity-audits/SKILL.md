---
name: designing-interaction-fidelity-audits
description: Audit implemented interactions against intended state transitions, timing, input behavior, focus, interruption, and recovery rather than judging fidelity from static appearance.
---

# Designing interaction fidelity audits

A UI can match a design screenshot while behaving differently in ways that change usability. Use this skill when verifying implemented controls, prototypes, or cross-platform ports against an intended interaction contract.

## Decision ownership

Own audit scenarios, reference contract, state-transition comparison, timing/input/focus criteria, deviation severity, and evidence. Decide which differences are intentional native adaptations versus fidelity defects.

## Inputs and evidence

Collect interaction specs, prototypes, recordings, state machines, keyboard/gesture rules, motion timing, focus behavior, error/retry states, and the implemented build. Include edge and interrupted states.

## Procedure

Compare behavior as sequences: trigger, intermediate feedback, state transition, side effect, focus, and recovery. Test pointer, keyboard, touch, and assistive interaction as relevant. Measure timing where latency or motion affects comprehension.

Record deviations with exact reproduction and user consequence. Avoid treating prototype behavior as automatically authoritative if it was only illustrative; resolve conflicts against the canonical interaction contract.

## Failure topology

Static QA misses missing pressed states, wrong focus restoration, or impossible interruption. Another failure is flagging every native-platform difference as a defect even when semantic behavior is equivalent.

Audits may test only successful completion and miss error recovery or rapid repeated input.

## Falsification

Run scripted and adversarial sequences: double activation, Escape, resize, interruption, slow network, errors, and alternate input. Compare recordings frame/state by state where needed. Ask whether each deviation changes user understanding or control.

## Output contract

Produce an `interaction-fidelity-audits-contract` containing reference states, tested sequences, input modalities, timing/focus criteria, deviations, severity/rationale, intentional adaptations, and reproduced evidence.

## Handoffs

Use `designing-ui-regression-evidence` for ongoing gating, motion specialists for timing defects, accessibility specialists for focus/semantics, and `designing-prototype-test-fidelity` when the reference prototype is incomplete.