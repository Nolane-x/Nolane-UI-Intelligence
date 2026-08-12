---
name: critiquing-cognitive-load
description: Use when a UI is dense, multi-step, realtime, interruption-heavy, expert, cognitive-accessibility-sensitive, monitoring-oriented, or likely to burden memory, attention, mode awareness, comprehension, or resumption.
---

# Critiquing Cognitive Load

## Overview
Independently test whether the interface makes users hold avoidable context in memory, divide attention among equivalent signals, infer hidden modes, or repeatedly reconstruct where they were.

## Parent Contract
**Required parent:** `challenging-ui-designs`.

**May modify:** false. Consume task analysis, attention budget, cognitive-accessibility obligations, realtime/notification contracts, and actual task behavior. Do not judge cognitive load by visual minimalism alone.

## Decision Model
Review each critical or frequent task for **recall**, **competition**, **decision complexity**, **mode state**, and **resumption**. Recall finding: information needed now existed earlier but is no longer visible or retrievable nearby. Competition finding: multiple elements demand simultaneous attention with no consequence-based priority. Decision complexity finding: choices are difficult because labels/relationships are unclear rather than inherently numerous. Mode finding: the same input has different effects but current mode is weakly signaled. Resumption finding: after interruption users cannot tell what was completed, pending, selected, or next.

Look for false simplification. A “clean” wizard can increase cognitive load if comparison requires navigating back and remembering previous values. Hidden controls can reduce clutter while increasing discovery and recall. Expert dashboards can legitimately be dense when spatial stability and simultaneous comparison reduce switching.

Evaluate dynamic behavior: live sorting, notifications, animated changes, background AI output, and disappearing status can hijack attention. Check whether transient toasts carry information needed later. Error flows should preserve correct input and context rather than forcing reconstruction.

## Evidence
Use realistic task walkthroughs, interruption/resume tests, representative user research, time-to-resume, error patterns, comprehension evidence, and observed attention competition. Eye tracking is optional evidence, not a required proxy. Internal preference for “clean UI” is not cognitive evidence.

## Output Contract
Return a `finding-set` with `may_modify:false`, `artifact_revision`, `findings[] {finding_id, severity, load_type, evidence, task_effect, user_impact, falsifier, recommended_repair, required_reverification}`, `memory_dependencies[]`, `attention_conflicts[]`, `mode_risks[]`, `resumption_gaps[]`, and `release_recommendation`.

## Failure Traps
- Counting elements to estimate cognitive load.
- Assuming fewer screens means easier task.
- Penalizing dense expert UI merely for density.
- Ignoring cognitive cost of navigation and hidden context.
- Treating user preference as task-performance evidence.
- Suggesting “simplify” without naming what load is extraneous.
- Visual critic’s praise reducing severity of a memory or mode defect.

A cognitive finding must identify what the user is forced to think about that the interface could safely carry for them.