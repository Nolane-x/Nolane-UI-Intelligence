---
name: routing-ui-work
description: Use when a contracted UI task needs the smallest sufficient set of product, human-factors, architecture, interaction, visual, platform, modality, inclusive, AI, specialist, research, and verification faculties.
---

# Routing UI Work

## Overview
The router is a classifier, dependency planner, and obligation selector. It is not a designer and must not solve domain work inside routing. Its job is to construct the smallest sufficient faculty graph for the actual interface while making silent omission of a material domain difficult. Minimal routing means no irrelevant context; it never means skipping a high-impact owner or verifier.

## Parent Contract
**Required parent:** `nolane-ui`.

Require a valid `ui-contract`. If the contract is absent, contradictory, or too vague to classify platform, users, task, risk, and evidence needs, return to `ui-contracting`. Do not invent a replacement contract inside the router.

## Build `UI_TASK_PROFILE`
Profile observable conditions rather than prompt keywords. Record unknowns explicitly instead of converting them into defaults.

- `intent[]`: design-new, redesign, extend, audit, reproduce, implement, verify, systemize, research.
- `platform_surfaces[]`: web, mobile, desktop, large-screen-foldable, tv-ten-foot, wearable, automotive, flight-deck, spatial-xr, game-hud, cli-tui, embedded-kiosk, robotics-teleoperation, ambient-context-aware, supervisory-control-room, or another atlas-owned emerging surface.
- `input_modalities[]`: pointer, touch, pen, keyboard, alternative-input, physical-controls, gamepad, remote, voice, gaze, hand-gesture, motion, haptics, neuroinput, or another explicitly modeled modality.
- `ai_role`: none, assistive, generative, agentic, multi-agent, generative-ui.
- `risk_class`: routine, privacy-sensitive, security-sensitive, financial, medical, safety-critical.
- `temporal_behaviors[]`: streaming, realtime, offline-degraded, long-running, interruption-sensitive, background-work.
- `social_context`: personal, shared-screen, collaborative, public, supervised, multi-operator.
- `specialized_ui_domains[]`: affective-adaptive, avatar-embodied, aac-communication, cross-device-action-equivalence, accessibility-settings, accessible-media, sign-language-presentation, in-product-assistance, or another specialized decision class with explicit atlas ownership.
- `regulatory_or_standard_sensitivity`: low, medium, high, regulated.
- `research_freshness_requirement`: stable-foundation, current-platform, current-standard, frontier.
- `driving_context`: not-applicable, parked, driving, mixed.
- `user_context`: expertise, frequency, time pressure, cognitive load, accessibility needs, environment, error cost, fatigue, and whether assistance is available.
- `information_context`: density, hierarchy depth, volatility, comparability, reading versus scanning, real-time ordering, provenance needs.
- `interaction_context`: selection, direct manipulation, drag/drop, destructive action, permissions, undo, concurrency, collaboration, async behavior, latency sensitivity.
- `visual_context`: brand maturity, existing design-system strength, reference fidelity, desired character, novelty tolerance, imagery availability, density, and whether memorability or task transparency dominates.
- `evidence_capabilities`: design source, browser/runtime inspection, screenshot capture, accessibility tree, interaction automation, component explorer, device access, human review, domain-expert review, user research, simulation, operational validation.

An unclassified high-impact dimension becomes a `capability_gap` or routing unknown. It does not inherit a convenient default.

## Routing Algorithm
1. Start from product semantics and users/tasks.
2. Add every owner skill whose decision boundary materially exists in the profile.
3. Add parent dependencies required by those owners.
4. Add independent verifier skills according to failure impact, even when a corresponding generation faculty is not otherwise needed.
5. Apply deterministic hard-route predicates from the kernel. A mandatory route cannot be removed by model preference.
6. Mark nearby but inactive faculties with a concrete reason tied to the contract.
7. Resolve authority/freshness when the task depends on a current standard, platform behavior, regulated context, or frontier technology.
8. Produce a dependency graph. Parallelize faculties that consume stable upstream contracts; do not force a theatrical linear chain.

## Baseline faculties for material new UI
Unless an existing design/source fixes the corresponding decision, route product intent, user/task modeling, information architecture, interaction design, component state modeling, visual hierarchy, design tokens, responsive/platform obligations, accessibility, and at least the applicable visual/UX verification lenses. `exploring-aesthetic-directions` is required when visual direction is materially open; faithful reproduction routes to `verifying-design-fidelity` instead of fabricating novelty.

