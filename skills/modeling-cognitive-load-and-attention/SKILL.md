---
name: modeling-cognitive-load-and-attention
description: Use when a UI is dense, interruption-prone, multi-step, time-sensitive, memory-heavy, modeful, notification-heavy, or requires people to compare, monitor, resume, or decide among competing signals.
---

# Modeling Cognitive Load and Attention

## Overview
Attention is a scarce routing resource and working memory is not storage. This skill allocates what the interface asks a person to notice, retain, compare, switch between, and recover after interruption.

## Parent Contract
**Required parent:** `routing-ui-work`.

Consume task structure and user/task pressure. Do not infer cognitive difficulty solely from element count; complexity depends on dependency, novelty, switching, consequence, and what information must remain mentally active.

## Decision Model
Trace each task through four budgets. **Perceptual competition:** how many signals compete at the same moment and which must win. **Working-memory burden:** what facts, codes, selections, or intermediate states must be remembered because the UI fails to keep them visible. **Decision burden:** number and similarity of alternatives, uncertainty, consequence, and frequency. **Switching/resumption cost:** what context disappears when a user is interrupted, navigates away, changes mode, or handles a second case.

Reduce intrinsic load only where the task permits; do not hide necessary complexity behind ambiguous automation. Reduce extraneous load aggressively: repeated re-reading, decorative data, unstable placement, unexplained modes, redundant choices, and simultaneous animations. Externalize memory with persistent context, summaries, comparison tables, breadcrumbs, recent history, draft state, and resume markers. Group by decision relationship rather than visual symmetry.

For monitoring interfaces, use change detection deliberately. Distinguish current state, new state, acknowledged state, and resolved state. Avoid animation that competes continuously for attention. For expert work, progressive disclosure must not force experienced users through beginner sequencing when a dense stable overview is more efficient.

## Evidence
Evidence includes task analysis, completion/error patterns, interruption tests, time-to-resume, eye/attention observations when available, cognitive-accessibility testing, and expert-user workflows. Treat self-reported “cleanliness” as weak evidence for cognitive efficiency.

## Output Contract
Return an `attention-budget` with `critical_attention_targets[]`, `working_memory_dependencies[]`, `decision_points[]`, `interruptions[]`, `resume_requirements[]`, `mode_boundaries[]`, `load_reduction_moves[]`, `expert_shortcuts[]`, and `unresolved_cognitive_risks[]`.

## Failure Traps
- “Minimal UI” that hides context and increases memory load.
- Infinite badges, color, motion, and alerts all claiming urgency.
- Requiring recall when recognition or persistent context is possible.
- Treating every user as a novice and removing expert overview/shortcuts.
- Counting clicks as a proxy for cognitive effort.
- Moving content during live updates without preserving the user’s locus of attention.
- Using one giant wizard to avoid thinking about task relationships.

The interface should carry context for the person; the person should not be forced to carry the interface in working memory.