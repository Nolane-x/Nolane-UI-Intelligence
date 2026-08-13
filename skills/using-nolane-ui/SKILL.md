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

## Output: `bootstrap-directive`
Return the bootstrap directive that binds the task to `nolane-ui`, preserving the original request, known context, available references, runtime capabilities, materiality decision, and any justified reduced-scope boundary.

## Red flags
If you are thinking “the user said just code,” “I can infer the design while implementing,” “it compiles so the UI is done,” or “checking this would take too long,” you are at the exact trigger for this bootstrap. Do not bypass it.

## V6 Bootstrap Integrity Protocol
NUI itself can fail before design begins if the bootstrap silently drops facts while converting a request into a route. Build a **task-profile checksum** that restates, in compact structured form, the product surface, user/job, visual ambition, risk, modalities, platform, evidence capabilities, named sources, hard constraints, and unresolved facts. Compare that checksum with the raw request before loading specialist faculties; a mismatch is a routing defect, not an acceptable summary.

Maintain a **route-justification ledger**. Every activated owner records the observed trigger it answers; every plausible high-impact owner that remains inactive records why. This makes progressive disclosure auditable rather than a convenient excuse to omit expensive reasoning. Keep a **capability-evidence boundary** as well: the agent may only promise screenshot inspection, browser execution, repository archaeology, accessibility-tree inspection, performance tracing, or external research when those capabilities actually exist in the current runtime. Missing capability changes the evidence state to UNKNOWN; it never authorizes invented evidence.

For material tasks emit an **omission declaration** listing excluded domains or verification classes that could alter the answer. The declaration is especially important when context limits force a narrower route. If an omission is later discovered to affect product truth, safety, accessibility, or the selected aesthetic thesis, enter the **bootstrap recovery path**: invalidate downstream completion, repair the task profile, reroute from the earliest affected lifecycle state, and preserve already-valid evidence instead of restarting blindly.

### Falsification
Try to falsify the bootstrap by deleting one user constraint, changing one risk/modality field, and adding a named external source after routing. If the route and obligations do not materially react where they should, the bootstrap is under-sensitive. Conversely, inject an irrelevant domain and verify that the router can reject it with a reason rather than loading the entire graph.

### Recovery
When the task-profile checksum or route-justification ledger fails, stop implementation work. Reconstruct the profile from source language, mark uncertain inferences explicitly, rerun routing, and regenerate only artifacts whose parent obligations changed. A bootstrap defect cannot be waived by later visual quality.
