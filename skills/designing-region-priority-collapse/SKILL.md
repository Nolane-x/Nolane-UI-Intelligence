---
name: designing-region-priority-collapse
description: Use when limited space forces interface regions to compress, summarize, defer, relocate, or disappear and task priority must govern what is sacrificed before mere visual convenience.
---

# Designing Region-Priority Collapse

## Scarcity Decision
When every region cannot retain its full presentation, the UI needs an explicit priority order. This skill owns which information and controls remain primary, which may compress, which can move behind disclosure, and which may disappear because their task value is genuinely lower in the constrained state.

## Parent Contract
**Required parent:** `adapting-responsive-layouts`.

The parent owns overall adaptation. This specialist governs semantic sacrifice under space pressure, not mere geometric reflow.

## Priority Model
Classify regions by task criticality, time sensitivity, reversibility, frequency, decision dependency, and recovery cost if hidden. Define transformations such as `full -> compact`, `full -> summary`, `inline -> deferred panel`, or `visible -> omitted` with explicit retained meaning. Do not infer priority from current visual size; a small warning can outrank a large illustration.

If hiding a region removes information required to interpret another region, the dependency raises its effective priority. Likewise, a low-frequency emergency action may still be non-collapsible because consequence dominates frequency.

## Invariants
Critical task inputs and irreversible-action context remain available. Deferred content has a discoverable path. Summaries preserve decision-relevant truth and signal when detail exists. Collapse order is stable enough that small width changes do not make unrelated regions jump unpredictably.

## Evidence
Evidence includes task maps, constrained-width walkthroughs, priority rationale, dependency graphs, and comparisons of full versus collapsed states. Test errors, warnings, permissions, and non-happy states because these often change priority relative to a polished default screen.

## Failure Modes
Failure includes hiding validation context while keeping decorative media, moving primary actions into generic overflow, summaries that omit exception states, layouts that preserve equal visual weight for unequal tasks, and “mobile simplification” that removes necessary decision evidence.

## Falsification
Falsification asks users or task simulations to complete high-priority flows using only the constrained state, injects warnings/errors, and removes each deferred region to determine whether a decision becomes under-informed. If a collapsed state makes a critical task impossible or misleading, priority ordering is disproved.

## Recovery
Recovery restores the missing high-priority region, compresses lower-priority content instead, or redesigns the task so dependencies are explicit. Do not simply add scrolling if the problem is competing simultaneous decision context.

## Output and Handoff
Output: `region-priority-collapse-contract` with region ranks, dependency adjustments, allowed transformations, discoverability requirements, and falsification cases. Handoff pure visual ordering without sacrifice to responsive region reordering.

## Sibling Boundary and delete-the-skill
Reordering preserves all regions while changing position; priority collapse decides what can lose fidelity or immediate presence. The delete-the-skill test passes because no sibling owns that semantic sacrifice hierarchy.