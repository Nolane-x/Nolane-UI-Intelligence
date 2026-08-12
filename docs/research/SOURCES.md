# Research and Source Ledger

This document is the human-readable provenance index for Nolane UI Intelligence (NUI). Detailed machine-readable records live under `knowledge/source-ledger*.json`, where each source carries publisher, authority class, lifecycle/status, domain, drift, review date, licensing note, and the specific mechanism synthesized into NUI.

NUI does not bulk-copy third-party skill text, third-party design databases, paywalled standards, or platform documentation. Skill prose, contracts, router rules, critics, validators, and eval fixtures are independently authored for NUI. When a paywalled standard is not supplied under license, only public metadata/abstract/status is used to establish scope and research direction.

## Authority policy

When guidance conflicts, NUI uses this order:

1. explicit product, user, accepted-target, and safety constraints;
2. applicable law, regulation, and normative standards;
3. safety/regulatory authority guidance;
4. authoritative platform guidance;
5. active project design system and validated product evidence;
6. direct empirical human-factors/usability evidence;
7. mature design-system guidance;
8. high-quality official/community agent heuristics;
9. community heuristics;
10. model aesthetic preference.

A community recommendation never becomes a normative requirement because it is popular. A draft standard never becomes a published requirement because its direction is useful. A platform trend never becomes a universal aesthetic default.

## Source-status policy

Every research-sensitive source should preserve its status, for example:

- published normative standard;
- published technical specification;
- regulation or regulatory guidance;
- W3C Recommendation;
- working draft / committee draft / DIS / FDIS / AWI;
- current platform guidance;
- empirical research;
- design-system guidance;
- agent/community heuristic.

High-drift sources are monitored in `knowledge/research-radar.json` and can reopen a previously saturated research domain.

## Agent design systems and skills consulted

| Source | Authority in NUI | Mechanism synthesized | Reuse/licensing posture |
|---|---|---|---|
| OpenAI `frontend-app-builder` — https://github.com/openai/plugins/blob/main/plugins/build-web-apps/skills/frontend-app-builder/SKILL.md | High-quality official agent workflow | Designer-before-engineer sequencing; complete-surface design; system extraction before implementation; target-vs-render fidelity; handoff blocked by missing visual comparison | No source text/assets vendored; mechanisms independently implemented. |
| OpenAI Product Design router — https://github.com/openai/role-specific-plugins/blob/main/plugins/product-design/skills/index/SKILL.md | High-quality official agent workflow | Router-only index; focused audit/ideate/build/QA paths; separation of audit from implementation fidelity QA | NUI uses its own router, contracts, names and runtime-independent policy. |
| Anthropic `frontend-design` — https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md | High-quality official design heuristic | Subject-grounded visual language; deliberate typography/composition; justified visual signature; self-critique against generic defaults | Concepts synthesized; protected expression not copied. |
| UI Craft — https://github.com/educlopez/ui-craft | High-quality community design-engineering system | Separate deterministic checks from design judgment; independent reviewers; craft floor; durable brief/system | Repository reports MIT; NUI does not vendor the project. |
| Impeccable — https://github.com/pbakaus/impeccable | High-quality community design language | Critique/refinement vocabulary; design-review passes; anti-pattern awareness | Repository reports Apache-2.0; NUI independently writes its rules. |
| UI/UX Pro Max — https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Community knowledge engine | Structured/retrievable design knowledge and product-aware recommendation | CLI README states CC-BY-NC-4.0; NUI deliberately does not import its databases/prose. |
| Podo Design Agent Skills — https://github.com/podo/design-agent-skills | Community routing/catalogue pattern | Progressive disclosure and broad domain routing rather than mega-prompt loading | Repository reports MIT; NUI uses its own graph/contracts/content. |

## Core normative and platform sources

