---
name: compiling-ui-obligations
description: Use when a routed UI task needs design, interaction, accessibility, fidelity, responsive, content, or system claims converted into explicit pass-fail-unknown obligations.
---

# Compiling UI Obligations

## Overview
An obligation turns “this should be good” into something that can be observed, attacked, and evidenced. It is the bridge between design reasoning and release gating.

## Parent Contract
**Required parent:** `nolane-ui`.

Consume the `ui-contract`, `ui-task-profile`, and specialist outputs available so far. Do not invent obligations unrelated to the contract merely to increase checklist size.

## Obligation anatomy
Every material obligation must declare:
- `id`
- `claim`
- `domain`
- `scope`
- `authority`
- `oracle`: what observation could establish or refute it
- `falsifier`: a concrete counterexample
- `required_evidence_methods`
- `status`: `UNTESTED | PASS | FAIL | UNKNOWN | ACCEPTED_RISK`
- `severity_if_failed`
- `dependencies`

A statement without a falsifier is usually a preference, not a proof obligation.

## Compile by failure surface
Derive obligations from what can go wrong:

### Product/task
Can the primary user find the start point, understand the current state, complete the core task, and recover from likely mistakes without hidden system knowledge?

### Information/hierarchy
Are high-priority facts visible at the decision point? Are labels and grouping semantically true? Can repeated/critical information be scanned and compared?

### Interaction
For every critical control: discoverability, input modality, focus, activation, feedback, async behavior, disabled/permission state, cancellation/undo, and destructive recovery where relevant.

### State coverage
Derive applicable states from the component state algebra rather than a fixed universal list. Obligations must include long content, narrow viewport, and failure states when those can materially change geometry or meaning.

### Visual craft
Avoid subjective “looks premium.” Use concrete obligations such as readable hierarchy, intentional density, coherent typographic roles, consistent alignment, restrained emphasis, and a visual direction traceable to the brief.

### Design system
Repeated semantics must resolve to shared tokens/components or an explicit exception. Token layers may not encode one-off page coordinates as global semantics.

### Accessibility/inclusion
Bind obligations to the relevant standard/platform/source, not to an unlabeled “a11y best practice.” Automated evidence cannot close obligations that require human/semantic judgment.

### Responsive/platform
Define behavior under content growth and viewport reduction, not just a list of device widths. Preserve task priority and interaction semantics across adaptations.

### Fidelity
When a visual target is authoritative, specify allowed and forbidden deltas. A “close enough” tolerance must come from the contract, not convenience.

## Minimality rule
A shorter obligation set that covers material failure modes is stronger than hundreds of trivial checks. Merge duplicates that share the same claim, scope, and oracle. Split an obligation when one half can pass while the other fails.

## Output: `obligation-ledger`
Return ordered obligations grouped by release criticality. Identify which obligations can be closed deterministically, which require runtime evidence, and which require independent human/model judgment.

## Stop conditions
If an obligation has no feasible oracle because a required capability is missing, set it `UNKNOWN` and expose the capability gap. Do not rewrite the claim into something easier to test.

## V6 Obligation Compiler Protocol
Preserve an **obligation provenance chain** from raw request/source/standard/product evidence through interpretation to the normalized obligation. Encode **force-level encoding** (`MUST`, `SHOULD`, preference, hypothesis, forbidden) so a later summary cannot silently weaken “must” into “nice to have.”

Resolve collisions with a **conflict precedence map** based on authority, product truth, safety/accessibility, user intent, platform constraints, and current evidence—not whichever rule appears later. Enforce **waiver prohibition** for non-waivable legal/safety/accessibility/product-truth requirements. Assign a **closure evidence class** describing what can legitimately satisfy each obligation (render, runtime, source audit, usability evidence, normative proof, etc.).

### Falsification
Apply semantic mutations to force words and remove provenance. If downstream routing/gating remains unchanged, obligation compilation is not preserving meaning.

### Recovery
Recompile from the original authoritative source, restore precedence/force, invalidate dependent artifacts, and rerun only affected routes.
