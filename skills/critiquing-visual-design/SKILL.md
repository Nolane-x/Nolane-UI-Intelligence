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
