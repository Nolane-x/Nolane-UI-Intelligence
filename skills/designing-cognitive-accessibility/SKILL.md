---
name: designing-cognitive-accessibility
description: Use when a UI may create barriers through memory demands, complex language, inconsistent behavior, distraction, time pressure, unfamiliar symbols, error recovery, multi-step tasks, or cognitive and learning differences.
---

# Designing Cognitive Accessibility

## Overview
Cognitive accessibility reduces unnecessary demands on memory, comprehension, attention, language processing, planning, and recovery. It is not equivalent to “make it simpler”; expert or inherently complex work may remain rich while the interface externalizes context and behaves consistently.

## Parent Contract
**Required parent:** `designing-accessible-interfaces`.

Consume user/task model, cognitive-load analysis when applicable, content rules, and task flows. If the target population includes known cognitive or learning disabilities, user research with relevant participants is evidence, not an optional polish step.

## Decision Model
Inspect the task for **memory**, **language**, **attention**, **planning**, **consistency**, and **recovery** barriers. Memory barriers include codes, rules, selections, or prior-step values that disappear. Externalize them through persistent summaries, visible requirements, examples, history, and recognition-based choices. Language barriers include jargon, figurative wording, unexplained abbreviations, dense instructions, and labels that change names through a flow. Use concrete familiar terms and stable action vocabulary.

Attention barriers arise from competing motion, alerts, dense unrelated content, timeout pressure, and interruption without resume cues. Reduce extraneous competition and provide a clear current goal. Planning barriers occur when users must infer hidden sequences or prerequisites; expose progress and next actions without turning every task into a rigid wizard. Consistency means equivalent controls behave and appear predictably across contexts, especially authentication, forms, navigation, and error recovery.

Errors should preserve input, identify the specific problem, show how to correct it, and avoid blame. For consequential actions, support review and recovery without requiring users to remember hidden prior state. Authentication must not depend on cognitive function tests where applicable accessibility requirements disallow it unless an allowed alternative or exception applies.

## Evidence
Use representative usability research, comprehension tests, interruption/resume scenarios, plain-language review, error-recovery observation, accessibility specialists, and W3C cognitive guidance. Automated linting can identify some labels or structure but cannot prove comprehension or memory accessibility.

## Output Contract
Return `cognitive-accessibility-obligations` with `memory_dependencies[]`, `language_barriers[]`, `attention_competition[]`, `planning_support[]`, `consistency_invariants[]`, `error_recovery_rules[]`, `authentication_constraints[]`, `user_research_needs[]`, and `verification_scenarios[]`.

## Failure Traps
- “Minimal” screen that hides information users need to remember.
- Long instructions shown once and removed before the task.
- Clever synonyms causing the same action to change names.
- Auto-advancing or timing out before slower comprehension is possible.
- Error that clears all correct fields.
- Icon-only actions based on unfamiliar metaphor.
- Automated accessibility pass treated as proof of cognitive accessibility.

A cognitively accessible interface carries context, explains consequences, and makes recovery possible without demanding perfect memory or concentration.