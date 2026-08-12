# Nolane UI Intelligence — Universal Design Cognition & Verification System

## Status
Approved for implementation on 2026-08-12.

## Purpose
Nolane UI Intelligence (NUI) is a platform-agnostic Agent Skill system for designing, implementing, criticizing, and verifying UI/UX work. It is not a style preset, a component library, a prompt that says “make it beautiful,” or a claim that an LLM can deterministically judge beauty. NUI constrains the observable design process so an agent must establish product intent, information architecture, interaction semantics, visual direction, design-system rules, component states, responsive behavior, accessibility obligations, implementation fidelity, and independent verification before it can make a bounded completion claim.

The system is designed to improve agents across Codex, Claude Code, Gemini CLI, Cursor, OpenCode, GitHub Copilot, and generic Agent Skills runtimes through a universal core plus runtime adapters.

## Non-negotiable principles
1. **Design before implementation when design is material.** A new or materially redesigned interface may not jump directly from prompt to code.
2. **A build is not a design proof.** Compiling, linting, or rendering does not establish UX quality, visual quality, accessibility, or fidelity.
3. **A design may not certify itself.** Generative skills produce artifacts; critic skills evaluate them under independent contracts.
4. **Unknown is not pass.** Missing evidence produces `UNKNOWN` or `BLOCKED`, never an inferred success.
5. **Deterministic facts belong to deterministic checks.** Token consistency, required files, state coverage, graph validity, contrast arithmetic, and evidence freshness must not depend solely on model self-report.
6. **Normative sources outrank heuristics.** User/product requirements, standards, and platform guidance outrank community style opinions.
7. **No aesthetic dogma.** Cards, gradients, glass, serif faces, minimalism, maximalism, and motion are contextual tools, not universal good/bad patterns.
8. **Beauty must coexist with usability.** A visually striking result that harms task success, legibility, accessibility, trust, or platform expectations is not a successful UI.
9. **Progressive disclosure applies to the skill system itself.** The router loads only the faculties needed for the current problem.
10. **Every completion claim is bounded.** The agent states what was verified, with which evidence, and what remains unverified.

## Authority hierarchy
When guidance conflicts, apply this order:

`L0 User/product requirements > L1 normative standards > L2 authoritative platform guidance > L3 project design system > L4 direct measured evidence > L5 mature design-system guidance > L6 high-quality agent skill heuristics > L7 community heuristics > L8 model preference`.

Lower layers may refine higher layers but may not silently override them.

## Lifecycle
The required lifecycle for material UI work is:

`INTAKE → CONTRACTED → ROUTED → DISCOVERED → ARCHITECTED → DIVERGED → DESIGN_SELECTED → SYSTEMIZED → SPECIFIED → IMPLEMENTABLE → RENDERED → CRITIQUED → VERIFIED → RELEASED`

Any contradiction, failed gate, stale evidence, inaccessible interaction, broken responsive state, or fidelity regression routes to `RECOVERY`. Recovery preserves failed evidence and findings; it does not erase them.

### Lightweight exception
Tiny local UI changes may use a reduced path only when the router records why product discovery, divergence, or systemization is unnecessary. Reduced scope never waives relevant accessibility, interaction, regression, or verification obligations.

## Architecture
NUI uses four layers:

### 1. Cognitive kernel
A small mandatory layer owns lifecycle, authority, routing, obligations, evidence, adversarial review, recovery, and completion.

Core skills:
- `using-nolane-ui`
- `nolane-ui`
- `ui-contracting`
- `routing-ui-work`
- `compiling-ui-obligations`
- `binding-ui-evidence`
- `challenging-ui-designs`
- `gating-ui-completion`
- `recovering-ui-work`

### 2. Design faculties
Narrow skills own one kind of judgment. Initial families:
- product intent and user/task modeling
- information architecture and navigation
- interaction architecture and component semantics
- aesthetic exploration and art direction
- visual hierarchy, composition, typography, color, spacing, depth, iconography, imagery
- design tokens and component systems
- responsive/adaptive behavior and platform conventions
- accessibility, inclusive design, localization, RTL, and content design
- dashboards, forms, search, data visualization, onboarding, empty/error states
- implementation fidelity and visual QA

### 3. Deterministic kernel tools
Python utilities validate machine-checkable invariants. Initial tools validate skill metadata, skill graph integrity, contracts, completion packets, state matrices, token tiers, evidence records, and quality-gate structure.

### 4. Runtime adapters
Adapters translate generic capabilities into platform instructions without contaminating the universal core. Initial adapters target generic Agent Skills, Codex, Claude Code, Gemini CLI, Cursor, and OpenCode.

## Router model
The router first produces a typed `UI_TASK_PROFILE` rather than choosing skills from keywords alone. The profile captures:
- intent: design, redesign, audit, reproduce, implement, verify
- surface family and product subtype
- primary/secondary platforms
- user expertise and task frequency
- information density and volatility
- interaction modality, destructive actions, keyboard/touch intensity
- brand state, novelty tolerance, emotional target
- accessibility, localization, RTL, privacy, trust, and safety constraints
- available references and required fidelity
- implementation/runtime capabilities

The router then selects the minimum sufficient faculty set. It must record why each selected faculty is required and why any normally relevant faculty is intentionally inactive.

## Design reasoning model
### Product and task model
Before visual styling, the agent identifies primary users, high-value jobs, frequent/critical tasks, decision points, information priorities, trust requirements, error costs, and constraints.

