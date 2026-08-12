---
name: routing-ui-work
description: Use when a contracted UI task needs the smallest sufficient set of product, architecture, interaction, visual, platform, modality, human-factors, AI, trust, inclusive, specialist, and verification skills.
---

# Routing UI Work

## Overview
The router is a classifier and scheduler, never the designer. It converts the UI contract into an orthogonal task profile and loads only faculties that own material decisions or verification obligations. Its opposite errors are both serious: maximal routing dilutes context; under-routing silently removes expertise or safety gates.

## Parent Contract
**Required parent:** `nolane-ui`.

Require a valid `ui-contract`. If it is missing, return to `ui-contracting`. The router may expose an uncertainty or research freshness gap, but it may not invent a different product contract to avoid that gap.

## UI_TASK_PROFILE v2
Profile observable constraints rather than product-name keywords.

- `intent[]`: design-new, redesign, extend, audit, reproduce, implement, verify, systemize, research.
- `product_family`: the product/task description; never use it as a style preset.
- `platform_surfaces[]`: web, mobile, desktop, large-screen-foldable, tv-ten-foot, wearable, automotive, spatial-xr, game-hud, cli-tui, embedded-kiosk, or a concretely described emerging surface.
- `input_modalities[]`: pointer, touch, pen, keyboard, alternative-input, gamepad, remote, voice, gaze, hand-gesture, motion, haptics.
- `ai_role`: none, assistive, generative, agentic, multi-agent, generative-ui.
- `risk_class`: routine, privacy-sensitive, security-sensitive, financial, medical, safety-critical.
- `temporal_behaviors[]`: instant, long-running, streaming, realtime, background, offline-degraded, interruption-sensitive.
- `social_context`: personal, shared-screen, collaborative, public, supervised.
- `regulatory_or_standard_sensitivity`: none, accessibility, security, regulated-domain, safety, or explicit source ids/versions.
- `research_freshness_requirement`: stable, current-platform, high-drift, regulatory-current, or unknown.
- `driving_context`: driving, parked, passenger, mixed, or not-applicable when automotive is present.
- `users`: expertise, capability range, frequency, time pressure, accessibility needs, language/locale, supervision.
- `information`: density, hierarchy depth, volatility, comparison, uncertainty, freshness, reading-versus-monitoring.
- `interaction`: selection, direct manipulation, drag, forms, navigation, search, destructive actions, permissions, collaboration, modes, async work.
- `visual_freedom`: accepted target, brand maturity, design-system strength, desired emotion, novelty tolerance, signature need, imagery/content availability.
- `evidence_capabilities`: visual target, browser/runtime, screenshot, semantic tree, device test, assistive technology, product telemetry, representative research, domain expert, formal validation.

Missing high-impact dimensions remain `unknown`; do not silently default safety-critical, medical, automotive, agentic, or accessibility scope to routine web assumptions.

## Baseline routing
For material new product UI, normally include product intent, users/tasks, information architecture, interaction/state semantics, visual direction/hierarchy when not already fixed, design tokens/system fit, responsive/platform behavior where relevant, and root accessibility. Existing accepted design systems or faithful targets can suppress redundant generation faculties, but cannot suppress verification obligations.

Route focused functions when they exist: task flow, navigation, search, forms, data-dense surfaces, visualization, empty/loading/error states, onboarding, localization, interface copy, motion, design fidelity, or specialist components. A named leaf skill owns its output; the router does not do the leaf’s work.

## Human-factors routing
Route `engineering-human-factors` when error consequence, workload, alarm, environmental use, safety, driving, medical, industrial, emergency, or repeated operator tasks materially affect interaction. Route `modeling-cognitive-load-and-attention` for dense monitoring, interruptions, multi-step memory dependencies, mode switching, realtime churn, or cognitive accessibility. Route `conducting-task-analysis` before restructuring complex expert or critical workflows. Route research faculties when an unresolved decision needs human evidence rather than taste.

Consequential actions route to `designing-high-stakes-decisions`. Financial actions additionally route to `designing-financial-transaction-ui`; medical critical actions route to `designing-medical-safety-critical-ui`. These are not optional “extra review” lenses.

