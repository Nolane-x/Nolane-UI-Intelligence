---
name: designing-generative-ui-schema-fallbacks
description: Use when generative UI may receive unknown, partial, invalid, newer, or unsupported component schemas and the host must degrade to safe representations without losing tool truth, user control, or provenance.
---

# Designing Generative UI Schema Fallbacks

## Failure is part of the renderer contract
Generative UI cannot assume every produced schema matches the current renderer. Models may emit partial structures, a server may send a newer schema version, extensions may be unavailable, or an otherwise valid component may exceed the current platform’s capabilities. This skill owns the fallback ladder that keeps the product useful and truthful when structured rendering cannot proceed as intended.

## Parent Contract
**Required parent:** `designing-generative-ui`.

The parent owns the overall generative-UI runtime. This specialist begins when schema recognition, validation, capability matching, or component rendering is incomplete or fails.

## Schema state model
Represent schema handling as `recognized_valid`, `recognized_partial`, `recognized_invalid`, `unsupported_version`, `unknown_component`, `capability_unavailable`, or `renderer_failed`. Those states should not be collapsed into tool failure. The tool result may be entirely valid even when the preferred component cannot render.

The decision owner is the safest representation that still preserves meaning. A typical ladder is: native structured component → reduced structured component → generic key/value or tabular rendering → sanitized textual representation → raw evidence inspection. Domain-specific products may add specialized fallbacks, but every step must preserve provenance and should never invent absent fields.

## Compatibility rules
Version schemas explicitly. Backward-compatible additions may be ignored or represented generically; breaking changes require a supported migration or fallback. Unknown fields should be retained in raw evidence even if not displayed. Required fields missing from a component should prevent action controls whose semantics depend on those fields.

Do not let fallback presentation silently broaden authority. A generic renderer that exposes raw action descriptors must not convert them into executable buttons. Likewise, a textual fallback must distinguish model-generated labels from trusted source fields.

## User experience under degradation
Keep degradation calm and local. If one card cannot render, the entire conversation or task should not fail. Tell the user when the representation is simplified only if that affects interpretation or available actions. Preserve useful data and offer inspection instead of a generic “something went wrong.”

If the missing renderer is platform-specific, the UI may offer continuation on a capable surface, but the current surface should still expose enough evidence to understand what exists and what cannot be done here.

## Evidence
Evidence includes schema version, validation result, unsupported fields/components, chosen fallback level, preserved raw payload, capability checks, and any controls removed during degradation. Test with unknown component types, missing required fields, extra fields from a future version, renderer exceptions, and intentionally malformed action descriptors.

## Failure modes
Characteristic Failure includes treating renderer failure as tool failure, discarding raw results, showing a blank card for unknown schemas, enabling actions from an invalid component, silently dropping fields that alter meaning, and crashing the whole agent surface because one extension is unavailable. Another failure is false fidelity: a fallback looks complete but omits material state without disclosure.

## Falsification
Falsification should send future-version schemas, remove required fields, corrupt one nested component while leaving siblings valid, disable a platform capability, and trigger a runtime renderer exception after partial display. The contract fails if tool truth disappears, if invalid controls remain actionable, if the fallback invents values, or if a local rendering problem escalates into loss of the whole run.

## Recovery
When a better renderer later becomes available, re-render from the preserved canonical payload rather than from lossy fallback output. If a migration is introduced, validate the migrated schema and retain the original version for evidence. Recovery should upgrade representation without changing the underlying tool-result identity.

## Output and Handoff
Output: `generative-ui-schema-fallbacks-contract`, containing schema states, version policy, fallback ladder, capability gating, provenance preservation, action suppression, and upgrade behavior. Handoff authority decisions to generated-component authority and result lifecycle decisions to tool-result presentation.

## Sibling Boundary and delete-the-skill
Sibling generated-component authority governs what a valid generated component may do. This skill governs what happens when the component cannot be trusted or rendered as designed. The delete-the-skill test passes because without a fallback owner, generative UI either becomes brittle or masks schema incompatibility by fabricating a successful-looking representation.