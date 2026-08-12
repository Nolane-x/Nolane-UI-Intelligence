---
name: critiquing-ai-trust-and-agency
description: Use when AI generates consequential content, recommends decisions, calls tools, acts autonomously, mixes human and AI authorship, streams uncertain results, or delegates across agents and the user must retain calibrated trust and control.
---

# Critiquing AI Trust and Agency

## Overview
Independently challenge whether the AI UI encourages appropriate reliance and preserves meaningful human authority. Fluent output and successful demos are not evidence that users understand provenance, uncertainty, delegation, or irreversible action.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

**May modify:** false. Consume the human-AI contract, autonomy envelope, provenance evidence, action ledger, and current rendered behavior where applicable. Missing contracts for agentic action are major findings.

## Decision Model
Inspect four boundaries. **Identity:** can the user tell AI-generated/retrieved/tool-produced/human-edited content apart when that affects a decision? **Epistemic boundary:** are evidence, freshness, uncertainty, and unverifiable claims represented without false precision? **Authority boundary:** does each agent action have an explicit permitted scope and appropriate approval threshold? **Recovery boundary:** can the user interrupt, compare, correct, revert, or understand what cannot be undone?

Adversarially test inference. If a user says “send this to the team,” what defines team? If an agent chooses recipients, budget, environment, or file targets, is that choice visible before consequential action? Standing permission must not silently expand across context changes. Confirmations must occur before external commit and describe the actual inferred target.

Review progress states. “AI working” must not hide tool execution, partial success, or already committed side effects. Stop/cancel language must match reality. Multi-agent interfaces must preserve which agent/tool produced or changed material state and which revision was reviewed.

## Evidence
Use action logs, authorization records, rendered controls, model/tool failure cases, stale-context tests, user comprehension research, and provenance verification. General model safety claims or benchmark scores cannot substitute for interface-specific control evidence.

## Output Contract
Return a `finding-set` with `may_modify:false`, `artifact_revision`, `findings[] {finding_id, severity, evidence, violated_constraint, agency_failure, user_impact, falsifier, recommended_repair, required_reverification}`, `hidden_inferences[]`, `authority_gaps[]`, `provenance_gaps[]`, and `release_recommendation`.

## Failure Traps
- Treating an AI badge as complete transparency.
- “User can undo” when an email/payment was already external.
- One session-level approval covering unrelated future actions.
- Numeric confidence with no calibration basis.
- Reviewer exposing private chain-of-thought as the explanation mechanism.
- Agent identity represented by cute avatars but not responsibility.
- High task-success demo compensating for invisible authority expansion.

Agentic UI cannot pass while consequential authority is ambiguous.