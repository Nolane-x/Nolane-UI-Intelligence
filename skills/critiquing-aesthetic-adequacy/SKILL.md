---
name: critiquing-aesthetic-adequacy
description: Use when working after a direction is rendered to judge whether the selected thesis itself is strong enough for the original experiential intent, not merely whether implementation faithfully followed it.
---

# Critiquing Aesthetic Adequacy

## Parent Contract
**Required parent:** `critiquing-visual-design`.

This child strengthens the parent and may not waive parent obligations.

## Decision Boundary
Own thesis adequacy. The existing visual critic still owns thesis execution quality. Adequacy may reopen aesthetic exploration even when execution is coherent.

## Product Truth
Contract fidelity can be a trap: a dark, restrained, technical, dense direction can be implemented perfectly and still fail ‘extremely beautiful, awe-inspiring, monumental’. The critic must compare against original intent, not only against the contract produced by the generator.

## Decision Model
Re-read experiential intent and visual ambition without assuming the chosen thesis is correct. Assess aesthetic fit, emotional force, memorability, material richness, visual refinement, signature strength, perceptual harmony, role identity fit, and subject specificity as an evidence vector rather than one beauty score. Compare the candidate with the reference frontier and at least one materially different alternative. Record critic lineage; if generator and critic share model/context, mark correlation rather than calling it epistemically independent. A FAIL has authority to reopen exploration.

## Evidence
Return findings tied to original intent phrases, reference/alternative comparisons, correlation_class, and decision `ADEQUATE | INADEQUATE | UNKNOWN`. INADEQUATE routes to basin escape.

## Output Contract: `aesthetic-adequacy-findings`
Return the canonical `aesthetic-adequacy-findings` artifact with explicit status, evidence references, unresolved unknowns, and downstream routes. Missing material evidence must remain UNKNOWN/BLOCKED rather than being inferred from confidence.

## Failure Traps
‘Thesis fidelity good’ treated as success; judging only polish defects; scalar beauty score; same-context self-critique labeled independent; refusing to reopen because code is already implemented; comparing only to a mediocre internal baseline.

## V6 Thesis Adequacy Court
Judge **thesis adequacy**, not simply polish. First restate the selected visual thesis in observable terms and trace it to experiential intent, role identity, product truth and reference mechanisms. Then separate “the thesis was executed well” from “the thesis was worth executing.”

Use a **blind comparison** whenever feasible: hide treatment names, implementation effort and source prestige. Compare the candidate with internal baseline, materially different alternative, and relevant references on intent fit, emotional force, memorability, subject specificity, material richness, visual refinement, signature strength, usability and accessibility constraints.

Compute a qualitative **reference-frontier delta**: where does the candidate clearly surpass, match or trail accepted reference mechanisms? Do not average dimensions into one universal beauty number; preserve tradeoffs and disqualifying weaknesses.

Trace the **intent-to-render gap** for each major affective invariant. A beautiful screen can be inadequate if it expresses the wrong identity. A calm, precise interface can still fail a request for awe and magnitude. A dramatic interface can fail if the task requires sustained analytical focus.

Watch the **execution-success trap**: teams become attached to a coherent direction because implementation quality is high. High sunk cost cannot convert a weak thesis into an adequate one.

### Falsification
Ask whether a different thesis with comparable execution plausibly serves the preserved intent better. If the answer is yes and the current thesis lacks evidence advantage, adequacy is unresolved. Remove signature/media layers; if the thesis remains indistinguishable from category defaults, distinctiveness claims are falsified.

### Recovery
Return `INADEQUATE` or `RE_DIVERGE` when the thesis itself is weak; do not issue a list of local polish tweaks. Recovery identifies which invariant/reference delta caused failure and which design degrees of freedom must reopen.

## V7 Concrete Adequacy Test
Adequacy now asks whether the chosen direction is not only coherent but **concretely competitive with the problem's real authority and reference frontier**. Compare the render to local experiential intent and to task-relevant evidence: platform craft when platform-native, institutional workflow clarity when service/enterprise, domain-native specificity, visual ambition, and the implementation quality possible from current specialist ecosystems.

Do not reward complexity. A quiet public-service form can be more adequate than a cinematic composition if the task demands trust, comprehension and assisted use. An exceptional creative workspace can be inadequate if it retreats to generic cards despite perfect semantics. Use the concrete design packet to check whether high-leverage decisions survived implementation and rendered-perception evidence to check whether they are visible.

### Falsification
Swap in a well-tested domain pattern or stronger subject-native signature. If the current direction has no defensible advantage on task fit, clarity or experiential intent, adequacy is false.

### Recovery
Return `RE_DIVERGE`, reopen only the weak authority/signature/composition dimension, and generate a direction with a materially different causal thesis.
