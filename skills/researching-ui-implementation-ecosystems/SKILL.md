---
name: researching-ui-implementation-ecosystems
description: Use when UI work may benefit from current external component libraries, motion engines, headless primitives, editors, canvas SDKs, data visualization systems, mobile systems, design-agent skills, or other implementation ecosystems and the agent must discover evidence rather than invent from memory.
---

# Researching UI Implementation Ecosystems

## Parent Contract
**Required parent:** `routing-ui-work`.

Receive the product obligation, required capability, platform and framework truth, interaction complexity, accessibility requirements, visual direction, dependency constraints, adoption intent, and any source already named by the user. The parent owns whether ecosystem research is necessary; this faculty owns the search space and the evidence returned from it.

## Decision Boundary
This faculty owns **task-specific discovery**. It answers *what current sources could materially help this exact UI problem, what role does each source play, and what must be inspected before another faculty may select it?* It does not decide to install a dependency, copy code, approve a license, choose final visual style, or declare an upstream demo correct in the local product.

Discovery is typed. A motion engine is not a component library. A headless dialog primitive is not an aesthetic reference. A chart grammar is not a dashboard design system. A canvas SDK is not a generic page-layout solution. A catalogue of AI skills is not evidence that all of those skills should be loaded. Every candidate must therefore carry a **source role** before it may enter the selection stage.

## Product Truth
AI agents routinely know the names of famous libraries but use that memory poorly. They recommend whatever is salient, copy an attractive demo without reading its source, miss a smaller primitive that fits better, treat stars as quality, or use a gallery component to solve a semantic problem. They also freeze an ecosystem at the model's training date while APIs, licenses, maintainers, package names, accessibility behavior and commercial terms continue to change.

The correct unit of research is not “best UI library.” It is a bounded need such as: *a keyboard-operable sortable interaction for a React data workspace; a morphing continuity effect that survives reduced motion; a headless combobox with strong screen-reader behavior; a block editor that can be themed into an existing design system; a high-density chart layer with custom interaction; or a canvas abstraction whose production license is acceptable.* A useful result narrows a decision; a long list of fashionable repositories increases uncertainty.

## Decision Model
1. **Translate the request into capability atoms.** Name the required behavior before naming repositories: animated text, object continuity, scroll-linked narrative, dialog semantics, collision-aware overlay positioning, keyboard reordering, infinite canvas, rich text, table state, data visualization, 3D interaction, mobile-native controls, or another concrete capability.
2. **Bind product constraints.** Record stack, rendering model, SSR/hydration constraints, platform, input modalities, accessibility obligations, performance envelope, bundle policy, design-system ownership, security constraints and whether the project permits new dependencies.
3. **Declare adoption intent.** Distinguish `inspire`, `adapt`, `adopt`, `build`, and `reject`. Inspiration may transfer a mechanism across stacks; adoption requires implementation and license compatibility. Never silently escalate inspiration into copied code.
4. **Query the local typed registry first.** Search `ui-ecosystem-registry.json` by capabilities, categories, stack and intent. The registry is an index, not truth. Its result is a candidate set plus freshness requirements.
5. **Trigger live research when required.** Search live primary sources when no good candidate exists, the source is high-drift, a named source is not in the registry, an API/version matters, or license posture is material. Prefer canonical repositories, official documentation, license files, release notes, examples and issue trackers over listicles or search snippets.
6. **Inspect source role and abstraction level.** Decide whether a candidate provides visual examples, production primitives, behavior state machines, a rendering engine, an editor model, a data model, a full SDK, agent instructions, or a design system. A role mismatch is a research finding, not something selection should discover late.
7. **Inspect implementation evidence.** For serious candidates inspect README/docs, package/dependency shape, representative implementation, release or maintenance signals, accessibility claims and known limitations. For `adapt` or `adopt`, license evidence is mandatory.
8. **Look for negative evidence.** Open issues about hydration, focus, keyboard behavior, version breakage or performance can be more decision-relevant than polished demos. Record them as risks, not automatic rejection.
9. **Diversify candidates by mechanism.** Return alternatives that solve the need differently. For animation, compare a copyable component, an engine and a locally implementable CSS/native approach when appropriate. This avoids ecosystem monoculture.
10. **Stop when marginal discovery falls below decision value.** The output should contain enough differentiated candidates to support selection, not every repository on GitHub.

## Evidence
Primary evidence is the canonical repository, official docs, current license or terms, package/release metadata, representative source paths, official examples and issue/release history when it changes risk. Search engine snippets are leads only. Community showcases may reveal aesthetics but do not establish API, license, accessibility or production fitness.

For every material source, write a reference-ledger record with canonical URL, retrieval date, inspected files/pages, extracted mechanism, source role, freshness, adoption intent and an adaptation boundary. If a source is merely an inspiration reference, say explicitly that no code or trade dress is being adopted. If it is a candidate for material code reuse, hand it to `selecting-ui-building-blocks`; do not approve it here.

The registry must include sources beyond React. Cross-framework headless systems, native/mobile systems, JavaScript motion engines, editors, canvas systems, visualization grammars and agent skill suites are valid candidates when the product requires them. The search should follow the product, not the researcher's favorite stack.

## Output Contract
Return `ui-ecosystem-query` with:
- `need {capabilities[], categories[], stack[], platform[], modalities[], constraints[], adoption_intent}`
- `registry_query {terms, filters, registry_as_of}`
- `candidates[] {source_id, canonical_url, source_role, matched_capabilities[], stack_fit, license_posture, accessibility_posture, drift, verify_live_before_use, inspected[], evidence_refs[], known_risks[]}`
- `mechanism_alternatives[]`
- `rejected_candidates[] {source_id, reason}`
- `live_search_performed`
- `live_search_gaps[]`
- `reference_ledger_delta[]`
- `handoff_to_selection[]`

Candidate order must be explainable through capability, stack, role, accessibility and integration fit. Popularity may be recorded as incidental context but must never be a ranking factor.

## Failure Traps
- Searching “best React UI library” before defining the product need.
- Treating GitHub stars, social popularity, awards, visual polish or recency as authority.
- Returning ten visually similar component galleries and calling that breadth.
- Failing to distinguish an animation engine from an animated component distribution.
- Assuming “open source” means unrestricted copying, redistribution or production deployment.
- Trusting a README accessibility claim without understanding local composition risk.
- Using screenshots as sufficient evidence for SSR, keyboard, focus or dependency behavior.
- Recommending a React-only source to a native Swift problem without explicitly downgrading to mechanism inspiration.
- Reusing registry facts after a high-drift source changes versions or terms.
- Installing a catalogue of hundreds of agent skills when one routed specialist is enough.
- Returning links with no inspected path, mechanism extraction or reason they matter.
- Letting research choose final architecture; selection belongs downstream.

**Hard gate:** a source cannot become a material candidate unless its role, product-fit mechanism, canonical citation, inspected evidence and freshness/license requirements are explicit.
