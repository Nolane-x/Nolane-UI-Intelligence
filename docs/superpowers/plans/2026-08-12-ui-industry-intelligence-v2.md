# Nolane UI Industry Intelligence v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand Nolane UI Intelligence from 47 general UI skills into a domain-complete UI industry reasoning system with a machine-readable atlas, research-saturation controls, deep platform/modality/AI/risk faculties, independent critics, and deterministic coverage gates.

**Architecture:** Keep the v1 lifecycle and evidence gate unchanged as the authority layer. Add an orthogonal UI Industry Atlas and source ledger; route only task-relevant domain faculties from the expanded task profile; use deterministic validators for ownership/freshness/mandatory-route invariants and independent critics for judgment-heavy verification.

**Tech Stack:** Agent Skills Markdown/YAML, JSON knowledge ledgers and eval fixtures, Python 3 standard library, `unittest`, GitHub Actions.

## Global Constraints
- The v1 kernel and exact-revision completion semantics MUST remain authoritative.
- New skills MUST own unique decisions or failure modes; count is not a target.
- Current visual trends MUST remain contextual knowledge, never universal aesthetic defaults.
- Missing atlas ownership, source authority, evidence, or required critic coverage MUST block rather than infer PASS.
- WCAG 3 MUST be labeled draft; WCAG 2.2 remains the normative web conformance baseline captured by this wave.
- Third-party prose/databases MUST NOT be bulk-copied; mechanisms are synthesized and provenance recorded.
- Safety/security/accessibility/agency hard gates MUST NOT be offset by aesthetic quality scores.
- No placeholder, TODO, TBD, generated filler, or empty skill shell is permitted.

---

### Task 1: RED — industry coverage contract
**Files:** create `tests/test_industry_atlas.py`, `tests/test_router_v2.py`, `tests/test_research_saturation.py`, `evals/v2/coverage/required-domains.json`.

**Interfaces:** tests consume the current graph/router and future `knowledge/ui-domain-atlas.json`, `knowledge/source-ledger.json`, `knowledge/research-saturation.json`.

- [ ] Add a failing test asserting mandatory surfaces include web, mobile, desktop, large-screen/foldable, TV, wearable, automotive, spatial/XR, game/HUD, CLI/TUI, and embedded/kiosk.
- [ ] Add a failing test asserting each mandatory surface has at least one owner skill and one verifier skill declared in the graph.
- [ ] Add a failing router test asserting v2 task-profile dimensions exist and risk/platform-specific mandatory routes cannot be omitted.
- [ ] Add a failing saturation test asserting breadth, depth, contradiction, novelty, and freshness evidence are present.
- [ ] Push RED commit and confirm GitHub CI fails for missing v2 artifacts/fields, not syntax errors.

### Task 2: Knowledge plane and research authority
**Files:** create `knowledge/ui-domain-atlas.json`, `knowledge/source-ledger.json`, `knowledge/research-radar.json`, `knowledge/research-saturation.json`; create skills `researching-ui-frontiers`, `calibrating-ui-authority`, `maintaining-ui-domain-atlas`, `measuring-research-saturation`, `translating-standards-into-obligations`.

**Interfaces:** produces `research-wave`, `authority-resolution`, `coverage-delta`, `saturation-decision`, and `standard-obligation-set`.

- [ ] Populate atlas axes and mandatory coverage cells from the approved design.
- [ ] Populate source ledger with authoritative sources actually reviewed in this wave, recording status, domain, drift, reviewed date, license/use note, and absorbed mechanism.
- [ ] Encode research radar with high-drift platform/AI/accessibility/automotive/safety sources.
- [ ] Implement the five research skills with distinct responsibilities and parent contracts.
- [ ] Extend graph with research skills and validate no parent cycle or output collision.

### Task 3: Human factors and research faculties
**Files:** create skills `engineering-human-factors`, `modeling-cognitive-load-and-attention`, `modeling-perception-and-motor-control`, `conducting-task-analysis`, `planning-usability-research`, `evaluating-usability-evidence`, `designing-high-stakes-decisions`; create `evals/v2/human-factors/cases.json`.

**Interfaces:** produces `human-factors-model`, `attention-budget`, `perceptual-motor-envelope`, `task-analysis`, `research-plan`, `usability-evidence-assessment`, `high-stakes-decision-contract`.

