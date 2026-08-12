# Nolane UI Intelligence v2 — UI Industry Intelligence Design

## Status
Approved continuation of the v1 Universal UI Intelligence architecture. This wave expands coverage without replacing the v1 kernel or weakening its evidence gates.

## Goal
Turn Nolane UI Intelligence from a strong general web/app design skill graph into a domain-complete UI reasoning system that can route, design, critique, and verify interfaces across modern interaction surfaces, input modalities, AI roles, risk classes, accessibility needs, and platform conventions.

The goal is not a fixed skill count. A new skill is justified only when it owns a decision class, failure mode, evidence requirement, or platform/risk obligation that existing skills do not own.

## Non-goals
- Do not make one monolithic mega-prompt.
- Do not turn current visual trends into universal style defaults.
- Do not copy third-party skill prose or restricted databases.
- Do not claim research is permanently complete.
- Do not let a visual-quality score compensate for safety, accessibility, security, or agency gate failure.

## Architecture

### 1. Existing cognitive kernel remains authoritative
The v1 lifecycle, authority hierarchy, obligations, evidence ledger, adversarial court, recovery, and completion gate remain the control plane. New faculties must be children of the router or critic court and cannot bypass kernel obligations.

### 2. UI Industry Atlas
Create `knowledge/ui-domain-atlas.json` as the canonical coverage map. It models each UI domain on orthogonal axes instead of treating product categories as templates:

- surface: web, mobile, desktop, tablet/large-screen/foldable, TV/10-foot, wearable, automotive, spatial/XR, game/HUD, CLI/TUI, embedded/kiosk
- input: pointer, touch, pen, keyboard, switch/alternative input, gamepad, remote, voice, gaze, hand gesture, motion, haptics
- AI role: none, assistive, generative, agentic, multi-agent, generative-UI
- risk: routine, privacy-sensitive, security-sensitive, financial, medical, safety-critical
- temporal behavior: instant, long-running, streaming, realtime, background, offline/degraded, interruption-sensitive
- social context: personal, shared screen, collaborative, public, supervised
- evidence: visual target, browser/runtime, semantic tree, device/platform test, human research, domain expert review

Every material cell maps to one or more owner skills, verifier skills, and primary authority categories.

### 3. Research Intelligence Plane
Add faculties and machine-readable ledgers that distinguish:

- normative standard
- regulator/safety authority
- platform authoritative guidance
- mature design-system guidance
- empirical research/toolkit
- community heuristic

Each source record carries `authority`, `status`, `domains`, `reviewed_at`, `drift`, `license_note`, and `mechanisms_absorbed`.

Research saturation is not “we searched a lot.” A research wave reaches SATURATED only when:
1. breadth coverage has no unowned mandatory domain cell,
2. high-risk/current domains have multiple independent primary authorities where available,
3. contradictions have an explicit resolution or are preserved as context-dependent alternatives,
4. a final search wave yields no material new decision mechanism or uncovered domain class.

Saturation is scoped to the timestamp and source set. It expires for high-drift domains.

### 4. Human factors and research faculties
Add dedicated ownership for attention, cognitive load, perception/motor constraints, task analysis, usability research, and high-stakes decisions. These faculties translate human limitations into observable design constraints rather than generic advice.

### 5. Input-modality faculties
Add explicit design reasoning for keyboard power users, pointer/touch/pen, accessible drag-and-drop, gamepad/remote focus, voice/conversation, gaze/hand spatial input, and haptics/multisensory feedback. A gesture or modality may never be the only path when the target population or applicable standard requires an alternative.

### 6. Surface/platform faculties
Add deep skills for desktop windowed workspaces, foldable/large-screen adaptation, TV/10-foot interfaces, wearable/glanceable interfaces, automotive, spatial/XR, game HUD/menus, and CLI/TUI surfaces.

Each skill owns platform-specific geometry, attention model, input model, navigation/focus, density, environmental constraints, and transition/adaptation rules; it does not own generic typography/color already covered elsewhere.

### 7. AI and agent UI faculties
Add human-AI interaction, agent autonomy/control, uncertainty/provenance, streaming responses, feedback/correction, multi-agent surfaces, and generative UI.

Core invariant: capability does not imply authority. The interface must make action scope, reversibility, provenance, uncertainty, latency, and handoff boundaries legible when those properties materially affect user decisions.

Generative UI is treated as a runtime contract problem as well as a visual problem: allowed component vocabulary, schema validation, data/action binding, security boundary, accessibility semantics, and recovery must be specified before arbitrary generated presentation can be trusted.