## Modality routing
Keyboard-intensive expert work → `designing-keyboard-power-user-ux`. Mixed mouse/touch/pen → `designing-pointer-touch-pen-input`. Functional drag/reorder → `designing-accessible-drag-and-drop`; include `designing-alternative-input` when a non-drag path is required. Directional controller/remote → `designing-gamepad-remote-focus`. Voice → `designing-voice-conversational-ui`. Gaze/hand spatial input → `designing-gaze-hand-spatial-input`. Haptic/audio feedback with semantic meaning → `designing-haptics-and-multisensory-feedback`. Alternative input or custom canvas reachability → `designing-alternative-input`.

A task may use several modalities concurrently. Route the contracts that change behavior; do not load touch, pen, and pointer skills independently when one shared direct-input skill owns that combined model.

## Surface routing
Desktop long-session/multiwindow work → `designing-desktop-windowed-workspaces`. Foldable/tablet/large resizable posture changes → `designing-foldable-large-screen-interfaces`. TV/10-foot → `designing-tv-ten-foot-interfaces` plus directional focus. Wearable → `designing-wearable-glanceable-interfaces`. Automotive → `designing-automotive-interfaces`. Spatial/XR → `designing-spatial-xr-interfaces` plus gaze/hand input when applicable. Game HUD/meta menus → `designing-game-hud-and-menus`. CLI/TUI → `designing-cli-tui-interfaces`. Public/dedicated embedded hardware → `designing-embedded-kiosk-interfaces`.

Generic `adapting-platform-conventions` still owns smaller platform deltas; it does not replace these faculties when the surface changes attention, geometry, or input model.

## AI and agent routing
Any consequential AI output routes through `designing-human-ai-interaction` and independent `critiquing-ai-trust-and-agency`. Generated or retrieved claims where origin/freshness matters route to `designing-ai-uncertainty-and-provenance`. Agentic tool/action capability routes to `designing-agent-autonomy-and-control`; standing delegation does not waive this. Streaming model/tool work routes to `designing-streaming-ai-responses`. Editing/regeneration/revert needs route to `designing-ai-feedback-and-correction`. Multiple workers sharing state route to `designing-multi-agent-surfaces`. Runtime-generated interface structures route to `designing-generative-ui` and security/privacy critique.

## Trust and sensitive-domain routing
Authentication/passkeys → `designing-authentication-and-passkeys`. Permission/consent → `designing-permissions-and-consent`. Sensitive data/shared devices → `designing-privacy-sensitive-interfaces`. Checkout → `designing-commerce-checkout`. Collaborative shared state → `designing-collaboration-and-presence`. Canvas/editor semantics → `designing-editor-canvas-workspaces`.

Security/privacy review is independently selected when authorization, account existence, sensitive data, generated actions, consent, payments, public/shared devices, or agent authority creates a boundary. Do not let a design generator decide that its own permission model is safe.

## Temporal and resilience routing
Noticeable latency or long work → `designing-latency-and-progressive-feedback`. Offline/service/peripheral degradation → `designing-offline-degraded-experiences`. Notifications/alerts → `designing-notifications-and-interruptions`. Live changing data → `designing-real-time-updates`. These may add `critiquing-performance-and-resilience` even when implementation performance is not the main user request because state ambiguity can create duplicate or unsafe actions.

## Design-system operations routing
Shared-system contribution/adoption/exception questions → `governing-design-systems`. Component API/state/semantic migration → `evolving-component-apis`. Theme/personalization → `managing-theming-and-personalization`. Durable high-impact rationale → `documenting-design-decisions`. Design-to-code semantic handoff → `annotating-accessibility-intent`.

## Accessibility specialist routing
Root `designing-accessible-interfaces` remains the baseline. Add `designing-cognitive-accessibility` for memory/comprehension/attention/consistency barriers; `designing-low-vision-and-high-contrast` for magnification/reflow/forced-colors; `designing-screen-reader-experiences` for complex semantics/dynamic UI; `designing-reduced-motion-and-photosensitivity` for motion, flash, game camera, parallax, or XR comfort; and `designing-alternative-input` for non-primary motor paths. Specialist skills strengthen rather than replace root obligations.

