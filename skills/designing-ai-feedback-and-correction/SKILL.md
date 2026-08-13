---
name: designing-ai-feedback-and-correction
description: Use when users need to refine, reject, edit, compare, regenerate, revert, report, rate, or otherwise correct AI output and the feedback path affects future output or product behavior.
---

# Designing AI Feedback and Correction

## Overview
AI errors are expected system states. Make correction fast, local, reversible, and understandable; do not trap users in repeated regeneration when a precise edit or rollback would solve the problem.

## Parent Contract
**Required parent:** `routing-ui-work`.

Require output mutability, original user content, model context, whether feedback trains/personalizes anything, privacy policy, and what corrections can be applied locally versus requiring regeneration.

## Decision Model
Match correction control to error granularity. Wrong word or field: direct edit. Wrong section: targeted regenerate/replace. Wrong direction: alternative instruction or compare variants. Harmful/incorrect content: report plus preserve user work. Entire failed attempt: retry/regenerate. Always preserve the user-owned baseline or a version history when AI can overwrite material work.

Separate **product feedback** from **content correction**. Thumbs up/down may inform product quality but should not be the only way to fix the current output. If a feedback signal changes future personalization, explain the effect and offer review/reset where material.

Comparison needs stable context. Show what changed, not two giant nearly identical blocks. For generated code/design, diff structural changes and maintain a route to the previous functioning state. For autonomous agents, correction may include changing standing delegation, not merely editing text.

Avoid feedback coercion. Do not require a rating to continue, and do not imply that reporting a model error will automatically correct external consequences. Sensitive prompts/output attached to feedback require clear data handling.

## Evidence
Test common model errors, user edits followed by regeneration, partial selection rewrite, revert after several iterations, feedback privacy, personalization reset, and whether corrections survive navigation/reload. Measure time to recover from a bad result, not only satisfaction with good results.

## Output Contract
Return a `correction-contract` with `error_granularity_map`, `direct_edit_rules`, `targeted_regeneration`, `variant_comparison`, `version_and_revert`, `reporting_flow`, `product_feedback_semantics`, `personalization_effects`, `privacy_handling`, and `correction_tests[]`.

## Failure Traps
- “Regenerate” as the only correction tool.
- AI rewrite permanently replacing human original.
- Thumbs-down button with unknown effect.
- Regeneration silently discarding user edits.
- Diff view that highlights formatting noise instead of semantic change.
- Feedback submission leaking sensitive content unexpectedly.
- “Undo” that cannot restore tool actions or external changes.

AI quality includes the cost of recovering when the model is wrong.

## V6 AI Correction Protocol
Create a **correction affordance loop** from noticing error → selecting target → expressing correction → seeing changed model/output state → verifying repair. Require **feedback target specificity** so users can correct the exact claim, field, generated UI element, tool action, preference, or policy—not merely thumbs-up/down.

Distinguish local output editing from **model-state repair**: does the correction change only this artifact, the current conversation, a saved preference, a workflow rule, or future model behavior? Set a **learning-consent boundary** before persistent use of feedback. Preserve **correction persistence** only at the scope users were told and make it inspectable/resettable.

### Falsification
Correct one local error, start a new task/session, and inspect whether behavior changes at the claimed scope. Hidden persistence or no effective repair falsifies feedback semantics.

### Recovery
Clarify scope, revert unintended memory/learning, re-run affected actions, and expose a deterministic way to edit/override the current result.
