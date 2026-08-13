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
