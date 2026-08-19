---
name: designing-field-validation-and-error-recovery
description: Use when a form needs precise validation timing, actionable error presentation, and recovery behavior that preserves user work instead of merely rejecting invalid input.
---

# Designing Field Validation and Error Recovery

## Parent Contract
**Required parent:** `designing-forms`.

This faculty owns the boundary between user-entered data, validation evidence, and a recoverable path back to a valid state. It does not define the business rule itself; it decides when that rule is evaluated, where its failure is explained, how focus and summaries expose it, and what happens to the user’s already-entered work.

## Decision Model
Classify every validation rule by when reliable evidence exists. Syntax and local constraints can often be checked after meaningful input or on blur. Cross-field rules require the related values. Server-authoritative facts such as uniqueness, eligibility, inventory, or account state cannot truthfully be certified by client validation alone. Avoid the common failure of showing red errors while the user is still forming a value that is not yet judgeable.

Choose an error location based on repair locality. A field-specific error belongs beside the field and must be programmatically associated with it. A submission failure spanning multiple fields needs a summary that links back to repair targets. A global service failure must not masquerade as “invalid field.” Preserve the submitted values unless safety requires otherwise.

Error copy should identify the violated condition and the next corrective action without exposing implementation internals. “Invalid input” is rarely sufficient. If formatting can be normalized safely, distinguish normalization from rejection; do not silently alter semantically meaningful values.

## Failure Topology
- Validation fires per keystroke and punishes incomplete-but-normal intermediate states.
- Client validation promises acceptance that the server later rejects without explaining the new evidence.
- Submission scrolls to an error but focus remains elsewhere, leaving keyboard and screen-reader users disoriented.
- A server outage is rendered as a field mistake, prompting pointless edits.
- Correcting one field clears unrelated errors or destroys entered data.
- Error color is the only signal and disappears after focus moves.

## Falsification and Recovery
Falsify the design with empty submit, partially typed values, multiple simultaneous errors, async validation racing with edits, server disagreement, localization expansion, screen reader navigation, keyboard-only repair, and a failed resubmission. The design fails if users cannot answer: what is wrong, where is it, why is it wrong, and what must change without re-entering valid data.

Recover by separating local, cross-field, server-authoritative, and system failures; delaying judgment until evidence exists; binding messages to repair targets; preserving values; and making post-submit focus/order deterministic.

## Output Contract
Return `field-validation-recovery-contract` containing rule classes, validation timing, message placement, accessibility bindings, error-summary behavior, async race policy, focus/scroll recovery, value-preservation rules, server-disagreement behavior, and falsification cases.