| Source | URL | NUI use |
|---|---|---|
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ | Current web accessibility conformance baseline used by this research wave. |
| WCAG 3 draft | https://www.w3.org/TR/wcag-3.0/ | High-drift future accessibility research; explicitly not treated as current normative replacement for WCAG 2.2. |
| WAI-ARIA Authoring Practices Guide | https://www.w3.org/WAI/ARIA/apg/ | Widget semantics, names/states, keyboard interaction, and custom-control patterns. |
| Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | Apple platform interaction, layout, accessibility, spatial and AI guidance. |
| Material Design 3 | https://m3.material.io/ | Android/material components, states, interaction and current expressive-system guidance. |
| Fluent 2 | https://fluent2.microsoft.design/ | Mature token/component and semantic design-system guidance. |
| Design Tokens Community Group 2025.10 | https://www.designtokens.org/tr/2025.10/ | Portable design-token interchange; NUI remains format-independent internally. |
| Unicode CLDR | https://cldr.unicode.org/ | Locale data, text expansion, pluralization, calendars and internationalization research. |

## Human factors, safety and regulated UI sources

The v2 wave expanded beyond consumer-app heuristics by reviewing current authority for high-consequence interaction.

| Source family | Representative URL | Mechanism synthesized |
|---|---|---|
| FDA human factors / usability engineering | https://www.fda.gov/medical-devices/device-advice-comprehensive-regulatory-assistance/human-factors-and-medical-devices | Use-related risk, representative users/environments, critical tasks, validation evidence, and separation of UI guidance from regulatory approval claims. |
| FAA Flight Deck Human Factors | https://www.faa.gov/aircraft/air_cert/step/disciplines/flight_deck_human_factors | Flight-deck automation, alerting, controls/displays, workload, complexity, fatigue, design-related flightcrew error, and certification evidence as a coupled discipline. |
| FAA AC 20-175 | https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentid/1019692 | Human-factors considerations for flight-deck control devices including multifunction/touch/cursor controls. |
| FAA AC 25.1302-1 | https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1021086 | Minimize design-related flightcrew error and support detection/management of remaining errors. |
| IEC/ISO medical and rehabilitation-robot standards | machine ledgers under `knowledge/` | Medical safety, essential performance, human factors, physical human-robot interaction and bounded certification claims. |
| Process/control-room HMI and alarm guidance | machine ledgers under `knowledge/` | Supervisory control, alarm fatigue, trend/state perception, long-duration operation, degraded conditions and operator workload. |

## Emerging and specialist standards synthesized in v2

The detailed lifecycle/status for every item is recorded in `knowledge/source-ledger.json` and the four extension ledgers. Representative source families include:

### Intelligent systems, robotics and ambient computing

- ISO 9241-810 family for robotic, intelligent, autonomous, ambient and related systems.
- Current/draft ISO 9241-812 work for intelligent-system human-centred design.
- Relevant NIST/IEC/FDA material where safety, autonomy or cyber-physical interaction changes the evidence boundary.

These sources informed `designing-robotic-teleoperation-interfaces`, `designing-ambient-context-aware-interfaces`, AI/agent faculties, human-factors routing and safety critique.

### Brain-computer interfaces

Current ISO/IEC SC 43 BCI standardization and 2026 BCI data work established BCI as a distinct modality boundary. NUI does not infer medical efficacy; it owns UI concerns such as calibration, signal confidence, false activation, fatigue, privacy, alternatives and control authority.

### Affective computing

- ISO/IEC 30150-1:2022 — affective-computing user-interface model.
- Later 30150 parts under development are tracked as drafts.

These sources support explicit separation of sensed signal, inference, confidence/freshness, adaptation, consent and adaptation authority.

### Avatars and embodied representation

- ISO/IEC 24216-1:2026 — avatar UI requirements/recommendations and categorization.

The mechanism synthesized is identity/controller separation, automation disclosure, likeness authority, impersonation risk, social representation and accessible attribution.

### AAC and symbol personalization

- ISO/IEC TS 20071-40:2026 — AAC in ICT.
- W3C AAC Symbol Registry — https://www.w3.org/TR/aac-registry/
- WAI-Adapt Symbols — https://www.w3.org/TR/adapt-symbols/

These sources support concept-to-symbol semantics, communication ownership, stable vocabulary organization, multiple access methods and portable personalized communication.

### Cross-device action equivalence

- ISO/IEC 4933:2026 — unifying input actions across devices.

NUI preserves canonical operation meaning/consequence while allowing native input triggers on each device.

### Accessibility settings and profiles