## Human-factors and research routing
High task pressure, sustained attention, alarm/notification load, memory burden, complex motor requirements, or meaningful error cost route to `engineering-human-factors` plus the relevant cognitive/perceptual faculty. Safety-critical, medical, automotive-driving, flight-deck, robotics, and supervisory-control work must include `critiquing-human-factors-and-safety` independently of visual quality.

When a decision depends on claims about users rather than established project evidence, route `planning-usability-research` or `evaluating-usability-evidence`. Frontier or high-drift knowledge routes to `researching-ui-frontiers`, `calibrating-ui-authority`, and when appropriate `measuring-research-saturation`. Draft standards must remain draft in the obligation ledger.

## Modality routing
- keyboard-heavy or command-dense work → `designing-keyboard-power-user-ux`.
- pointer/touch/pen mechanics → `designing-pointer-touch-pen-input`.
- physical controls such as switches, knobs, dedicated keys, joysticks or constrained hardware inputs → model them through the applicable surface skill plus `modeling-perception-and-motor-control`; do not pretend a pointer prototype validates physical interaction.
- dragging that carries task meaning → `designing-accessible-drag-and-drop` and an alternative path.
- TV/gamepad/remote directional navigation → `designing-gamepad-remote-focus` plus `critiquing-input-modality`.
- voice → `designing-voice-conversational-ui`; do not assume speech is always available, private, or recognized correctly.
- gaze/hand in spatial environments → `designing-gaze-hand-spatial-input` plus spatial/platform verification.
- haptic or multisensory signals → `designing-haptics-and-multisensory-feedback`; never make a critical state haptic-only.
- switch, scanning, head tracking, voice control, or other alternative access → `designing-alternative-input` plus modality critique.
- neuroinput → `designing-brain-computer-interface-ux`, human factors, and modality/safety review according to consequence.

Concurrent modalities remain concurrent. Do not delete keyboard support because touch exists or remove pointer access because pen is preferred.

## Surface routing
- desktop → `designing-desktop-windowed-workspaces` when multiwindow, shortcuts, precision input, long sessions, or system integration matter.
- large-screen/foldable → `designing-foldable-large-screen-interfaces` for posture, pane, continuity, resizing, and hinge/window changes.
- tv-ten-foot → `designing-tv-ten-foot-interfaces`, directional focus, remote input, distance legibility.
- wearable → `designing-wearable-glanceable-interfaces` and cognitive-load review.
- automotive → `designing-automotive-interfaces`; driving context additionally forces human-factors/safety constraints and reduced interaction authority.
- flight-deck → `designing-flight-deck-interfaces`, `engineering-human-factors`, `designing-high-stakes-decisions`, and human-factors/safety critique. Phase of flight, crew role, automation-mode awareness, alerting and certification evidence remain explicit rather than being generalized into an enterprise dashboard.
- spatial-xr → `designing-spatial-xr-interfaces`, gaze/hand input, platform-fit and modality critique.
- game-hud → `designing-game-hud-and-menus`; pair with controller, accessibility, localization, or data-display faculties as needed.
- cli-tui → `designing-cli-tui-interfaces` plus keyboard/power-user behavior.
- embedded-kiosk → `designing-embedded-kiosk-interfaces` plus degraded/recovery behavior when unattended or constrained.
- robotics-teleoperation → `designing-robotic-teleoperation-interfaces`, human factors, input-modality and safety review.
- ambient-context-aware → `designing-ambient-context-aware-interfaces`, privacy, agency, interruption, and security review.
- supervisory-control-room → `designing-supervisory-control-room-hmi`, human factors, cognitive-load and safety review.

## AI and agent routing
Any material AI behavior routes to `designing-human-ai-interaction` and `critiquing-ai-trust-and-agency`. Generative or agentic behavior also routes to `designing-ai-uncertainty-and-provenance`. Agentic action requires `designing-agent-autonomy-and-control`; multi-agent attribution requires `designing-multi-agent-surfaces`; streaming output uses `designing-streaming-ai-responses`; correction/revert behavior uses `designing-ai-feedback-and-correction`.