### Information architecture
The agent establishes content grouping, labels, navigation model, wayfinding, search/findability, hierarchy depth, and task pathways. Visual grouping must follow semantic grouping rather than substitute for it.

### Interaction architecture
Interactive surfaces require an explicit model of affordance, input modality, focus, feedback, undo/recovery, destructive confirmation, async transitions, permission states, and interruption cost.

### Aesthetic search
Instead of mapping a product category to a fixed visual preset, NUI derives an aesthetic search space from product semantics, audience, brand personality, desired emotion, trust requirements, information density, task frequency, platform, cultural context, and novelty tolerance. When exploration is valuable, candidate directions must differ structurally, not merely by recoloring the same layout.

### Constraint solver
Component choices must be justified by user/task and interaction constraints. A card, modal, drawer, tooltip, tab, table, or carousel is not valid because it is fashionable; the agent must state the semantic/interaction reason the pattern exists and the failure mode avoided by the chosen pattern.

## Component state algebra
Applicable component states are derived from:

`structure × content × interaction state × validation state × async state × permission state × viewport × modality × theme × locale × accessibility mode`.

The router computes an applicable subset. Required examples include default, hover when applicable, keyboard focus, pressed/selected, disabled, loading, empty, error, success, permission denied, long-content stress, RTL where relevant, reduced motion, high contrast, touch, and narrow viewport.

## Design-system model
Tokens use four semantic tiers:
1. primitive values
2. semantic aliases
3. component tokens
4. contextual/state overrides

Component APIs separate semantic role from surface styling. Reuse is preferred when it preserves product semantics; forced reuse that creates misleading behavior is rejected.

## Accessibility model
Accessibility is integrated at design-time, component-time, and runtime. The system distinguishes normative requirements from automated heuristics. Automated checks are evidence, not a complete proof of accessibility. Relevant flows require keyboard/focus analysis, semantic naming, state exposure, contrast/reflow checks, motion preferences, target sizing, reading order, and assistive-technology considerations.

## Independent critics
A critic must not simply praise or rewrite the design. Findings use a typed shape:

- `finding_id`
- `domain`
- `severity`
- `evidence`
- `violated_constraint`
- `user_impact`
- `falsifier`
- `recommended_repair`
- `status`

Initial critic lenses: visual hierarchy, product/UX friction, information architecture, interaction, design-system consistency, accessibility, responsive behavior, content/UX writing, platform-native behavior, anti-slop/contextual distinctiveness, and fidelity.

## Contextual anti-slop
NUI never bans a visual technique by name alone. Anti-pattern detection evaluates pattern + context + intent + frequency + user impact + justification. Repeated generic decoration with no information or brand function is a finding; a justified use of the same technique is not.

## Fidelity court
When a target exists, the implementation must maintain a fidelity ledger comparing target and render by region and dimension: geometry, typography, color, imagery, spacing, hierarchy, state, interaction, and responsive behavior. Missing comparison blocks completion for high-fidelity work.

## Evidence model
Evidence records include source, timestamp, scope, artifact digest where possible, method, claim supported, and freshness. Evidence may be direct measurement, screenshot comparison, browser observation, automated audit, interaction test, semantic/accessibility tree snapshot, design token validation, or documented manual inspection. A completion packet references evidence; it may not merely say that verification happened.

## Completion gate
A release packet is accepted only when:
- lifecycle phase is valid
- task contract and routing profile exist
- required obligations are present and resolved
- relevant design direction/system artifacts exist
- applicable component states are covered
- critical flows are verified
- independent critic findings have no unresolved critical/major blockers
- evidence references are valid and fresh enough for the claim
- required deterministic checks pass
- completion bounds and unknowns are explicit

## Skill authoring rules
Each skill must have:
- valid Agent Skills frontmatter
- a trigger-only `description` beginning with `Use when...`
- one responsibility
- required parent or invocation context
- input contract
- procedure expressed as observable actions
- typed output/return contract
- stop conditions
- rationalization counters when the skill enforces discipline
- a compact quick reference
- common failures
- links to heavy references instead of duplicating encyclopedic content

Descriptions may not summarize the workflow; agents must read the body.

## Source-use policy
NUI synthesizes mechanisms from authoritative standards and high-quality public skill systems. It does not bulk-copy third-party copyrighted skill text. External material is recorded in `docs/research/SOURCES.md` with source purpose and license notes when available. Normative standards are referenced rather than mirrored unless redistribution terms clearly permit it.

## Evaluation strategy
NUI is not allowed to claim superiority by repository size. Evals cover:
- routing correctness
- lifecycle/gate compliance under pressure
- aesthetic diversity
- information hierarchy
- component state completeness
- responsive stress
- keyboard/focus behavior
- accessibility obligations
- localization/RTL stress
- design-system consistency
- screenshot/fidelity reproduction
- anti-slop contextual reasoning
- dashboard/forms/search/data-viz specialist surfaces
- adversarial completion attempts

The initial repository includes deterministic fixtures plus pressure-scenario specifications. Live cross-model benchmark results require compatible agent runtimes and are reported separately; absent runtime execution is recorded as unverified, not passed.

## Success criteria for v1
V1 is complete when the repository contains a valid universal skill graph; deep kernel and core design faculties; deterministic validators and tests; source/research ledger; adapters for the targeted runtimes; eval fixtures and pressure scenarios; installation/usage documentation; and a verified completion packet produced by the repository's own validator.
