---
name: researching-ui-frontiers
description: Use when UI guidance may be stale, a task reaches an unfamiliar interaction surface, or a design decision depends on current standards, platform behavior, AI patterns, safety guidance, or emerging interface technology.
---

# Researching UI Frontiers

## Overview
Treat UI knowledge as a changing evidence base, not a frozen prompt library. This skill owns discovery of genuinely new decision mechanisms and uncovered domain classes; it does not collect links for volume or restate sources the system already understands.

## Parent Contract
**Required parent:** `routing-ui-work`.

The router must identify a freshness need, authority gap, unknown domain, contradictory guidance, or high-drift topic. If the task can be answered from current authoritative knowledge without material freshness risk, do not research merely to look thorough.

## Decision Model
Start with a precise uncertainty statement: what UI decision could change if newer evidence exists? Search outward in authority order: normative/regulatory sources, platform owners, government or standards research, mature design systems, then high-quality empirical/community work. Separate a *new source* from a *new mechanism*. A source is worth absorbing only when it adds a rule, boundary condition, failure mode, measurement method, platform delta, or evidence relationship not already represented.

Classify each finding by scope. A car-driver distraction rule is not a general mobile heuristic. A current visual language such as Liquid Glass or Material 3 Expressive is platform context, not universal taste. A Working Draft is not a Recommendation. When two sources disagree, preserve the disagreement until `calibrating-ui-authority` resolves it; never average incompatible rules.

Search in waves. After each wave, update uncovered atlas cells and the mechanism ledger. A final wave is specifically adversarial: search adjacent terminology and competing platforms to try to falsify the belief that coverage is saturated.

## Evidence
Evidence must include source identity, publisher, date/status when relevant, authority class, reviewed timestamp, affected atlas domains, drift rate, and a concise `mechanisms_absorbed` list. Record license or usage restrictions before copying any text or data. Prefer primary sources for technical/platform claims; community skills may inspire heuristics but cannot become normative truth by repetition.

## Output Contract
Return a `research-wave` containing `uncertainties[]`, `queries_or_sources_examined[]`, `new_mechanisms[]`, `contradictions[]`, `coverage_deltas[]`, `source_records[]`, `stale_records[]`, `followup_required`, and `bounded_conclusion`. `new_mechanisms` must be empty when research only reconfirms existing knowledge.

## Failure Traps
- Link accumulation with no mechanism extraction.
- Treating popularity, star count, or visual fashion as authority.
- Converting draft guidance into mandatory conformance.
- Copying restricted source prose or databases instead of synthesizing.
- Stopping after sources that all share one platform worldview.
- Claiming “complete forever.” Research saturation always expires relative to domain drift.
- Searching so broadly that the original decision uncertainty becomes untestable.

A strong research wave makes the router or an obligation more accurate. If nothing in the system would change, record confirmation and stop expanding context.

## V6 Frontier Research Protocol
Maintain a **frontier uncertainty map** of UI domains/mechanisms where current evidence is weak, contradictory, rapidly changing, or outside established standards. Set **evidence-gap priority** by product relevance, risk, novelty, and decision leverage.

Run an **emerging-source watch** for new platform guidance, research, repositories, input modalities, AI interaction patterns, accessibility work, and design-system shifts without promoting novelty to authority. Mark **speculative-vs-actionable** findings explicitly. Define a **frontier exit criterion** for when a topic becomes sufficiently supported to enter stable registry/ontology/skill obligations—or when it remains research-only.

### Falsification
Seek a newer primary source or contradictory implementation that changes the frontier thesis. If the frontier record cannot absorb uncertainty, it is hype tracking rather than research.

### Recovery
Downgrade claims, refresh sources, widen domain sampling, and keep speculative mechanisms out of non-waivable production rules.