`generative-ui` forces `designing-generative-ui` plus security/privacy review. Generated rendering must not silently become privileged action authority; typed actions, authorization, target binding, confirmation policy, idempotency, and recovery live outside untrusted generated structure.

## Specialized standardized-domain routing
- affective-adaptive sensing or behavior → `designing-affective-adaptive-interfaces`, `designing-permissions-and-consent`, `designing-privacy-sensitive-interfaces`, and independent security/privacy review. Affective inference never receives consequential authority merely because confidence is high.
- avatar-embodied representation → `designing-avatar-embodied-representation` plus security/privacy and accessibility verification. If the avatar is AI-controlled, also apply the relevant AI/agency routes.
- aac-communication → root `designing-accessible-interfaces` plus `designing-aac-communication-interfaces` and accessibility critique. Route the real access modality separately; AAC does not imply touch.
- cross-device-action-equivalence → `designing-cross-device-action-equivalence`, `adapting-platform-conventions`, and input-modality critique. Preserve the canonical operation and consequence while allowing device-native triggers; never equate consistency with identical gestures.
- accessibility-settings → root accessibility plus `designing-accessibility-settings-and-profiles` and accessibility critique. The settings surface must remain operable before the preferred accessibility mode is enabled and must provide safe rollback from unusable configurations.
- accessible-media → root accessibility plus `designing-accessible-media-alternatives` and accessibility critique. Captions, subtitles, transcripts, audio description, and spoken on-screen text are distinct information channels rather than one interchangeable checkbox.
- sign-language-presentation → `designing-accessible-media-alternatives`, `designing-sign-language-presentation`, and accessibility critique. Treat the requested sign language as a natural language with readable signing space, attribution, timing, and linguistic validation; it is neither universal nor an AAC pictogram system.
- in-product-assistance → `designing-in-product-assistance` plus UX critique. First repair primary interaction when the control can simply be clearer; assistance owns residual conceptual, procedural, diagnostic, troubleshooting, recovery, and escalation gaps after onboarding.

These are not visual tags. They change inference, identity, authorship, communication, cross-device operation semantics, access authority, or the way users recover missing knowledge and therefore deserve explicit profile entries.

## Trust, risk, and transaction routing
Authentication and recovery → `designing-authentication-and-passkeys`. Permissions or sensitive capability grants → `designing-permissions-and-consent`. Sensitive data visibility, inference, sharing, or retention → `designing-privacy-sensitive-interfaces` and security/privacy critique. Financial consequence → `designing-financial-transaction-ui` plus high-stakes decision review. Checkout funnels route to `designing-commerce-checkout`; do not trade clarity or recovery for conversion. Medical UI routes to `designing-medical-safety-critical-ui`, human factors, high-stakes decisions and safety critique.

Hard gates for safety, security/privacy, accessibility, and AI agency cannot be offset by visual-quality scores.

## Temporal and resilience routing
Streaming → `designing-latency-and-progressive-feedback`, resilience critique, and AI streaming skill when AI is involved. Realtime → `designing-real-time-updates`; preserve ordering, staleness, conflict and attention behavior. Offline/degraded → `designing-offline-degraded-experiences`. Interruption-sensitive work → `designing-notifications-and-interruptions` and cognitive-load modeling. Long-running actions require progress, cancellation/continuation semantics, duplicate-action protection, and a truthful state model.

## Accessibility specialist routing
Root accessibility remains mandatory when accessibility is material. Add `designing-cognitive-accessibility`, `designing-low-vision-and-high-contrast`, `designing-screen-reader-experiences`, `designing-reduced-motion-and-photosensitivity`, `designing-accessibility-settings-and-profiles`, `designing-accessible-media-alternatives`, `designing-sign-language-presentation`, alternative input, AAC, or another specialist faculty according to real needs and failure modes. Specialist faculties augment root semantics; they never replace them. A sign-language task inherits accessible-media obligations, and an AAC task separately routes the person’s real input modality.

## Design-system and content routing
New or materially changed component language routes to `architecting-component-systems`, `architecting-design-tokens`, and when shared across teams `governing-design-systems`. Breaking component semantics or API changes route to `evolving-component-apis`. Theme/personalization changes route to `managing-theming-and-personalization`. Durable rationale routes to `documenting-design-decisions`; accessibility intent crossing design/engineering boundaries routes to `annotating-accessibility-intent`.

