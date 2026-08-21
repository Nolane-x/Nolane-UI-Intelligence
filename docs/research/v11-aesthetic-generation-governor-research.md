# V11 Phase 4 — Aesthetic Generation Governor Research Synthesis

**Date:** 2026-08-21

**Purpose:** Record external research that informed Phase 4 questions, workflow structure, and falsification strategies. This document is a research ledger, not an implementation provenance claim.

## Transfer boundary

All Phase 4 code, schemas, rule wording, thresholds, state transitions, evaluation contracts, and tests are independently authored for NUI.

External systems may contribute:

- a problem framing;
- a workflow pattern worth testing;
- a perceptual/craft dimension worth observing;
- a falsification method;
- a quality-control habit.

They do not contribute copied implementation, copied skill bodies, copied rule text, a global house style, or authority to override product/user/platform truth.

## 1. Impeccable

Primary references inspected:

- https://github.com/pbakaus/impeccable/blob/main/plugin/skills/impeccable/SKILL.md
- https://github.com/pbakaus/impeccable/blob/main/skill/reference/new-work.md
- https://github.com/pbakaus/impeccable/blob/main/skill/reference/live.md
- https://github.com/pbakaus/impeccable/blob/main/skill/reference/craft-floor.md
- https://github.com/pbakaus/impeccable/blob/main/skill/reference/document.md
- https://github.com/pbakaus/impeccable/blob/main/PRODUCT.md

### Useful ideas

- Treat visibly AI-generated/generic output as a real production-quality failure, not only as user preference language.
- Commit to a chosen visual world instead of allowing implementation to drift back toward safe defaults.
- Separate “craft floor” checks from visual direction selection.
- Extract incumbent product identity before varying an existing surface.
- Generate variants on genuinely different axes (hierarchy, topology, typography, density, decomposition, etc.), not palette swaps.
- Keep live variation inside identity unless departure is explicitly authorized.
- Store a project design description so later agents have a stable identity reference.
- Run bounded inspection/fix cycles rather than unlimited self-polish.

### What NUI deliberately does not inherit

- fixed universal radius ranges;
- fixed font bans;
- fixed category-to-light/dark prescriptions;
- universal statements that one shadow/border recipe is always correct;
- implementation/config formats;
- detector wording/thresholds;
- catalog-driven aesthetic worlds as product authority.

### NUI elevation

NUI separates stable craft hypotheses from time-bounded trend tells, routes every observation to existing canonical owners, requires falsifiers, preserves product authority, and refuses to reduce genericity to one style blacklist or one AI score.

## 2. Anthropic — Prompting for frontend aesthetics

Reference inspected:

- https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics

### Useful ideas

Anthropic explicitly documents that frontier models can converge toward generic, conservative visual outputs without targeted guidance. The guide improves output by allocating attention to typography, color/theme, motion, backgrounds, and common model defaults.

### What NUI learns

- model default convergence is a generation-time problem, not only a post-render problem;
- visual dimensions should receive explicit attention before generation;
- commitment to a coherent direction matters;
- current overused defaults may be worth surfacing as warnings.

### What NUI changes

NUI does not encode “avoid Inter,” “avoid purple gradients,” or any other contemporary default as timeless authority. Current model-convergence tells belong in an expiring research-backed registry. Stable rules operate on product specificity, causality, hierarchy, accumulation, and evidence.

## 3. Vercel — Web Interface Guidelines

Reference inspected:

- https://vercel.com/design/guidelines

### Useful ideas

The guideline set treats interface quality as hundreds of decisions across interaction, animation, layout, accessibility, design detail, browser behavior, and performance. Particularly relevant Phase 4 lenses include:

- optical alignment;
- intentional alignment anchors;
- responsive verification across form factors;
- interruptible/purposeful motion;
- interaction state clarity;
- nested geometry/material relationships;
- font loading and rendered text quality;
- explicit browser-residue handling.

### NUI adaptation

NUI uses these as candidate observable dimensions for craft evidence. A Vercel recommendation is not automatically a NUI rule: each admitted rule needs local scope, falsifier, owner, false-positive tests, and compatibility with the project’s selected design system.

## 4. Linear — Output isn’t design

Reference inspected:

- https://linear.app/now/output-isn-t-design

### Useful ideas

Linear distinguishes generated form from design and frames good design as fit between form and full context: human needs, technical constraints, relationships, edge cases, and conflicting requirements.

### NUI adaptation

This directly reinforces the Design Intent Compiler. Phase 4 must not optimize merely for more distinctive form. It must bind product thesis, task, domain objects, constraints, identity, and semantic anchors before generation. “Surprising” output that fits the context worse is a regression.

## 5. Linear — Quality Wednesdays

Reference inspected:

