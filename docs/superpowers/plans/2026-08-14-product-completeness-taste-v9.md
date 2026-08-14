# NUI V9 Product Completeness & Taste Intelligence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make NUI reason broadly enough to design complete production-grade products while also ranking visual quality, critiquing real renders, eliminating default-browser residue, preserving domain/audience fit, and translating design intent into faithful implementation.

**Architecture:** V9 adds a bounded product-envelope layer above the existing capability ledger and closure graph, plus a separate perceptual/taste layer above V8 flagship synthesis. It does not replace the 174-skill graph: new owners exist only where V8 lacks canonical ownership, while existing editor, desktop, interaction, aesthetic, platform and closure faculties receive explicit V9 protocols. Deterministic Python validators make the new contracts falsifiable and the completion gate refuses claims that are internally closed but externally under-scoped.

**Tech Stack:** Python 3.10+, unittest, Markdown skill contracts, JSON knowledge/eval artifacts, GitHub Actions.

## Global Constraints

- Always explore a broad product capability envelope before narrowing implementation scope; broad discovery does not mean every discovered capability is required.
- Every expected capability receives an explicit disposition: `REQUIRED`, `EXPECTED`, `OPTIONAL`, `EXCLUDED`, or `UNKNOWN`.
- No full-platform completion claim may pass with unresolved `UNKNOWN` or undispositioned high-impact expected capabilities.
- Visual taste is comparative and evidence-bearing; it may rank candidates but may not override accessibility, security, product truth, platform or functional closure gates.
- Screenshot critique must reason from rendered evidence, not from spec text alone.
- Native/default browser or OS appearance is permitted only when intentional and platform-appropriate; accidental residue is a defect.
- Reference knowledge teaches mechanisms, not imitation; provenance and source role remain explicit.
- Domain signatures and audience profiles constrain aesthetic choices without turning product classes into rigid templates.
- Motion must have semantic purpose, interruption/reduced-motion behavior and implementation fidelity.
- V9 remains backward-compatible with V8 validation entry points.

---

### Task 1: Product capability envelope and scope-adequacy kernel

**Files:**
- Create: `src/nolane_ui/product_v9.py`
- Create: `tests/test_product_v9.py`

**Interfaces:**
- Produces: `validate_capability_envelope(record)`, `validate_settings_architecture(record)`, `validate_account_workspace_lifecycle(record)`, `validate_interface_residue_audit(record)`, `validate_taste_comparison(record)`, `validate_render_critique(record)`, `validate_domain_audience_fit(record)`, `validate_render_fidelity(record)`, `validate_v9_product_system(record)`.

- [ ] Write failing tests proving a tiny “complete sales platform” envelope is rejected, expected capabilities require disposition, settings require scope/inheritance/search/recovery, account lifecycle requires post-auth states, default residue requires intentional treatment, taste requires comparative evidence, screenshot critique requires render evidence, and domain/audience fit plus render fidelity are independently gated.
- [ ] Push RED commit and confirm GitHub Actions fails because `nolane_ui.product_v9` does not exist.
- [ ] Implement minimal deterministic validators with explicit error messages and no hidden scoring magic.
- [ ] Confirm targeted and full CI pass.

### Task 2: V9 completion facade and package API

**Files:**
- Modify: `src/nolane_ui/validators.py`
- Modify: `src/nolane_ui/__init__.py`
- Modify: `pyproject.toml`
- Create: `tests/test_v9_completion.py`

**Interfaces:**
- Produces: `validate_v9_completion_evidence(record)` and public exports for V9 validators.
- Consumes: all Task 1 validators and inherited `validate_v8_completion_evidence`.

- [ ] Write tests proving full-platform/product-platform claims require capability-envelope and scope-adequacy evidence; flagship/exceptional visual claims require taste + render critique + render fidelity; material settings/account surfaces require their contracts.
- [ ] Implement the V9 facade without weakening V8 gates.
- [ ] Bump package version to `0.9.0` and export new API.
- [ ] Run completion tests and full CI.

### Task 3: New canonical owner skills

**Files:**
- Create: `skills/expanding-product-capability-envelope/SKILL.md`
- Create: `skills/architecting-account-workspace-lifecycle/SKILL.md`
- Create: `skills/architecting-settings-preference-systems/SKILL.md`
- Create: `skills/eliminating-unintentional-interface-residue/SKILL.md`
- Create: `skills/critiquing-product-scope-adequacy/SKILL.md`

**Interfaces:**
- Product-envelope output feeds capability inventory and the independent scope critic.
- Account/settings owners feed capability, flow, state, privacy/security and closure artifacts.
- Residue owner feeds platform-fit, implementation fidelity and render critique.

- [ ] Define narrow ownership boundaries to avoid duplicating authentication, theming, platform or functional-completeness owners.
- [ ] Encode discovery-first / disposition-second behavior with falsification and recovery.
- [ ] Add concrete protocols for role/lifecycle/settings scope, default chrome, scrollbar strategy, native controls, focus/caret/selection, system dialogs, overflow and micro-surface treatment.
- [ ] Verify metadata/graph tests and repair only legitimate graph obligations.

