---
name: designing-generative-ui
description: Use when an AI dynamically chooses, assembles, or generates interface components, layouts, forms, visualizations, actions, or interactive surfaces at runtime rather than returning only static text or predetermined screens.
---

# Designing Generative UI

## Overview
Generative UI is a constrained runtime protocol. Let models compose within an explicit component/action language; never treat arbitrary executable interface code as a harmless extension of text generation.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require generation architecture, allowed components, data schemas, actions/tools, renderer/runtime, trust boundary, accessibility target, persistence, and fallback. Agentic actions additionally require autonomy control.

## Decision Model
Choose the least-open generation mode that solves the task. **Selection:** model chooses among known components/templates. **Declarative composition:** model emits a validated UI tree/schema using an allowlisted vocabulary. **Open code generation:** highest flexibility and highest security/reliability burden; avoid for runtime user-facing UI unless isolated execution and review are the explicit product model.

Define a component vocabulary with semantic purpose, required/optional properties, content limits, interaction states, accessibility semantics, responsive behavior, and allowed child relationships. The model may compose components but cannot invent hidden actions or bypass component contracts.

Action binding is separate from rendering. Generated buttons reference typed action ids; authorization, target validation, idempotency, and confirmation happen outside the model-generated tree. Treat data bindings similarly: generated UI receives scoped data rather than arbitrary object access.

Validate schema before render and after incremental updates. Unknown component/property/action fails closed to a safe fallback. Preserve focus/state when the generated tree changes. Generated forms need stable field identity so user input is not lost on regeneration. Provide a readable fallback if the specialized renderer is unavailable.

## Evidence
Fuzz malformed payloads, unknown components, malicious labels/URLs, unauthorized action ids, schema version mismatch, partial streaming trees, focus/state preservation, accessibility tree, responsive rendering, localization, and fallback. Security review must inspect renderer and action boundary, not only model prompts.

## Output Contract
Return a `generative-ui-runtime-contract` with `generation_mode`, `component_vocabulary[]`, `schema_version`, `composition_rules`, `data_binding_policy`, `action_registry`, `authorization_boundary`, `validation_pipeline`, `state_identity_rules`, `accessibility_contract`, `fallback_renderer`, and `adversarial_tests[]`.

## Failure Traps
- Executing arbitrary JavaScript returned by an agent.
- Model-generated button directly invoking privileged tool arguments.
- Unknown component silently rendered as generic HTML.
- Regeneration erasing user-entered form state.
- Dynamic layout with no stable focus/semantic structure.
- Schema version drift between agent and renderer.
- “Safe because the model was instructed not to” used instead of runtime enforcement.

Generative UI becomes powerful when creativity is separated from authority and rendering is separated from privileged action.

## V6 Generative Surface Authority Model
Define a **generation authority envelope** before allowing a model to create interface structure. Specify which actions, data bindings, components, copy, ordering, styling, and navigation may be generated; which require deterministic templates or human approval; and which are prohibited. Generated UI must not silently acquire more product authority than generated text.

Use a **schema-to-surface contract** so generated controls bind only to known capabilities, typed inputs, permissions, and canonical actions. Unknown fields or actions are not “creative opportunities.” Place malformed, unsupported, unsafe, or semantically ambiguous output into **invalid-generation quarantine** with a recoverable explanation rather than partially rendering an executable interface.

Preserve **ephemeral-state continuity** during regeneration: focus, form input, selection, scroll, open disclosure, unsaved edits, pending actions, and assistive-technology context must not evaporate because the model emitted a new tree. Run a **regeneration identity test** to decide when a generated element is the same conceptual object versus a replacement; stable IDs and action bindings must survive where identity is preserved.

### Falsification
Perturb the model output with a plausible unknown action, changed order, missing label, duplicate ID, and regeneration during active input. If unsafe controls render or user state disappears, the generation contract is false.

### Recovery
Fall back to deterministic components, reduce the authority envelope, preserve last-known-valid UI, and request/derive a corrected schema. Never ask the user to “try the generated UI again” after losing committed state.
