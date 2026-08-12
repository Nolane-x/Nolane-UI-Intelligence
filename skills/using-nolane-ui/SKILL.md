---
name: using-nolane-ui
description: Use when a task materially designs, redesigns, audits, reproduces, implements, or verifies a user interface or user experience.
---

# Using Nolane UI

## Overview
This is the mandatory bootstrap for material UI/UX work. Its only job is to prevent the agent from collapsing product reasoning, visual design, implementation, and verification into one unstructured act.

**Core rule:** invoke `nolane-ui` before material design or implementation. A child skill may strengthen this protocol; it may not waive it.

## Materiality test
Treat the task as material when any of these are true: a new screen or flow is being created; navigation or information hierarchy changes; the visual language changes; a reusable component/system is introduced; a high-fidelity target must be reproduced; accessibility/interaction behavior is consequential; or the result will be shipped rather than used as disposable exploration.

A tiny, local change may take a reduced path only when `nolane-ui` records the scope and why omitted faculties cannot affect the result.

## Absolute constraints
- Build success is not design success.
- Visual attractiveness is not UX correctness.
- Automated accessibility output is evidence, not complete accessibility proof.
- A generator may not certify its own material completion.
- Missing evidence is `UNKNOWN` or `BLOCKED`, never `PASS`.
- User/product requirements outrank aesthetic heuristics.
- Do not load every NUI skill. Route first.

## Start
Hand the task to `nolane-ui` with the user request, known product context, available references, repository constraints, and runtime capabilities.

## Red flags
If you are thinking “the user said just code,” “I can infer the design while implementing,” “it compiles so the UI is done,” or “checking this would take too long,” you are at the exact trigger for this bootstrap. Do not bypass it.
