---
name: modeling-aspirational-identity
description: Use when a product should let users feel like a more powerful, expert, creative, authoritative, or otherwise aspirational version of their actual role.
---

# Modeling Aspirational Identity

## Parent Contract
**Required parent:** `modeling-users-and-tasks`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own the experiential model of role fantasy: `actual_role`, `aspirational_role`, `status_projection`, `power_perception`, `agency_expression`, `competence_signaling`, `rituals_of_use`, `institutional_presence`, `emotional_reward`, and `symbolic_objects`. Do not fabricate permissions or capabilities the product does not have.

## Product Truth
Aspirational identity is created by what the interface lets a person oversee, orchestrate, understand, delegate, and ritualize—not by a badge that says “Principal Researcher”. High-status UX without actual agency becomes costume.

## Decision Model
Map desired identity to legitimate product affordances. A principal-scientist fantasy may be supported by strategic overview, research-program orchestration, lineage, delegations, discoveries, high-value alerts, institutional scale, and authoritative actions. Separate symbolic reinforcement from functional authority and ensure both are truthful. `power_perception` must come from controllable scope and consequence, not intimidation or clutter. Define rituals_of_use that reinforce mastery through repeated meaningful actions.

## Evidence
For each identity claim record the product capability that supports it, the surface where it appears, the action or information that expresses agency, and the emotional reward expected. Unsupported status projection is a finding.

## Output Contract: `aspirational-identity-model`
Return the canonical `aspirational-identity-model` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
Role title as decoration; fake command-center visuals without authority; granting visual status by reducing legibility; inventing organizational scale; confusing complexity with competence; using exclusive language that harms accessibility or ordinary users.
