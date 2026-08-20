---
name: designing-design-to-code-handoffs
description: Use when authored design intent must become production UI code and the workflow must preserve component identity, tokens, responsive rules, interaction states, accessibility intent, assets, exceptions, and later drift evidence rather than exporting pixels or generated markup blindly.
---

# Designing Design to Code Handoffs

Design-to-code is a translation of intent across representations. The handoff is successful when implementation can reconstruct the intended component, token, responsive, state, content, interaction, and accessibility decisions—not when generated code happens to resemble one screenshot.

## Parent Contract
**Required parent:** `routing-ui-work`.

This owner coordinates design-to-code translation. It does not replace `architecting-design-tokens`, `architecting-component-systems`, `compiling-ui-implementation-specifications`, or `verifying-design-fidelity`; it binds their outputs into a traceable handoff and routes mapping/drift specialists.

## Handoff Model
Separate design artifact identity, semantic component mapping, token binding, layout/responsive intent, interaction/state behavior, content/assets, accessibility annotations, and implementation target constraints. A design node with only x/y/width/color values is insufficient when the production system has reusable semantic components.

Declare authority per layer. Existing production components may outrank a design tool's local instance for semantics and accessibility; design tokens may outrank raw sampled values; the design artifact may own composition and visual intent; product requirements own behavior. Resolve conflicts explicitly rather than choosing whichever source is easiest to export.

## Translation States
Track unmapped, confidently mapped, mapped-with-override, unsupported, intentionally custom, and ambiguous states. Generated code must not silently invent a component mapping when multiple candidates exist. Ambiguity should appear in the handoff packet with the evidence needed to decide.

## Round Trip and Drift
After implementation, compare production rendering/behavior to the intended handoff at the same revision. Later design changes and code changes should produce drift records that identify whether the divergence is intentional, unresolved, or stale. Do not sync bidirectionally by overwriting one side without authority.

## Evidence
Test a design containing system components, custom component, token aliases, responsive recomposition, hover/focus/error/loading states, keyboard behavior, imagery, and one deliberate production exception. Trace every implementation decision back to handoff evidence and render the result.

## Failure Modes
- Screenshot pixels are treated as the complete implementation spec.
- Generated code duplicates an existing production component.
- Raw color values replace semantic tokens.
- Only desktop frame is exported and mobile behavior is guessed.
- Accessibility/interaction state disappears in translation.
- Bidirectional sync overwrites intentional production exception.
- “Matches design” is claimed without rendered behavior evidence.

## Falsification
Change a token alias and responsive rule without changing the desktop screenshot. Falsify if the handoff cannot detect the semantic changes or generates the same implementation packet. Then implement an intentional exception; falsify if later sync erases it silently.

## Recovery
Re-establish layer authority, mark ambiguous mappings, bind stable component/token identities, include responsive/state intent, and record intentional exceptions. Missing evidence blocks automated translation rather than authorizing guessed markup.

## Handoff
Component mapping uses `designing-component-mapping-to-code`; token mapping uses `designing-token-mapping-to-code`; responsive and interaction intent have dedicated owners; production divergence uses `designing-design-code-drift-review`.

## Output Contract
Return a `design-to-code-handoffs-contract` with `design_revision`, `layer_authority`, `mapping_states[]`, `component_links[]`, `token_links[]`, `responsive_intent`, `interaction_state_intent`, `accessibility_intent`, `exception_records[]`, `implementation_evidence[]`, and `recovery_actions[]`.