Forms, search, navigation, onboarding, data-dense surfaces, data visualization, collaboration, editor/canvas, empty/loading/error states, motion, localization, UX writing, and visual craft route only when their decision domains exist.

## Hard routing
The following are non-optional examples enforced by deterministic predicates rather than prose alone:
- automotive driving → `designing-automotive-interfaces` + `engineering-human-factors` + `critiquing-human-factors-and-safety`.
- flight-deck → `designing-flight-deck-interfaces` + human-factors + high-stakes decision + human-factors/safety critic.
- spatial-xr → `designing-spatial-xr-interfaces` + `designing-gaze-hand-spatial-input` + platform/modality critics.
- tv-ten-foot → `designing-tv-ten-foot-interfaces` + directional focus + modality critic.
- wearable → `designing-wearable-glanceable-interfaces` + cognitive-load critic.
- material AI → `designing-human-ai-interaction` + `critiquing-ai-trust-and-agency`.
- agentic AI → `designing-agent-autonomy-and-control` + provenance + AI agency critic.
- medical/safety-critical → high-stakes/human-factors owner paths + `critiquing-human-factors-and-safety`.
- affective-adaptive → affective owner + consent/privacy + security/privacy critic.
- avatar-embodied → avatar owner + security/privacy and accessibility critics.
- aac-communication → root accessibility + AAC owner + accessibility critic.
- cross-device-action-equivalence → cross-device owner + platform adaptation + modality critic.
- accessibility-settings → root accessibility + settings owner + accessibility critic.
- accessible-media → root accessibility + media-alternatives owner + accessibility critic.
- sign-language-presentation → media-alternatives owner + sign-language owner + accessibility critic.
- in-product-assistance → assistance owner + UX critic.
- robotics, ambient, supervisory-control, and neuroinput → their extension-owned mandatory routes.

## Verification routing
Generation and verification are independent. Select critic lenses based on plausible harm, not on which creation skill ran. Material completion commonly needs visual and UX critique; add accessibility, responsive, platform, human-factors/safety, AI agency, input modality, cognitive load, security/privacy, research-validity, performance/resilience, localization, design-system, or fidelity courts when their failure dimensions are present.

A critic can produce findings but cannot silently rewrite its own evidence and certify itself. Repaired findings require fresh verification.

## Inactive Faculties
A neighboring faculty may be inactive only with a specific contract-bound reason. `designing-motion inactive — accepted static surface and no meaningful transition state` is valid. `not needed` is not. If a deterministic hard route is inactive, the router must return `BLOCKED` rather than invent an exemption.

## Output Contract
Return `ui-task-profile` with every profile dimension above plus:
- `selected_skills[] {name, reason, required_inputs, expected_output, authority}`
- `inactive_faculties[] {faculty, reason}`
- `dependency_edges[]`
- `critical_paths[]`
- `verification_lenses[]`
- `hard_routes[]`
- `capability_gaps[]`
- `research_freshness_state`
- `routing_confidence`

Before emitting the profile, compare selected skills with deterministic mandatory routes. Any missing hard route means the profile is invalid.

## Failure Traps
- Keyword routing: “dashboard” automatically means cards, charts, dark mode.
- Maximal routing: every available skill loaded “to be safe.” Context dilution is a defect.
- Aesthetic routing before product semantics and human constraints.
- Treating responsive web as mobile-native design or treating mobile as a smaller desktop.
- Treating a flight deck as a control-room theme without phase/crew/automation/certification evidence.
- Treating an AI avatar as self-disclosing because it looks synthetic.
- Treating affect inference as fact or AAC as an icon theme.
- Treating cross-device consistency as identical gestures or identical pixels.
- Treating accessible-media presence as equivalent to usable synchronization and information coverage.
- Treating sign language as universal or as captions expressed with hands.
- Making accessibility settings inaccessible until accessibility is already configured.
- Using help overlays to excuse an interface that can simply be made clearer.
- Treating a current visual trend as a universal style requirement.
- Letting framework choice suppress accessibility, safety, state, or recovery obligations.
- Using one modality to justify deleting alternative input paths.
- Marking a standard “current” without checking its status when freshness is material.
- Allowing a high beauty score to compensate for a hard-gate failure.