- [ ] Add adversarial cases for alarm fatigue, repeated confirmation blindness, time pressure, weak evidence, and memory-heavy flows.
- [ ] Write each skill around observable human constraints and evidence, not generic usability slogans.
- [ ] Route high-risk classes through human-factors faculties automatically.

### Task 4: Input modality intelligence
**Files:** create skills `designing-keyboard-power-user-ux`, `designing-pointer-touch-pen-input`, `designing-accessible-drag-and-drop`, `designing-gamepad-remote-focus`, `designing-voice-conversational-ui`, `designing-gaze-hand-spatial-input`, `designing-haptics-and-multisensory-feedback`, `designing-alternative-input`; create `evals/v2/modalities/cases.json`.

**Interfaces:** each skill produces a modality contract including discoverability, focus/target model, alternative path, error recovery, and applicable accessibility obligations.

- [ ] Add fixtures for keyboard-only, imprecise pointer, no-drag alternative, D-pad focus trap, speech ambiguity, gaze dwell, haptic-only signal, and switch-control navigation.
- [ ] Require concurrent-input and alternative-path reasoning when multiple modalities coexist.
- [ ] Make modality critics independently verify focus, target, gesture alternatives, and feedback channels.

### Task 5: Surface/platform intelligence
**Files:** create skills `designing-desktop-windowed-workspaces`, `designing-foldable-large-screen-interfaces`, `designing-tv-ten-foot-interfaces`, `designing-wearable-glanceable-interfaces`, `designing-automotive-interfaces`, `designing-spatial-xr-interfaces`, `designing-game-hud-and-menus`, `designing-cli-tui-interfaces`, `designing-embedded-kiosk-interfaces`; create platform eval fixtures.

**Interfaces:** produces platform contracts for geometry, viewing distance, focus/navigation, density, interruption model, environmental conditions, and platform deltas.

- [ ] Add desktop multiwindow/shortcut, foldable reflow, TV remote, watch glance, driving distraction, XR comfort, HUD legibility, terminal keyboard, and kiosk recovery scenarios.
- [ ] Encode automotive driving/parked context as a hard router distinction.
- [ ] Encode XR field-of-view and gaze/hand input as required supporting faculties rather than decorative 3D guidance.

### Task 6: AI, agent, and generative UI intelligence
**Files:** create skills `designing-human-ai-interaction`, `designing-agent-autonomy-and-control`, `designing-ai-uncertainty-and-provenance`, `designing-streaming-ai-responses`, `designing-ai-feedback-and-correction`, `designing-multi-agent-surfaces`, `designing-generative-ui`; create `evals/v2/ai-agent/cases.json`.

**Interfaces:** produces `human-ai-contract`, `autonomy-envelope`, `provenance-contract`, `stream-contract`, `correction-contract`, `multi-agent-context-model`, `generative-ui-runtime-contract`.

- [ ] Add cases for hidden AI identity, overconfident output, irreversible agent action, stale streaming state, missing cancel/revert, multi-agent attribution collision, and arbitrary-code generative UI.
- [ ] Require action scope, reversibility, provenance, uncertainty, latency, and human control whenever material.
- [ ] Require generated UI to declare allowed component vocabulary, schema/data/action binding, semantic accessibility, and recovery boundary.

### Task 7: Trust, safety, transactions, and specialist domains
**Files:** create skills `designing-authentication-and-passkeys`, `designing-permissions-and-consent`, `designing-privacy-sensitive-interfaces`, `designing-medical-safety-critical-ui`, `designing-financial-transaction-ui`, `designing-commerce-checkout`, `designing-collaboration-and-presence`, `designing-editor-canvas-workspaces`; create `evals/v2/trust-safety/cases.json`.

**Interfaces:** produces authentication, consent, privacy, safety, transaction, checkout, collaboration, and workspace contracts.

- [ ] Add passkey recovery/user-enumeration, coercive consent, privacy leakage, dose/action confirmation, financial irreversible action, checkout error recovery, presence ambiguity, and editor undo/history cases.
- [ ] Require high-risk confirmation to communicate object/action/consequence/reversibility rather than add generic modal friction.
- [ ] Route medical/safety-critical work through human-factors and safety critic automatically.

