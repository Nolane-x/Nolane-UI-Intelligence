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

## V6 Identity, Status and Competence Model
Model aspiration through behavior and ritual, not luxury clichés. Identify the user's current role, desired role, feared identity, authority boundaries, expertise signals, social audience, and moments where the interface can let the user *feel* more capable. A **competence ritual** is a repeatable sequence whose interaction form reinforces mastery: scanning a complex field efficiently, commanding a system through a palette, comparing scenarios, manipulating a model directly, or confirming a high-stakes choice with informed control.

Separate status from ornament. A **status projection trap** occurs when dark chrome, gold accents, glass, monospaced labels, dense telemetry, or oversized institutional branding are used to manufacture prestige without changing agency or competence. Status should emerge from information command, precision, trustworthy feedback, authorship, speed, and ownership of consequences where the product truly supports them.

Design **power without false capability**. The UI may make real capability legible and satisfying, but must never imply permissions, certainty, automation, precision, safety or control that the system does not possess. In agentic products, apparent command must be coupled to authority boundaries, provenance, reversibility and human confirmation.

Run an **identity contradiction** analysis: which product states make the user feel like the opposite of the desired role? A principal scientist UI that buries evidence behind decorative dashboards creates novice dependence. A creative expert tool that interrupts every action with tutorials creates learner identity. A calm clinical system that dramatizes every anomaly creates panic rather than professional composure.

Perform a **symbolic object audit**. Identify domain-native objects that carry meaning—samples, timelines, layers, runs, specimens, ledgers, canvases, scenes, tracks, commands, cohorts—and test whether the visual/interaction system gives these objects appropriate presence. Prefer authentic symbolic objects over generic “premium” decoration.

### Falsification
Remove decorative prestige cues while keeping task structure. If aspiration disappears completely, the model was superficial. Then hide job-title labels and marketing copy; if users/critics cannot infer the intended agency and competence from interaction structure, the role fantasy has not been operationalized.

### Recovery
If identity cues conflict with real authority or create intimidation, dependency, or performative complexity, rebuild around genuine competence rituals and symbolic objects. Escalate to product intent when the desired identity requires capabilities the product does not actually provide.
