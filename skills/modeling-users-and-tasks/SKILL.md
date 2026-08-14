---
name: modeling-users-and-tasks
description: Use when UI structure, density, explanation, shortcuts, defaults, or safety behavior depends on who uses the product and how often or under what pressure they perform a task.
---

# Modeling Users and Tasks

## Overview
Users are not personas made of adjectives. Model the capabilities, frequency, context, incentives, and error costs that change interface behavior.

## Parent Contract
**Required parent:** `routing-ui-work`.

Use actors and outcomes from the UI contract/product model. Do not invent demographic detail unless it affects the interaction.

## User/task dimensions
For each material actor record:
- domain expertise: novice / intermittent / expert, with evidence
- product familiarity: first-use, occasional, daily, continuous
- task frequency and repetition
- time pressure and interruption rate
- consequences of error or delay
- input environment: keyboard-heavy desk, touch, mobile one-handed, kiosk, assistive technology, noisy/low-connectivity context
- information needed to decide vs information merely available
- likely shortcuts, automation, bulk actions, or comparison needs
- authority and permission boundaries

## Progressive disclosure by learning curve
Do not equate “simple” with “few controls.”

For novices, reduce simultaneous choices, explain consequences at decision points, provide safe defaults, and preserve discoverable pathways.

For experts, optimize repeated paths: keyboard access, stable positions, dense scanning, bulk operations, persistent filters, predictable state, and low interruption. Do not force expert users through decorative onboarding or repeated confirmations for reversible actions.

When both populations matter, design layers rather than a compromised middle: safe defaults and clear labels on the surface, advanced controls and shortcuts discoverable without dominating novices.

## Task decomposition
For each critical job capture:
- trigger: what makes the user start
- input information already known
- decisions the user must make
- system feedback needed to maintain orientation
- commit points and irreversible boundaries
- recovery paths
- completion evidence the user needs
- next likely action

Distinguish **task sequence** from **screen sequence**. Multiple task steps may live on one screen; one conceptual step may require multiple surfaces only when interruption or complexity justifies it.

## Attention budget
Classify information as `must-see-now`, `needed-to-decide`, `available-on-demand`, or `rare/administrative`. Visual hierarchy and disclosure must follow this budget. Do not use identical card weight for all four classes.

## Error ecology
Model likely human mistakes, not only invalid input:
- wrong target selected
- stale context
- mode confusion
- accidental repeat action
- misread units/time zones
- destructive action under pressure
- permission misunderstanding
- leaving with unsaved work

Design should make expensive mistakes difficult and cheap mistakes easy to recover from.

## Output: `user-task-model`
Return `actors`, `context_dimensions`, `critical_jobs`, `attention_budget`, `learning_curve`, `error_ecology`, `expert_accelerators`, `novice_support`, `permission_boundaries`, and `design_implications`.

## Common failures
- Persona theater: inventing age/name/preferences unrelated to design.
- Designing every task for a first-time user.
- Treating information density as inherently bad.
- Requiring confirmations for every action rather than matching reversibility and cost.
- Assuming desktop equals mouse.

## V5 Aspirational Identity Trigger
Task efficiency does not exhaust user modeling. When the brief contains **aspirational identity**, status projection, “feel like”, authority, mastery, institutional power, or **role fantasy**, route `modeling-aspirational-identity`. Preserve the distinction between actual role and aspirational role. The resulting experience must be backed by truthful agency, overview, orchestration, lineage, rituals or symbolic objects rather than titles/badges alone.

## V6 User/Task Model Protocol
Maintain **role-vs-persona distinction**: permissions/responsibility/authority are roles; behavior/motivation/context patterns may form personas/segments. Model **expertise trajectory** from first use through frequent expert use, including shortcuts, automation, error recovery, and changing information needs.

Assign a **task-criticality map** by frequency, consequence, time pressure, reversibility, collaboration, and environmental context. Ensure **edge-user inclusion** for disabled users, unusual permissions, high volume, constrained devices, and domain-expert edge cases whose failures can expose structural problems. Bind each claim to **behavior-evidence trace** from observation, product data, user statement, or explicit hypothesis.

### Falsification
Find a real role/context whose job cannot be represented without changing the flow/IA. If the model calls them an outlier despite material product scope, it is too narrow.

### Recovery
Split/refine roles/tasks, update evidence status, and reroute affected product/interaction decisions.

## V9 Audience Strategy Sensitivity
In addition to operational roles, model the **decision posture** that changes what “good design” means for the audience. Do not infer taste from demographics. Record whether the experience is primarily `trust-first`, `delight-first`, `speed-first`, `comprehension-first`, `precision-first`, `exploration-first`, or a justified combination, then tie that posture to actual tasks and consequences.

Distinguish a founder/owner who wants fast system overview from a mass consumer who needs recognition and confidence, a professional creator who needs dense precision from a casual creator who needs progressive discovery, and an operator who needs exceptions/history from an executive who needs decision compression. The same feature set can require radically different density, explanation, action exposure and visual tone.

For each material audience profile record `expertise`, `primary_intent`, and `decision_mode`, plus the evidence status for each assumption. Ask whether the person is buying quickly or reading deeply, comparing or creating, monitoring or acting, exploring or completing a known task, and whether trust, emotional delight, status, mastery, calm or speed should dominate. Translate these into design consequences rather than persona adjectives.

Use domain signatures as a prior, not destiny. Fintech often raises trust/precision needs; creative tools often raise agency/flow; education often raises scaffolding/cognitive load. But a consumer investing app and an institutional trading console should not inherit one visual-density signature just because both are “fintech.” Product-local role and task evidence override generic domain expectation.

When audiences conflict, create layered access rather than averaging them into a mediocre middle. Keep essential meaning stable while varying default density, progressive disclosure, shortcut exposure, onboarding, explanation depth, workspace persistence or role-specific home surfaces where justified. Personalization cannot hide safety/trust essentials.

### V9 Falsification
Take one visually strong proposal and test it against two materially different audiences who share the product. If no hierarchy, density, explanation, control exposure or trust behavior needs to change, the audience model is probably decorative. Also swap `trust-first` and `delight-first`; if the design consequences remain identical, the strategic label has no causal value.

### V9 Recovery
Return to jobs, consequence and expertise; split the audience model where behavior truly differs, update attention budgets and progressive disclosure, then reroute aesthetic/domain decisions. Do not fix an audience mismatch by merely changing colors, illustrations or marketing copy.
