---
name: critiquing-visual-design
description: Use when an independent reviewer must identify perceptual, compositional, typographic, color, spacing, surface, imagery, or distinctiveness defects in a UI design or render.
---

# Critiquing Visual Design

## Overview
Judge whether the chosen visual direction is executed coherently and supports the product hierarchy. Do not redesign from personal taste.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

`may_modify: false`. Use the accepted aesthetic direction, hierarchy, craft contracts, and inspectable artifact.

## Review lenses
### Thesis fidelity
Can you see the selected visual thesis, or did implementation regress to generic defaults? Identify the specific missing signature or incompatible trope.

### Hierarchy
Name first/second/third focal points. Report competing emphasis, hidden primary actions, excessively loud status/decor, or flat equivalence.

### Composition
Check alignment anchors, container logic, proportion, whitespace grouping, scroll ownership, repetitive section formulas, and nested framing.

### Typography
Check role separation, line length, wrapping, weight/size relationships, control text, numerals, fallback, and whether typography actually carries the intended personality.

### Color/surface
Check semantic role, contrast intent, chroma budget, state distinguishability, dark-theme layering, and unjustified gradient/elevation.

### Rhythm/detail
Check repeated gaps, optical alignment, icon consistency, borders/radii/shadows, media crop, and edge treatment after macro issues are stable.

### Genericity
Use contextual anti-slop rules. A familiar pattern is not a defect by itself; report only when it lacks product/brand function or damages hierarchy.

## Evidence discipline
Each finding cites a visible region/state and a violated design contract/principle. “I don’t like the font” is not a finding. “Utility labels use the display face at nearly heading weight, collapsing role separation specified by typography contract” is.

## Output: `finding-set`
Produce typed findings only. Include a `preserve` note when an existing strength would be easy to damage during repair. End with `BLOCK`, `REPAIR_AND_RETEST`, or `NO_VISUAL_BLOCKER_FOUND` for this lens only.

## V5 Dual-Critic Split
Separate the **execution critic** (“Did the render faithfully execute the selected thesis?”) from the **adequacy critic** (“Was that thesis good enough for the original intent?”). Coherent execution cannot close an inadequacy finding. `critiquing-aesthetic-adequacy` re-reads experiential intent and visual ambition, compares against references/alternatives, and may reopen aesthetic exploration even when thesis fidelity is excellent.

## V6 Multi-Scale Visual Execution Critique
Start with a **squint test**: reduce detail and ask whether primary/secondary/tertiary hierarchy, large color masses and spatial grouping remain clear. Then use a **grayscale hierarchy** pass to isolate luminance/scale/position from hue. These are diagnostics, not aesthetic laws.

Trace the intended **saliency path** through the first seconds and through task execution. Does the eye land on the primary object/action, then supporting context, or is attention captured by decorative glow, badges, microcharts or a giant title unrelated to the next task?

Inspect rhythm at multiple scales. A **rhythm fracture** can be a one-off gap, but more important are mismatched section cadence, row density, card/pane boundary frequency, typography intervals or motion timing introduced by different component sources.

Audit **material inconsistency**: surfaces that imply different light models, opacity, border logic, radius language or depth semantics without product reason. A visually polished component can still be an integration defect if it belongs to another material world.

Critique typography, color, spacing, surfaces, iconography, imagery, data encoding, motion and responsive composition against their own contracts. Separate local execution defects from thesis adequacy; this critic fixes the former and hands the latter to `critiquing-aesthetic-adequacy`.

### Falsification
Compare rendered evidence at several viewports/themes/content stresses, not the designer's hero screenshot. Temporarily remove decorative layers and check whether hierarchy improves. If the critic's finding cannot name an observable visual relation and a plausible consequence, downgrade it from defect to preference.

### Recovery
Route systemic defects to the owning craft/system skill instead of issuing dozens of pixel tweaks. When visual polish is high but the screen still lacks identity or emotional force, do not keep polishing—escalate to adequacy/basin analysis.

## V7 Render-First Critique
Run visual critique against rendered artifacts, not the design intent document. Build observations from the capture matrix: what wins attention, what becomes visual noise, which surfaces merge unintentionally, whether type resolves as expected, whether the domain signature is actually visible, and whether responsive recomposition changes the thesis. Source code is diagnostic evidence only after the perceptual defect is located.

Separate defects into thesis, composition, craft, implementation drift, and environment/rendering noise. A pixel delta can locate regression but cannot establish aesthetic quality. Conversely, a visually obvious hierarchy failure remains real even if screenshot diff is numerically small. Use task-relevant references as comparative lenses, never as a style-template score.

### Falsification
Ask a critic who has not read the design rationale to identify the page's primary action, subject identity and signature from renders alone. Failure exposes intent that never reached perception.

### Recovery
Change the smallest causal layer, recapture the failed state/viewport, and escalate to re-divergence when local polish cannot repair the thesis.

## V9 Rendered Design-Director Court
For flagship or high-visual-ambition work, perform a **screenshot-based critique loop** as a design director would: render the actual interface, capture the required viewport/state/theme matrix, inspect perception before source code, issue causal findings, repair, re-render, then compare the before/after evidence. A design spec, Figma-like intention, token file, component story or unit test cannot substitute for the final pixels users perceive.