- https://linear.app/now/quality-wednesdays

### Useful ideas

- subtle quality defects are difficult for the original builder to perceive;
- different reviewers catch different small failures;
- repeated small fixes compound into a much higher product quality bar;
- training attention changes future construction behavior so some papercuts stop appearing;
- examples such as inconsistent hover timing and adjacent-control size mismatch can strongly affect perceived finish despite not being major bugs.

### NUI adaptation

Phase 4 creates a bounded Quality Residue Loop after macro direction is sound. The loop focuses on cumulative small defects, preserves evidence, and stops after a limited observe→repair→confirm cycle. It never becomes an infinite pixel-polish agent.

## 6. Linear — A calmer interface for a product in motion

Reference inspected:

- https://linear.app/now/behind-the-latest-design-refresh

### Useful idea

A product can become inconsistent one individually reasonable feature at a time. Pruning and re-establishing predictable placement/rhythm can be a design quality act.

### NUI adaptation

Genericity/craft judgment must inspect accumulation and cross-region coherence, not only isolated components. A hundred locally plausible borders, badges, cards, or controls can form one systemic quality failure.

## 7. GitHub Primer

References inspected:

- https://primer.style/product/getting-started/
- https://primer.style/product/getting-started/foundations/
- https://primer.style/product/getting-started/foundations/layout/
- https://primer.style/product/getting-started/foundations/typography/
- https://primer.style/product/getting-started/foundations/responsive
- https://primer.style/accessibility/foundations/

### Useful ideas

- cohesive familiar behavior can be a quality feature for productivity software;
- accessibility belongs at the beginning of design rather than as retrofit;
- responsive design is an adaptive behavior problem, not desktop shrinkage;
- typography should serve readable hierarchy and semantic structure;
- layout should minimize friction and respect acquired mental models;
- design system foundations provide a stable local identity/implementation vocabulary.

### NUI adaptation

The Generation Governor has an explicit `UTILITY` mode so anti-generic logic does not punish productive familiarity. Identity lock and platform/task fit outrank novelty. Responsive and accessibility hard truth remains non-compensatory in the taste court.

## 8. IBM Carbon

References inspected:

- https://carbondesignsystem.com/guidelines/content/overview/
- https://v10.carbondesignsystem.com/guidelines/spacing/overview/
- https://v10.carbondesignsystem.com/guidelines/themes/overview/

### Useful ideas

- system spacing reduces arbitrary local decisions and clarifies relationships;
- different spacing roles may require different scales/semantics;
- typography, spacing, themes, and content operate as a coherent system rather than isolated visual tweaks;
- content guidance is part of product design quality.

### NUI adaptation

Craft observations should be contract-aware. Literal values, unusual spacing, or distinct typography are not defects when they are authorized by the local system. Drift becomes a finding only relative to an owned design-system/context contract.

## 9. Cross-source synthesis

The strongest common pattern is not a shared visual style. It is a shared **discipline of authored decisions**:

```text
understand context
-> decide what should remain familiar
-> identify where visual freedom is valuable
-> commit to a coherent direction
-> make dimensions work together
-> inspect actual rendered behavior
-> compare alternatives or reviewers when self-judgment is weak
-> detect cumulative small defects
-> repair causally
-> preserve the resulting system for later work
```

That is the mechanism NUI Phase 4 operationalizes.

## 10. Research-derived design laws for Phase 4

These are not aesthetic laws; they are system-design laws for the governor:

1. **Context before novelty.** A distinctive form that fits the product worse is not an improvement.
2. **Identity before variation.** Existing products need explicit departure authority before aesthetic-world changes.
3. **Mechanisms before adjectives.** “Premium,” “bold,” or “editorial” must decompose into observable visual/interaction mechanisms.
4. **Commitment after divergence.** Exploration must end in a frozen direction contract so implementation cannot regress to model defaults.
5. **Accumulation over single tells.** One fashionable pattern is weak evidence; systemic default accumulation is stronger evidence.
6. **Dynamic tells, stable falsifiers.** Trend warnings expire; product specificity and observable consequences remain the durable basis.
7. **Render before final visual judgment.** Source intent cannot substitute for pixels and states actually perceived.
8. **Comparison before scalar taste.** Pairwise dimension evidence is more auditable than one opaque beauty number.
9. **Small defects compound.** Residue deserves a bounded dedicated pass after macro design is correct.
10. **No self-certification.** Generation, critique, runtime observation, and release authority remain separate roles.

## 11. Claim boundary

This research synthesis supports the architecture and test hypotheses for V11 Phase 4. It does **not** prove that NUI improves real-model UI quality. Any causal efficacy claim still requires the existing V10 matched treatment/ablation/holdout/judge-blind empirical protocol.