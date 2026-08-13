---
name: iterating-rendered-visual-design
description: Use when visual quality matters enough that a single generated mockup is insufficient and the agent must compare rendered evidence, isolate changes, critique outcomes, and converge deliberately.
---

# Iterating Rendered Visual Design

## Parent Contract
**Required parent:** `critiquing-visual-design`.

Receive accepted product/interaction constraints, candidate visual directions, visual reference mechanisms, current design-system rules, and an inspectable render capability. The visual critic owns findings; this faculty owns the controlled iteration process that responds to them.

## Decision Boundary
This skill owns **visual experimentation as evidence**, not subjective self-congratulation. It transforms aesthetic hypotheses into rendered candidates, compares them under controlled conditions, records what changed, and updates the selected direction based on evidence. It does not waive functional completeness: the product can be visually excellent and still blocked elsewhere.

Iteration is not “make it nicer” repeated until token budget runs out. Each round has a hypothesis and a bounded variable set. The agent must know why it changed hierarchy, typography, composition, color, surface treatment, density, iconography, imagery, or motion and what evidence would count as improvement.

## Product Truth
LLMs are prone to local edits that accumulate incoherently. Increase the title, then add cards to organize content, then add glow for emphasis, then add badges to explain cards, then reduce clutter with more whitespace—each step sounds reasonable, while the overall UI becomes generic or internally inconsistent.

Rendered iteration needs a memory of cause and effect. It also needs comparison against the product’s actual content, not empty demo text. A direction that looks elegant with four sample rows may collapse with long names, localization, errors, dense metadata, or realistic images.

## Decision Model
1. **Freeze non-visual truth.** Before comparison, hold product actions, required content, semantic hierarchy, and scenario state constant unless the iteration explicitly tests a structural alternative already authorized.
2. **State the hypothesis.** Example: “Replacing nested cards with border-and-spacing groups will improve scan hierarchy and reduce visual noise while preserving density.” Define expected observable improvement.
3. **Choose a bounded variable set.** Change one coherent cluster per experiment: typography scale/rhythm, surface hierarchy, color emphasis, density model, imagery treatment, or motion continuity. Avoid changing every axis simultaneously unless comparing fully distinct art directions.
4. **Render realistic states.** Include representative populated data plus applicable empty/loading/error/selected/disabled/focus states and critical viewport sizes. A hero-only beauty pass does not prove product UI quality.
5. **Capture evidence consistently.** Same viewport, content fixture, theme, zoom, and state for comparisons. Store render IDs and artifact revision.
6. **Run independent critique.** Evaluate hierarchy, composition, typography, color semantics, rhythm, information density, distinctiveness, platform fit, accessibility implications, motion restraint, and anti-generic risks. Separate severe functional issues from visual preference.
7. **Compare candidates, not memories.** Side-by-side or structured evidence reduces recency bias. Record both wins and regressions.
8. **Decide keep/revert/refine.** A change can improve one axis and harm another. Preserve the trade-off and rationale rather than declaring every new render better.
9. **Stress test the winner.** Long text, localization, extreme content, narrow/wide viewport, reduced motion, dark/light themes if supported, and critical interaction states can falsify a visually promising direction.
10. **Update project design memory.** Store accepted mechanisms and rejected experiments with scope, evidence, confidence, and expiry. The next task can start informed without treating preference as universal law.

## Evidence
Primary evidence is rendered output. Code diffs can explain what changed but not prove perceived hierarchy. Reference sets justify hypotheses but do not prove fit. Human preference can be evidence when the target audience/authority is clear; otherwise label it as taste rather than objective quality.

Use quantitative measures only where meaningful: contrast, text size, layout overflow, frame performance, animation duration, density counts, or token consistency. Do not manufacture a single “beauty score” that hides trade-offs. Comparative critique should stay multi-dimensional.

## Output Contract
Return `visual-iteration-evidence` with:
- `baseline_render_refs[]`
- `iterations[] {id, hypothesis, variables_changed, render_refs, critic_findings, improvements, regressions, decision: keep|revert|refine}`
- `comparison_context {content_fixture, viewports, states, theme, platform}`
- `stress_tests[] {condition, render_ref, result, finding_refs}`
- `selected_iteration`
- `rejected_mechanisms[]`
- `memory_updates[]`
- `unresolved_visual_risks[]`
- `status: PASS|FAIL|UNKNOWN`

`PASS` requires at least one inspectable rendered comparison for material aesthetic iteration. Pure prose cannot close this artifact.

## Failure Traps
- Calling the latest version “better” without preserving a baseline.
- Changing typography, layout, color, components, and motion at once, making causality unknowable.
- Rendering only ideal content.
- Using a numeric beauty score as a substitute for multi-axis critique.
- Following references so closely that product identity becomes derivative.
- Repeating a previously rejected mechanism because project memory was not consulted.
- Optimizing desktop screenshots while mobile, focus, error, or reduced-motion states regress.
- Letting visual iteration rewrite product actions to simplify the composition.
- Treating code compilation as evidence of visual improvement.

**Hard gate:** a material claim that iterative visual design improved the interface requires rendered before/after evidence and an explicit keep/revert/refine decision tied to findings.

## V5 Basin-Escape Trigger
Before another local refinement, ask whether the current aesthetic **basin** is viable. Compare affective fit, distinctiveness, signature depth and current candidate against the **reference frontier** and a materially different alternative. If fit remains below target, repeated comparisons lose, signature depth fails, or adequacy critic rejects the thesis, emit `RE_DIVERGE`; do not continue local hill-climbing. Preserve strengths and reopen only the axes implicated by the failure.