Start every pass by identifying **focal hierarchy**: what the eye sees first, second and third; whether the primary work/object/action owns enough saliency; and whether decoration, cards, badges, chrome or empty hero space steals attention. Then inspect **visual rhythm** across macro and micro scales: variation in dense/quiet regions, section cadence, row frequency, alignment beats, repeated boundaries, type intervals and the distribution of negative space. Uniform spacing can still feel dead; irregular spacing can still feel intentional when its rhythm is coherent.

Judge density as a composition, not a number. Ask where information should breathe, where professional work should become compact, whether every region has the same weight, and whether progressive disclosure creates useful contrast between primary work and secondary controls. Inspect type at rendered size: actual glyph density, x-height, line breaks, line-height, weight contrast, numeral alignment, label compression and optical alignment. “The type scale is valid” is weaker evidence than “the rendered hierarchy reads with the intended authority.”

Run the court at minimum on the critical desktop/wide state and, for responsive products, a real mobile/small state. Mobile is not a compliance screenshot. Ask whether the thesis, focal order, signature, content priority, action reachability and material quality survive recomposition. Inspect overlays, keyboard/safe-area pressure, sticky regions, truncation and accidental horizontal/nested scroll. A desktop masterpiece with a generic stacked mobile fallback is not a flagship result.

Use **A/B** comparison whenever refinement is ambiguous. A/B may compare two candidate renders, before/after repair, or two mechanism variants. Compare one dimension at a time when possible—type, density, border/elevation, spacing, image crop, motion frame—then also judge the whole. Record which variant wins, why, and which strengths of the losing variant must be preserved. If evidence is inconclusive, do not average both into a muddy compromise.

Explicitly inspect for “still feels cheap / AI-generated / template-like” residue and decompose it into observable causes: repeated rounded cards, indiscriminate borders, equal-density sections, stock gradients, weak type personality, excessive pills, icon noise, default browser controls, hard/dirty shadows, arbitrary glass, over-animated microinteractions, fake metrics, or visual effects disconnected from product semantics. These are hypotheses, not universal bans.

The court must not over-polish one hero screenshot while states degrade. Inspect empty, loading, error, selected/focused, overflow/long-content and at least one representative populated state when those materially affect the surface. Preserve accessibility cues and product truth even when they make the composition less pristine.

### V9 Falsification
Give an independent critic only the screenshots, not the design rationale, and ask for the primary task, focal order, perceived quality level, domain cues and likely interaction hierarchy. If the answer differs materially from intent, the render failed. Then run A/B against the proposed repair; if the visual relation cannot be named, the repair is preference rather than evidence.

### V9 Recovery
Route macro composition failures to hierarchy/layout/aesthetic owners, systemic detail failures to token/component/fidelity owners, browser-residue failures to platform/fidelity, and thesis failures back to aesthetic divergence. Repair the smallest causal layer, recapture the same viewport/state, and keep the evidence pair so improvement is inspectable rather than asserted.

## V10 Causal Render-Critique Experiment
`H-RENDER-CRITIQUE-CAUSAL` tests whether a render-first critic changes outcomes beyond producing more critique prose. The target behaviors are **causal specificity** and **repair effectiveness**: a finding should identify a visible relation, connect it to a plausible perceptual/task consequence, change the smallest owning mechanism, and then be re-observed in a named rendered state.

Each benchmarked finding should therefore carry a closed chain:

`render_ref → region/state → observation → causal hypothesis → affected contract → bounded repair → after_render_ref → same-region re-observation → verdict`

Do not allow “improve hierarchy,” “add breathing room,” “make it premium,” or “fix spacing” to count as causal findings unless the critic identifies the competing saliency, grouping, line-wrap, density, material boundary or optical relation that makes the change testable. Preserve a `preserve[]` set so the repair does not win one dimension by erasing useful density, state cues or signature character.

The `critique-spec-only` mutation removes required rendered evidence and permits closure from source/design intent. The `render-critique` ablation removes this court. On matched critique tasks, full NUI should improve `critique-causal-specificity` and the blinded before/after judgment of targeted **repair effectiveness**. It should not merely issue more findings: false positives, redundant repairs and hard-constraint regressions are negative evidence.

### V10 evidence independence
The generator's rationale is not a judge input. Where runtime permits, the critic should receive the rendered artifact, task/accepted contracts and state identifiers without the generator's self-evaluation. A later diagnosis may inspect source code to locate the implementation cause, but source interpretation cannot replace the initial perceptual observation. If generator and critic share the same model/context lineage, record the correlation; do not call it independent merely because two prompts were used.

### V10 falsification and recovery
Attribution fails when spec-only critique catches the same hidden rendered defects and produces equivalent verified repair effects, or when full NUI's proposed changes fail to improve the dimension they claim to repair. A full condition that improves visual calm by hiding error/status truth is a hard regression, not a visual win. If no effect appears, inspect capture coverage, critic blindness, task defect salience and whether the owning fix was actually implemented before adding more critique vocabulary.

A screenshot can prove what was rendered at a moment; it cannot by itself prove usability or NUI efficacy. Cross-model/holdout efficacy language remains blocked until the V10 empirical claim court has matching evidence.