### Task 4: Deepen existing flagship, editor, desktop, interaction and aesthetic skills

**Files:**
- Modify: `skills/exploring-aesthetic-directions/SKILL.md`
- Modify: `skills/critiquing-visual-quality/SKILL.md`
- Modify: `skills/verifying-rendered-ui/SKILL.md` (or the canonical rendered-verification skill present in the graph)
- Modify: `skills/designing-editor-canvas-workspaces/SKILL.md`
- Modify: `skills/designing-desktop-windowed-workspaces/SKILL.md`
- Modify: `skills/engineering-rich-interactive-components/SKILL.md`
- Modify: `skills/routing-ui-work/SKILL.md`

**Interfaces:**
- Add V9 protocols for taste discrimination, screenshot A/B critique, instrument architecture, professional-workspace completeness, motion cadence, and hard routing of product-wide/full-platform work.

- [ ] Add a comparative taste protocol that distinguishes correct from refined/premium/editorial/domain-native outcomes.
- [ ] Add screenshot-based director critique: focal hierarchy, rhythm, density variance, type refinement, spacing breath, material coherence, mobile preservation and A/B verdict.
- [ ] Add instrument architecture for tool-rich products: global shell, modes, tools, context inspector, secondary panels, command/search, history, status and persistent workspace state.
- [ ] Deepen motion from animation mechanics to structural teaching, causality, emotional cadence and intentional absence.
- [ ] Route product-wide/full-platform tasks through the V9 envelope and scope critic.

### Task 5: Curated reference, domain signature and implementation-fidelity knowledge

**Files:**
- Create: `knowledge/v9-design-benchmark-gallery.json`
- Create: `knowledge/v9-domain-signatures.json`
- Create: `knowledge/v9-render-fidelity.json`
- Create: `tests/test_v9_knowledge.py`

**Interfaces:**
- References are mechanism-tagged exemplars, never copy targets.
- Domain records express trust/density/emotional/interaction expectations as hypotheses and constraints.
- Render-fidelity rules bridge skill intent to tokens/components/CSS/runtime verification.

- [ ] Test required schema fields, mechanism tags, anti-copy language, domain/audience dimensions and implementation constraints.
- [ ] Curate references across product/editorial/developer/creative/commerce categories with explicit mechanism lessons.
- [ ] Encode domain signatures for fintech, medtech, developer tools, creative tools, AI products, education, commerce and consumer social/content surfaces.
- [ ] Encode typography, spacing, line-height, border/opacity, elevation, motion, breakpoint, density, scrollbar/native-control and visual-regression obligations.

### Task 6: Adversarial V9 evaluation corpus

**Files:**
- Create: `evals/v9-product-completeness-adversarial.json`
- Create: `tests/test_v9_adversarial.py`

**Interfaces:**
- Cases falsify narrow-scope closure, decorative feature inflation, settings omission, auth-lifecycle omission, classic scrollbar residue, generic dashboard monoculture, “pretty but cheap” taste errors, screenshot/spec divergence, wrong-domain aesthetics, audience mismatch and gratuitous motion.

- [ ] Write schema/integrity test first.
- [ ] Add at least 24 causally distinct adversarial cases with expected verdict and protected invariant.
- [ ] Require cases to include both false-positive and false-negative traps.

### Task 7: Repository gate, release evidence, CI artifact and closure docs

**Files:**
- Create: `src/nolane_ui/v9_repository.py`
- Modify: `src/nolane_ui/validators.py`
- Modify: `scripts/nui-release-packet`
- Modify: `.github/workflows/verify.yml`
- Create: `docs/V9-PRODUCT-COMPLETENESS-TASTE-CLOSURE.md`
- Modify: `README.md`
- Create: `tests/test_v9_repository.py`

**Interfaces:**
- `v9_repository.extend(root, base)` asserts V9 source/skills/knowledge/evals/docs/version exist and are structurally valid.
- Release packet emits V9 obligations and CI packages `Nolane-UI-Intelligence-v9-complete.zip`.

- [ ] Write repository-gate test first.
- [ ] Add V9 repository extension and chain it after V8 validation.
- [ ] Update release packet, workflow artifact names and closure documentation.
- [ ] Run full GitHub Actions on `build/v9-product-completeness` until green.
- [ ] Fast-forward `main` to the verified V9 commit, rerun main CI, download the complete-project artifact, and persist the archive to ChatGPT Library.

## Self-review

- Spec coverage: all user-requested dimensions are mapped: full product scope, connected capability graph, login/account/settings lifecycle, professional tool workspaces, classic/default residue, taste engine, screenshot critique, curated benchmark memory, skill→render fidelity, domain signature, audience sensitivity and deep motion.
- Duplication control: authentication, theming, editor, desktop, platform and functional closure remain canonical; V9 owners cover only missing scope/disposition/residue ownership.
- Safety/quality precedence: taste never overrules accessibility/security/platform/product truth.
- Placeholder scan: no deferred implementation items are accepted as completion.
- Type consistency: all V9 public validator names are defined in Task 1 or Task 2 before repository/release integration.
