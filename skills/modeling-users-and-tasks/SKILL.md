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
