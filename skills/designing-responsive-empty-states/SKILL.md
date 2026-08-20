---
name: designing-responsive-empty-states
description: Adapt empty-state guidance and calls to action across constrained layouts without losing explanation, recovery paths, or the hierarchy of next steps.
---

# Designing responsive empty states

Empty states often include illustration, explanation, primary action, secondary help, and contextual examples. On narrow surfaces, decorative content can crowd out the actual recovery path. Use this skill to preserve purpose while recomposing.

## Decision ownership

Own responsive prioritization of empty-state elements, illustration treatment, text measure, action stacking, and placement relative to surrounding controls. Decide what may be reduced or removed and what remains essential to explain why the state exists.

## Inputs and evidence

Collect empty-state causes, user knowledge, action availability, illustration dimensions, localized copy, permission variants, narrow-height constraints, and surrounding shell controls. Distinguish first-use emptiness from filtered-no-results or permission-blocked states; they need different content priorities.

## Procedure

Keep cause and next step prominent before decoration. Define how actions stack and whether secondary links move below explanatory text. Scale or remove nonessential illustration when it competes with actionable content, but preserve visuals that teach structure or convey important domain information.

Constrain text measure even on wide screens and ensure narrow layouts do not create excessive vertical separation between explanation and action. Preserve contextual filters or reset controls when emptiness results from user-selected criteria.

## Failure topology

A large hero illustration can push the only action below the fold. Mobile simplification can remove the explanation users need to understand why data is absent. Another failure is treating all empty states as the same responsive component even when the recovery control belongs elsewhere in the shell.

## Falsification

Test short and long localized copy, very short viewport height, zoom, filtered states, permission states, and first-use states. Ensure the primary recovery path remains visible or easily reachable. Remove images and verify semantic completeness; if meaning disappears, the image is informational and needs alternate treatment.

## Output contract

Produce a `responsive-empty-states-contract` defining per-state content priority, illustration behavior, text measure, action layout, shell relationships, vertical constraints, and representative responsive examples.

## Handoffs

Use `designing-empty-states` for base content strategy, `designing-responsive-error-recovery` for failure states, `designing-responsive-media-crops` for informational imagery, and `verifying-responsive-state-parity` for recovery-path completeness.