## Research routing
Use `researching-ui-frontiers` when currentness is material or the atlas has an unknown surface/mechanism. `calibrating-ui-authority` resolves conflicts. `translating-standards-into-obligations` turns applicable authoritative guidance into testable obligations. `maintaining-ui-domain-atlas` changes coverage only for genuinely new decision classes. `measuring-research-saturation` is used at the end of a substantial research wave, never as a reason to stop early.

## Hard routing
The following routes are mandatory and MUST NOT be waived by visual preference, framework choice, time pressure, or user wording such as “just build it”:

- automotive + driving → `designing-automotive-interfaces` + `engineering-human-factors` + `critiquing-human-factors-and-safety`; include voice/input contracts when used.
- spatial-xr → `designing-spatial-xr-interfaces` + `designing-gaze-hand-spatial-input` when gaze/hand applies + `critiquing-platform-fit` + `critiquing-input-modality`.
- tv-ten-foot → `designing-tv-ten-foot-interfaces` + `designing-gamepad-remote-focus` + modality verification.
- wearable → `designing-wearable-glanceable-interfaces`; high interruption/density adds cognitive critique.
- any non-none AI role with material output → `designing-human-ai-interaction` + `critiquing-ai-trust-and-agency`.
- agentic → `designing-agent-autonomy-and-control` + `designing-ai-uncertainty-and-provenance`; consequential actions also use high-stakes decision controls.
- generative-ui → `designing-generative-ui` + `critiquing-security-and-privacy` + accessibility verification.
- medical → `designing-medical-safety-critical-ui` + `engineering-human-factors` + `designing-high-stakes-decisions` + `critiquing-human-factors-and-safety`.
- safety-critical → human factors + high-stakes decision + safety critic.
- functional drag → accessible drag/drop contract and an applicable alternative path.
- streaming/realtime/offline-degraded → the corresponding temporal faculty + resilience critic.

These rules are also enforced by deterministic `validate_mandatory_routes`; prose routing is not the only control.

## Independent verification routing
Generation and verification are separate graphs. Select critics from failure impact, even if the corresponding generation skill was not needed. Available courts include visual design, UX, accessibility, design system, responsive, platform, human-factors/safety, AI trust/agency, modality, cognitive load, security/privacy, research validity, performance/resilience, localization, and fidelity.

A hard-gate critic cannot be marked inactive because the visual critic is positive. Inactive faculties require an observable reason tied to the profile, such as “no AI role,” not “seems unnecessary.”

## Sequence by dependency
Prefer stable upstream contracts: product/users/task analysis → IA/flow → interaction/semantics/states → human-factor/modality/surface constraints → visual direction/craft → tokens/components/system → inclusive/platform/temporal specifics → render → independent courts → evidence gate. Research may precede any stage whose assumptions are stale. Parallel leaves may run when they consume the same stable inputs.

## Output: `ui-task-profile`
Return every profile dimension plus `selected_skills[] {name, reason, required_inputs, expected_output}`, `inactive_faculties[] {faculty, reason}`, `mandatory_routes[]`, `critical_paths[]`, `verification_lenses[]`, `authority_dependencies[]`, `research_freshness_gaps[]`, `capability_gaps[]`, and `routing_confidence`.

Before execution, validate mandatory routes deterministically when the profile contains a hard-route predicate.

## Failure Traps
- Keyword routing: “dashboard” automatically means charts/cards/dark mode.
- Maximal routing: all 112 skills loaded “to be safe.”
- Aesthetic routing before product/task semantics.
- Treating responsive web as native mobile, TV, desktop, wearable, car, or XR.
- Treating an AI badge as sufficient human-AI routing.
- Calling a high-risk reviewer optional because unit tests pass.
- Current platform visual trends promoted into universal style law.
- Research source count used as a proxy for research saturation.

The router is correct when it is small enough to protect context and strict enough that no material failure domain disappears.