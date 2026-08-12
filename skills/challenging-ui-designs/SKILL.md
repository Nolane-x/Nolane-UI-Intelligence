---
name: challenging-ui-designs
description: Use when a material UI design or rendered implementation needs independent adversarial review before completion, especially after the generating agent is satisfied with it.
---

# Challenging UI Designs

## Overview
This skill creates the adversarial court. Its purpose is not to make the design different; it is to discover reasons the current design should not ship.

## Parent Contract
**Required parent:** `nolane-ui`.

Consume the contract, task profile, obligations, current design/render, and available evidence. The critic role is logically independent from the role that generated the artifact.

## Critic contract
A critic has `may_modify: false`. It produces findings only. Repair is a separate action followed by fresh verification. This separation prevents the reviewer from quietly changing the artifact until its own criticism disappears.

## Select attack lenses
Use the router's `verification_lenses`; add a lens if the artifact reveals a new material risk.

Core lenses:
- **Product/UX:** task friction, dead ends, ambiguous actions, trust, recovery, interruption, progressive disclosure.
- **Information architecture:** grouping, labels, hierarchy, discoverability, wayfinding, comparison.
- **Interaction:** affordance, keyboard/touch, focus, state feedback, async transitions, destructive behavior.
- **Visual:** hierarchy, composition, typography, color, density, rhythm, cohesion, intentionality, brand/subject specificity.
- **Design system:** token drift, inconsistent semantics, variant explosion, one-off styling, misleading reuse.
- **Accessibility:** semantic name/role/state, focus, contrast/reflow, motion, target size, reading order, non-color cues.
- **Responsive:** priority preservation, content growth, overflow, touch ergonomics, transformed navigation, dense data behavior.
- **Platform fit:** violations of platform conventions that create user cost.
- **Fidelity:** target-vs-render drift on authoritative axes.
- **Anti-slop:** generic choices with no product/brand function, repetitive framing, decorative information, unsupported visual tropes.

## Finding standard
Every finding must contain `finding_id`, `domain`, `severity`, `evidence`, `violated_constraint`, `user_impact`, `falsifier`, `recommended_repair`, and `status`.

If you cannot point to evidence or a violated contract/standard/explicit design principle, phrase the observation as a hypothesis and leave it open; do not inflate taste into fact.

## Severity
- `critical`: can cause severe exclusion, destructive action, loss of trust/data, or core task impossibility.
- `major`: materially blocks or degrades a primary task, accessibility path, responsive target, or accepted fidelity.
- `moderate`: repeated friction or meaningful craft/system inconsistency.
- `minor`: localized polish issue with low task impact.
- `observation`: non-blocking hypothesis or opportunity.

## Adversarial moves
1. **Remove the decoration:** does information structure remain understandable? If not, decoration was masking IA weakness.
2. **Stress content:** long labels, empty data, extreme values, localization expansion, validation errors.
3. **Change modality:** mouse → keyboard → touch; check whether affordance/state survives.
4. **Change viewport:** preserve priority rather than merely compressing pixels.
5. **Change user:** novice/expert, low vision, reduced motion, screen reader, high operational pressure when relevant.
6. **Invert the design claim:** if the design says “clear hierarchy,” identify where two elements compete for the same priority.
7. **Compare sibling semantics:** same meaning should not acquire unrelated visual/interaction rules without reason.
8. **Counterfactual pattern:** if the fashionable pattern were removed, would the user lose information or capability? If not, challenge its cost.

## Anti-praise rule
Do not open with compliments. Findings can include strengths only when they explain why another part is inconsistent or must be preserved during repair.

## Output: `critic-session`
Return selected lenses, findings, untested hypotheses, evidence gaps, and a release recommendation of `BLOCK`, `REPAIR_AND_RETEST`, or `NO_BLOCKER_FOUND`. `NO_BLOCKER_FOUND` is not equivalent to overall release PASS; the completion gate still decides.

## Rationalizations to reject
- “It feels polished.” Feelings do not close obligations.
- “Users will figure it out.” State the discoverability evidence or leave the claim unknown.
- “This is standard SaaS UI.” Familiarity is not a justification for irrelevant structure.
- “The design system does it.” A system rule that harms this task is still a finding against the project contract.
