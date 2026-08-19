---
name: designing-multi-step-forms
description: Use when data capture must be split across stages and the product needs explicit progress, checkpoint, backtracking, validation, and abandonment semantics.
---

# Designing Multi-Step Forms

## Parent Contract
**Required parent:** `designing-forms`.

This faculty owns staged form progression. It decides where a long data-capture task is partitioned, what a completed step means, which information is committed versus provisional, and how users move backward or resume. It does not turn every long form into a wizard; segmentation must reduce cognitive or operational risk rather than merely create more screens.

## Decision Architecture
Partition by user task, evidence dependency, or commitment boundary. A step should form a coherent question set whose completion has meaning. Do not split fields solely to produce a fashionable progress bar. If later questions depend heavily on earlier answers, the sequence may be justified; if users need to compare values across sections, a single structured page may be better.

Define three states separately: locally complete, validated enough to advance, and durably saved. A checkmark in a stepper must not imply server persistence unless that is true. Back navigation should preserve valid work and expose when an upstream edit invalidates downstream answers. If downstream invalidation is material, show the affected stages before users commit the change.

Progress indicators must match the real structure. “Step 2 of 4” is misleading if conditional answers can add six hidden steps. Prefer named stages or bounded progress when the path branches. Users need a visible route to save/exit when the task is interruptible.

## Failure Topology
- Next is enabled because required fields are hidden in a later collapsed section.
- Back navigation reinitializes a stage and discards entered work.
- An early edit changes eligibility but stale later answers remain marked complete.
- The progress bar jumps backward or changes denominator without explanation.
- Final submit reveals errors from distant prior steps without a repair route.
- Closing the flow gives no clue whether anything was saved.

## Falsification and Recovery
Falsify with conditional branches, browser refresh, expired sessions, resume on another device, changing a first-step answer after completing all later steps, final server rejection, and keyboard/screen-reader navigation through the step indicator. The flow fails if stage status cannot be reconciled with actual saved/valid state or if a user cannot safely abandon and resume according to the product promise.

Recover by separating progression from persistence, recording dependency invalidation between steps, using truthful stage labels, preserving state on backtracking, routing final errors to exact stages, and making save/exit consequences explicit.

## Output Contract
Return `multi-step-form-contract` with stage boundaries, progression rules, branching model, completion semantics, persistence checkpoints, backtracking policy, cross-step invalidation, progress representation, abandonment/resume behavior, final-submit repair routing, and falsification cases.