### 8. Security, privacy, and trust faculties
Add authentication/passkey UX, permissions/consent, privacy-sensitive interfaces, and transaction confirmation. Security UX must avoid dark patterns, accidental disclosure, user enumeration, irreversible ambiguity, and confirmation dialogs that fail to communicate consequence.

### 9. Safety-critical and domain faculties
Add safety-critical/medical, financial transactions, commerce/checkout, collaboration/presence, and editor/canvas workspaces. High-risk domains automatically route to human-factors and independent critic lenses.

### 10. Resilience and temporal faculties
Add long latency/progressive feedback, offline/degraded mode, notifications/interruptions, and realtime updates. Performance is part of interaction correctness: delayed feedback can cause duplicate actions, loss of trust, or unsafe repeated input.

### 11. Design-system operations
Add governance, component API evolution, theming/personalization, design-decision records, and accessibility annotations. The system must reason about migration, deprecation, semantic-token stability, variant explosion, and cross-platform consistency rather than merely generating tokens/components.

### 12. Deeper accessibility faculties
Split specialist accessibility concerns into cognitive accessibility, low vision/high contrast, screen reader semantics, reduced motion/photosensitivity, and alternative input. These augment — never replace — `designing-accessible-interfaces`.

### 13. Expanded independent critics
Add critics for human factors/safety, AI trust/agency, input modality, cognitive load, security/privacy, research validity, performance/resilience, and localization. Critics remain `may_modify: false` and return evidence-bound findings.

## Router v2
Expand `UI_TASK_PROFILE` with:
- `platform_surfaces[]`
- `input_modalities[]`
- `ai_role`
- `risk_class`
- `temporal_behaviors[]`
- `social_context`
- `regulatory_or_standard_sensitivity`
- `research_freshness_requirement`

Hard routing examples:
- automotive + driving context -> automotive + human factors + attention + voice/remote/input + accessibility + safety critic
- agentic AI -> human-AI + autonomy/control + uncertainty/provenance + streaming/latency when applicable + AI trust critic
- spatial/XR -> spatial + gaze/hand + motion/comfort + accessibility + platform critic
- TV -> TV + gamepad/remote focus + large-distance typography/layout + accessibility
- high-stakes medical -> safety-critical + human factors + cognitive load + error prevention + independent safety critic
- drag/drop -> accessible drag/drop + alternative input + accessibility critic

## Authority hierarchy v2
1. Explicit user/product safety constraints
2. Applicable law/regulation and normative standards
3. Safety/regulatory authority guidance
4. Platform authoritative guidance
5. Project design system and validated product evidence
6. Empirical human-factors/usability evidence
7. Mature design-system guidance
8. High-quality agent/UI community heuristics
9. Model aesthetic preference

Lower authority may refine but never silently override higher authority.

## Current-source principles captured in this wave
- WCAG 2.2 remains normative for web conformance; WCAG 3 is a 2026 Working Draft and broadens the future design space to emerging technologies including wearables and XR.
- ARIA APG is pattern guidance rather than a substitute for native semantics.
- Cognitive accessibility requires user research and many checks that cannot be reduced to automated linting.
- Current Apple and Android design languages are platform context, not cross-product aesthetic law.
- Automotive and medical UI require human-factors reasoning because interaction cost and error consequence can be safety relevant.
- Modern AI UI requires control, correction/revert, provenance/uncertainty communication, and deliberate autonomy boundaries.
- Declarative generative UI standards strengthen the case for schema-constrained component vocabularies instead of arbitrary code execution.

## Verification
Repository-level validation will add:
- atlas coverage and ownership validation
- source-ledger authority/freshness validation
- router dimension/mandatory-route validation
- research-saturation validation
- cross-domain critic coverage validation

Eval suites will include adversarial scenarios for automotive distraction, TV focus traps, wearable overload, spatial comfort, unsafe agent autonomy, misleading AI confidence, generated-UI action binding, auth enumeration, inaccessible drag/drop, cognitive overload, medical irreversible action, realtime churn, offline recovery, and design-system breaking change.

## Release bar
v2 can be released only when:
- every graph node has a substantive skill file and parent contract,
- every mandatory atlas domain has an owner and verifier,
- high-risk domains have authority-backed obligations,
- router tests prove mandatory routes cannot be omitted,
- adversarial completion tests cannot convert missing/unknown evidence into PASS,
- exact-revision CI generates and validates the completion packet,
- a full project ZIP is produced from the verified main checkout.

Research saturation for this wave is a bounded claim only. New platform standards, regulations, interface paradigms, or empirical evidence reopen the research gate.