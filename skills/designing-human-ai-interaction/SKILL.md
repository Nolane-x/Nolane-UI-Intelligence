---
name: designing-human-ai-interaction
description: Use when a UI includes predictions, recommendations, generation, classification, conversational AI, model-assisted decisions, or adaptive behavior whose uncertainty and failure modes change how users should understand and control the system.
---

# Designing Human-AI Interaction

## Overview
Design the relationship between human judgment and probabilistic capability. Good AI UI sets realistic expectations before use, supports efficient collaboration during use, and makes error correction cheaper than blind trust.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require the AI role, user goal, consequence of wrong output, model capabilities/limitations, latency, data sensitivity, and whether output is advisory or can trigger actions. Agentic work routes additionally to autonomy control.

## Decision Model
Define the user’s mental model in three phases. **Before interaction:** what the system can and cannot do, what inputs it uses, whether content is generated, and what the person remains responsible for. **During interaction:** what the AI is doing, what context it is using, how long it may take, and how the user can steer or stop it. **After output:** how to inspect, verify, edit, compare, reject, report, or recover.

Calibrate reliance to consequence. A low-risk suggestion can optimize flow and learn from dismissal. A medical, financial, legal, or destructive recommendation needs stronger provenance, uncertainty treatment, independent verification, and may never be allowed to become silent authority. Do not use anthropomorphic confidence or fluent prose as evidence of correctness.

Expose enough model status to support decisions without turning the UI into ML diagnostics. Show why a recommendation matters when the explanation changes action; otherwise prioritize useful evidence and controls over decorative “AI reasoning.” Provide non-AI or manual fallback where feasible when AI availability or trust is not guaranteed.

Make correction part of the primary workflow. The UI should accept edits, preference signals, selection among alternatives, or explicit rejection without forcing the user to start over.

## Evidence
Use task-specific model evaluation, user research on reliance/calibration, error cases, latency behavior, feedback use, accessibility, and product telemetry that distinguishes acceptance from successful outcome. General benchmark scores do not prove fitness for this interface task.

## Output Contract
Return a `human-ai-contract` with `ai_role`, `user_responsibility`, `capabilities[]`, `limitations[]`, `expectation_setting`, `interaction_states[]`, `reliance_risk`, `steering_controls[]`, `verification_support[]`, `correction_paths[]`, `fallback`, and `human_ai_tests[]`.

## Failure Traps
- Magic sparkle icon as the entire AI explanation.
- Fluent output presented as authoritative truth.
- Hiding generated origin to make content feel seamless.
- No manual path when the AI is unavailable.
- Asking for feedback but providing no visible effect or recovery.
- One global AI disclaimer instead of task-relevant limitation.
- Treating model benchmark accuracy as user-task safety.

The interface should make appropriate reliance easier than either reflexive trust or reflexive distrust.