- ISO/IEC 20071-5:2022 — accessible UI for accessibility settings.
- ISO/IEC 24756:2009, confirmed later — framework for user/system/environment access needs and capabilities.

These sources expose the bootstrap problem: settings must remain operable before the preferred accessibility feature is enabled.

### Accessible media and sign-language presentation

- ISO/IEC 20071-23:2018 — captions/subtitles and visual audio information.
- ISO/IEC TS 20071-25:2017 — audio presentation of on-screen text.
- ISO/IEC DIS 20071-24 — sign-language visual presentation, explicitly tracked as a draft.

NUI separates captions, transcripts, audio description/spoken text and sign-language presentation rather than treating them as interchangeable accessibility tracks.

### User assistance

- ISO/FDIS 9241-130 — user assistance in interactive systems, explicitly tracked as a Final Draft rather than a published requirement.

This research distinguished in-product assistance from onboarding and from primary UI clarity.

## Final decomposition sweep sources

The final adversarial sweep intentionally looked for evidence that would require another owner skill. It produced useful knowledge but no new non-decomposable owner. Examples recorded in `knowledge/final-saturation-evidence.json` include:

- ISO 9241-112:2025 — information presentation;
- ISO 9241-222:2026 — HCD self-assessment;
- ISO/IEC 4944:2024 — usability evaluation of natural user interfaces;
- ISO/CD 9241-812 — intelligent systems;
- ISO/IEC 7818:2025 — voice UI for personal mobility;
- ISO 9241-920:2024 — tactile/haptic interactions;
- ISO/IEC 23090-28:2026 — immersive media;
- IEC 80601-2-78 and revision work — rehabilitation robotics;
- ISO/IEC CD 25420 — multimodal customer service;
- current Apple generative-AI guidance.

Each item is recorded with the existing skills that own its user-facing decision mechanics and a reason no new owner was created.

## Verification/tooling sources

These are execution oracles, not design authorities.

| Source | URL | NUI use |
|---|---|---|
| Storybook testing | https://storybook.js.org/docs/writing-tests | Component-state surfaces, interaction tests, accessibility checks and visual-regression integration. |
| Storybook accessibility testing | https://storybook.js.org/docs/writing-tests/accessibility-testing | Automated axe evidence while preserving partial-coverage limits. |
| Playwright visual comparisons | https://playwright.dev/docs/test-snapshots | Rendered screenshot baselines/diffs for fidelity/regression claims. |
| Playwright ARIA snapshots | https://playwright.dev/docs/aria-snapshots | Semantic/accessibility-tree evidence complementary to pixels. |
| shadcn MCP | https://ui.shadcn.com/docs/mcp | Verified component discovery when a compatible registry is actually present. |
| Chrome DevTools / Lighthouse | https://developer.chrome.com/docs/devtools/ and https://developer.chrome.com/docs/lighthouse/ | Runtime inspection and performance/accessibility diagnostics where available. |

## What NUI intentionally did not import

- No UI/UX Pro Max style/palette/font/product database.
- No copied anti-pattern list from Impeccable or UI Craft.
- No copied OpenAI or Anthropic skill prose.
- No mirrored WCAG, ARIA APG, HIG, Material, Fluent, ISO, IEC, FAA, FDA, Storybook or Playwright documentation.
- No paywalled standards text obtained from public abstracts.
- No third-party component source code.

NUI instead translates recurring mechanisms into its own architecture: authority hierarchy, typed contracts, state algebra, human-factors models, contextual anti-slop, specialist decision owners, independent critics, evidence binding, capability adapters, research radar, and deterministic completion/saturation gates.

## Provenance rule for future contributions

When a new source materially changes NUI:

1. record the exact source and publisher;
2. record authority class and lifecycle/status;
3. record the UI decision mechanism learned;
4. record drift/freshness expectations;
5. record licensing/reuse constraints;
6. decide whether it modifies an existing owner or proves a new owner is needed;
7. add a pressure test before changing the skill graph;
8. update `research-radar.json` if the source can drift materially;
9. never claim the source proves more than its actual scope.

For the full wave narrative and bounded-saturation reasoning, see `UI-INDUSTRY-RESEARCH-2026-08-12.md`.