### Task 8: Temporal, resilience, and design-system operations
**Files:** create skills `designing-latency-and-progressive-feedback`, `designing-offline-degraded-experiences`, `designing-notifications-and-interruptions`, `designing-real-time-updates`, `governing-design-systems`, `evolving-component-apis`, `managing-theming-and-personalization`, `documenting-design-decisions`, `annotating-accessibility-intent`; create resilience/system evals.

**Interfaces:** produces latency, degraded-mode, interruption, realtime, governance, migration, theme, decision-record, and accessibility-annotation contracts.

- [ ] Add duplicate-action latency, reconnect merge, alert fatigue, realtime reorder, breaking component API, token migration, high-contrast theme, lost rationale, and semantics-regression scenarios.
- [ ] Treat performance feedback as interaction correctness, not merely engineering optimization.
- [ ] Require design-system changes to carry migration/deprecation and semantic impact.

### Task 9: Deep accessibility and independent critics
**Files:** create skills `designing-cognitive-accessibility`, `designing-low-vision-and-high-contrast`, `designing-screen-reader-experiences`, `designing-reduced-motion-and-photosensitivity`, plus critics `critiquing-human-factors-and-safety`, `critiquing-ai-trust-and-agency`, `critiquing-input-modality`, `critiquing-cognitive-load`, `critiquing-security-and-privacy`, `critiquing-research-validity`, `critiquing-performance-and-resilience`, `critiquing-localization`; create accessibility/critic evals.

**Interfaces:** specialist accessibility obligations and `finding-set` critic outputs with `may_modify: false`.

- [ ] Add cognitive memory/consistency, forced-colors, virtual-cursor reading order, vestibular motion, safety, AI agency, modality, security, performance, and locale adversarial cases.
- [ ] Ensure specialist accessibility skills augment rather than replace the root accessibility skill.
- [ ] Ensure hard-gate critics cannot be omitted by a high visual score.

### Task 10: Router v2 and deterministic validators
**Files:** modify `skills/routing-ui-work/SKILL.md`, `skills/skill-graph.json`, `src/nolane_ui/validators.py`; create `tests/test_industry_validators.py`.

**Interfaces:** add `validate_industry_atlas(atlas, graph)`, `validate_source_ledger(ledger)`, `validate_research_saturation(record, ledger, atlas)`, `validate_mandatory_routes(profile, selected_skills)`.

- [ ] Write failing behavior tests for unowned atlas cells, unknown authority classes, stale high-drift sources, false SATURATED claims, and missing mandatory routes.
- [ ] Implement validators using Python standard library only.
- [ ] Expand router profile and explicit hard-route rules for platform/modality/AI/risk combinations.
- [ ] Run full unit suite and repository validator to green.

### Task 11: Research synthesis, eval rubric, and release gate
**Files:** create `docs/research/UI-INDUSTRY-RESEARCH-2026-08-12.md`, update `docs/research/SOURCES.md`, `docs/research/SYNTHESIS.md`, `README.md`, `docs/USAGE.md`; create `evals/v2/rubric.json`; update release packet generator/CI only if new claims require it.

**Interfaces:** documents bounded research saturation and gives eval runners falsifiable expectations.

- [ ] Record authoritative findings and disagreements with authority/status labels.
- [ ] Add v2 hard gates for safety, accessibility, security/privacy, AI agency, modality reachability, atlas ownership, and research validity.
- [ ] Keep quality dimensions separate from hard gates.
- [ ] Confirm no prose claims permanent completeness or superiority without comparative evidence.

### Task 12: Final verification, merge, ZIP, and Library persistence
**Files:** CI-generated artifacts plus final delivery ZIP.

**Interfaces:** exact-revision GitHub Actions evidence and recoverable Library artifact.

- [ ] Run PR CI on exact branch tree and inspect logs, not just status badges.
- [ ] Review diff for repetitive filler, duplicate skill ownership, source-status mistakes, and gate loopholes.
- [ ] Fix important findings with RED-GREEN regression coverage.
- [ ] Merge only after CI succeeds.
- [ ] Verify post-merge `main` CI separately.
- [ ] Download CI-packaged complete project, add exact main completion evidence, CRC/SHA verify delivery ZIP, and upload a copy to ChatGPT Library.

## Self-review
Every approved v2 architecture section has an implementation task. High-risk domains have both generation and independent verification ownership. Research saturation is explicitly bounded by time and evidence rather than treated as permanent completeness. No task relies on placeholder content or on a future unspecified validator. The plan preserves v1 completion semantics and adds coverage without making the router load every faculty.