---
name: designing-reliability-experiment-guardrails
description: Use when this specialist's decision ownership is materially in scope. Own the operator interface for controlled reliability or chaos experiments, emphasizing blast-radius bounds, prerequisites, abort conditions, observation, and evidence rather than experiment execution techniques.
---
# Designing Reliability Experiment Guardrails

## Parent Contract

**Required parent:** `designing-incident-response-operations`.

Inherit the broader routing and decision boundary from this canonical parent; this specialist remains accountable only for the narrower ownership, failure topology, falsification criteria, and output contract defined below.

## Decision ownership

Own safety and evidence boundaries around planned resilience experiments that intentionally perturb a system. Decide target/blast-radius preview, prerequisites, approvals, start conditions, monitoring, abort thresholds, time limit, concurrent-change conflicts, and outcome recording. This skill is interface governance; it does not instruct users how to exploit or damage systems.

## Inputs and evidence

Require experiment definition from an authorized system, target scope, environment, expected hypothesis, allowed impact, monitoring signals, abort thresholds, rollback/recovery capability, owner, approvers, maintenance/change context, and maximum duration. Identify production versus non-production policy differences.

## Procedure

Before start, present hypothesis, exact authorized target scope, expected safe impact, monitoring signals, abort triggers, duration, recovery plan, and conflicting active changes/incidents. Scope selectors must default to the narrowest authorized target and make expansion deliberate. During the experiment, show elapsed time, current affected scope, key health signals, and abort control continuously. Abort should remain available even if telemetry is degraded. Completion separates "experiment ended" from "hypothesis supported" and captures observed evidence plus unintended effects.

## Failure topology

Failures include ambiguous target scope, production experiment launched with stale approval, abort hidden behind navigation, telemetry failure interpreted as healthy, experiment continuing beyond duration, concurrent maintenance confounding results, and completion marked successful solely because the tool ran. Another failure is interface copy that normalizes broad impact rather than emphasizing authorization and bounds.

## Falsification

Reject if the exact target/blast radius cannot be reviewed before start; if scope can expand without new confirmation; if abort becomes unavailable when telemetry disconnects; if missing monitoring appears green; if time limit can expire without an automatic stop/escalation policy; if active incident conflict is not surfaced; or if outcome can be marked validated without evidence.

## Output contract

Return a `reliability-experiment-guardrails-contract` with: hypothesis; authorized target scope; environment; expected impact bound; prerequisites/approval; monitoring signals; missing-telemetry state; abort thresholds/control; duration; concurrent-change checks; recovery plan; outcome evidence; and unintended-effect record. Include one telemetry-loss scenario.

## Handoffs

High-stakes decisions govern authorization, maintenance windows may host planned execution, service health provides observation, incident response takes over unexpected impact, and postmortem follow-up can consume findings. This skill intentionally excludes offensive or exploit instructions.